#!/usr/bin/env python3
"""
Auto Edit Processor - Automatically processes edits from edits_list.xlsx
and creates entries in STATIC_MODELS_CONFIG.

This script:
1. Reads edits_list.xlsx file
2. Parses edit information from "List of Edits that need to be Automated" column
3. Extracts EDIT ID, model name with LOB, and EOB code
4. Generates config entries in STATIC_MODELS_CONFIG format
5. Checks if command already exists
6. Updates models_config.py with new entries
7. Updates Excel file with command status
"""

import os
import re
import pandas as pd
from typing import Dict, List, Optional, Tuple
from pathlib import Path


# Model mapping from Excel sheet names to config keys
MODEL_SHEET_MAPPING = {
    "WGS_CSBD": "wgs_csbd",
    "GBDF": "gbdf_mcr",  # Default to MCR, can be extended
    "KERNAL": "wgs_kernal"
}


def parse_edit_string(edit_string: str, sheet_name: str = "WGS_CSBD") -> Optional[Dict[str, str]]:
    """
    Parse edit string in ANY flexible format with any number of parts:
    - Standard: RULEEM000001~covid~wgs~csbd~00W17--live (5 parts)
    - Short: RULESUB4000001~Expansion on sub-edit4--live (2 parts)
    - With space: RULESUB4000001~Expansion on sub-edit4 --live (2 parts)
    - Any format: RULEXXX~part1~part2~...~partN--live (any N parts)
    
    Returns:
        Dictionary with keys: edit_id, model_name_with_lob, eob_code
        or None if parsing fails
    """
    if not edit_string or pd.isna(edit_string):
        return None
    
    edit_string = str(edit_string).strip()
    
    # Remove common prefixes like "Note:" or other metadata
    if edit_string.startswith("Note:"):
        edit_string = edit_string[5:].strip()
    
    # Extract the actual edit string (first line if multiline)
    edit_string = edit_string.split('\n')[0].strip()
    
    # Normalize spacing around --live (handle both "--live" and " --live")
    edit_string = re.sub(r'\s+--', '--', edit_string)
    edit_string = re.sub(r'--\s+', '--', edit_string)
    
    # Split by ~ to get parts
    parts = [p.strip() for p in edit_string.split('~') if p.strip()]
    
    if len(parts) < 1:
        print(f"[WARNING] Invalid edit string format (empty or no valid parts): {edit_string}")
        return None
    
    # Extract edit_id (first part is always edit_id)
    edit_id = parts[0]
    
    if not edit_id:
        print(f"[WARNING] Empty edit_id in: {edit_string}")
        return None
    
    # EOB code patterns to search for
    eob_patterns = [
        r'00W\d+',      # Pattern like 00W04, 00W17, 00W28
        r'v\d+',        # Pattern like v04, v17, v28
        r'\d{2}W\d{2}', # Pattern like 00W04
        r'\d{1,2}W\d{1,2}', # More flexible pattern
    ]
    
    # Search for EOB code across ALL parts (excluding edit_id)
    eob_code = None
    eob_code_part_index = None
    
    # First, check the last part (most common location for EOB code)
    if len(parts) > 1:
        last_part = parts[-1]
        # Remove --live suffix if present
        last_part_clean = last_part.split('--')[0].strip()
        
        for pattern in eob_patterns:
            match = re.search(pattern, last_part_clean)
            if match:
                eob_code = match.group(0)
                eob_code_part_index = len(parts) - 1
                break
    
    # If not found in last part, search all remaining parts
    if not eob_code and len(parts) > 1:
        for idx, part in enumerate(parts[1:], start=1):
            # Remove --live suffix if present
            part_clean = part.split('--')[0].strip()
            for pattern in eob_patterns:
                match = re.search(pattern, part_clean)
                if match:
                    eob_code = match.group(0)
                    eob_code_part_index = idx
                    break
            if eob_code:
                break
    
    # If still not found, use placeholder
    if not eob_code:
        eob_code = "00W00"  # Placeholder - user should verify/update
    
    # Build model_name_with_lob from remaining parts
    # Exclude edit_id (first part) and the part containing EOB code (if found)
    model_parts = []
    
    if len(parts) > 1:
        for idx, part in enumerate(parts[1:], start=1):
            # Skip the part that contains the EOB code (if it's a standalone EOB code)
            if eob_code_part_index is not None and idx == eob_code_part_index:
                # Check if this part is ONLY the EOB code (not a description with EOB code)
                part_clean = part.split('--')[0].strip()
                if part_clean == eob_code or re.match(r'^' + re.escape(eob_code) + r'(--.*)?$', part):
                    continue  # Skip this part as it's just the EOB code
            
            # Remove --live suffix and clean the part
            part_clean = part.split('--')[0].strip()
            
            # If this part contains the EOB code but also has other text, include it
            if part_clean and part_clean != eob_code:
                model_parts.append(part_clean)
    
    # Build model name from collected parts
    if model_parts:
        # Join parts and sanitize
        model_name_with_lob = '_'.join(model_parts)
        # Convert to lowercase and replace spaces/special chars with underscores
        model_name_with_lob = re.sub(r'[^\w\s-]', '', model_name_with_lob.lower())
        model_name_with_lob = re.sub(r'[\s-]+', '_', model_name_with_lob)
        # Remove multiple consecutive underscores
        model_name_with_lob = re.sub(r'_+', '_', model_name_with_lob).strip('_')
    else:
        # No model parts found, create from edit_id or use default
        model_name_with_lob = "edit"
    
    # Ensure model name is not empty
    if not model_name_with_lob:
        model_name_with_lob = "edit"
    
    # Add sheet-based prefix if model name doesn't already have it
    if sheet_name == "WGS_CSBD":
        if not any(prefix in model_name_with_lob.lower() for prefix in ['wgs', 'csbd']):
            model_name_with_lob = f"wgs_csbd_{model_name_with_lob}"
    elif sheet_name == "GBDF":
        if not any(prefix in model_name_with_lob.lower() for prefix in ['gbdf', 'mcr', 'grs']):
            model_name_with_lob = f"gbdf_mcr_{model_name_with_lob}"
    elif sheet_name == "KERNAL":
        if not any(prefix in model_name_with_lob.lower() for prefix in ['wgs', 'nyk', 'kernal']):
            model_name_with_lob = f"wgs_nyk_{model_name_with_lob}"
    
    # Clean up EOB code (remove any trailing spaces)
    eob_code = eob_code.strip() if eob_code else "00W00"
    
    return {
        "edit_id": edit_id,
        "model_name_with_lob": model_name_with_lob,
        "eob_code": eob_code,
        "raw_string": edit_string
    }


def get_next_ts_number(model_config: List[Dict]) -> str:
    """
    Get the next available TS number for a model.
    
    Args:
        model_config: List of model configurations
        
    Returns:
        Next TS number as string (e.g., "58")
    """
    if not model_config:
        return "01"
    
    # Extract all TS numbers and convert to integers
    ts_numbers = []
    for config in model_config:
        ts_num = config.get("ts_number", "0")
        try:
            ts_numbers.append(int(ts_num))
        except ValueError:
            continue
    
    if not ts_numbers:
        return "01"
    
    # Find the maximum and add 1
    next_num = max(ts_numbers) + 1
    return f"{next_num:02d}"  # Format as 2-digit string


def generate_model_name(edit_id: str, model_name_with_lob: str) -> str:
    """
    Generate a readable model name from edit_id and model_name_with_lob.
    For now, we'll use a simple approach - can be enhanced later.
    """
    # Extract a simple name from model_name_with_lob
    # e.g., "covid_wgs_csbd" -> "Covid"
    parts = model_name_with_lob.split('_')
    if parts:
        # Capitalize first letter
        return parts[0].capitalize()
    return "Model"


def generate_config_entry(
    ts_number: str,
    edit_id: str,
    eob_code: str,
    model_name_with_lob: str,
    model_type: str = "wgs_csbd"
) -> Dict:
    """
    Generate a config entry in STATIC_MODELS_CONFIG format.
    
    Args:
        ts_number: TS number (e.g., "01")
        edit_id: Edit ID (e.g., "RULEEM000001")
        eob_code: EOB code (e.g., "00W04")
        model_name_with_lob: Model name with LOB (e.g., "covid_wgs_csbd")
        model_type: Model type key (e.g., "wgs_csbd")
        
    Returns:
        Dictionary with config entry
    """
    # Determine folder structure based on model type
    if model_type == "wgs_csbd":
        ts_prefix = "CSBDTS"
        source_base = "source_folder/WGS_CSBD"
        dest_base = "renaming_jsons/CSBDTS"
        model_name = generate_model_name(edit_id, model_name_with_lob)
        folder_name = f"{ts_prefix}_{ts_number}_{model_name}_WGS_CSBD_{edit_id}_{eob_code}"
    elif model_type == "gbdf_mcr":
        ts_prefix = "GBDTS"
        source_base = "source_folder/GBDF"
        dest_base = "renaming_jsons/GBDTS"
        model_name = generate_model_name(edit_id, model_name_with_lob)
        folder_name = f"{ts_prefix}_{ts_number}_{model_name}_gbdf_mcr_{edit_id}_{eob_code}"
    elif model_type == "wgs_kernal":
        ts_prefix = "NYKTS"
        source_base = "source_folder/WGS_Kernal"
        dest_base = "renaming_jsons/NYKTS"
        model_name = generate_model_name(edit_id, model_name_with_lob)
        folder_name = f"{ts_prefix}_{ts_number}_{model_name}_WGS_NYK_{edit_id}_{eob_code}"
    else:
        # Default to wgs_csbd format
        ts_prefix = "CSBDTS"
        source_base = "source_folder/WGS_CSBD"
        dest_base = "renaming_jsons/CSBDTS"
        model_name = generate_model_name(edit_id, model_name_with_lob)
        folder_name = f"{ts_prefix}_{ts_number}_{model_name}_WGS_CSBD_{edit_id}_{eob_code}"
    
    # Generate paths
    source_dir = f"{source_base}/{folder_name}_sur/payloads/regression"
    dest_dir = f"{dest_base}/{folder_name}_dis/payloads/regression"
    
    # Generate Postman collection name
    postman_collection_name = f"{ts_prefix}_{ts_number}_{model_name}_Collection"
    
    # Generate Postman file name
    postman_file_name = f"{model_name_with_lob}_{edit_id}_{eob_code}.json"
    
    return {
        "ts_number": ts_number,
        "edit_id": edit_id,
        "code": eob_code,
        "source_dir": source_dir,
        "dest_dir": dest_dir,
        "postman_collection_name": postman_collection_name,
        "postman_file_name": postman_file_name
    }


def check_command_exists(
    df: pd.DataFrame,
    ts_number: str,
    model_type: str = "wgs_csbd"
) -> bool:
    """
    Check if command already exists in Excel file.
    
    Args:
        df: DataFrame from Excel sheet
        ts_number: TS number to check
        model_type: Model type (wgs_csbd, gbdf_mcr, etc.)
        
    Returns:
        True if command exists, False otherwise
    """
    # Generate command pattern
    if model_type == "wgs_csbd":
        cmd_pattern = f"CSBDTS{ts_number}"
    elif model_type == "gbdf_mcr":
        cmd_pattern = f"GBDTS{ts_number}"
    elif model_type == "wgs_kernal":
        cmd_pattern = f"NYKTS{ts_number}"
    else:
        cmd_pattern = f"CSBDTS{ts_number}"
    
    # Check in "Test Sutie ID" column (note: typo in original column name)
    if "Test Sutie ID" in df.columns:
        test_suite_ids = df["Test Sutie ID"].astype(str)
        return any(cmd_pattern in str(val) for val in test_suite_ids if pd.notna(val))
    
    return False


def generate_command(ts_number: str, model_type: str = "wgs_csbd") -> str:
    """
    Generate command string.
    
    Args:
        ts_number: TS number (e.g., "01")
        model_type: Model type (wgs_csbd, gbdf_mcr, etc.)
        
    Returns:
        Command string (e.g., "python main_processor.py --wgs_csbd --CSBDTS01")
    """
    if model_type == "wgs_csbd":
        return f"python main_processor.py --wgs_csbd --CSBDTS{ts_number}"
    elif model_type == "gbdf_mcr":
        return f"python main_processor.py --gbdf_mcr --GBDTS{ts_number}"
    elif model_type == "wgs_kernal":
        return f"python main_processor.py --wgs_nyk --NYKTS{ts_number}"
    else:
        return f"python main_processor.py --wgs_csbd --CSBDTS{ts_number}"


def read_edits_list(excel_path: str = "edits_list.xlsx") -> Dict[str, pd.DataFrame]:
    """
    Read edits_list.xlsx file.
    
    Returns:
        Dictionary mapping sheet names to DataFrames
    """
    try:
        excel_data = pd.read_excel(excel_path, sheet_name=None)
        return excel_data
    except Exception as e:
        print(f"[ERROR] Failed to read Excel file: {e}")
        return {}


def process_edits_from_excel(
    excel_path: str = "edits_list.xlsx",
    sheet_name: str = "WGS_CSBD",
    dry_run: bool = False
) -> List[Dict]:
    """
    Process edits from Excel file and generate config entries.
    
    Args:
        excel_path: Path to Excel file
        sheet_name: Sheet name to process
        dry_run: If True, don't update files, just return results
        
    Returns:
        List of generated config entries
    """
    print(f"\n{'='*60}")
    print(f"Processing edits from {sheet_name} sheet")
    print(f"{'='*60}\n")
    
    # Read Excel file
    excel_data = read_edits_list(excel_path)
    
    if sheet_name not in excel_data:
        print(f"[ERROR] Sheet '{sheet_name}' not found in Excel file")
        return []
    
    df = excel_data[sheet_name]
    
    # Get model type
    model_type = MODEL_SHEET_MAPPING.get(sheet_name, "wgs_csbd")
    
    # Read current config
    from models_config import STATIC_MODELS_CONFIG
    current_config = STATIC_MODELS_CONFIG.get(model_type, [])
    
    # Process each row
    generated_configs = []
    edit_column = "List of Edits that need to be Automated"
    
    if edit_column not in df.columns:
        print(f"[ERROR] Column '{edit_column}' not found in sheet")
        return []
    
    for idx, row in df.iterrows():
        edit_string = row.get(edit_column)
        
        if pd.isna(edit_string):
            continue
        
        # Skip rows that are just notes (contain "Note:" and command info)
        edit_str_lower = str(edit_string).lower()
        if "note:" in edit_str_lower and "python main_processor.py" in edit_str_lower:
            print(f"\n[SKIP] Row {idx + 1}: Note row (already has command)")
            continue
        
        # Check if command already exists (warn but still process)
        cmd_status = row.get("Cmd status", "")
        command_exists = False
        if pd.notna(cmd_status) and str(cmd_status).strip().lower() == "created":
            command_exists = True
            print(f"\n[WARNING] Row {idx + 1}: Command already created in Excel")
            print(f"  [INFO] Argument is already in use @edits_list.xlsx")
        
        # Parse edit string
        parsed = parse_edit_string(edit_string, sheet_name=sheet_name)
        if not parsed:
            print(f"\n[SKIP] Row {idx + 1}: Could not parse edit string")
            continue
        
        edit_id = parsed["edit_id"]
        model_name_with_lob = parsed["model_name_with_lob"]
        eob_code = parsed["eob_code"]
        
        print(f"\n[INFO] Processing edit: {edit_id}")
        print(f"  Model: {model_name_with_lob}")
        print(f"  EOB Code: {eob_code}")
        
        # Warn if EOB code is a placeholder
        if eob_code == "00W00" or eob_code == "":
            print(f"  [WARNING] EOB code not found in edit string - using placeholder '{eob_code}'")
            print(f"  [INFO] Please verify and update the EOB code in models_config.py if needed")
        
        # Check if edit_id already exists in config (with same EOB code)
        existing_entry = None
        for config in current_config:
            if config.get("edit_id") == edit_id and config.get("code") == eob_code:
                existing_entry = config
                break
        
        if existing_entry:
            print(f"  [SKIP] Entry already exists with TS number: {existing_entry.get('ts_number')}")
            continue
        
        # Check if edit_id exists with different EOB code (warn but allow)
        existing_with_different_code = None
        for config in current_config:
            if config.get("edit_id") == edit_id and config.get("code") != eob_code:
                existing_with_different_code = config
                print(f"  [WARNING] Edit ID {edit_id} already exists with different EOB code: {config.get('code')} (TS{config.get('ts_number')})")
                break
        
        # Get next TS number
        ts_number = get_next_ts_number(current_config)
        
        # Check if Test Suite ID is already set in Excel
        test_suite_id = row.get("Test Sutie ID", "")
        if pd.notna(test_suite_id) and str(test_suite_id).strip():
            print(f"  [INFO] Test Suite ID already set: {test_suite_id}")
            # Extract TS number from existing Test Suite ID if possible
            ts_match = re.search(r'(\d+)', str(test_suite_id))
            if ts_match:
                existing_ts = ts_match.group(1)
                # Check if this TS number already has this edit_id + eob_code combination
                existing_config = None
                for config in current_config:
                    if (config.get("ts_number") == existing_ts.zfill(2) and 
                        config.get("edit_id") == edit_id and 
                        config.get("code") == eob_code):
                        existing_config = config
                        break
                
                if existing_config:
                    print(f"  [SKIP] Entry already exists with TS{existing_ts} for this edit_id and eob_code combination")
                    continue
                else:
                    # Use existing TS number if edit_id+eob_code combination is different
                    print(f"  [INFO] Using existing TS number: {existing_ts} (different eob_code)")
                    ts_number = existing_ts.zfill(2)  # Ensure 2-digit format
        
        # Check if command already exists
        if command_exists or check_command_exists(df, ts_number, model_type):
            print(f"  [WARNING] Command for TS{ts_number} already exists in Excel")
            print(f"  [INFO] Argument is already in use @edits_list.xlsx")
            # Don't generate new config if command already exists and entry exists
            if existing_entry:
                continue
            # Still generate config if entry doesn't exist, but note the warning
        
        # Generate config entry
        config_entry = generate_config_entry(
            ts_number=ts_number,
            edit_id=edit_id,
            eob_code=eob_code,
            model_name_with_lob=model_name_with_lob,
            model_type=model_type
        )
        
        generated_configs.append({
            "config": config_entry,
            "row_index": idx,
            "command": generate_command(ts_number, model_type)
        })
        
        print(f"  [SUCCESS] Generated config for TS{ts_number}")
        print(f"  Command: {generate_command(ts_number, model_type)}")
    
    return generated_configs


def update_models_config(
    new_configs: List[Dict],
    model_type: str = "wgs_csbd"
) -> bool:
    """
    Update models_config.py with new config entries.
    
    Args:
        new_configs: List of config dictionaries
        model_type: Model type key
        
    Returns:
        True if successful, False otherwise
    """
    if not new_configs:
        print("[INFO] No new configs to add")
        return True
    
    try:
        # Read current models_config.py
        config_path = "models_config.py"
        with open(config_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Find the model type section
        model_key = f'    "{model_type}": ['
        start_idx = None
        end_idx = None
        
        for i, line in enumerate(lines):
            if model_key in line:
                start_idx = i
                break
        
        if start_idx is None:
            print(f"[ERROR] Could not find '{model_type}' in models_config.py")
            return False
        
        # Find the closing bracket for this list
        bracket_count = 0
        for i in range(start_idx, len(lines)):
            line = lines[i]
            bracket_count += line.count('[')
            bracket_count -= line.count(']')
            if bracket_count == 0 and i > start_idx:
                end_idx = i
                break
        
        if end_idx is None:
            print(f"[ERROR] Could not find end of '{model_type}' list")
            return False
        
        # Find the last entry before closing bracket (look for last '},')
        insert_idx = end_idx
        needs_comma = False
        for i in range(end_idx - 1, start_idx, -1):
            if '},' in lines[i]:
                insert_idx = i + 1
                needs_comma = True
                break
            elif '}' in lines[i] and i < end_idx - 1:
                # Last entry without comma
                insert_idx = i + 1
                needs_comma = False
                # Need to add comma to the last existing entry
                if not lines[i].strip().endswith(','):
                    lines[i] = lines[i].rstrip() + ',\n'
                break
        
        # Generate config string for each new entry
        new_lines = []
        for idx, item in enumerate(new_configs):
            config = item["config"]
            
            new_lines.append("    {\n")
            new_lines.append(f'        "ts_number": "{config["ts_number"]}",\n')
            new_lines.append(f'        "edit_id": "{config["edit_id"]}",\n')
            new_lines.append(f'        "code": "{config["code"]}",\n')
            new_lines.append(f'        "source_dir": "{config["source_dir"]}",\n')
            new_lines.append(f'        "dest_dir": "{config["dest_dir"]}",\n')
            new_lines.append(f'        "postman_collection_name": "{config["postman_collection_name"]}",\n')
            new_lines.append(f'        "postman_file_name": "{config["postman_file_name"]}"\n')
            
            # Add comma except for the last entry
            if idx < len(new_configs) - 1:
                new_lines.append("    },\n")
            else:
                new_lines.append("    }\n")
        
        # Insert new lines
        new_file_lines = lines[:insert_idx] + new_lines + lines[insert_idx:]
        
        # Write back
        with open(config_path, 'w', encoding='utf-8') as f:
            f.writelines(new_file_lines)
        
        print(f"\n[SUCCESS] Updated {config_path} with {len(new_configs)} new entries")
        return True
        
    except Exception as e:
        print(f"[ERROR] Failed to update models_config.py: {e}")
        import traceback
        traceback.print_exc()
        return False


def update_excel_file(
    excel_path: str,
    sheet_name: str,
    new_configs: List[Dict]
) -> bool:
    """
    Update Excel file with command information.
    
    Args:
        excel_path: Path to Excel file
        sheet_name: Sheet name
        new_configs: List of config dictionaries with row indices
        
    Returns:
        True if successful, False otherwise
    """
    if not new_configs:
        return True
    
    try:
        # Read Excel file
        excel_data = pd.read_excel(excel_path, sheet_name=None)
        
        if sheet_name not in excel_data:
            print(f"[ERROR] Sheet '{sheet_name}' not found")
            return False
        
        df = excel_data[sheet_name]
        
        # Update rows
        for item in new_configs:
            row_idx = item["row_index"]
            command = item["command"]
            ts_number = item["config"]["ts_number"]
            
            # Update Test Suite ID column
            if "Test Sutie ID" in df.columns:
                df.at[row_idx, "Test Sutie ID"] = f"CSBDTS{ts_number}" if "CSBDTS" in command else f"GBDTS{ts_number}" if "GBDTS" in command else f"NYKTS{ts_number}"
            
            # Update Cmd status column
            if "Cmd status" in df.columns:
                df.at[row_idx, "Cmd status"] = "Created"
        
        # Write back to Excel
        with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
            # Write all sheets
            for sheet, data in excel_data.items():
                if sheet == sheet_name:
                    df.to_excel(writer, sheet_name=sheet, index=False)
                else:
                    data.to_excel(writer, sheet_name=sheet, index=False)
        
        print(f"\n[SUCCESS] Updated {excel_path} with command information")
        return True
        
    except Exception as e:
        print(f"[ERROR] Failed to update Excel file: {e}")
        return False


def main():
    """
    Main function to process edits from Excel file.
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Automatically process edits from edits_list.xlsx"
    )
    parser.add_argument(
        "--sheet",
        type=str,
        default="WGS_CSBD",
        help="Excel sheet name to process (default: WGS_CSBD)"
    )
    parser.add_argument(
        "--excel",
        type=str,
        default="edits_list.xlsx",
        help="Path to Excel file (default: edits_list.xlsx)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't update files, just show what would be done"
    )
    
    args = parser.parse_args()
    
    # Process edits
    generated_configs = process_edits_from_excel(
        excel_path=args.excel,
        sheet_name=args.sheet,
        dry_run=args.dry_run
    )
    
    if not generated_configs:
        print("\n[INFO] No new edits to process")
        return
    
    # Show summary
    print(f"\n{'='*60}")
    print(f"SUMMARY: Generated {len(generated_configs)} new config entries")
    print(f"{'='*60}\n")
    
    for item in generated_configs:
        print(f"TS{item['config']['ts_number']}: {item['config']['edit_id']} - {item['command']}")
    
    if args.dry_run:
        print("\n[INFO] Dry run mode - no files were updated")
        return
    
    # Update files
    model_type = MODEL_SHEET_MAPPING.get(args.sheet, "wgs_csbd")
    
    print(f"\n{'='*60}")
    print("Updating files...")
    print(f"{'='*60}\n")
    
    # Update models_config.py
    update_models_config(generated_configs, model_type)
    
    # Update Excel file
    update_excel_file(args.excel, args.sheet, generated_configs)
    
    print(f"\n{'='*60}")
    print("Processing complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()

