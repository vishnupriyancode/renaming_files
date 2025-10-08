#!/usr/bin/env python3
"""
Dynamic model discovery system for TS folders.
Automatically detects TS_XX_REVENUE_WGS_CSBD_* folders and extracts model parameters.
"""

import os
import re
import glob
from typing import List, Dict, Optional


def normalize_ts_number(ts_number_raw: str) -> str:
    """
    Normalize TS number to handle different digit patterns.
    
    Args:
        ts_number_raw: Raw TS number from folder name (e.g., "1", "01", "001", "10", "100")
        
    Returns:
        Normalized TS number string
        
    Examples:
        "1" -> "01"     (single digit)
        "01" -> "01"    (already 2 digits)
        "001" -> "001"  (already 3 digits)
        "10" -> "10"    (2 digits)
        "100" -> "100"  (3 digits)
    """
    ts_num = int(ts_number_raw)
    
    # Determine padding based on value range
    if 1 <= ts_num <= 9:
        # Single digit: TS01 to TS09
        return f"{ts_num:02d}"
    elif 10 <= ts_num <= 99:
        # Two digits: TS10 to TS99
        return f"{ts_num:02d}"
    elif 100 <= ts_num <= 999:
        # Three digits: TS100 to TS999
        return f"{ts_num:03d}"
    else:
        # Fallback: use original format
        return ts_number_raw


def generate_postman_collection_name(ts_number: str) -> str:
    """
    Generate Postman collection name based on TS number pattern.
    
    Args:
        ts_number: Normalized TS number (e.g., "01", "10", "100")
        
    Returns:
        Postman collection name
        
    Examples:
        "01" -> "ts_01_collection"
        "10" -> "ts_10_collection"
        "100" -> "ts_100_collection"
    """
    return f"ts_{ts_number}_collection"


def format_ts_argument(ts_number: str) -> str:
    """
    Format TS number for command line arguments.
    
    Args:
        ts_number: TS number (can be "1", "01", "10", "100", etc.)
        
    Returns:
        Formatted TS number for arguments
        
    Examples:
        "1" -> "01"
        "10" -> "10"
        "100" -> "100"
    """
    ts_num = int(ts_number)
    
    if 1 <= ts_num <= 9:
        return f"{ts_num:02d}"
    elif 10 <= ts_num <= 99:
        return f"{ts_num:02d}"
    elif 100 <= ts_num <= 999:
        return f"{ts_num:03d}"
    else:
        return ts_number


def discover_ts_folders(base_dir: str = ".", use_wgs_csbd_destination: bool = False) -> List[Dict]:
    """
    Discover all TS_XX_REVENUE_WGS_CSBD_* folders and extract model parameters.
    Supports flexible digit patterns: TS01-TS09, TS10-TS99, TS100-TS999
    Also supports GBDF MCR patterns
    
    Args:
        base_dir: Base directory to search for TS folders
        
    Returns:
        List of model configurations extracted from folder names
    """
    models = []
    
    # Check if this is a GBDF directory
    is_gbdf = "GBDF" in base_dir
    
    if is_gbdf:
        # GBDF MCR patterns
        pattern1 = os.path.join(base_dir, "TS_*_Covid_gbdf_mcr_*_sur")
        ts_folders = glob.glob(pattern1)
    else:
        # WGS_CSBD patterns
        # Pattern to match TS_XX_REVENUE_WGS_CSBD_* folders
        # Handle both "payloads_sur" and "_sur" patterns
        # Also handle new Revenue code pattern and Lab panel Model pattern
        pattern1 = os.path.join(base_dir, "TS_*_REVENUE_WGS_CSBD_*_payloads_sur")
        pattern2 = os.path.join(base_dir, "TS_*_REVENUE_WGS_CSBD_*_ayloads_sur")
        pattern3 = os.path.join(base_dir, "TS_*_REVENUE_WGS_CSBD_*_sur")
        pattern4 = os.path.join(base_dir, "TS_*_Revenue code Services not payable on Facility claim Sub Edit *_WGS_CSBD_*_sur")
        pattern5 = os.path.join(base_dir, "TS_*_Lab panel Model_WGS_CSBD_*_sur")
        pattern6 = os.path.join(base_dir, "TS_*_Recovery Room Reimbursement_WGS_CSBD_*_sur")
        pattern7 = os.path.join(base_dir, "TS_*_Covid_WGS_CSBD_*_sur")
        pattern8 = os.path.join(base_dir, "TS_*_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_*_sur")
        pattern9 = os.path.join(base_dir, "TS_*_Device Dependent Procedures(R1)-1B_WGS_CSBD_*_sur")
        pattern10 = os.path.join(base_dir, "TS_*_revenue model_WGS_CSBD_*_sur")
        pattern11 = os.path.join(base_dir, "TS_*_Revenue Code to HCPCS Xwalk-1B_WGS_CSBD_*_sur")
        pattern12 = os.path.join(base_dir, "TS_*_Incidentcal Services Facility_WGS_CSBD_*_sur")
        pattern13 = os.path.join(base_dir, "TS_*_Revenue model CR v3_WGS_CSBD_*_sur")
        pattern14 = os.path.join(base_dir, "TS_*_HCPCS to Revenue Code Xwalk_WGS_CSBD_*_sur")
        pattern15 = os.path.join(base_dir, "TS_*_Multiple E&M Same day_WGS_CSBD_*_sur")
        pattern16 = os.path.join(base_dir, "TS_*_Multiple Billing of Obstetrical Services_WGS_CSBD_*_sur")
        ts_folders = (glob.glob(pattern1) + glob.glob(pattern2) + glob.glob(pattern3) + 
                     glob.glob(pattern4) + glob.glob(pattern5) + glob.glob(pattern6) + 
                     glob.glob(pattern7) + glob.glob(pattern8) + glob.glob(pattern9) + 
                     glob.glob(pattern10) + glob.glob(pattern11) + glob.glob(pattern12) + 
                     glob.glob(pattern13) + glob.glob(pattern14) + glob.glob(pattern15) + 
                     glob.glob(pattern16))
    
    print(f"Scanning for TS folders in: {base_dir}")
    print(f"Found {len(ts_folders)} TS folders")
    
    for folder_path in ts_folders:
        folder_name = os.path.basename(folder_path)
        
        # Extract parameters using flexible regex pattern
        # Pattern 1: TS_XX_REVENUE_WGS_CSBD_EDIT_ID_EOB_CODE_sur (original pattern)
        # Pattern 2: TS_XX_Revenue code Services not payable on Facility claim Sub Edit X_WGS_CSBD_RULEREVE00000X_00W28_sur (new pattern)
        # Supports 1-3 digit TS numbers: TS_1, TS_01, TS_001, TS_10, TS_100, etc.
        # Supports any alphanumeric edit_id and EOB code formats
        # Examples: TS_60_REVENUE_WGS_CSBD_ASDFGJEUSK_00W29_sur, TS_07_REVENUE_WGS_CSBD_rvn011_00W11_sur
        # Examples: TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_sur
        
        # Try original pattern first
        match = re.match(r'TS_(\d{1,3})_REVENUE_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try new Revenue code pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Revenue code Services not payable on Facility claim Sub Edit \d+_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Lab panel Model pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Lab panel Model_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Recovery Room Reimbursement pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Recovery Room Reimbursement_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Covid pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Covid_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Laterality Policy pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Device Dependent Procedures pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Device Dependent Procedures\(R1\)-1B_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try revenue model pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_revenue model_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Revenue Code to HCPCS Xwalk-1B pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Revenue Code to HCPCS Xwalk-1B_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Incidentcal Services Facility pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Incidentcal Services Facility_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Revenue model CR v3 pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Revenue model CR v3_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try HCPCS to Revenue Code Xwalk pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_HCPCS to Revenue Code Xwalk_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Multiple E&M Same day pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Multiple E&M Same day_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match, try Multiple Billing of Obstetrical Services pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_Multiple Billing of Obstetrical Services_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match and this is GBDF, try GBDF MCR pattern
        if not match and is_gbdf:
            match = re.match(r'TS_(\d{1,3})_Covid_gbdf_mcr_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        if match:
            ts_number_raw = match.group(1)
            edit_id = match.group(2)
            code = match.group(3)
            
            # Normalize TS number to handle different digit patterns
            ts_number = normalize_ts_number(ts_number_raw)
            
            # Check if regression subfolder exists
            regression_path = os.path.join(folder_path, "regression")
            if not os.path.exists(regression_path):
                print(f"Warning: Regression folder not found in {folder_name}")
                continue
            
            # Generate destination directory name
            # Handle "payloads_sur", "ayloads_sur" (typo), and "_sur" patterns
            if "_payloads_sur" in folder_name:
                dest_folder_name = folder_name.replace("_payloads_sur", "_payloads_dis")
            elif "_ayloads_sur" in folder_name:
                dest_folder_name = folder_name.replace("_ayloads_sur", "_payloads_dis")
            elif "_sur" in folder_name:
                dest_folder_name = folder_name.replace("_sur", "_dis")
            else:
                dest_folder_name = folder_name  # fallback
            
            # Generate destination directory based on model type
            if is_gbdf:
                # GBDF MCR models go to GBDF subdirectory
                dest_dir = os.path.join("renaming_jsons", "GBDF", dest_folder_name, "regression")
            elif use_wgs_csbd_destination:
                # WGS_CSBD models with flag go to WGS_CSBD subdirectory
                dest_dir = os.path.join("renaming_jsons", "WGS_CSBD", dest_folder_name, "regression")
            else:
                # Default to renaming_jsons root
                dest_dir = os.path.join("renaming_jsons", dest_folder_name, "regression")
            
            # Generate Postman collection name with flexible formatting
            # For Revenue code Services models, use the full descriptive name
            if "Revenue code Services not payable on Facility claim" in folder_name:
                # Extract the Sub Edit number and create proper collection name
                sub_edit_match = re.search(r'Sub Edit (\d+)', folder_name)
                if sub_edit_match:
                    sub_edit_num = sub_edit_match.group(1)
                    postman_collection_name = f"TS_{ts_number}_Revenue code Services not payable on Facility claim Sub Edit {sub_edit_num}_Collection"
                else:
                    postman_collection_name = generate_postman_collection_name(ts_number)
                postman_file_name = f"revenue_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Lab panel Model" in folder_name:
                # For Lab panel Model, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Lab panel Model_Collection"
                postman_file_name = f"lab_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Recovery Room Reimbursement" in folder_name:
                # For Recovery Room Reimbursement, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Recovery Room Reimbursement_Collection"
                postman_file_name = f"recovery_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Covid" in folder_name:
                # For Covid, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Covid_Collection"
                postman_file_name = f"covid_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Laterality Policy" in folder_name:
                # For Laterality Policy, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Laterality_Collection"
                postman_file_name = f"laterality_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Device Dependent Procedures" in folder_name:
                # For Device Dependent Procedures, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Device Dependent Procedures_Collection"
                postman_file_name = f"device_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "revenue model" in folder_name:
                # For revenue model, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_revenue model_Collection"
                postman_file_name = f"revenue_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Revenue Code to HCPCS Xwalk-1B" in folder_name:
                # For Revenue Code to HCPCS Xwalk-1B, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Revenue Code to HCPCS Xwalk-1B_Collection"
                postman_file_name = f"revenue_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Incidentcal Services Facility" in folder_name:
                # For Incidentcal Services Facility, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Incidentcal Services Facility_Collection"
                postman_file_name = f"incidentcal_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Revenue model CR v3" in folder_name:
                # For Revenue model CR v3, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Revenue model CR v3_Collection"
                postman_file_name = f"revenue_model_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "HCPCS to Revenue Code Xwalk" in folder_name:
                # For HCPCS to Revenue Code Xwalk, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_HCPCS to Revenue Code Xwalk_Collection"
                postman_file_name = f"hcpcs_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Multiple E&M Same day" in folder_name:
                # For Multiple E&M Same day, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Multiple E&M Same day_Collection"
                postman_file_name = f"multiple_em_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Multiple Billing of Obstetrical Services" in folder_name:
                # For Multiple Billing of Obstetrical Services, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Multiple Billing of Obstetrical Services_Collection"
                postman_file_name = f"multiple_billing_obstetrical_wgs_csbd_{edit_id}_{code.lower()}.json"
            elif "Covid_gbdf_mcr" in folder_name:
                # For GBDF MCR Covid, use the full descriptive name
                postman_collection_name = f"TS_{ts_number}_Covid_gbdf_mcr_Collection"
                postman_file_name = f"covid_gbdf_mcr_{edit_id}_{code.lower()}.json"
            else:
                postman_collection_name = generate_postman_collection_name(ts_number)
                postman_file_name = f"revenue_wgs_csbd_{edit_id}_{code.lower()}.json"
            
            model_config = {
                "ts_number": ts_number,
                "ts_number_raw": ts_number_raw,  # Keep original for reference
                "edit_id": edit_id,
                "code": code,
                "source_dir": regression_path,
                "dest_dir": dest_dir,
                "postman_collection_name": postman_collection_name,
                "postman_file_name": postman_file_name,
                "folder_name": folder_name
            }
            
            models.append(model_config)
            print(f"Discovered: TS_{ts_number} ({edit_id}_{code}) [Raw: {ts_number_raw}]")
        else:
            print(f"Warning: Could not parse folder name: {folder_name}")
    
    return models


def get_model_by_ts_number(ts_number: str, base_dir: str = ".") -> Optional[Dict]:
    """
    Get model configuration for a specific TS number.
    Supports flexible TS number formats (e.g., "1", "01", "10", "100").
    
    Args:
        ts_number: TS number (e.g., "1", "01", "10", "100")
        base_dir: Base directory to search for TS folders
        
    Returns:
        Model configuration dict or None if not found
    """
    models = discover_ts_folders(base_dir)
    
    # Normalize the input TS number for comparison
    normalized_input = normalize_ts_number(ts_number)
    
    for model in models:
        if model["ts_number"] == normalized_input:
            return model
    
    return None


def get_all_models(base_dir: str = ".") -> List[Dict]:
    """
    Get all discovered model configurations.
    
    Args:
        base_dir: Base directory to search for TS folders
        
    Returns:
        List of all model configurations
    """
    return discover_ts_folders(base_dir)


def validate_model_config(model: Dict) -> bool:
    """
    Validate that a model configuration has all required fields and paths exist.
    
    Args:
        model: Model configuration dictionary
        
    Returns:
        True if valid, False otherwise
    """
    required_fields = ["ts_number", "edit_id", "code", "source_dir", "dest_dir"]
    
    # Check required fields
    for field in required_fields:
        if field not in model:
            print(f"Missing required field: {field}")
            return False
    
    # Check if source directory exists
    if not os.path.exists(model["source_dir"]):
        print(f"Source directory does not exist: {model['source_dir']}")
        return False
    
    return True


def print_discovered_models(models: List[Dict]):
    """
    Print a formatted list of discovered models.
    
    Args:
        models: List of model configurations
    """
    if not models:
        print("No TS models discovered")
        return
    
    print(f"\nDISCOVERED TS MODELS ({len(models)} found)")
    print("=" * 60)
    
    for i, model in enumerate(models, 1):
        print(f"{i}. TS_{model['ts_number']}: {model['edit_id']}_{model['code']}")
        print(f"   Source: {model['source_dir']}")
        print(f"   Dest:   {model['dest_dir']}")
        print(f"   Collection: {model['postman_collection_name']}")
        print()


def print_nested_models_display():
    """
    Display all models in a nested, hierarchical structure showing WGS_CSBD and GBDF categories.
    This provides a clear, organized view of all available models.
    """
    print("\n" + "=" * 80)
    print("🏗️  NESTED MODEL STRUCTURE")
    print("=" * 80)
    
    # Get WGS_CSBD models
    wgs_csbd_models = discover_ts_folders("source_folder/WGS_CSBD", use_wgs_csbd_destination=True)
    
    # Get GBDF models
    gbdf_models = discover_ts_folders("source_folder/GBDF", use_wgs_csbd_destination=False)
    
    total_models = len(wgs_csbd_models) + len(gbdf_models)
    
    print(f"📊 Total Models Found: {total_models}")
    print("=" * 80)
    
    # Display WGS_CSBD models
    if wgs_csbd_models:
        print(f"\n🔵 WGS_CSBD MODELS ({len(wgs_csbd_models)} models)")
        print("─" * 50)
        
        for i, model in enumerate(wgs_csbd_models, 1):
            ts_number = model['ts_number']
            edit_id = model['edit_id']
            code = model['code']
            collection_name = model['postman_collection_name']
            
            # Extract model type from collection name for better display
            model_type = "General"
            if "Covid" in collection_name:
                model_type = "Covid"
            elif "Laterality" in collection_name:
                model_type = "Laterality Policy"
            elif "Revenue code Services" in collection_name:
                model_type = "Revenue Services"
            elif "Lab panel" in collection_name:
                model_type = "Lab Panel"
            elif "Device Dependent" in collection_name:
                model_type = "Device Procedures"
            elif "Recovery Room" in collection_name:
                model_type = "Recovery Room"
            elif "Revenue Code to HCPCS" in collection_name:
                model_type = "Revenue-HCPCS Crosswalk"
            elif "Incidentcal Services" in collection_name:
                model_type = "Incidental Services"
            elif "Revenue model CR v3" in collection_name:
                model_type = "Revenue Model CR v3"
            elif "HCPCS to Revenue Code" in collection_name:
                model_type = "HCPCS-Revenue Crosswalk"
            elif "Multiple E&M Same day" in collection_name:
                model_type = "Multiple E&M Same day"
            elif "revenue model" in collection_name:
                model_type = "Revenue Model"
            
            print(f"  {i:2d}. TS_{ts_number:02s} │ {model_type}")
            print(f"      ├─ Edit ID: {edit_id}")
            print(f"      ├─ Code: {code}")
            print(f"      └─ Collection: {collection_name}")
            print()
    else:
        print(f"\n🔵 WGS_CSBD MODELS (0 models)")
        print("─" * 50)
        print("   No WGS_CSBD models found")
    
    # Display GBDF models
    if gbdf_models:
        print(f"\n🟢 GBDF MODELS ({len(gbdf_models)} models)")
        print("─" * 50)
        
        for i, model in enumerate(gbdf_models, 1):
            ts_number = model['ts_number']
            edit_id = model['edit_id']
            code = model['code']
            collection_name = model['postman_collection_name']
            
            # Extract model type from collection name for better display
            model_type = "General"
            if "Covid_gbdf_mcr" in collection_name or "Covid" in collection_name:
                model_type = "Covid GBDF MCR"
            
            print(f"  {i:2d}. TS_{ts_number:02s} │ {model_type}")
            print(f"      ├─ Edit ID: {edit_id}")
            print(f"      ├─ Code: {code}")
            print(f"      └─ Collection: {collection_name}")
            print()
    else:
        print(f"\n🟢 GBDF MODELS (0 models)")
        print("─" * 50)
        print("   No GBDF models found")
    
    # Summary
    print("=" * 80)
    print("📋 SUMMARY")
    print("=" * 80)
    print(f"🔵 WGS_CSBD Models: {len(wgs_csbd_models)}")
    print(f"🟢 GBDF Models: {len(gbdf_models)}")
    print(f"📊 Total Models: {total_models}")
    
    if total_models > 0:
        print(f"\n💡 USAGE EXAMPLES:")
        print("─" * 30)
        print("WGS_CSBD Models:")
        print("  python main_processor.py --wgs_csbd --TS01")
        print("  python main_processor.py --wgs_csbd --all")
        print()
        print("GBDF Models:")
        print("  python main_processor.py --gbdf_mcr --TS47")
        print("  python main_processor.py --gbdf_mcr --all")
        print()
        print("List all models:")
        print("  python main_processor.py --list")
    
    print("=" * 80)


if __name__ == "__main__":
    # Test the discovery system
    print("🧪 Testing Dynamic Model Discovery")
    print("=" * 50)
    
    # Show nested display
    print_nested_models_display()
    
    # Also show traditional display for comparison
    print("\n" + "=" * 50)
    print("📋 TRADITIONAL DISPLAY")
    print("=" * 50)
    
    models = discover_ts_folders()
    print_discovered_models(models)
    
    # Test specific TS number lookup
    if models:
        first_model = models[0]
        ts_number = first_model["ts_number"]
        print(f"🔍 Testing lookup for TS_{ts_number}...")
        
        found_model = get_model_by_ts_number(ts_number)
        if found_model:
            print(f"✅ Found model: {found_model['edit_id']}_{found_model['code']}")
        else:
            print(f"❌ Model not found for TS_{ts_number}")
