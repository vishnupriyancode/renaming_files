#!/usr/bin/env python3
"""
Rename Files Module - Handles file renaming functionality.

This module contains all the functions related to renaming JSON files from old naming
conventions to new formats, including:
- File renaming with suffix mapping
- Header/footer transformations for WGS_CSBD and WGS_KERNAL files
- CLCL_ID generation for GBDF files
- Model information extraction
- File validation and processing

This functionality was extracted from main_processor.py for better code organization.
"""

import os
import re
import shutil
import json
from postman_generator import PostmanCollectionGenerator
from report_generate import ExcelReportGenerator, TimingTracker, get_excel_reporter


def extract_model_info_from_directory(dest_dir: str, renamed_files: list) -> dict:
    """
    Extract model information from directory structure and file names.
    
    Args:
        dest_dir: Destination directory path
        renamed_files: List of renamed files
        
    Returns:
        Dictionary with extracted model information
    """
    model_info = {
        "tc_id": "Unknown",
        "model_lob": "Unknown", 
        "model_name": "Unknown",
        "edit_id": "Unknown",
        "eob_code": "Unknown"
    }
    
    def extract_from_match(match, is_gbdf=False):
        """Helper to extract model info from regex match."""
        if not match:
            return False
        groups = match.groups()
        if is_gbdf and len(groups) >= 5:
            ts_number, model_name, _, edit_id, eob_code = groups[0], groups[1], groups[2], groups[3], groups[4]
        elif len(groups) >= 4:
            ts_number, model_name, edit_id, eob_code = groups[0], groups[1], groups[2], groups[3]
        else:
            return False
        
        model_info["tc_id"] = f"TS_{ts_number}"
        model_info["model_name"] = model_name.replace('_', ' ').replace('-', ' ')
        model_info["edit_id"] = edit_id
        model_info["eob_code"] = eob_code
        return True
    
    try:
        # Determine model LOB and patterns
        patterns = []
        if "CSBDTS" in dest_dir or "WGS_CSBD" in dest_dir:
            model_info["model_lob"] = "WGS_CSBD"
            patterns = [
                (r'CSBDTS_(\d{1,3})_(.+?)_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_(sur|dis)$', False),
                (r'TS_(\d{1,3})_(.+?)_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_(sur|dis)$', False)
            ]
        elif "GBDTS" in dest_dir or "GBDF" in dest_dir:
            model_info["model_lob"] = "GBDF_MCR" if "mcr" in dest_dir.lower() else "GBDF_GRS" if "grs" in dest_dir.lower() else "GBDF"
            patterns = [
                (r'TS_(\d{1,3})_(.+?)_gbdf_(mcr|grs)_([A-Za-z0-9]+)_([A-Za-z0-9]+)_(sur|dis)$', True),
                (r'GBDTS_(\d{1,3})_(.+?)_gbdf_(mcr|grs)_([A-Za-z0-9]+)_([A-Za-z0-9]+)_(sur|dis)$', True)
            ]
        elif "NYKTS" in dest_dir or "WGS_KERNAL" in dest_dir or "WGS_NYK" in dest_dir:
            model_info["model_lob"] = "WGS_NYK"
            patterns = [
                (r'NYKTS_(\d{1,3})_(.+?)_WGS_NYK_([A-Za-z0-9]+)_([A-Za-z0-9]+)_(sur|dis)$', False)
            ]
        
        # Try patterns in directory traversal
        current_path = dest_dir
        for _ in range(5):
            current_path = os.path.dirname(current_path)
            dir_name = os.path.basename(current_path)
            
            for pattern, is_gbdf in patterns:
                if extract_from_match(re.match(pattern, dir_name), is_gbdf):
                    return model_info
            
            if dir_name in ["CSBDTS", "GBDTS", "NYKTS", "WGS_CSBD", "GBDF", "WGS_KERNAL", "WGS_NYK", "renaming_jsons", "source_folder", ""]:
                break
        
        # Fallback: Try patterns in full path
        path_parts = dest_dir.split(os.sep)
        for part in path_parts:
            for pattern, is_gbdf in patterns:
                if extract_from_match(re.search(pattern, part), is_gbdf):
                    return model_info
        
        # Final fallback: Extract from filename
        if renamed_files and model_info["tc_id"] == "Unknown":
            first_file = renamed_files[0]
            if '#' in first_file:
                parts = first_file.split('#')
                if len(parts) >= 4:
                    model_info["edit_id"] = parts[2]
                    model_info["eob_code"] = parts[3]
                    tc_part = parts[1]
                    model_info["tc_id"] = f"TS_{tc_part.split('_')[0]}" if '_' in tc_part else f"TS_{tc_part}"
    
    except Exception as e:
        print(f"[WARNING] Error extracting model info from directory: {e}")
    
    return model_info


def clean_duplicate_fields_csbd(file_path):
    """
    Clean up duplicate fields in existing CSBD JSON files.
    This function removes duplicate fields that may have been created by previous versions.
    
    Args:
        file_path: Path to the JSON file to clean
        
    Returns:
        bool: True if cleaning was successful, False otherwise
    """
    try:
        # Read the existing JSON content
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        
        # Check if the file has duplicate fields in the payload
        if (isinstance(existing_data, dict) and 
            "payload" in existing_data and 
            isinstance(existing_data["payload"], dict)):
            
            payload = existing_data["payload"]
            
            # Check for duplicate fields in payload
            duplicate_fields = []
            for field in ["adhoc", "analyticId", "hints", "responseRequired", "meta-src-envrmt", "meta-transid"]:
                if field in payload and field in existing_data:
                    duplicate_fields.append(field)
            
            if duplicate_fields:
                print(f"[INFO] Found duplicate fields in {file_path}: {duplicate_fields}")
                
                # Remove duplicate fields from payload, keep only the test case data
                cleaned_payload = {}
                for key, value in payload.items():
                    if key not in ["adhoc", "analyticId", "hints", "responseRequired", "meta-src-envrmt", "meta-transid"]:
                        cleaned_payload[key] = value
                
                # Update the structure
                existing_data["payload"] = cleaned_payload
                
                # Write the cleaned JSON back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(existing_data, f, indent=2, ensure_ascii=False)
                
                print(f"[SUCCESS] Cleaned duplicate fields from {file_path}")
                return True
            else:
                print(f"[INFO] No duplicate fields found in {file_path}")
                return True
        else:
            print(f"[INFO] File {file_path} doesn't have the expected structure for cleaning")
            return True
        
    except json.JSONDecodeError as e:
        print(f"[ERROR] Error parsing JSON in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Error cleaning duplicate fields in {file_path}: {e}")
        return False


def apply_wgs_csbd_header_footer(file_path):
    """
    Apply header and footer structure to WGS_CSBD and WGS_KERNAL JSON files.
    This function transforms the JSON content by wrapping the existing data
    with the required header and footer metadata, avoiding duplicate fields.
    Additionally, generates random 11-digit numbers for KEY_CHK_CDN_NBR field.
    
    This function ALWAYS ensures the header/footer structure is present,
    even if the file already has it (to ensure consistency).
    
    Args:
        file_path: Path to the JSON file to transform
        
    Returns:
        bool: True if transformation was successful, False otherwise
    """
    import random
    
    try:
        # Read the existing JSON content
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        
        # Check if the file already has the correct structure
        has_correct_structure = (isinstance(existing_data, dict) and 
                                "adhoc" in existing_data and 
                                "payload" in existing_data and 
                                "responseRequired" in existing_data and
                                "meta-src-envrmt" in existing_data and
                                "meta-transid" in existing_data)
        
        # Header and footer structure (always use these values)
        header_footer = {
            "adhoc": "true",
            "analyticId": " ",
            "hints": ["congnitive_claims_async"],
            "responseRequired": "false",
            "meta-src-envrmt": "IMST",
            "meta-transid": "20220117181853TMBL20359Cl893580999",
            "Protigrity": "true"
        }
        
        # Generate random 11-digit number for KEY_CHK_DCN_NBR field
        # Check both root level and payload level for KEY_CHK_DCN_NBR
        if isinstance(existing_data, dict):
            # Check root level
            if "KEY_CHK_DCN_NBR" in existing_data:
                random_11_digit = str(random.randint(10000000000, 99999999999))
                existing_data["KEY_CHK_DCN_NBR"] = random_11_digit
                print(f"[INFO] Generated random 11-digit number for KEY_CHK_DCN_NBR (root level): {random_11_digit}")
            
            # Check payload level
            if "payload" in existing_data and isinstance(existing_data["payload"], dict):
                if "KEY_CHK_DCN_NBR" in existing_data["payload"]:
                    random_11_digit = str(random.randint(10000000000, 99999999999))
                    existing_data["payload"]["KEY_CHK_DCN_NBR"] = random_11_digit
                    print(f"[INFO] Generated random 11-digit number for KEY_CHK_DCN_NBR (payload level): {random_11_digit}")
        
        # Always ensure header/footer structure is correct
        if has_correct_structure:
            # File has structure, but ensure all header/footer fields are correct
            new_structure = {
                "adhoc": header_footer["adhoc"],
                "analyticId": header_footer["analyticId"],
                "hints": header_footer["hints"],
                "payload": existing_data.get("payload", existing_data),  # Use existing payload or entire data
                "responseRequired": header_footer["responseRequired"],
                "meta-src-envrmt": header_footer["meta-src-envrmt"],
                "meta-transid": header_footer["meta-transid"],
                "Protigrity": header_footer["Protigrity"]
            }
            
            # Preserve KEY_CHK_DCN_NBR if it exists at root level
            if "KEY_CHK_DCN_NBR" in existing_data:
                new_structure["KEY_CHK_DCN_NBR"] = existing_data["KEY_CHK_DCN_NBR"]
            
            # Write the updated structure back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(new_structure, f, indent=2, ensure_ascii=False)
            print(f"[INFO] Updated header/footer structure in: {file_path}")
        else:
            # File doesn't have correct structure, wrap existing data in payload
            new_structure = {
                "adhoc": header_footer["adhoc"],
                "analyticId": header_footer["analyticId"],
                "hints": header_footer["hints"],
                "payload": existing_data,  # The existing JSON becomes the payload
                "responseRequired": header_footer["responseRequired"],
                "meta-src-envrmt": header_footer["meta-src-envrmt"],
                "meta-transid": header_footer["meta-transid"],
                "Protigrity": header_footer["Protigrity"]
            }
            
            # Write the transformed JSON back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(new_structure, f, indent=2, ensure_ascii=False)
            print(f"[SUCCESS] Applied header/footer structure to: {file_path}")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"[ERROR] Error parsing JSON in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Error applying header/footer to {file_path}: {e}")
        return False


def apply_gbdf_clcl_id_generation(file_path):
    """
    Generate random 11-digit number for CLCL_ID field in GBDF JSON files.
    This function modifies the CLCL_ID field to have a random 11-digit value.
    Handles root-level, nested payload structure, and GBDF claim_header path.
    
    Args:
        file_path: Path to the JSON file to transform
        
    Returns:
        bool: True if transformation was successful, False otherwise
    """
    import random
    
    def update_clcl_id(data, path_name):
        """Helper to update CLCL_ID at a given path."""
        if isinstance(data, dict) and "CLCL_ID" in data:
            data["CLCL_ID"] = random_11_digit
            print(f"[INFO] Generated random 11-digit number for CLCL_ID ({path_name}): {random_11_digit}")
            return True
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        
        random_11_digit = str(random.randint(10000000000, 99999999999))
        clcl_id_updated = False
        
        # Check all possible paths for CLCL_ID
        paths_to_check = [
            (existing_data, "root level"),
            (existing_data.get("payload", {}) if isinstance(existing_data, dict) else {}, "payload level"),
            (existing_data.get("claim_header", [{}])[0] if isinstance(existing_data, dict) and isinstance(existing_data.get("claim_header"), list) and existing_data["claim_header"] else {}, "claim_header[0] level"),
            (existing_data.get("payload", {}).get("claim_header", [{}])[0] if isinstance(existing_data, dict) and isinstance(existing_data.get("payload"), dict) and isinstance(existing_data["payload"].get("claim_header"), list) and existing_data["payload"]["claim_header"] else {}, "payload.claim_header[0] level")
        ]
        
        for data, path_name in paths_to_check:
            if update_clcl_id(data, path_name):
                clcl_id_updated = True
        
        if clcl_id_updated:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
            print(f"[SUCCESS] Applied CLCL_ID generation to: {file_path}")
            return True
        else:
            print(f"[WARNING] CLCL_ID field not found in {file_path}, skipping transformation")
            return False
        
    except json.JSONDecodeError as e:
        print(f"[ERROR] Error parsing JSON in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Error applying CLCL_ID generation to {file_path}: {e}")
        return False


def validate_suffix(suffix, filename):
    """
    Validate that the suffix is one of the allowed values.
    
    Args:
        suffix: The suffix to validate
        filename: The filename being processed (for error reporting)
        
    Returns:
        bool: True if valid, False if invalid
    """
    valid_suffixes = {"deny", "bypass", "exclusion"}
    
    if suffix not in valid_suffixes:
        print(f"ERROR: Invalid suffix '{suffix}' found in file '{filename}'")
        print(f"Valid suffixes are: {', '.join(sorted(valid_suffixes))}")
        print("No files will be created due to invalid suffix.")
        return False
    
    return True


def rename_files(edit_id="rvn001", code="00W5", source_dir=None, dest_dir=None, generate_postman=True, postman_collection_name=None, postman_file_name=None, excel_reporter=None):
    """
    STAGE 1: FILE RENAMING FUNCTION
    ===============================
    This is the core function that handles file renaming and Postman collection generation.
    
    PROCESSING FLOW:
    1. Setup suffix mapping for file conversion
    2. Auto-generate source/destination paths if not provided
    3. Process JSON files with different naming patterns (3-part, 4-part, 5-part)
    4. Convert files to new naming convention: TC#XX_XXXXX#edit_id#code#suffix.json
    5. Move files from source to destination directory
    6. Generate Postman collection for API testing
    7. Track timing information for Excel reporting
    
    Args:
        edit_id: The edit ID (e.g., "rvn001", "rvn002")
        code: The code (e.g., "00W5", "00W6")
        source_dir: Source directory path (auto-generated if None)
        dest_dir: Destination directory path (auto-generated if None)
        generate_postman: If True, generate Postman collection after renaming
        postman_collection_name: Name for the Postman collection
        postman_file_name: Custom filename for the Postman collection JSON file
        excel_reporter: Excel reporter instance for timing tracking
        
    Returns:
        list: List of renamed file names
    """
    
    # STAGE 1.0: TIMING INITIALIZATION
    # ================================
    # Initialize timing tracking for this operation
    naming_tracker = TimingTracker()
    postman_tracker = TimingTracker()
    if excel_reporter is None:
        excel_reporter = get_excel_reporter()
    
    # Start timing for naming convention operations
    naming_tracker.start("naming_convention")
    
    # STAGE 1.1: SUFFIX MAPPING CONFIGURATION
    # =======================================
    # Mapping for suffixes based on the expected output format
    suffix_mapping = {
        "positive": {
            "deny": "LR",    # deny -> LR
        },
        "negative": {
            "bypass": "NR",  # bypass -> NR
        },
        "exclusion": {
            "exclusion": "EX",   # exclusion -> EX
        }
    }
    
    # Valid suffixes that are allowed
    valid_suffixes = {"deny", "bypass", "exclusion"}
    
    # STAGE 1.2: PATH CONFIGURATION AND VALIDATION
    # ============================================
    # Auto-generate paths if not provided
    if source_dir is None:
        source_dir = f"source_folder/WGS_CSBD/TS_01_REVENUE_WGS_CSBD_{edit_id}_{code}_payloads_sur/regression"
    
    if dest_dir is None:
        # Default to renaming_jsons for backward compatibility
        dest_dir = f"renaming_jsons/TS_01_REVENUE_WGS_CSBD_{edit_id}_{code}_payloads_dis/regression"
    
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} not found!")
        return []
    
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # STAGE 1.3: FILE DISCOVERY
    # =========================
    # Get all JSON files in the source directory
    json_files = [f for f in os.listdir(source_dir) if f.endswith('.json')]
    
    print("Files to be renamed and moved:")
    print("=" * 60)
    
    renamed_files = []
    
    # STAGE 1.4: FILE PROCESSING LOOP
    # ===============================
    # Process each JSON file and convert to new naming convention
    for filename in json_files:
        # STAGE 1.4.1: FILENAME PARSING
        # =============================
        # Parse the current filename to understand its structure
        parts = filename.split('#')
        
        if len(parts) == 3:
            # STAGE 1.4.1A: 3-PART TEMPLATE PROCESSING
            # ========================================
            # Handle 3-part template: TC#XX_XXXXX#suffix.json
            tc_part = parts[0]  # TC
            tc_id_part = parts[1]  # 01_12345
            suffix = parts[2].replace('.json', '')  # deny, bypass, exclusion
            
            # Validate suffix before processing
            if not validate_suffix(suffix, filename):
                continue  # Skip this file and move to next
            
            # Get the correct suffix mapping for the new template
            mapped_suffix = suffix
            for category in suffix_mapping.values():
                if suffix in category:
                    mapped_suffix = category[suffix]
                    break
            
            # STAGE 1.4.1A: CREATE NEW FILENAME
            # =================================
            # Create new filename according to new template: TC#XX_XXXXX#rvn001#00W5#LR.json
            new_filename = f"{tc_part}#{tc_id_part}#{edit_id}#{code}#{mapped_suffix}.json"
            
            print(f"Current: {filename}")
            print(f"Converting to new template...")
            print(f"New:     {new_filename}")
            print(f"Moving to: {dest_dir}")
            print("-" * 40)
            
            # STAGE 1.4.1A: FILE OPERATIONS
            # =============================
            # Source and destination paths - normalize paths for Windows compatibility
            source_path = os.path.normpath(os.path.join(source_dir, filename))
            dest_path = os.path.normpath(os.path.join(dest_dir, new_filename))
            
            try:
                # Copy the file to destination with new name
                # Use shutil.copy2 for cross-platform compatibility
                shutil.copy2(source_path, dest_path)
                print(f"Successfully copied and renamed: {filename} -> {new_filename}")
                
                # Apply header/footer transformation for WGS_CSBD, WGS_KERNAL, and WGS_NYK (NYKTS) files
                if "WGS_CSBD" in dest_dir or "WGS_KERNAL" in dest_dir or "WGS_Kernal" in dest_dir or "NYKTS" in dest_dir or "WGS_NYK" in dest_dir:
                    model_type = "WGS_CSBD" if "WGS_CSBD" in dest_dir else ("WGS_NYK" if ("NYKTS" in dest_dir or "WGS_NYK" in dest_dir) else "WGS_KERNAL")
                    print(f"Applying {model_type} header/footer transformation to: {new_filename}")
                    if apply_wgs_csbd_header_footer(dest_path):
                        print(f"[SUCCESS] Header/footer applied to: {new_filename}")
                    else:
                        print(f"[WARNING] Failed to apply header/footer to: {new_filename}")
                
                # Apply CLCL_ID generation for GBDF files
                elif "GBDF" in dest_dir:
                    print(f"Applying GBDF CLCL_ID generation to: {new_filename}")
                    if apply_gbdf_clcl_id_generation(dest_path):
                        print(f"[SUCCESS] CLCL_ID generation applied to: {new_filename}")
                    else:
                        print(f"[WARNING] Failed to apply CLCL_ID generation to: {new_filename}")
                
                # Remove the original file
                os.remove(source_path)
                print(f"Removed original file: {filename}")
                
                renamed_files.append(new_filename)
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
        elif len(parts) == 4:
            # STAGE 1.4.1B: 4-PART TEMPLATE PROCESSING
            # ========================================
            # Handle 4-part template: TC#XX_XXXXX#edit_id#suffix.json
            tc_part = parts[0]  # TC
            tc_id_part = parts[1]  # 01_12345
            file_edit_id = parts[2]  # rvn001
            suffix = parts[3].replace('.json', '')  # deny, bypass, exclusion
            
            # Validate suffix before processing
            if not validate_suffix(suffix, filename):
                continue  # Skip this file and move to next
            
            # Get the correct suffix mapping for the new template
            mapped_suffix = suffix
            for category in suffix_mapping.values():
                if suffix in category:
                    mapped_suffix = category[suffix]
                    break
            
            # Create new filename according to new template: TC#XX_XXXXX#rvn001#00W5#LR.json
            new_filename = f"{tc_part}#{tc_id_part}#{edit_id}#{code}#{mapped_suffix}.json"
            
            print(f"Current: {filename}")
            print(f"Converting from 4-part to 5-part template...")
            print(f"New:     {new_filename}")
            print(f"Moving to: {dest_dir}")
            print("-" * 40)
            
            # Source and destination paths - normalize paths for Windows compatibility
            source_path = os.path.normpath(os.path.join(source_dir, filename))
            dest_path = os.path.normpath(os.path.join(dest_dir, new_filename))
            
            try:
                # Copy the file to destination with new name
                shutil.copy2(source_path, dest_path)
                print(f"Successfully copied and renamed: {filename} -> {new_filename}")
                
                # Apply header/footer transformation for WGS_CSBD, WGS_KERNAL, and WGS_NYK (NYKTS) files
                if "WGS_CSBD" in dest_dir or "WGS_KERNAL" in dest_dir or "WGS_Kernal" in dest_dir or "NYKTS" in dest_dir or "WGS_NYK" in dest_dir:
                    model_type = "WGS_CSBD" if "WGS_CSBD" in dest_dir else ("WGS_NYK" if ("NYKTS" in dest_dir or "WGS_NYK" in dest_dir) else "WGS_KERNAL")
                    print(f"Applying {model_type} header/footer transformation to: {new_filename}")
                    if apply_wgs_csbd_header_footer(dest_path):
                        print(f"[SUCCESS] Header/footer applied to: {new_filename}")
                    else:
                        print(f"[WARNING] Failed to apply header/footer to: {new_filename}")
                
                # Apply CLCL_ID generation for GBDF files
                elif "GBDF" in dest_dir:
                    print(f"Applying GBDF CLCL_ID generation to: {new_filename}")
                    if apply_gbdf_clcl_id_generation(dest_path):
                        print(f"[SUCCESS] CLCL_ID generation applied to: {new_filename}")
                    else:
                        print(f"[WARNING] Failed to apply CLCL_ID generation to: {new_filename}")
                
                # Remove the original file
                os.remove(source_path)
                print(f"Removed original file: {filename}")
                
                renamed_files.append(new_filename)
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
        elif len(parts) == 5:
            # STAGE 1.4.1C: 5-PART TEMPLATE PROCESSING
            # ========================================
            # Handle 5-part template: TC#XX_XXXXX#edit_id#code#suffix.json (already converted)
            tc_part = parts[0]  # TC
            tc_id_part = parts[1]  # 01_12345
            file_edit_id = parts[2]  # rvn001
            file_code = parts[3]  # 00W5
            suffix = parts[4].replace('.json', '')  # LR, NR, EX, exclusion, etc.
            
            # Validate suffix before processing (check if it's a valid input suffix)
            # For 5-part files, we need to check if the suffix is a valid input suffix
            # or if it's already a mapped suffix (LR, NR, EX)
            valid_input_suffixes = {"deny", "bypass", "exclusion"}
            valid_mapped_suffixes = {"LR", "NR", "EX"}
            
            if suffix not in valid_input_suffixes and suffix not in valid_mapped_suffixes:
                print(f"ERROR: Invalid suffix '{suffix}' found in file '{filename}'")
                print(f"Valid input suffixes are: {', '.join(sorted(valid_input_suffixes))}")
                print(f"Valid mapped suffixes are: {', '.join(sorted(valid_mapped_suffixes))}")
                print("No files will be created due to invalid suffix.")
                continue  # Skip this file and move to next
            
            # Apply suffix mapping to ensure correct format
            mapped_suffix = suffix
            for category in suffix_mapping.values():
                if suffix in category:
                    mapped_suffix = category[suffix]
                    break
            
            # Check if this file matches our target model
            if file_edit_id == edit_id and file_code == code:
                # Create new filename with mapped suffix
                new_filename = f"{tc_part}#{tc_id_part}#{file_edit_id}#{file_code}#{mapped_suffix}.json"
                
                print(f"Current: {filename}")
                if mapped_suffix != suffix:
                    print(f"Applying suffix mapping: '{suffix}' -> '{mapped_suffix}'")
                print(f"New:     {new_filename}")
                print(f"Moving to: {dest_dir}")
                print("-" * 40)
                
                # Source and destination paths
                source_path = os.path.join(source_dir, filename)
                dest_path = os.path.join(dest_dir, new_filename)
                
                try:
                    # Copy the file to destination
                    shutil.copy2(source_path, dest_path)
                    print(f"Successfully moved: {filename}")
                    
                    # Apply header/footer transformation for WGS_CSBD, WGS_KERNAL, and WGS_NYK (NYKTS) files
                    if "WGS_CSBD" in dest_dir or "WGS_KERNAL" in dest_dir or "WGS_Kernal" in dest_dir or "NYKTS" in dest_dir or "WGS_NYK" in dest_dir:
                        model_type = "WGS_CSBD" if "WGS_CSBD" in dest_dir else ("WGS_NYK" if ("NYKTS" in dest_dir or "WGS_NYK" in dest_dir) else "WGS_KERNAL")
                        print(f"Applying {model_type} header/footer transformation to: {new_filename}")
                        if apply_wgs_csbd_header_footer(dest_path):
                            print(f"[SUCCESS] Header/footer applied to: {new_filename}")
                        else:
                            print(f"[WARNING] Failed to apply header/footer to: {new_filename}")
                    
                    # Apply CLCL_ID generation for GBDF files
                    elif "GBDF" in dest_dir:
                        print(f"Applying GBDF CLCL_ID generation to: {new_filename}")
                        if apply_gbdf_clcl_id_generation(dest_path):
                            print(f"[SUCCESS] CLCL_ID generation applied to: {new_filename}")
                        else:
                            print(f"[WARNING] Failed to apply CLCL_ID generation to: {new_filename}")
                    
                    # Remove the original file
                    os.remove(source_path)
                    print(f"Removed original file: {filename}")
                    
                    renamed_files.append(new_filename)
                    
                except Exception as e:
                    print(f"Error processing {filename}: {e}")
            else:
                print(f"Warning: {filename} has different model parameters ({file_edit_id}_{file_code}) than target ({edit_id}_{code})")
                continue
        else:
            print(f"Warning: {filename} doesn't match expected format (needs 3, 4, or 5 parts)")
            continue
    
    print("\n" + "=" * 60)
    print("Renaming and moving completed!")
    print(f"Files moved to: {dest_dir}")
    
    # End timing for naming convention operations
    naming_convention_time = naming_tracker.end()
    print(f"[TIMING] Naming convention operations completed in {naming_convention_time:.2f}ms")
    
    # STAGE 2: POSTMAN COLLECTION GENERATION
    # =====================================
    # Generate Postman collection if requested
    if generate_postman and renamed_files:
        # Start timing for Postman collection generation
        postman_tracker.start("postman_collection")
        print("\n" + "=" * 60)
        print("Generating Postman collection...")
        print("-" * 40)
        
        try:
            # STAGE 2.1: POSTMAN GENERATOR SETUP
            # ==================================
            # Initialize Postman generator with specific model directory
            # Use appropriate subdirectory when processing models
            output_dir = "postman_collections"
            if "WGS_CSBD" in dest_dir:
                output_dir = "postman_collections/WGS_CSBD"
            elif "GBDF" in dest_dir:
                output_dir = "postman_collections/GBDF"
            elif "WGS_KERNAL" in dest_dir or "WGS_Kernal" in dest_dir or "WGS_NYK" in dest_dir:
                output_dir = "postman_collections/WGS_KERNAL"
            
            generator = PostmanCollectionGenerator(
                source_dir=dest_dir,  # Use the specific model's destination directory
                output_dir=output_dir
            )
            
            # STAGE 2.2: COLLECTION NAME EXTRACTION
            # =====================================
            # Extract collection name from destination directory if not provided
            if postman_collection_name is None:
                # Extract from dest_dir path
                dest_path_parts = dest_dir.split(os.sep)
                for part in dest_path_parts:
                    if part.startswith("TS_") and ("_payloads_dis" in part or "_dis" in part):
                        # Handle both _payloads_dis and _dis patterns
                        if "_payloads_dis" in part:
                            postman_collection_name = part.replace("_payloads_dis", "")
                        elif "_dis" in part:
                            postman_collection_name = part.replace("_dis", "")
                        break
                
                # Fallback to auto-generated name if not found
                if postman_collection_name is None:
                    postman_collection_name = f"TS_01_REVENUE_WGS_CSBD_{edit_id}_{code}"
            
            # Get custom filename from model config if available
            custom_filename = postman_file_name
            
            # STAGE 2.3: COLLECTION GENERATION
            # ===============================
            # Determine if this is a GBDF model
            is_gbdf_model = "GBDF" in dest_dir
            
            # Generate collection
            collection_path = generator.generate_postman_collection(postman_collection_name, custom_filename, is_gbdf_model)
            
            if collection_path:
                print(f"Postman collection generated: {collection_path}")
                print(f"Collection name: {postman_collection_name}")
                print("\nReady for API testing!")
                print("=" * 60)
                print("To use this collection:")
                print("1. Open Postman")
                print("2. Click 'Import'")
                print(f"3. Select the file: {collection_path}")
                print("4. Start testing your APIs!")
            else:
                print("Failed to generate Postman collection")
                
        except Exception as e:
            print(f"Error generating Postman collection: {e}")
        
        # End timing for Postman collection generation
        postman_collection_time = postman_tracker.end()
        print(f"[TIMING] Postman collection generation completed in {postman_collection_time:.2f}ms")
    else:
        postman_collection_time = 0.0
    
    # STAGE 3: TIMING RECORD CREATION
    # ===============================
    # Add timing record to Excel reporter
    if renamed_files:
        # Extract model information from directory structure
        model_info = extract_model_info_from_directory(dest_dir, renamed_files)
        
        # Extract type (regression or smoke) from source_dir
        test_type = "regression"  # default
        if source_dir:
            if "smoke" in source_dir.lower():
                test_type = "smoke"
            elif "regression" in source_dir.lower():
                test_type = "regression"
        
        # Add timing record with extracted information
        excel_reporter.add_timing_record(
            tc_id=model_info["tc_id"],
            model_lob=model_info["model_lob"],
            model_name=model_info["model_name"],
            edit_id=model_info["edit_id"],
            eob_code=model_info["eob_code"],
            naming_convention_time_ms=naming_convention_time,
            postman_collection_time_ms=postman_collection_time,
            status="Success" if renamed_files else "Failed",
            type=test_type
        )
        
        print(f"[TIMING] Added timing record: {model_info['tc_id']} - {model_info['model_lob']} - {model_info['model_name']} - Total: {naming_convention_time + postman_collection_time:.2f}ms")
    
    return renamed_files
