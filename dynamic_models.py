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


def discover_ts_folders(base_dir: str = ".") -> List[Dict]:
    """
    Discover all TS_XX_REVENUE_WGS_CSBD_* folders and extract model parameters.
    Supports flexible digit patterns: TS01-TS09, TS10-TS99, TS100-TS999
    
    Args:
        base_dir: Base directory to search for TS folders
        
    Returns:
        List of model configurations extracted from folder names
    """
    models = []
    
    # Pattern to match TS_XX_REVENUE_WGS_CSBD_* folders
    # Handle both "payloads_sur" and "_sur" patterns
    pattern1 = os.path.join(base_dir, "TS_*_REVENUE_WGS_CSBD_*_payloads_sur")
    pattern2 = os.path.join(base_dir, "TS_*_REVENUE_WGS_CSBD_*_ayloads_sur")
    pattern3 = os.path.join(base_dir, "TS_*_REVENUE_WGS_CSBD_*_sur")
    ts_folders = glob.glob(pattern1) + glob.glob(pattern2) + glob.glob(pattern3)
    
    print(f"🔍 Scanning for TS folders in: {base_dir}")
    print(f"📁 Found {len(ts_folders)} TS folders")
    
    for folder_path in ts_folders:
        folder_name = os.path.basename(folder_path)
        
        # Extract parameters using regex with flexible digit patterns
        # Pattern: TS_XX_REVENUE_WGS_CSBD_rvnXXX_00WX_payloads_sur or TS_XX_REVENUE_WGS_CSBD_rvnXXX_00WX_ayloads_sur or TS_XX_REVENUE_WGS_CSBD_rvnXXX_00WX_sur
        # Supports 1-3 digit TS numbers: TS_1, TS_01, TS_001, TS_10, TS_100, etc.
        match = re.match(r'TS_(\d{1,3})_REVENUE_WGS_CSBD_(rvn\d+)_(00W\d+)_sur$', folder_name)
        
        if match:
            ts_number_raw = match.group(1)
            edit_id = match.group(2)
            code = match.group(3)
            
            # Normalize TS number to handle different digit patterns
            ts_number = normalize_ts_number(ts_number_raw)
            
            # Check if regression subfolder exists
            regression_path = os.path.join(folder_path, "regression")
            if not os.path.exists(regression_path):
                print(f"⚠️  Warning: Regression folder not found in {folder_name}")
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
            dest_dir = os.path.join("renaming_jsons", dest_folder_name, "regression")
            
            # Generate Postman collection name with flexible formatting
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
            print(f"✅ Discovered: TS_{ts_number} ({edit_id}_{code}) [Raw: {ts_number_raw}]")
        else:
            print(f"⚠️  Warning: Could not parse folder name: {folder_name}")
    
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
            print(f"❌ Missing required field: {field}")
            return False
    
    # Check if source directory exists
    if not os.path.exists(model["source_dir"]):
        print(f"❌ Source directory does not exist: {model['source_dir']}")
        return False
    
    return True


def print_discovered_models(models: List[Dict]):
    """
    Print a formatted list of discovered models.
    
    Args:
        models: List of model configurations
    """
    if not models:
        print("❌ No TS models discovered")
        return
    
    print(f"\n📋 DISCOVERED TS MODELS ({len(models)} found)")
    print("=" * 60)
    
    for i, model in enumerate(models, 1):
        print(f"{i}. TS_{model['ts_number']}: {model['edit_id']}_{model['code']}")
        print(f"   📁 Source: {model['source_dir']}")
        print(f"   📁 Dest:   {model['dest_dir']}")
        print(f"   📦 Collection: {model['postman_collection_name']}")
        print()


if __name__ == "__main__":
    # Test the discovery system
    print("🧪 Testing Dynamic Model Discovery")
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
