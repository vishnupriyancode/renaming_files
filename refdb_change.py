#!/usr/bin/env python3
"""
refdb_change.py - Replace specific values in JSON files with user-provided values

This module provides refdb value replacement functionality for refdb-specific models.
It is primarily used by main_processor.py when the --refdb flag is specified.

This script replaces the following variables in JSON files:
- HCID
- PAT_BRTH_DT
- PAT_FRST_NME
- PAT_LAST_NM
- PROV_TAX_ID
- BILLG_NPI
- NAT_EA2_RNDR_NPI

Note: This module is integrated into main_processor.py. Use the following command:
  python main_processor.py --wgs_csbd --CSBDTS46 --refdb
  python main_processor.py --wgs_nyk --NYKTS123 --refdb

Currently supported refdb models:
- wgs_csbd: CSBDTS_46, CSBDTS_47
- wgs_kernal: NYKTS_123

Path patterns: CSBDTS_XX_* (for wgs_csbd) or NYKTS_XX_* (for wgs_kernal)
Values are loaded from refdb_values.json based on the specified model.
"""

import json
import os
import sys
import argparse
import re
from pathlib import Path
from typing import Dict, Optional, List

# Fix Windows encoding issues for Unicode characters in print statements
if sys.platform == 'win32':
    try:
        # Set UTF-8 encoding for stdout and stderr on Windows
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8')
    except (AttributeError, ValueError):
        # Fallback: if reconfigure is not available, try to set encoding via environment
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# List of refdb-specific TS numbers that support refdb value replacement
# Only files from these TS numbers will be processed by this script
# Example refdb models: TS_46 (Multiple E&M Same day), TS_47 (Multiple Billing of Obstetrical Services)
# To add more refdb models, add their TS numbers to the appropriate list below
REFDB_TS_NUMBERS = {
    "wgs_csbd": ["46", "47","59"],  # TS_46: Multiple E&M Same day, TS_47: Multiple Billing of Obstetrical Services, TS_59: Antepartum Services
    "wgs_kernal": ["123"]  # NYKTS_123: Observation Services
}


def load_default_values(model: str, config_file: Optional[Path] = None) -> Dict[str, str]:
    """
    Load default values from JSON configuration file for a specific model.
    Creates the file with a template if it doesn't exist.
    
    Args:
        model: Model name (must be 'wgs_csbd' or 'wgs_kernal')
        config_file: Path to the JSON config file. If None, looks for refdb_values.json
                     in the same directory as the script.
        
    Returns:
        Dictionary of default values for the specified model
        
    Raises:
        SystemExit: If the config file has invalid JSON, cannot be read, or model is invalid
    """
    # Validate model
    valid_models = ["wgs_csbd", "wgs_kernal"]
    if model not in valid_models:
        print(f"Error: Invalid model '{model}'. Valid models are: {', '.join(valid_models)}")
        sys.exit(1)
    
    if config_file is None:
        # Look for refdb_values.json in the same directory as this script
        script_dir = Path(__file__).parent
        config_file = script_dir / "refdb_values.json"
    
    # Template structure for the config file
    template_values = {
        "HCID": "",
        "PAT_BRTH_DT": "",
        "PAT_FRST_NME": "",
        "PAT_LAST_NM": "",
        "PROV_TAX_ID": "",
        "BILLG_NPI": "",
        "NAT_EA2_RNDR_NPI": ""
    }
    
    # Template structure with both models
    template_config = {
        "wgs_csbd": template_values.copy(),
        "wgs_kernal": template_values.copy()
    }
    
    # Create file with template if it doesn't exist
    if not config_file.exists():
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(template_config, f, indent=2, ensure_ascii=False)
            print(f"Created config file template: {config_file}")
            print("Please fill in the values for each model in the config file and run the script again.")
            sys.exit(1)
        except Exception as e:
            print(f"Error: Cannot create config file {config_file}: {e}")
            sys.exit(1)
    
    # Try to load from JSON file
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        
        # Validate structure - should be a dict with model keys
        if not isinstance(config_data, dict):
            print(f"Error: Config file {config_file} must contain a JSON object with model keys.")
            sys.exit(1)
        
        # Check if model exists in config
        if model not in config_data:
            print(f"Error: Model '{model}' not found in {config_file}")
            print(f"Available models: {', '.join(config_data.keys())}")
            sys.exit(1)
        
        values = config_data[model]
        
        if not isinstance(values, dict):
            print(f"Error: Model '{model}' in {config_file} must contain a JSON object.")
            sys.exit(1)
        
        # Validate that all required keys exist
        missing_keys = set(template_values.keys()) - set(values.keys())
        if missing_keys:
            print(f"Error: Missing required keys for model '{model}' in {config_file}: {', '.join(missing_keys)}")
            sys.exit(1)
        
        # Check if any values are empty
        empty_keys = [key for key, value in values.items() if not value or (isinstance(value, str) and value.strip() == "")]
        if empty_keys:
            print(f"Warning: Empty values found for model '{model}' in {config_file} for: {', '.join(empty_keys)}")
            print("These fields will not be replaced in target JSON files.")
        
        print(f"Loaded default values for model '{model}' from: {config_file}")
        return values
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {config_file}: {e}")
        print("Please fix the JSON syntax and try again.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Cannot read {config_file}: {e}")
        sys.exit(1)


# Global variable to store default values (loaded at runtime)
DEFAULT_VALUES = {}


def get_user_input(default_values: Dict[str, str]) -> Dict[str, str]:
    """
    Prompt user for replacement values interactively.
    
    Args:
        default_values: Dictionary of default values to use as prompts
        
    Returns:
        Dictionary with the values to replace
    """
    replacements = {}
    
    print("\n" + "="*60)
    print("JSON Value Replacement Tool")
    print("="*60)
    print("\nEnter new values for each field (press Enter to keep default):\n")
    
    for key, default_value in default_values.items():
        user_input = input(f"{key} (default: {default_value}): ").strip()
        replacements[key] = user_input if user_input else default_value
    
    return replacements


def replace_values_in_json(data: dict, replacements: Dict[str, str]) -> tuple[dict, int]:
    """
    Recursively search and replace values in JSON data structure.
    
    Args:
        data: The JSON data (dict or list)
        replacements: Dictionary of key-value pairs to replace
        
    Returns:
        Tuple of (modified_data, count_of_replacements)
    """
    count = 0
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key in replacements:
                if isinstance(value, str):
                    data[key] = replacements[key]
                    count += 1
                    print(f"  Replaced {key}: '{value}' -> '{replacements[key]}'")
            elif isinstance(value, (dict, list)):
                sub_data, sub_count = replace_values_in_json(value, replacements)
                data[key] = sub_data
                count += sub_count
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, (dict, list)):
                sub_data, sub_count = replace_values_in_json(item, replacements)
                data[i] = sub_data
                count += sub_count
    
    return data, count


def extract_ts_number_from_path(file_path: Path, model: str) -> Optional[str]:
    """
    Extract TS number from file path or directory structure.
    Only recognizes CSBDTS_XX_ for wgs_csbd and NYKTS_XX_ for wgs_kernal.
    
    Args:
        file_path: Path to the JSON file or directory
        model: Model type (wgs_csbd or wgs_kernal)
        
    Returns:
        TS number as string if found, None otherwise
    """
    path_str = str(file_path)
    
    # Model-specific patterns only
    if model == "wgs_csbd":
        # Only CSBDTS_XX_ pattern for wgs_csbd models
        pattern = r'CSBDTS_(\d{1,3})_'  # CSBDTS_46_, CSBDTS_47_, etc.
        match = re.search(pattern, path_str)
        if match:
            return match.group(1)
    elif model == "wgs_kernal":
        # Only NYKTS_XX_ pattern for wgs_kernal models
        pattern = r'NYKTS_(\d{1,3})_'  # NYKTS_122_, NYKTS_123_, etc.
        match = re.search(pattern, path_str)
        if match:
            return match.group(1)
    
    return None


def validate_refdb_model(file_path: Path, model: str) -> bool:
    """
    Validate if the file path belongs to a refdb-specific model.
    
    Args:
        file_path: Path to the JSON file or directory
        model: Model type (wgs_csbd or wgs_kernal)
        
    Returns:
        True if the path belongs to a refdb model, False otherwise
    """
    ts_number = extract_ts_number_from_path(file_path, model)
    
    if ts_number is None:
        return False
    
    # Check if TS number is in the refdb list for this model
    if model in REFDB_TS_NUMBERS:
        return ts_number in REFDB_TS_NUMBERS[model]
    
    return False


def process_json_file(file_path: Path, replacements: Dict[str, str], backup: bool = True, model: str = None) -> bool:
    """
    Process a single JSON file and replace values.
    Only processes files from refdb-specific models (e.g., TS_46, TS_47 for wgs_csbd).
    
    Args:
        file_path: Path to the JSON file
        replacements: Dictionary of key-value pairs to replace
        backup: Whether to create a backup file
        model: Model type for validation (required for refdb validation)
        
    Returns:
        True if successful, False otherwise
    """
    # Validate refdb model - model is required for refdb processing
    if not model:
        print(f"  ✗ Error: Model parameter is required for refdb processing")
        return False
    
    # Strict validation: only process refdb-specific models
    if not validate_refdb_model(file_path, model):
        ts_number = extract_ts_number_from_path(file_path, model)
        refdb_models = REFDB_TS_NUMBERS.get(model, [])
        if ts_number:
            if model == "wgs_csbd":
                print(f"  ⚠ Skipping {file_path.name}: CSBDTS_{ts_number} is not a refdb-specific model")
                print(f"     Refdb models for {model}: CSBDTS_{', CSBDTS_'.join(refdb_models) if refdb_models else 'None configured'}")
            elif model == "wgs_kernal":
                print(f"  ⚠ Skipping {file_path.name}: NYKTS_{ts_number} is not a refdb-specific model")
                print(f"     Refdb models for {model}: NYKTS_{', NYKTS_'.join(refdb_models) if refdb_models else 'None configured'}")
        else:
            print(f"  ⚠ Skipping {file_path.name}: Could not determine TS number from path")
            if model == "wgs_csbd":
                print(f"     Expected path pattern: CSBDTS_XX_* (e.g., CSBDTS_46_, CSBDTS_47_)")
            elif model == "wgs_kernal":
                print(f"     Expected path pattern: NYKTS_XX_* (e.g., NYKTS_122_, NYKTS_123_)")
        return False
    
    try:
        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Create backup if requested
        if backup:
            backup_path = file_path.with_suffix(file_path.suffix + '.bak')
            with open(backup_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"  Backup created: {backup_path}")
        
        # Replace values
        print(f"\nProcessing: {file_path}")
        modified_data, count = replace_values_in_json(data, replacements)
        
        if count > 0:
            # Write the modified JSON back
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(modified_data, f, indent=2, ensure_ascii=False)
            print(f"  ✓ Successfully replaced {count} value(s)")
            return True
        else:
            print(f"  ⚠ No matching fields found to replace")
            return False
            
    except json.JSONDecodeError as e:
        print(f"  ✗ Error: Invalid JSON in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"  ✗ Error processing {file_path}: {e}")
        return False


def process_directory(directory: Path, replacements: Dict[str, str], 
                      recursive: bool = True, backup: bool = True, model: str = None) -> tuple[int, int]:
    """
    Process all JSON files in a directory.
    Only processes files from refdb-specific models.
    
    Args:
        directory: Path to the directory
        replacements: Dictionary of key-value pairs to replace
        recursive: Whether to process subdirectories recursively
        backup: Whether to create backup files
        model: Model type for validation (required for refdb processing)
        
    Returns:
        Tuple of (successful_count, failed_count)
    """
    if not model:
        print(f"Error: Model parameter is required for refdb processing")
        return 0, 1
    
    successful = 0
    failed = 0
    skipped = 0
    
    pattern = "**/*.json" if recursive else "*.json"
    
    json_files = list(directory.glob(pattern))
    
    if not json_files:
        print(f"No JSON files found in {directory}")
        return 0, 0
    
    print(f"\nFound {len(json_files)} JSON file(s) to process...")
    
    # Check if directory itself is a refdb model
    refdb_models = REFDB_TS_NUMBERS.get(model, [])
    is_refdb_dir = validate_refdb_model(directory, model)
    
    if not is_refdb_dir:
        ts_number = extract_ts_number_from_path(directory, model)
        if ts_number:
            if model == "wgs_csbd":
                print(f"\n⚠ Warning: Directory does not appear to be a refdb-specific model (CSBDTS_{ts_number})")
                print(f"   Refdb models for {model}: CSBDTS_{', CSBDTS_'.join(refdb_models) if refdb_models else 'None configured'}")
            elif model == "wgs_kernal":
                print(f"\n⚠ Warning: Directory does not appear to be a refdb-specific model (NYKTS_{ts_number})")
                print(f"   Refdb models for {model}: NYKTS_{', NYKTS_'.join(refdb_models) if refdb_models else 'None configured'}")
        else:
            print(f"\n⚠ Warning: Could not determine TS number from directory path")
            if model == "wgs_csbd":
                print(f"   Expected path pattern: CSBDTS_XX_* (e.g., CSBDTS_46_, CSBDTS_47_)")
            elif model == "wgs_kernal":
                print(f"   Expected path pattern: NYKTS_XX_* (e.g., NYKTS_122_, NYKTS_123_)")
        print("   Processing files individually - only refdb-specific files will be processed...\n")
    
    for json_file in json_files:
        result = process_json_file(json_file, replacements, backup, model)
        if result is True:
            successful += 1
        elif result is False:
            # Check if it was skipped due to not being a refdb model
            ts_number = extract_ts_number_from_path(json_file, model)
            if ts_number and ts_number not in refdb_models:
                skipped += 1
            failed += 1
    
    if skipped > 0:
        print(f"\n{'='*60}")
        print(f"Summary: {successful} successful, {failed} failed ({skipped} skipped - not refdb models)")
        print(f"{'='*60}")
    else:
        print(f"\n{'='*60}")
        print(f"Summary: {successful} successful, {failed} failed")
        print(f"{'='*60}")
    
    return successful, failed


def main():
    """Main function to handle command-line arguments and execute replacements."""
    parser = argparse.ArgumentParser(
        description='Replace specific values in JSON files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
NOTE: This script is primarily used as a module by main_processor.py.
      For normal usage, use main_processor.py with --refdb flag instead:

Examples (Recommended - Use main_processor.py):
  # Process CSBDTS_46 with refdb replacement
  python main_processor.py --wgs_csbd --CSBDTS46 --refdb
  
  # Process CSBDTS_47 with refdb replacement
  python main_processor.py --wgs_csbd --CSBDTS47 --refdb
  
  # Process NYKTS_123 with refdb replacement
  python main_processor.py --wgs_nyk --NYKTS123 --refdb

Standalone Usage (Advanced - Not recommended for normal workflow):
  # This script can be run standalone, but main_processor.py is preferred
  python refdb_change.py --model wgs_csbd --no-interactive -d path/to/directory

Note: This script ONLY processes refdb-specific models. 
      Path patterns: CSBDTS_XX_* (for wgs_csbd) or NYKTS_XX_* (for wgs_kernal)
      Currently supported refdb models:
      - wgs_csbd: CSBDTS_46, CSBDTS_47
      - wgs_kernal: NYKTS_123
      Files from other TS numbers will be automatically skipped.
      
      To add more refdb models, update REFDB_TS_NUMBERS in refdb_change.py
        """
    )
    
    # File/Directory options
    parser.add_argument('-f', '--file', type=str, help='Path to a specific JSON file to process')
    parser.add_argument('-d', '--directory', type=str, help='Path to directory containing JSON files')
    parser.add_argument('-r', '--recursive', action='store_true', default=True,
                        help='Process subdirectories recursively (default: True)')
    parser.add_argument('--no-recursive', dest='recursive', action='store_false',
                        help='Do not process subdirectories')
    
    # Value replacement options
    parser.add_argument('--hcid', type=str, help='New value for HCID')
    parser.add_argument('--pat-brth-dt', type=str, dest='pat_brth_dt', help='New value for PAT_BRTH_DT')
    parser.add_argument('--pat-frst-nme', type=str, dest='pat_frst_nme', help='New value for PAT_FRST_NME')
    parser.add_argument('--pat-last-nm', type=str, dest='pat_last_nm', help='New value for PAT_LAST_NM')
    parser.add_argument('--prov-tax-id', type=str, dest='prov_tax_id', help='New value for PROV_TAX_ID')
    parser.add_argument('--billg-npi', type=str, dest='billg_npi', help='New value for BILLG_NPI')
    parser.add_argument('--nat-ea2-rndr-npi', type=str, dest='nat_ea2_rndr_npi', 
                        help='New value for NAT_EA2_RNDR_NPI')
    
    # Other options
    parser.add_argument('--no-backup', action='store_true', 
                        help='Do not create backup files')
    parser.add_argument('--no-interactive', action='store_true',
                        help='Skip interactive input (use defaults or command-line values)')
    parser.add_argument('--config', type=str, 
                        help='Path to JSON configuration file with default values (default: refdb_values.json)')
    parser.add_argument('--model', type=str, required=True,
                        choices=['wgs_csbd', 'wgs_kernal'],
                        help='Model type: wgs_csbd or wgs_kernal (required)')
    
    args = parser.parse_args()
    
    # Load default values from JSON config file for the specified model
    config_path = Path(args.config) if args.config else None
    DEFAULT_VALUES = load_default_values(args.model, config_path)
    
    # Display refdb model information
    refdb_models = REFDB_TS_NUMBERS.get(args.model, [])
    if refdb_models:
        print(f"\n{'='*60}")
        print(f"REFDB-SPECIFIC MODEL PROCESSING")
        print(f"{'='*60}")
        print(f"Model: {args.model}")
        if args.model == "wgs_csbd":
            print(f"Refdb-specific TS numbers: CSBDTS_{', CSBDTS_'.join(refdb_models)}")
        elif args.model == "wgs_kernal":
            print(f"Refdb-specific TS numbers: NYKTS_{', NYKTS_'.join(refdb_models)}")
        print(f"\n⚠ IMPORTANT: Only files from these refdb-specific models will be processed.")
        print(f"   Path patterns: CSBDTS_XX_* (for wgs_csbd) or NYKTS_XX_* (for wgs_kernal)")
        print(f"   All other files will be skipped.\n")
    else:
        print(f"\n{'='*60}")
        print(f"WARNING: No refdb-specific models configured for '{args.model}'")
        print(f"{'='*60}")
        print("Please update REFDB_TS_NUMBERS in refdb_change.py to add refdb models.")
        print("Example: REFDB_TS_NUMBERS = {'wgs_csbd': ['46', '47'], ...}\n")
        response = input("Continue anyway? (y/N): ").strip().lower()
        if response != 'y':
            print("Exiting...")
            sys.exit(1)
    
    # Build replacements dictionary
    replacements = {}
    
    # Map command-line arguments to replacement keys
    arg_mapping = {
        'hcid': 'HCID',
        'pat_brth_dt': 'PAT_BRTH_DT',
        'pat_frst_nme': 'PAT_FRST_NME',
        'pat_last_nm': 'PAT_LAST_NM',
        'prov_tax_id': 'PROV_TAX_ID',
        'billg_npi': 'BILLG_NPI',
        'nat_ea2_rndr_npi': 'NAT_EA2_RNDR_NPI'
    }
    
    # Get values from command-line arguments
    for arg_key, json_key in arg_mapping.items():
        arg_value = getattr(args, arg_key, None)
        if arg_value:
            replacements[json_key] = arg_value
    
    # Filter out empty values from DEFAULT_VALUES
    filtered_defaults = {k: v for k, v in DEFAULT_VALUES.items() if v and str(v).strip()}
    
    # If no command-line values provided and not in no-interactive mode, get user input
    if not replacements and not args.no_interactive:
        replacements = get_user_input(filtered_defaults)
        # Filter out empty values from user input
        replacements = {k: v for k, v in replacements.items() if v and str(v).strip()}
    elif not replacements:
        # Use defaults if no-interactive and no command-line values (only non-empty)
        replacements = filtered_defaults.copy()
        if replacements:
            print("\nUsing default values from config file:")
            for key, value in replacements.items():
                print(f"  {key}: {value}")
        else:
            print("\nError: No valid values found in config file. Please fill in the values.")
            sys.exit(1)
    else:
        # Use defaults for any missing values (only non-empty)
        for key, default_value in filtered_defaults.items():
            if key not in replacements:
                replacements[key] = default_value
        # Filter out any empty values
        replacements = {k: v for k, v in replacements.items() if v and str(v).strip()}
        if replacements:
            print("\nUsing replacement values:")
            for key, value in replacements.items():
                print(f"  {key}: {value}")
        else:
            print("\nError: No valid replacement values specified.")
            sys.exit(1)
    
    # Determine what to process
    backup = not args.no_backup
    
    if args.file:
        # Process a single file
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            sys.exit(1)
        if not file_path.is_file():
            print(f"Error: Not a file: {file_path}")
            sys.exit(1)
        
        success = process_json_file(file_path, replacements, backup, args.model)
        sys.exit(0 if success else 1)
        
    elif args.directory:
        # Process a directory
        dir_path = Path(args.directory)
        if not dir_path.exists():
            print(f"Error: Directory not found: {dir_path}")
            sys.exit(1)
        if not dir_path.is_dir():
            print(f"Error: Not a directory: {dir_path}")
            sys.exit(1)
        
        successful, failed = process_directory(dir_path, replacements, args.recursive, backup, args.model)
        # Summary is already printed by process_directory
        sys.exit(0 if failed == 0 else 1)
        
    else:
        # Default: process current directory
        current_dir = Path.cwd()
        print(f"\nNo file or directory specified. Processing current directory: {current_dir}")
        successful, failed = process_directory(current_dir, replacements, args.recursive, backup, args.model)
        # Summary is already printed by process_directory
        sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
