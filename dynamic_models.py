#!/usr/bin/env python3
"""
Dynamic model discovery system for TS folders.
Automatically detects TS_XX_REVENUE_WGS_CSBD_* folders and extracts model parameters.
"""

# STAGE 1: Import required libraries
# - os: For file system operations (checking paths, joining paths)
# - re: For regular expressions (pattern matching in folder names)
# - glob: For finding files/folders using wildcard patterns
# - typing: For type hints to make code more readable and maintainable
import os
import re
import glob
from typing import List, Dict, Optional


# STAGE 2: TS Number Normalization Functions
# These functions ensure consistent formatting of TS numbers across the system

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


# STAGE 3: Main Folder Discovery Function
# This is the core function that scans directories and finds TS folders

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
    
    # Check if this is a GBDF directory or WGS_Kernal directory
    is_gbdf = "GBDF" in base_dir
    is_wgs_kernal = "WGS_Kernal" in base_dir or "WGS_KERNAL" in base_dir

    # STAGE 3.1: Define search patterns based on directory type
    if is_wgs_kernal:
        # WGS_NYK patterns - NYKTS naming convention
        # Match any NYKTS folder with any model name (including spaces)
        # Use a pattern that matches NYKTS_*_WGS_NYK_*_sur to catch all variations
        pattern1 = os.path.join(base_dir, "NYKTS_*")
        all_folders = glob.glob(pattern1)
        # Filter to only include folders that match the NYKTS pattern and end with _sur
        ts_folders = [f for f in all_folders if os.path.isdir(f) and "_WGS_NYK_" in os.path.basename(f) and f.endswith("_sur")]
    elif is_gbdf:
        # GBDF MCR patterns - multiple patterns to catch different folder naming conventions
        pattern1 = os.path.join(base_dir, "TS_*_Covid_gbdf_mcr_*_sur")
        pattern2 = os.path.join(base_dir, "TS_*_Multiple E&M Same day_gbdf_mcr_*_sur")
        pattern3 = os.path.join(base_dir, "TS_*_Multiple E&M Same day_gbdf_grs_*_sur")
        pattern4 = os.path.join(base_dir, "TS_*_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_*_sur")
        pattern5 = os.path.join(base_dir, "TS_*_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_*_sur")
        pattern6 = os.path.join(base_dir, "TS_*_No match of Procedure code_gbdf_mcr_*_sur")
        pattern7 = os.path.join(base_dir, "TS_*_No match of Procedure code_gbdf_grs_*_sur")
        pattern8 = os.path.join(base_dir, "TS_*_Nebulizer A52466 IPERP-132_gbdf_mcr_*_sur")
        pattern9 = os.path.join(base_dir, "TS_*_Nebulizer A52466 IPERP-132_gbdf_grs_*_sur")
        pattern10 = os.path.join(base_dir, "TS_*_Unspecified_dx_code_outpt_gbdf_mcr_*_sur")
        pattern11 = os.path.join(base_dir, "TS_*_Unspecified_dx_code_outpt_gbdf_grs_*_sur")
        pattern12 = os.path.join(base_dir, "TS_*_Unspecified_dx_code_prof_gbdf_mcr_*_sur")
        pattern13 = os.path.join(base_dir, "TS_*_Unspecified_dx_code_prof_gbdf_grs_*_sur")
        ts_folders = glob.glob(pattern1) + glob.glob(pattern2) + glob.glob(pattern3) + glob.glob(pattern4) + glob.glob(pattern5) + glob.glob(pattern6) + glob.glob(pattern7) + glob.glob(pattern8) + glob.glob(pattern9) + glob.glob(pattern10) + glob.glob(pattern11) + glob.glob(pattern12) + glob.glob(pattern13)
    else:
        # WGS_CSBD patterns - multiple patterns to catch different folder naming conventions
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
        pattern8_copy = os.path.join(base_dir, "TS_*_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_*_sur copy")
        pattern9 = os.path.join(base_dir, "TS_*_Device Dependent Procedures(R1)-1B_WGS_CSBD_*_sur")
        pattern10 = os.path.join(base_dir, "TS_*_revenue model_WGS_CSBD_*_sur")
        pattern11 = os.path.join(base_dir, "TS_*_Revenue Code to HCPCS Xwalk-1B_WGS_CSBD_*_sur")
        pattern12 = os.path.join(base_dir, "TS_*_Incidentcal Services Facility_WGS_CSBD_*_sur")
        pattern13 = os.path.join(base_dir, "TS_*_Revenue model CR v3_WGS_CSBD_*_sur")
        pattern14 = os.path.join(base_dir, "TS_*_HCPCS to Revenue Code Xwalk_WGS_CSBD_*_sur")
        pattern15 = os.path.join(base_dir, "TS_*_Multiple E&M Same day_WGS_CSBD_*_sur")
        pattern16 = os.path.join(base_dir, "TS_*_Multiple Billing of Obstetrical Services_WGS_CSBD_*_sur")
        pattern17 = os.path.join(base_dir, "TS_*_RadioservicesbilledwithoutRadiopharma_WGS_CSBD_*_sur")
        # CSBD_TS patterns for special models
        pattern18 = os.path.join(base_dir, "CSBD_TS_*_Revenue code to HCPCS Alignment edit_WGS_CSBD_*_sur")
        # CSBDTS patterns (without underscore between CSBD and TS) for all model types
        pattern19 = os.path.join(base_dir, "CSBDTS_*_Covid_WGS_CSBD_*_sur")
        pattern20 = os.path.join(base_dir, "CSBDTS_*_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_*_sur")
        pattern21 = os.path.join(base_dir, "CSBDTS_*_Revenue code Services not payable on Facility claim Sub Edit *_WGS_CSBD_*_sur")
        pattern22 = os.path.join(base_dir, "CSBDTS_*_RadioservicesbilledwithoutRadiopharma_WGS_CSBD_*_sur")
        pattern23 = os.path.join(base_dir, "CSBDTS_*_Multiple E&M Same day_WGS_CSBD_*_sur")
        pattern24 = os.path.join(base_dir, "CSBDTS_*_Multiple Billing of Obstetrical Services_WGS_CSBD_*_sur")
        pattern25 = os.path.join(base_dir, "CSBDTS_*_Revenue code to HCPCS Alignment edit_WGS_CSBD_*_sur")
        pattern26 = os.path.join(base_dir, "CSBDTS_*_Observation_Services_WGS_CSBD_*_sur")
        ts_folders = (glob.glob(pattern1) + glob.glob(pattern2) + glob.glob(pattern3) +
                     glob.glob(pattern4) + glob.glob(pattern5) + glob.glob(pattern6) +
                     glob.glob(pattern7) + glob.glob(pattern8) + glob.glob(pattern8_copy) + glob.glob(pattern9) +
                     glob.glob(pattern10) + glob.glob(pattern11) + glob.glob(pattern12) +
                     glob.glob(pattern13) + glob.glob(pattern14) + glob.glob(pattern15) +
                     glob.glob(pattern16) + glob.glob(pattern17) + glob.glob(pattern18) +
                     glob.glob(pattern19) + glob.glob(pattern20) + glob.glob(pattern21) +
                     glob.glob(pattern22) + glob.glob(pattern23) + glob.glob(pattern24) + glob.glob(pattern25) + glob.glob(pattern26))
    
    # STAGE 3.2: Display scanning progress
    print(f"Scanning for TS folders in: {base_dir}")
    print(f"Found {len(ts_folders)} TS folders")
    
    # STAGE 4: Process each found folder and extract parameters
    for folder_path in ts_folders:
        folder_name = os.path.basename(folder_path)
        
        # STAGE 4.1: Pattern matching - try different regex patterns to extract folder information
        # Extract parameters using flexible regex pattern
        # Pattern 1: TS_XX_REVENUE_WGS_CSBD_EDIT_ID_EOB_CODE_sur (original pattern)
        # Pattern 2: TS_XX_Revenue code Services not payable on Facility claim Sub Edit X_WGS_CSBD_RULEREVE00000X_00W28_sur (new pattern)
        # Supports 1-3 digit TS numbers: TS_1, TS_01, TS_001, TS_10, TS_100, etc.
        # Supports any alphanumeric edit_id and EOB code formats
        # Examples: TS_60_REVENUE_WGS_CSBD_ASDFGJEUSK_00W29_sur, TS_07_REVENUE_WGS_CSBD_rvn011_00W11_sur
        # Examples: TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_sur
        
        # Try CSBD_TS pattern first (for CSBD_TS_48, CSBD_TS_50, etc.)
        match = re.match(r'CSBD_TS_(\d{1,3})_(.+?)_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)

        # Try CSBDTS patterns (without underscore between CSBD and TS) - try these before TS patterns
        # Use a general pattern that captures the model name between TS number and WGS_CSBD
        if not match:
            match = re.match(r'CSBDTS_(\d{1,3})_(.+?)_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)

        # Try original pattern if no match
        if not match:
            match = re.match(r'TS_(\d{1,3})_REVENUE_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # STAGE 4.2: Try multiple regex patterns until one matches
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
        
        # If no match, try Laterality Policy pattern with "_sur copy" suffix
        if not match:
            match = re.match(r'TS_(\d{1,3})_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur copy$', folder_name)
        
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
        
        # If no match, try RadioservicesbilledwithoutRadiopharma pattern
        if not match:
            match = re.match(r'TS_(\d{1,3})_RadioservicesbilledwithoutRadiopharma_WGS_CSBD_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # If no match and this is WGS_Kernal, try NYKTS patterns
        if not match and is_wgs_kernal:
            # NYKTS pattern: NYKTS_130_Observation_Services_WGS_NYK_RULERCTH00001_00W28_sur
            # Also matches: NYKTS_122_Revenue code to HCPCS Alignment edit_WGS_NYK_RULERCTH00001_00W26_sur
            match = re.match(r'NYKTS_(\d{1,3})_(.+?)_WGS_NYK_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)

        # If no match and this is GBDF, try GBDF MCR patterns
        if not match and is_gbdf:
            # Try Covid GBDF MCR pattern
            match = re.match(r'TS_(\d{1,3})_Covid_gbdf_mcr_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try Multiple E&M Same day GBDF MCR pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_Multiple E&M Same day_gbdf_mcr_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try Multiple E&M Same day GBDF GRS pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_Multiple E&M Same day_gbdf_grs_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try NDC UOM Validation Edit Expansion Iprep-138 GBDF MCR pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try No match of Procedure code GBDF MCR pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_No match of Procedure code_gbdf_mcr_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try No match of Procedure code GBDF GRS pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_No match of Procedure code_gbdf_grs_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try Nebulizer A52466 IPERP-132 GBDF MCR pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_Nebulizer A52466 IPERP-132_gbdf_mcr_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try Nebulizer A52466 IPERP-132 GBDF GRS pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_Nebulizer A52466 IPERP-132_gbdf_grs_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try Unspecified_dx_code_outpt GBDF MCR pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_Unspecified_dx_code_outpt_gbdf_mcr_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try Unspecified_dx_code_outpt GBDF GRS pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_Unspecified_dx_code_outpt_gbdf_grs_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try Unspecified_dx_code_prof GBDF MCR pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_Unspecified_dx_code_prof_gbdf_mcr_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
            
            # Try Unspecified_dx_code_prof GBDF GRS pattern
            if not match:
                match = re.match(r'TS_(\d{1,3})_Unspecified_dx_code_prof_gbdf_grs_([A-Za-z0-9]+)_([A-Za-z0-9]+)_sur$', folder_name)
        
        # STAGE 5: Process successfully matched folders
        if match:
            # Extract the components from the folder name
            if folder_name.startswith("NYKTS_"):
                # NYKTS pattern: NYKTS_130_Observation_Services_WGS_NYK_RULERCTH00001_00W28_sur
                # Also matches: NYKTS_122_Revenue code to HCPCS Alignment edit_WGS_NYK_RULERCTH00001_00W26_sur
                ts_number_raw = match.group(1)  # TS number (e.g., "130", "122")
                model_name = match.group(2)     # Model name (e.g., "Observation_Services", "Revenue code to HCPCS Alignment edit")
                edit_id = match.group(3)        # Edit ID (e.g., "RULERCTH00001")
                code = match.group(4)           # Code (e.g., "00W28", "00W26")
            elif folder_name.startswith("CSBD_TS_") or folder_name.startswith("CSBDTS_"):
                # CSBD_TS or CSBDTS pattern: CSBD_TS_48_Revenue code to HCPCS Alignment edit_WGS_CSBD_RULERCTH00001_00W26_sur
                # or CSBDTS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_sur
                ts_number_raw = match.group(1)  # TS number (e.g., "48", "02")
                model_name = match.group(2)     # Model name (e.g., "Revenue code to HCPCS Alignment edit", "Laterality Policy-Disgnosis to Diagnosis")
                edit_id = match.group(3)        # Edit ID (e.g., "RULERCTH00001", "RULELATE000001")
                code = match.group(4)           # Code (e.g., "00W26", "00W17")
            else:
                # Standard TS pattern: TS_01_REVENUE_WGS_CSBD_RULEEM000001_W04_sur
                ts_number_raw = match.group(1)  # TS number (e.g., "1", "01", "47")
                edit_id = match.group(2)        # Edit ID (e.g., "RULEEM000001")
                code = match.group(3)           # Code (e.g., "v04", "00W28")
            
            # Normalize TS number to handle different digit patterns
            ts_number = normalize_ts_number(ts_number_raw)
            
            # STAGE 5.1: Validate folder structure and handle both regression and smoke folders
            # Check if payloads directory exists (for both WGS_CSBD and GBDF models)
            payloads_path = os.path.join(folder_path, "payloads")
            has_payloads_structure = os.path.exists(payloads_path)

            if has_payloads_structure:
                # Both WGS_CSBD and GBDF models with payloads/regression and payloads/smoke structure
                regression_path = os.path.join(payloads_path, "regression")
                smoke_path = os.path.join(payloads_path, "smoke")

                has_regression = os.path.exists(regression_path)
                has_smoke = os.path.exists(smoke_path)

                if not has_regression and not has_smoke:
                    print(f"Warning: Neither regression nor smoke folders found in {folder_name}/payloads")
                    continue

                # Create model configs for each existing folder
                folder_configs = []
                if has_regression:
                    folder_configs.append(("regression", regression_path))
                if has_smoke:
                    folder_configs.append(("smoke", smoke_path))

            else:
                # Legacy structure: direct regression folder (for older models without payloads)
                regression_path = os.path.join(folder_path, "regression")
                if not os.path.exists(regression_path):
                    print(f"Warning: Regression folder not found in {folder_name}")
                    continue
                folder_configs = [("regression", regression_path)]

            # STAGE 5.2: Generate destination directory names
            # Handle "payloads_sur", "ayloads_sur" (typo), and "_sur" patterns
            if "_payloads_sur" in folder_name:
                dest_folder_name = folder_name.replace("_payloads_sur", "_payloads_dis")
            elif "_ayloads_sur" in folder_name:
                dest_folder_name = folder_name.replace("_ayloads_sur", "_payloads_dis")
            elif "_sur" in folder_name:
                dest_folder_name = folder_name.replace("_sur", "_dis")
            else:
                dest_folder_name = folder_name  # fallback

            # Process each folder configuration
            for folder_type, source_path in folder_configs:
                # Generate destination directory based on model type and folder structure
                if is_wgs_kernal:
                    # WGS_NYK models go to WGS_KERNAL subdirectory
                    if has_payloads_structure:
                        dest_dir = os.path.join("renaming_jsons", "WGS_KERNAL", dest_folder_name, "payloads", folder_type)
                    else:
                        dest_dir = os.path.join("renaming_jsons", "WGS_KERNAL", dest_folder_name, folder_type)
                elif is_gbdf:
                    # GBDF models go to GBDF subdirectory
                    if has_payloads_structure:
                        dest_dir = os.path.join("renaming_jsons", "GBDF", dest_folder_name, "payloads", folder_type)
                    else:
                        dest_dir = os.path.join("renaming_jsons", "GBDF", dest_folder_name, folder_type)
                elif use_wgs_csbd_destination:
                    # WGS_CSBD models with flag go to WGS_CSBD subdirectory
                    if has_payloads_structure and not is_gbdf:
                        dest_dir = os.path.join("renaming_jsons", "WGS_CSBD", dest_folder_name, "payloads", folder_type)
                    else:
                        dest_dir = os.path.join("renaming_jsons", "WGS_CSBD", dest_folder_name, folder_type)
                else:
                    # Default to renaming_jsons root
                    if has_payloads_structure and not is_gbdf:
                        dest_dir = os.path.join("renaming_jsons", dest_folder_name, "payloads", folder_type)
                    else:
                        dest_dir = os.path.join("renaming_jsons", dest_folder_name, folder_type)
                
                # STAGE 5.3: Generate Postman collection and file names based on model type
                # Generate Postman collection name with flexible formatting
                # For CSBD_TS models, use the full descriptive name
                # CSBDTS models will be handled by the elif checks below (e.g., "Covid", "Laterality Policy")
                if folder_name.startswith("NYKTS_"):
                    # NYKTS pattern: Use the dynamic model name from the folder (extracted at line 345)
                    # model_name was extracted from regex match and can be "Observation_Services", 
                    # "Revenue code to HCPCS Alignment edit", "add_on without base", etc.
                    model_name_clean = model_name.replace(' ', '_').replace('-', '_')
                    base_collection_name = f"NYKTS_{ts_number}_{model_name_clean}_Collection"
                    base_file_name = f"{model_name.lower().replace(' ', '_').replace('-', '_')}_wgs_nyk_{edit_id}_{code}"
                elif folder_name.startswith("CSBD_TS_"):
                    # CSBD_TS pattern: Use the model name from the folder
                    base_collection_name = f"CSBD_TS_{ts_number}_{model_name}_Collection"
                    base_file_name = f"{model_name.lower().replace(' ', '_').replace('-', '_').replace('to', 'to').replace('alignment', 'alignment')}_wgs_csbd_{edit_id}_{code}"
                elif "Revenue code Services not payable on Facility claim" in folder_name:
                    # Extract the Sub Edit number and create proper collection name
                    sub_edit_match = re.search(r'Sub Edit (\d+)', folder_name)
                    if sub_edit_match:
                        sub_edit_num = sub_edit_match.group(1)
                        base_collection_name = f"TS_{ts_number}_Revenue code Services not payable on Facility claim Sub Edit {sub_edit_num}_Collection"
                    else:
                        base_collection_name = generate_postman_collection_name(ts_number)
                    base_file_name = f"revenue_wgs_csbd_{edit_id}_{code}"
                elif "Lab panel Model" in folder_name:
                    # For Lab panel Model, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Lab panel Model_Collection"
                    base_file_name = f"lab_wgs_csbd_{edit_id}_{code}"
                elif "Recovery Room Reimbursement" in folder_name:
                    # For Recovery Room Reimbursement, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Recovery Room Reimbursement_Collection"
                    base_file_name = f"recovery_wgs_csbd_{edit_id}_{code}"
                elif "Covid" in folder_name:
                    # For Covid, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Covid_Collection"
                    base_file_name = f"covid_wgs_csbd_{edit_id}_{code}"
                elif "Laterality Policy" in folder_name:
                    # For Laterality Policy, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Laterality_Collection"
                    base_file_name = f"laterality_wgs_csbd_{edit_id}_{code}"
                elif "Device Dependent Procedures" in folder_name:
                    # For Device Dependent Procedures, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Device Dependent Procedures_Collection"
                    base_file_name = f"device_wgs_csbd_{edit_id}_{code}"
                elif "revenue model" in folder_name:
                    # For revenue model, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_revenue model_Collection"
                    base_file_name = f"revenue_wgs_csbd_{edit_id}_{code}"
                elif "Revenue Code to HCPCS Xwalk-1B" in folder_name:
                    # For Revenue Code to HCPCS Xwalk-1B, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Revenue Code to HCPCS Xwalk-1B_Collection"
                    base_file_name = f"revenue_wgs_csbd_{edit_id}_{code}"
                elif "Incidentcal Services Facility" in folder_name:
                    # For Incidentcal Services Facility, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Incidentcal Services Facility_Collection"
                    base_file_name = f"incidentcal_wgs_csbd_{edit_id}_{code}"
                elif "Revenue model CR v3" in folder_name:
                    # For Revenue model CR v3, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Revenue model CR v3_Collection"
                    base_file_name = f"revenue_model_wgs_csbd_{edit_id}_{code}"
                elif "HCPCS to Revenue Code Xwalk" in folder_name:
                    # For HCPCS to Revenue Code Xwalk, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_HCPCS to Revenue Code Xwalk_Collection"
                    base_file_name = f"hcpcs_wgs_csbd_{edit_id}_{code}"
                elif "Multiple E&M Same day" in folder_name and not is_gbdf:
                    # For Multiple E&M Same day (WGS_CSBD), use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Multiple E&M Same day_Collection"
                    base_file_name = f"multiple_em_wgs_csbd_{edit_id}_{code}"
                elif "Multiple Billing of Obstetrical Services" in folder_name:
                    # For Multiple Billing of Obstetrical Services, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Multiple Billing of Obstetrical Services_Collection"
                    base_file_name = f"multiple_billing_obstetrical_wgs_csbd_{edit_id}_{code}"
                elif "RadioservicesbilledwithoutRadiopharma" in folder_name:
                    # For RadioservicesbilledwithoutRadiopharma, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_RadioservicesbilledwithoutRadiopharma_Collection"
                    base_file_name = f"radioservices_wgs_csbd_{edit_id}_{code}"
                elif "Revenue code to HCPCS Alignment edit" in folder_name:
                    # For CSBD_TS48 style models, use the full descriptive name
                    base_collection_name = f"CSBD_TS_{ts_number}_Revenue code to HCPCS Alignment edit_Collection"
                    base_file_name = f"revenue_hcpcs_alignment_wgs_csbd_{edit_id}_{code}"
                elif "Observation_Services" in folder_name:
                    # For CSBDTS Observation Services models, use the full descriptive name
                    base_collection_name = f"CSBDTS_{ts_number}_Observation_Services_Collection"
                    base_file_name = f"observation_services_wgs_csbd_{edit_id}_{code}"
                elif "Covid_gbdf_mcr" in folder_name:
                    # For GBDF MCR Covid, use the full descriptive name
                    base_collection_name = f"TS_{ts_number}_Covid_gbdf_mcr_Collection"
                    base_file_name = f"covid_gbdf_mcr_{edit_id}_{code}"
                elif "Multiple E&M Same day" in folder_name and is_gbdf:
                    # For any GBDF Multiple E&M Same day model, use GBDF naming
                    if "gbdf_mcr" in folder_name:
                        base_collection_name = f"TS_{ts_number}_Multiple E&M Same day_gbdf_mcr_Collection"
                        base_file_name = f"multiple_em_gbdf_mcr_{edit_id}_{code}"
                    elif "gbdf_grs" in folder_name:
                        base_collection_name = f"TS_{ts_number}_Multiple E&M Same day_gbdf_grs_Collection"
                        base_file_name = f"multiple_em_gbdf_grs_{edit_id}_{code}"
                    else:
                        base_collection_name = f"TS_{ts_number}_Multiple E&M Same day_gbdf_Collection"
                        base_file_name = f"multiple_em_gbdf_{edit_id}_{code}"
                elif "NDC UOM Validation Edit Expansion Iprep-138" in folder_name and is_gbdf:
                    # For NDC UOM Validation Edit Expansion Iprep-138 models, use GBDF naming
                    if "gbdf_mcr" in folder_name:
                        base_collection_name = f"TS_{ts_number}_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_Collection"
                        base_file_name = f"ndc_uom_gbdf_mcr_{edit_id}_{code}"
                    elif "gbdf_grs" in folder_name:
                        base_collection_name = f"TS_{ts_number}_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_Collection"
                        base_file_name = f"ndc_uom_gbdf_grs_{edit_id}_{code}"
                    else:
                        base_collection_name = f"TS_{ts_number}_NDC UOM Validation Edit Expansion Iprep-138_gbdf_Collection"
                        base_file_name = f"ndc_uom_gbdf_{edit_id}_{code}"
                elif "No match of Procedure code" in folder_name and is_gbdf:
                    # For No match of Procedure code models, use GBDF naming
                    if "gbdf_mcr" in folder_name:
                        base_collection_name = f"TS_{ts_number}_No match of Procedure code_gbdf_mcr_Collection"
                        base_file_name = f"no_match_procedure_gbdf_mcr_{edit_id}_{code}"
                    elif "gbdf_grs" in folder_name:
                        base_collection_name = f"TS_{ts_number}_No match of Procedure code_gbdf_grs_Collection"
                        base_file_name = f"no_match_procedure_gbdf_grs_{edit_id}_{code}"
                    else:
                        base_collection_name = f"TS_{ts_number}_No match of Procedure code_gbdf_Collection"
                        base_file_name = f"no_match_procedure_gbdf_{edit_id}_{code}"
                elif "Nebulizer A52466 IPERP-132" in folder_name and is_gbdf:
                    # For Nebulizer A52466 IPERP-132 models, use GBDF naming
                    if "gbdf_mcr" in folder_name:
                        base_collection_name = f"TS_{ts_number}_Nebulizer A52466 IPERP-132_gbdf_mcr_Collection"
                        base_file_name = f"nebulizer_gbdf_mcr_{edit_id}_{code}"
                    elif "gbdf_grs" in folder_name:
                        base_collection_name = f"TS_{ts_number}_Nebulizer A52466 IPERP-132_gbdf_grs_Collection"
                        base_file_name = f"nebulizer_gbdf_grs_{edit_id}_{code}"
                    else:
                        base_collection_name = f"TS_{ts_number}_Nebulizer A52466 IPERP-132_gbdf_Collection"
                        base_file_name = f"nebulizer_gbdf_{edit_id}_{code}"
                elif "Unspecified_dx_code_outpt" in folder_name and is_gbdf:
                    # For Unspecified_dx_code_outpt models, use GBDF naming
                    if "gbdf_mcr" in folder_name:
                        base_collection_name = f"TS_{ts_number}_Unspecified_dx_code_outpt_gbdf_mcr_Collection"
                        base_file_name = f"unspecified_dx_code_outpt_gbdf_mcr_{edit_id}_{code}"
                    elif "gbdf_grs" in folder_name:
                        base_collection_name = f"TS_{ts_number}_Unspecified_dx_code_outpt_gbdf_grs_Collection"
                        base_file_name = f"unspecified_dx_code_outpt_gbdf_grs_{edit_id}_{code}"
                    else:
                        base_collection_name = f"TS_{ts_number}_Unspecified_dx_code_outpt_gbdf_Collection"
                        base_file_name = f"unspecified_dx_code_outpt_gbdf_{edit_id}_{code}"
                elif "Unspecified_dx_code_prof" in folder_name and is_gbdf:
                    # For Unspecified_dx_code_prof models, use GBDF naming
                    if "gbdf_mcr" in folder_name:
                        base_collection_name = f"TS_{ts_number}_Unspecified_dx_code_prof_gbdf_mcr_Collection"
                        base_file_name = f"unspecified_dx_code_prof_gbdf_mcr_{edit_id}_{code}"
                    elif "gbdf_grs" in folder_name:
                        base_collection_name = f"TS_{ts_number}_Unspecified_dx_code_prof_gbdf_grs_Collection"
                        base_file_name = f"unspecified_dx_code_prof_gbdf_grs_{edit_id}_{code}"
                    else:
                        base_collection_name = f"TS_{ts_number}_Unspecified_dx_code_prof_gbdf_Collection"
                        base_file_name = f"unspecified_dx_code_prof_gbdf_{edit_id}_{code}"
                else:
                    base_collection_name = generate_postman_collection_name(ts_number)
                    base_file_name = f"revenue_wgs_csbd_{edit_id}_{code}"

                # Customize names based on folder type (regression/smoke)
                if folder_type == "smoke":
                    postman_collection_name = base_collection_name
                    postman_file_name = f"{base_file_name}_smoke.json"
                else:
                    postman_collection_name = base_collection_name
                    postman_file_name = f"{base_file_name}_regression.json"

                # STAGE 5.4: Create model configuration dictionary
                model_config = {
                    "ts_number": ts_number,
                    "ts_number_raw": ts_number_raw,  # Keep original for reference
                    "edit_id": edit_id,
                    "code": code,
                    "source_dir": source_path,
                    "dest_dir": dest_dir,
                    "postman_collection_name": postman_collection_name,
                    "postman_file_name": postman_file_name,
                    "folder_name": folder_name,
                    "folder_type": folder_type  # Add folder type for reference
                }

                # Add the model to our list and display success message
                models.append(model_config)
                print(f"Discovered: TS_{ts_number} ({edit_id}_{code}) [{folder_type}] [Raw: {ts_number_raw}]")
        else:
            # STAGE 5.5: Handle unmatched folders
            print(f"Warning: Could not parse folder name: {folder_name}")
    
    # STAGE 6: Return all discovered models
    return models


# STAGE 7: Utility Functions
# These functions provide convenient ways to access and validate model data

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


# STAGE 8: Display and Output Functions
# These functions format and display the discovered models in various ways

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
    print("NESTED MODEL STRUCTURE")
    print("=" * 80)
    
    # STAGE 8.1: Discover models from both WGS_CSBD and GBDF directories
    # Get WGS_CSBD models
    wgs_csbd_models = discover_ts_folders("source_folder/WGS_CSBD", use_wgs_csbd_destination=True)
    
    # Get GBDF models
    gbdf_models = discover_ts_folders("source_folder/GBDF", use_wgs_csbd_destination=False)
    
    total_models = len(wgs_csbd_models) + len(gbdf_models)
    
    print(f"Total Models Found: {total_models}")
    print("=" * 80)
    
    # STAGE 8.2: Display WGS_CSBD models with categorized formatting
    if wgs_csbd_models:
        print(f"\nWGS_CSBD MODELS ({len(wgs_csbd_models)} models)")
        print("-" * 50)
        
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
            elif "Observation_Services" in collection_name:
                model_type = "Observation Services"
            elif "revenue model" in collection_name:
                model_type = "Revenue Model"
            
            print(f"  {i:2d}. TS_{ts_number:02s} | {model_type}")
            print(f"      |- Edit ID: {edit_id}")
            print(f"      |- Code: {code}")
            print(f"      `- Collection: {collection_name}")
            print()
    else:
        print(f"\nWGS_CSBD MODELS (0 models)")
        print("-" * 50)
        print("   No WGS_CSBD models found")
    
    # STAGE 8.3: Display GBDF models with categorized formatting
    if gbdf_models:
        print(f"\nGBDF MODELS ({len(gbdf_models)} models)")
        print("-" * 50)
        
        for i, model in enumerate(gbdf_models, 1):
            ts_number = model['ts_number']
            edit_id = model['edit_id']
            code = model['code']
            collection_name = model['postman_collection_name']
            
            # Extract model type from collection name for better display
            model_type = "General"
            if "Covid_gbdf_mcr" in collection_name or "Covid" in collection_name:
                model_type = "Covid GBDF MCR"
            elif "Multiple E&M Same day_gbdf_mcr" in collection_name:
                model_type = "Multiple E&M Same day GBDF MCR"
            elif "Multiple E&M Same day_gbdf_grs" in collection_name:
                model_type = "Multiple E&M Same day GBDF GRS"
            elif "Multiple E&M Same day" in collection_name and "gbdf" in collection_name.lower():
                model_type = "Multiple E&M Same day GBDF"
            elif "Unspecified_dx_code_outpt_gbdf_mcr" in collection_name:
                model_type = "Unspecified dx code outpt GBDF MCR"
            elif "Unspecified_dx_code_outpt_gbdf_grs" in collection_name:
                model_type = "Unspecified dx code outpt GBDF GRS"
            elif "Unspecified_dx_code_outpt" in collection_name and "gbdf" in collection_name.lower():
                model_type = "Unspecified dx code outpt GBDF"
            elif "Unspecified_dx_code_prof_gbdf_mcr" in collection_name:
                model_type = "Unspecified dx code prof GBDF MCR"
            elif "Unspecified_dx_code_prof_gbdf_grs" in collection_name:
                model_type = "Unspecified dx code prof GBDF GRS"
            elif "Unspecified_dx_code_prof" in collection_name and "gbdf" in collection_name.lower():
                model_type = "Unspecified dx code prof GBDF"
            
            print(f"  {i:2d}. TS_{ts_number:02s} | {model_type}")
            print(f"      |- Edit ID: {edit_id}")
            print(f"      |- Code: {code}")
            print(f"      `- Collection: {collection_name}")
            print()
    else:
        print(f"\nGBDF MODELS (0 models)")
        print("-" * 50)
        print("   No GBDF models found")
    
    # STAGE 8.4: Display summary and usage examples
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"WGS_CSBD Models: {len(wgs_csbd_models)}")
    print(f"GBDF Models: {len(gbdf_models)}")
    print(f"Total Models: {total_models}")
    
    if total_models > 0:
        print(f"\nUSAGE EXAMPLES:")
        print("-" * 30)
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


# STAGE 9: Main Execution Block
# This section runs when the script is executed directly (not imported)

if __name__ == "__main__":
    # Test the discovery system
    print("Testing Dynamic Model Discovery")
    print("=" * 50)
    
    # Show nested display
    print_nested_models_display()
    
    # Also show traditional display for comparison
    print("\n" + "=" * 50)
    print("TRADITIONAL DISPLAY")
    print("=" * 50)
    
    models = discover_ts_folders()
    print_discovered_models(models)
    
    # Test specific TS number lookup
    if models:
        first_model = models[0]
        ts_number = first_model["ts_number"]
        print(f"Testing lookup for TS_{ts_number}...")
        
        found_model = get_model_by_ts_number(ts_number)
        if found_model:
            print(f"Found model: {found_model['edit_id']}_{found_model['code']}")
        else:
            print(f"Model not found for TS_{ts_number}")
