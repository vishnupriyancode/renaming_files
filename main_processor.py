#!/usr/bin/env python3
"""
Main Processor - Consolidated file for renaming files and generating Postman collections.
This file combines the functionality of:
- rename_files_with_postman.py (main processing logic)
- process_multiple_models.py (batch processing)
- rename_files.py (simple interface wrapper)

NOTE: File renaming functionality has been moved to rename_files.py module.
This file now imports the renaming functions from that module.

Supports both single model processing and batch processing of multiple models.

SCRIPT FLOW OVERVIEW:
===================
1. FILE RENAMING STAGE: Convert JSON files from old naming convention to new format (via rename_files.py)
2. POSTMAN GENERATION STAGE: Create Postman collections for API testing
3. BATCH PROCESSING STAGE: Handle multiple models simultaneously
4. COMMAND LINE INTERFACE STAGE: Provide user-friendly CLI for different operations
"""

import os
import re
import shutil
import sys
import subprocess
import argparse
import json
from pathlib import Path
from dotenv import load_dotenv
from postman_generator import PostmanCollectionGenerator
from report_generate import ExcelReportGenerator, TimingTracker, get_excel_reporter, create_excel_reporter_for_model_type
from rename_files import rename_files, extract_model_info_from_directory

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

# Optional report generation - gracefully handle if report_generate.py is missing or disabled
# Check .env file for ENABLE_REPORT_GENERATION setting (default: True)
# Set to 'false', 'False', '0', or comment out the line to disable
REPORT_GENERATION_ENABLED = os.getenv('ENABLE_REPORT_GENERATION', 'true').lower() in ('true', '1', 'yes', 'on')

# Postman generation per TS collection - from .env (default: True for each)
# Set to 'false' to disable Postman generation for that collection type
def _postman_enabled_for_collection(collection_key: str) -> bool:
    env_key = f"ENABLE_POSTMAN_{collection_key.upper()}"
    return os.getenv(env_key, 'true').lower() in ('true', '1', 'yes', 'on')

POSTMAN_ENABLED_WGS_CSBD = _postman_enabled_for_collection("WGS_CSBD")
POSTMAN_ENABLED_GBDF_MCR = _postman_enabled_for_collection("GBDF_MCR")
POSTMAN_ENABLED_GBDF_GRS = _postman_enabled_for_collection("GBDF_GRS")
POSTMAN_ENABLED_WGS_KERNAL = _postman_enabled_for_collection("WGS_KERNAL")
try:
    from report_generate import (
        extract_model_name_from_source_dir,
        generate_timing_report_for_model,
        generate_json_renaming_timing_report,
        generate_excel_timing_report,
        create_excel_reporter_for_processing,
        create_excel_reporter_for_batch_processing
    )
except ImportError:
    # Report generation module not available - create dummy functions
    REPORT_GENERATION_ENABLED = False
    def extract_model_name_from_source_dir(source_dir):
        return "Unknown"
    def generate_timing_report_for_model(model_config, model_type):
        pass
    def generate_json_renaming_timing_report(timing_data, model_config, model_type, total_time):
        pass
    def generate_excel_timing_report(excel_reporter, model_type=None):
        return None
    def create_excel_reporter_for_processing(model_type=None):
        return get_excel_reporter()
    def create_excel_reporter_for_batch_processing(model_type=None):
        return get_excel_reporter()

from refdb_change import load_default_values, process_directory, is_refdb_model_enabled
from pathlib import Path
import re


# NOTE: Renaming functionality has been moved to rename_files.py
# The rename_files() function and related helper functions are now imported from that module.


def process_multiple_models(models_config, generate_postman=True, model_type=None):
    """
    STAGE 3: BATCH PROCESSING FUNCTION
    =================================
    Process multiple models with their respective configurations.
    This function handles batch processing of multiple TS models simultaneously.
    
    PROCESSING FLOW:
    1. Iterate through each model configuration
    2. Call rename_files() for each model
    3. Track success/failure for each model
    4. Provide comprehensive summary report
    5. Generate Excel timing report
    
    Args:
        models_config: List of dictionaries containing model configurations
        generate_postman: Whether to generate Postman collections for each model
    
    Example models_config:
    [
        {
            "edit_id": "rvn001",
            "code": "00W5",
            "source_dir": "WGS_CSBD/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/regression",
            "dest_dir": "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis/regression",
            "postman_collection_name": "TS_01_REVENUE_WGS_CSBD_rvn001_00W5"
        },
        {
            "edit_id": "rvn002", 
            "code": "00W6",
            "source_dir": "WGS_CSBD/TS_01_REVENUE_WGS_CSBD_rvn002_00W6_payloads_sur/regression",
            "dest_dir": "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn002_00W6_payloads_dis/regression",
            "postman_collection_name": "TS_01_REVENUE_WGS_CSBD_rvn002_00W6"
        }
    ]
    """
    
    # STAGE 3.1: BATCH PROCESSING INITIALIZATION
    # ==========================================
    print("Starting Multi-Model Processing")
    print("=" * 80)
    
    # Initialize Excel reporter session (only if report generation is enabled)
    excel_reporter = None
    if REPORT_GENERATION_ENABLED:
        excel_reporter = create_excel_reporter_for_batch_processing(model_type)
    
    total_processed = 0
    successful_models = []
    failed_models = []
    
    # STAGE 3.2: MODEL ITERATION LOOP
    # ===============================
    for i, model_config in enumerate(models_config, 1):
        edit_id = model_config.get("edit_id")
        code = model_config.get("code")
        source_dir = model_config.get("source_dir")
        dest_dir = model_config.get("dest_dir")
        postman_collection_name = model_config.get("postman_collection_name")
        
        print(f"\nProcessing Model {i}/{len(models_config)}")
        print(f"   Edit ID: {edit_id}")
        print(f"   Code: {code}")
        print(f"   Source: {source_dir}")
        print(f"   Destination: {dest_dir}")
        print("-" * 60)
        
        try:
            # Process the model
            renamed_files = rename_files(
                edit_id=edit_id,
                code=code,
                source_dir=source_dir,
                dest_dir=dest_dir,
                generate_postman=generate_postman,
                postman_collection_name=postman_collection_name,
                excel_reporter=excel_reporter
            )
            
            if renamed_files:
                print(f"SUCCESS Model {edit_id}_{code}: Successfully processed {len(renamed_files)} files")
                successful_models.append({
                    "edit_id": edit_id,
                    "code": code,
                    "files_count": len(renamed_files),
                    "files": renamed_files
                })
                total_processed += len(renamed_files)
            else:
                print(f"WARNING  Model {edit_id}_{code}: No files were processed")
                failed_models.append({
                    "edit_id": edit_id,
                    "code": code,
                    "reason": "No files found or processed"
                })
                
        except Exception as e:
            print(f"ERROR Model {edit_id}_{code}: Failed with error - {e}")
            failed_models.append({
                "edit_id": edit_id,
                "code": code,
                "reason": str(e)
            })
    
    # STAGE 3.3: BATCH PROCESSING SUMMARY
    # ==================================
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY PROCESSING SUMMARY")
    print("=" * 80)
    print(f"Total models processed: {len(models_config)}")
    print(f"Successful models: {len(successful_models)}")
    print(f"Failed models: {len(failed_models)}")
    print(f"Total files processed: {total_processed}")
    
    if successful_models:
        print(f"\nSUCCESS SUCCESSFUL MODELS:")
        for model in successful_models:
            print(f"   - {model['edit_id']}_{model['code']}: {model['files_count']} files")
    
    if failed_models:
        print(f"\nERROR FAILED MODELS:")
        for model in failed_models:
            print(f"   - {model['edit_id']}_{model['code']}: {model['reason']}")
    
    print("\nTARGET All models processed!")
    
    # Generate Excel timing report (only if report generation is enabled and reporter exists)
    if REPORT_GENERATION_ENABLED and excel_reporter:
        generate_excel_timing_report(excel_reporter, model_type=model_type)
    
    return successful_models, failed_models




def main():
    """
    STAGE 4: COMMAND LINE INTERFACE FUNCTION
    =======================================
    Main function with comprehensive command line interface.
    This function provides the CLI for users to interact with the script.
    
    CLI FEATURES:
    1. Process specific TS models (WGS_CSBD or GBDF MCR)
    2. Process all discovered models
    3. List available models
    4. Custom parameter processing
    5. Skip Postman generation option
    6. Generate timing reports for specific models
    
    PROCESSING FLOW:
    1. Parse command line arguments
    2. Load model configurations
    3. Handle different processing modes
    4. Execute file renaming and Postman generation
    5. Provide comprehensive feedback
    """
    
    # STAGE 4.1: ARGUMENT PARSER SETUP
    # ================================
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Main Processor - Rename files and generate Postman collections for TS models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process WGS_CSBD models (must use --CSBDTSXX format)
  python main_processor.py --wgs_csbd --CSBDTS01    # Process TS01 model (Covid)
  python main_processor.py --wgs_csbd --CSBDTS02    # Process TS02 model (Laterality Policy)
  python main_processor.py --wgs_csbd --CSBDTS07    # Process TS07 model
  python main_processor.py --wgs_csbd --CSBDTS10    # Process TS10 model
  python main_processor.py --wgs_csbd --CSBDTS48    # Process CSBD_TS48 model (Revenue code to HCPCS Alignment)
  python main_processor.py --wgs_csbd --CSBDTS50    # Process CSBD_TS50 model

  # Process WGS_NYK models (must use --NYKTSXX format)
  python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation Services WGS NYK)
  python main_processor.py --wgs_nyk --NYKTS124   # Process TS124 model (Observation Services WGS NYK)
  python main_processor.py --wgs_nyk --NYKTS125   # Process TS125 model (Observation Services WGS NYK)

  # Process GBDF MCR models (GBDF MCR flag required)
  python main_processor.py --gbdf_mcr --GBDTS47    # Process TS47 model (Covid GBDF MCR)
  python main_processor.py --gbdf_mcr --GBDTS48    # Process TS48 model (Multiple E&M Same day GBDF MCR)
  python main_processor.py --gbdf_mcr --GBDTS138   # Process TS138 model (Multiple E&M Same day GBDF MCR)
  python main_processor.py --gbdf_mcr --GBDTS144   # Process TS144 model (Nebulizer A52466 IPERP-132 GBDF MCR)
  python main_processor.py --gbdf_mcr --GBDTS62    # Process TS62 model (Unspecified outpt_MCR GBDF MCR)
  python main_processor.py --gbdf_mcr --GBDTS64    # Process TS64 model (Unspecified Prof_MCR GBDF MCR)
  
  
  # Process GBDF GRS models (GBDF GRS flag required)
  python main_processor.py --gbdf_grs --GBDTS49    # Process TS49 model (Multiple E&M Same day GBDF GRS)
  python main_processor.py --gbdf_grs --GBDTS61    # Process TS61 model (Unspecified dx code prof GBDF GRS)
  python main_processor.py --gbdf_grs --GBDTS63    # Process TS63 model (Unspecified Outpt_GRS GBDF GRS)
  python main_processor.py --gbdf_grs --GBDTS139   # Process TS139 model (Multiple E&M Same day GBDF GRS)
  python main_processor.py --gbdf_grs --GBDTS141   # Process TS141 model (NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS)
  python main_processor.py --gbdf_grs --GBDTS145   # Process TS145 model (Nebulizer A52466 IPERP-132 GBDF GRS)
  python main_processor.py --gbdf_grs --GBDTS147   # Process TS147 model (No match of Procedure code GBDF GRS)
  
  # Process all discovered models
  python main_processor.py --wgs_csbd --all     # Process all discovered WGS_CSBD models
  python main_processor.py --gbdf_mcr --all     # Process all discovered GBDF MCR models
  python main_processor.py --gbdf_grs --all     # Process all discovered GBDF GRS models
  
  # List available models
  python main_processor.py --list    # List all available TS models
  
  # Generate timing reports for specific models
  python main_processor.py --wgs_csbd --CSBDTS01 --list    # Generate JSON renaming timing report for TS01
  
  # Postman generation: controlled by .env (ENABLE_POSTMAN_WGS_CSBD, ENABLE_POSTMAN_GBDF_MCR, etc.)
  
  # Process with custom parameters
  python main_processor.py --edit-id rvn001 --code 00W5 --source-dir custom/path
        """
    )
    
    # Add WGS_CSBD flag
    parser.add_argument("--wgs_csbd", action="store_true",
                       help="Process WGS_CSBD models (required for TS model processing)")

    # Add WGS_NYK flag
    parser.add_argument("--wgs_nyk", action="store_true",
                       help="Process WGS_NYK models (required for NYKTS model processing)")

    # Add GBDF MCR flag
    parser.add_argument("--gbdf_mcr", action="store_true",
                       help="Process GBDF MCR models (required for GBDF model processing)")

    # Add GBDF GRS flag
    parser.add_argument("--gbdf_grs", action="store_true",
                       help="Process GBDF GRS models (required for GBDF GRS model processing)")
    
    # Add model-specific arguments for available models
    # Note: WGS_CSBD models (TS01-TS15, TS20, TS46) now use --CSBDTSXX format only
    # GBDF MCR models (TS47, TS48, TS62, TS64, TS138, TS140, TS144, TS146) now only support --GBDTSXX format
    # GBDF GRS models (TS49, TS59, TS61, TS62, TS139, TS141, TS145, TS147) now only support --GBDTSXX format
    # WGS_CSBD models should use --CSBDTSXX format (e.g., --CSBDTS01, --CSBDTS02)
    # GBDF MCR models should use --GBDTSXX format with --gbdf_mcr flag (e.g., --gbdf_mcr --GBDTS47)
    # GBDF GRS models should use --GBDTSXX format with --gbdf_grs flag (e.g., --gbdf_grs --GBDTS49)
    # TS20 is WGS_CSBD only - should use --CSBDTS20 format instead
    # parser.add_argument("--TS20", action="store_true",
    #                    help="Process TS20 model (RadioservicesbilledwithoutRadiopharma)")
    parser.add_argument("--all", action="store_true", 
                       help="Process all discovered models")
    parser.add_argument("--list", action="store_true", 
                       help="List all available TS models")
    parser.add_argument("--no-report", action="store_true",
                       help="Disable Excel report generation (skip timing reports)")
    parser.add_argument("--refdb", action="store_true",
                       help="Apply refdb value replacement for refdb-specific models (CSBDTS_46, CSBDTS_47, CSBDTS_59, CSBDTS_75, NYKTS_123, NYKTS_149)")
    
    # Add custom parameter arguments
    parser.add_argument("--edit-id", type=str, help="Custom edit ID (e.g., rvn001)")
    parser.add_argument("--code", type=str, help="Custom code (e.g., 00W5)")
    parser.add_argument("--source-dir", type=str, help="Custom source directory path")
    parser.add_argument("--dest-dir", type=str, help="Custom destination directory path")
    parser.add_argument("--collection-name", type=str, help="Custom Postman collection name")
    
    # Parse arguments and handle unknown arguments for CSBDTS pattern
    args, unknown_args = parser.parse_known_args()
    
    # Import normalize_ts_number for consistent TS number normalization (used for both CSBDTS and GBDTS)
    try:
        from dynamic_models import normalize_ts_number
    except ImportError:
        # Fallback normalization function if import fails
        def normalize_ts_number(ts_number_raw: str) -> str:
            ts_num = int(ts_number_raw)
            if 1 <= ts_num <= 9:
                return f"{ts_num:02d}"
            elif 10 <= ts_num <= 99:
                return f"{ts_num:02d}"
            elif 100 <= ts_num <= 999:
                return f"{ts_num:03d}"
            return ts_number_raw
    
    # STAGE 4.1.1: CSBDTS PATTERN HANDLING
    # ====================================
    # Handle --CSBDTSXX pattern (e.g., --CSBDTS48) for WGS_CSBD models
    # Map CSBDTSXX to TSXX when --wgs_csbd flag is used
    # Example: --wgs_csbd --CSBDTS48 -> processes TS48 model in WGS_CSBD context
    csbd_ts_models = []

    if args.wgs_csbd:
        # Process unknown arguments to find --CSBDTSXX patterns
        for arg in unknown_args:
            # Match --CSBDTS followed by digits (e.g., --CSBDTS48, --CSBDTS50)
            if arg.startswith('--CSBDTS') and len(arg) > 8:
                ts_number_str = arg[8:]  # Extract digits after "--CSBDTS"
                if ts_number_str.isdigit():
                    # Normalize TS number for consistent matching
                    ts_number = normalize_ts_number(ts_number_str)
                    csbd_ts_models.append(ts_number)
                    print(f"[INFO] Detected CSBDTS{ts_number_str} for WGS_CSBD processing (maps to TS{ts_number})")

    # STAGE 4.1.1A: NYKTS PATTERN HANDLING
    # =====================================
    # Handle --NYKTSXX pattern (e.g., --NYKTS130) for WGS_NYK models
    # Map NYKTSXX to TSXX when --wgs_nyk flag is used
    # Example: --wgs_nyk --NYKTS130 -> processes TS130 model in WGS_NYK context
    nyk_ts_models = []

    if args.wgs_nyk:
        # Process unknown arguments to find --NYKTSXX patterns
        for arg in unknown_args:
            # Match --NYKTS followed by digits (e.g., --NYKTS130, --NYKTS124)
            if arg.startswith('--NYKTS') and len(arg) > 7:
                ts_number_str = arg[7:]  # Extract digits after "--NYKTS"
                if ts_number_str.isdigit():
                    # Normalize TS number for consistent matching
                    ts_number = normalize_ts_number(ts_number_str)
                    nyk_ts_models.append(ts_number)
                    print(f"[INFO] Detected NYKTS{ts_number_str} for WGS_NYK processing (maps to TS{ts_number})")
    
    # Store CSBD TS models for later processing
    args.csbd_ts_models = csbd_ts_models

    # Store NYK TS models for later processing
    args.nyk_ts_models = nyk_ts_models

    # STAGE 4.1.2: GBDTS PATTERN HANDLING
    # ====================================
    # Handle --GBDTSXX pattern (e.g., --GBDTS47) for GBDF models
    # Map GBDTSXX to TSXX when --gbdf_mcr or --gbdf_grs flag is used
    # Example: --gbdf_mcr --GBDTS47 -> processes TS47 model in GBDF MCR context
    # Example: --gbdf_grs --GBDTS49 -> processes TS49 model in GBDF GRS context
    gbdf_mcr_ts_models = []
    gbdf_grs_ts_models = []
    
    if args.gbdf_mcr:
        # Process unknown arguments to find --GBDTSXX patterns for MCR
        for arg in unknown_args:
            # Match --GBDTS followed by digits (e.g., --GBDTS47, --GBDTS48)
            if arg.startswith('--GBDTS') and len(arg) > 7:
                ts_number_str = arg[7:]  # Extract digits after "--GBDTS"
                if ts_number_str.isdigit():
                    # Normalize TS number for consistent matching
                    ts_number = normalize_ts_number(ts_number_str)
                    gbdf_mcr_ts_models.append(ts_number)
                    print(f"[INFO] Detected GBDTS{ts_number_str} for GBDF MCR processing (maps to TS{ts_number})")
    
    if args.gbdf_grs:
        # Process unknown arguments to find --GBDTSXX patterns for GRS
        for arg in unknown_args:
            # Match --GBDTS followed by digits (e.g., --GBDTS49, --GBDTS139)
            if arg.startswith('--GBDTS') and len(arg) > 7:
                ts_number_str = arg[7:]  # Extract digits after "--GBDTS"
                if ts_number_str.isdigit():
                    # Normalize TS number for consistent matching
                    ts_number = normalize_ts_number(ts_number_str)
                    gbdf_grs_ts_models.append(ts_number)
                    print(f"[INFO] Detected GBDTS{ts_number_str} for GBDF GRS processing (maps to TS{ts_number})")
    
    # Store GBDF TS models for later processing
    args.gbdf_mcr_ts_models = gbdf_mcr_ts_models
    args.gbdf_grs_ts_models = gbdf_grs_ts_models
    
    # STAGE 4.2: MODEL CONFIGURATION LOADING
    # ======================================
    # Load model configurations with dynamic discovery
    try:
        from models_config import get_models_config, get_model_by_ts
        models_config = get_models_config(use_dynamic=True, use_wgs_csbd_destination=args.wgs_csbd, use_gbd_mcr=args.gbdf_mcr, use_gbd_grs=args.gbdf_grs, use_wgs_nyk=args.wgs_nyk)
        print("Configuration loaded with dynamic discovery")
    except ImportError as e:
        print(f"Error: {e}")
        print("Please ensure models_config.py and dynamic_models.py exist.")
        sys.exit(1)
    
    # STAGE 4.3: LIST MODE HANDLING
    # =============================
    # Handle --list option
    if args.list:
        # Timing report generation is now handled via --CSBDTSXX or --GBDTSXX patterns
        # Legacy --TS47 --list format is no longer supported
        
        # Regular list mode - show available models
        try:
            from dynamic_models import print_nested_models_display
            print_nested_models_display()
        except ImportError:
            print("\nINFO AVAILABLE TS MODELS")
            print("=" * 50)
            if models_config:
                for model in models_config:
                    print(f"TS_{model['ts_number']}: {model['edit_id']}_{model['code']}")
                    print(f"  FOLDER Source: {model['source_dir']}")
                    print(f"  FOLDER Dest:   {model['dest_dir']}")
                    print()
            else:
                print("No TS models found")
        sys.exit(0)
    
    # STAGE 4.4: CUSTOM PARAMETER HANDLING
    # ====================================
    # Handle custom parameters
    if args.edit_id and args.code:
        print(f"\nTOOL Processing custom model: {args.edit_id}_{args.code}")
        print("=" * 60)
        
        try:
            renamed_files = rename_files(
                edit_id=args.edit_id,
                code=args.code,
                source_dir=args.source_dir,
                dest_dir=args.dest_dir,
                generate_postman=True,
                postman_collection_name=args.collection_name
            )
            
            if renamed_files:
                print(f"SUCCESS Custom model {args.edit_id}_{args.code}: Successfully processed {len(renamed_files)} files")
            else:
                print(f"WARNING  Custom model {args.edit_id}_{args.code}: No files were processed")
                
        except Exception as e:
            print(f"ERROR Custom model {args.edit_id}_{args.code}: Failed with error - {e}")
            sys.exit(1)
        
        sys.exit(0)
    
    # STAGE 4.5: MODEL SELECTION LOGIC
    # ================================
    # Determine which models to process
    models_to_process = []
    
    # Handle specific TS numbers for available models
    # WGS_CSBD models (TS01-TS15, TS20, TS46) now use --CSBDTSXX format only
    # Check if any WGS_CSBD TS flags are used with --wgs_csbd and reject them
    wgs_csbd_ts_flags = [
        ("TS01", "01"), ("TS02", "02"), ("TS03", "03"), ("TS04", "04"), ("TS05", "05"),
        ("TS06", "06"), ("TS07", "07"), ("TS08", "08"), ("TS09", "09"), ("TS10", "10"),
        ("TS11", "11"), ("TS12", "12"), ("TS13", "13"), ("TS14", "14"), ("TS15", "15"),
        ("TS20", "20"), ("TS46", "46")
    ]
    
    used_wgs_csbd_ts_flags = []
    for flag_name, ts_num in wgs_csbd_ts_flags:
        if hasattr(args, flag_name) and getattr(args, flag_name):
            if args.wgs_csbd:
                used_wgs_csbd_ts_flags.append((flag_name, ts_num))
    
    if used_wgs_csbd_ts_flags:
        print("ERROR Error: WGS_CSBD models must use --CSBDTSXX format instead of --TSXX!")
        print("\nPlease use the --CSBDTSXX format for WGS_CSBD models:")
        for flag_name, ts_num in used_wgs_csbd_ts_flags:
            print(f"  python main_processor.py --wgs_csbd --CSBDTS{ts_num}   # Instead of --{flag_name}")
        print("\nThe --TSXX format is no longer supported for WGS_CSBD models.")
        sys.exit(1)
    
    # TS20 is WGS_CSBD only - should use --CSBDTS20 format (handled in CSBDTS processing block below)
    
    # STAGE 4.5.1: CSBDTS MODEL HANDLING
    # =================================
    # Handle --CSBDTSXX patterns (e.g., --CSBDTS48) for WGS_CSBD models
    # When --wgs_csbd flag is used with --CSBDTSXX, process the corresponding TS model
    if hasattr(args, 'csbd_ts_models') and args.csbd_ts_models:
        if not args.wgs_csbd:
            print("ERROR Error: --wgs_csbd flag is required for CSBDTS model processing!")
            print("\nPlease use the --wgs_csbd flag with CSBDTS model commands:")
            for ts_num in args.csbd_ts_models:
                print(f"  python main_processor.py --wgs_csbd --CSBDTS{ts_num}   # Process CSBD_TS{ts_num} model")
            sys.exit(1)

        # Process each CSBDTS model
        for ts_number_str in args.csbd_ts_models:
            # Find ALL models with matching TS number (both smoke and regression)
            csbd_ts_models = [model for model in models_config if model.get("ts_number") == ts_number_str]
            if csbd_ts_models:
                models_to_process.extend(csbd_ts_models)
                folder_types = [m.get("folder_type", "regression") for m in csbd_ts_models]
                print(f"[INFO] Added {len(csbd_ts_models)} CSBD_TS{ts_number_str} model(s) to processing queue: {', '.join(folder_types)}")
            else:
                print(f"ERROR Error: CSBD_TS{ts_number_str} model not found!")
                print(f"Available models: {[m.get('ts_number') for m in models_config]}")
                # Continue processing other models instead of exiting

    # STAGE 4.5.1A: NYKTS MODEL HANDLING
    # ==================================
    # Handle --NYKTSXX patterns (e.g., --NYKTS130) for WGS_NYK models
    # When --wgs_nyk flag is used with --NYKTSXX, process the corresponding TS model
    if hasattr(args, 'nyk_ts_models') and args.nyk_ts_models:
        if not args.wgs_nyk:
            print("ERROR Error: --wgs_nyk flag is required for NYKTS model processing!")
            print("\nPlease use the --wgs_nyk flag with NYKTS model commands:")
            for ts_num in args.nyk_ts_models:
                print(f"  python main_processor.py --wgs_nyk --NYKTS{ts_num}   # Process NYK_TS{ts_num} model")
            sys.exit(1)

        # Process each NYKTS model
        for ts_number_str in args.nyk_ts_models:
            # Find ALL models with matching TS number (both smoke and regression)
            nyk_ts_models = [model for model in models_config if model.get("ts_number") == ts_number_str]
            if nyk_ts_models:
                models_to_process.extend(nyk_ts_models)
                folder_types = [m.get("folder_type", "regression") for m in nyk_ts_models]
                print(f"[INFO] Added {len(nyk_ts_models)} NYK_TS{ts_number_str} model(s) to processing queue: {', '.join(folder_types)}")
            else:
                print(f"ERROR Error: NYK_TS{ts_number_str} model not found!")
                print(f"Available models: {[m.get('ts_number') for m in models_config]}")
                # Continue processing other models instead of exiting
    
    # STAGE 4.5.2: GBDTS MODEL HANDLING FOR MCR
    # ==========================================
    # Handle --GBDTSXX patterns (e.g., --GBDTS47) for GBDF MCR models
    # When --gbdf_mcr flag is used with --GBDTSXX, process the corresponding TS model
    if hasattr(args, 'gbdf_mcr_ts_models') and args.gbdf_mcr_ts_models:
        if not args.gbdf_mcr:
            print("ERROR Error: --gbdf_mcr flag is required for GBDTS model processing!")
            print("\nPlease use the --gbdf_mcr flag with GBDTS model commands:")
            for ts_num in args.gbdf_mcr_ts_models:
                print(f"  python main_processor.py --gbdf_mcr --GBDTS{ts_num}   # Process GBDF MCR TS{ts_num} model")
            sys.exit(1)
        
        # Process each GBDTS model for MCR
        for ts_number_str in args.gbdf_mcr_ts_models:
            # Find ALL models with matching TS number (both smoke and regression)
            gbdf_ts_models = [model for model in models_config if model.get("ts_number") == ts_number_str]
            if gbdf_ts_models:
                models_to_process.extend(gbdf_ts_models)
                folder_types = [m.get("folder_type", "regression") for m in gbdf_ts_models]
                print(f"[INFO] Added {len(gbdf_ts_models)} GBDF MCR TS{ts_number_str} model(s) to processing queue: {', '.join(folder_types)}")
            else:
                print(f"ERROR Error: GBDF MCR TS{ts_number_str} model not found!")
                print(f"Available models: {[m.get('ts_number') for m in models_config]}")
                # Continue processing other models instead of exiting
    
    # STAGE 4.5.2A: GBDTS MODEL HANDLING FOR GRS
    # ==========================================
    # Handle --GBDTSXX patterns (e.g., --GBDTS49) for GBDF GRS models
    # When --gbdf_grs flag is used with --GBDTSXX, process the corresponding TS model
    if hasattr(args, 'gbdf_grs_ts_models') and args.gbdf_grs_ts_models:
        if not args.gbdf_grs:
            print("ERROR Error: --gbdf_grs flag is required for GBDTS model processing!")
            print("\nPlease use the --gbdf_grs flag with GBDTS model commands:")
            for ts_num in args.gbdf_grs_ts_models:
                print(f"  python main_processor.py --gbdf_grs --GBDTS{ts_num}   # Process GBDF GRS TS{ts_num} model")
            sys.exit(1)
        
        # Process each GBDTS model for GRS
        for ts_number_str in args.gbdf_grs_ts_models:
            # Find ALL models with matching TS number (both smoke and regression)
            gbdf_ts_models = [model for model in models_config if model.get("ts_number") == ts_number_str]
            if gbdf_ts_models:
                models_to_process.extend(gbdf_ts_models)
                folder_types = [m.get("folder_type", "regression") for m in gbdf_ts_models]
                print(f"[INFO] Added {len(gbdf_ts_models)} GBDF GRS TS{ts_number_str} model(s) to processing queue: {', '.join(folder_types)}")
            else:
                print(f"ERROR Error: GBDF GRS TS{ts_number_str} model not found!")
                print(f"Available models: {[m.get('ts_number') for m in models_config]}")
                # Continue processing other models instead of exiting
    
    if args.all:
        models_to_process = models_config
        print(f"SUCCESS Processing all {len(models_config)} discovered models")
    
    # Check if appropriate flag is required for TS model processing
    # WGS_CSBD models now use --CSBDTSXX format
    # GBDF MCR models now use --GBDTSXX format
    # GBDF GRS models now use --GBDTSXX format
    all_models = args.all
    
    if all_models and not args.wgs_csbd and not args.wgs_nyk and not args.gbdf_mcr and not args.gbdf_grs:
        print("ERROR Error: Either --wgs_csbd, --wgs_nyk, --gbdf_mcr, or --gbdf_grs flag is required for --all processing!")
        print("\nPlease specify which type of models to process:")
        print("  python main_processor.py --wgs_csbd --all     # Process all WGS_CSBD models")
        print("  python main_processor.py --wgs_nyk --all     # Process all WGS_NYK models")
        print("  python main_processor.py --gbdf_mcr --all     # Process all GBDF MCR models")
        print("  python main_processor.py --gbdf_grs --all     # Process all GBDF GRS models")
        print("\nUse --help for more information.")
        sys.exit(1)
    
    # If no specific model is selected, show help
    if not models_to_process:
        print("ERROR Error: No model specified!")
        print("\nPlease specify which model to process:")
        print("  --wgs_csbd --CSBDTS01    Process TS01 model (Covid)")
        print("  --wgs_csbd --CSBDTS02    Process TS02 model (Laterality Policy)")
        print("  --wgs_csbd --CSBDTS03    Process TS03 model (Revenue code Services not payable on Facility claim Sub Edit 5)")
        print("  --wgs_csbd --CSBDTS04    Process TS04 model (Revenue code Services not payable on Facility claim - Sub Edit 4)")
        print("  --wgs_csbd --CSBDTS05    Process TS05 model (Revenue code Services not payable on Facility claim Sub Edit 3)")
        print("  --wgs_csbd --CSBDTS06    Process TS06 model (Revenue code Services not payable on Facility claim Sub Edit 2)")
        print("  --wgs_csbd --CSBDTS07    Process TS07 model (Revenue code Services not payable on Facility claim Sub Edit 1)")
        print("  --wgs_csbd --CSBDTS08    Process TS08 model (Lab panel Model)")
        print("  --wgs_csbd --CSBDTS09    Process TS09 model (Device Dependent Procedures)")
        print("  --wgs_csbd --CSBDTS10    Process TS10 model")
        print("  --wgs_csbd --CSBDTS11    Process TS11 model (Revenue Code to HCPCS Xwalk-1B)")
        print("  --wgs_csbd --CSBDTS12    Process TS12 model (Incidentcal Services Facility)")
        print("  --wgs_csbd --CSBDTS13    Process TS13 model (Revenue model CR v3)")
        print("  --wgs_csbd --CSBDTS14    Process TS14 model (HCPCS to Revenue Code Xwalk)")
        print("  --wgs_csbd --CSBDTS15    Process TS15 model (revenue model)")
        print("  --wgs_csbd --CSBDTS20    Process TS20 model (RadioservicesbilledwithoutRadiopharma)")
        print("  --wgs_csbd --CSBDTS46    Process TS46 model (Multiple E&M Same day)")
        print("  --wgs_csbd --CSBDTS47    Process TS47 model (Multiple Billing of Obstetrical Services)")
        print("  --wgs_nyk --NYKTS130   Process TS130 model (Observation Services WGS NYK)")
        print("  --wgs_nyk --NYKTS124   Process TS124 model (Observation Services WGS NYK)")
        print("  --wgs_nyk --NYKTS125   Process TS125 model (Observation Services WGS NYK)")
        print("  --gbdf_mcr --GBDTS47    Process TS47 model (Covid GBDF MCR) - Required format")
        print("  --gbdf_mcr --GBDTS48    Process TS48 model (Multiple E&M Same day GBDF MCR) - Required format")
        print("  --gbdf_mcr --GBDTS138   Process TS138 model (Multiple E&M Same day GBDF MCR) - Required format")
        print("  --gbdf_mcr --GBDTS140   Process TS140 model (NDC UOM Validation Edit Expansion Iprep-138 GBDF MCR) - Required format")
        print("  --gbdf_mcr --GBDTS144   Process TS144 model (Nebulizer A52466 IPERP-132 GBDF MCR) - Required format")
        print("  --gbdf_mcr --GBDTS146   Process TS146 model (No match of Procedure code GBDF MCR) - Required format")
        print("  --gbdf_mcr --GBDTS62    Process TS62 model (Unspecified dx code outpt_MCR GBDF MCR) - Required format")
        print("  --gbdf_mcr --GBDTS64    Process TS64 model (Unspecified Prof_MCR GBDF MCR) - Required format")
        print("  --gbdf_grs --GBDTS49    Process TS49 model (Multiple E&M Same day GBDF GRS) - Required format")
        print("  --gbdf_grs --GBDTS59    Process TS59 model (Unspecified dx code outpt GBDF GRS) - Required format")
        print("  --gbdf_grs --GBDTS61    Process TS61 model (Unspecified dx code prof GBDF GRS) - Required format")
        print("  --gbdf_grs --GBDTS63    Process TS63 model (Unspecified Outpt_GRS GBDF GRS) - Required format")
        print("  --gbdf_grs --GBDTS139   Process TS139 model (Multiple E&M Same day GBDF GRS) - Required format")
        print("  --gbdf_grs --GBDTS141   Process TS141 model (NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS) - Required format")
        print("  --gbdf_grs --GBDTS145   Process TS145 model (Nebulizer A52466 IPERP-132 GBDF GRS) - Required format")
        print("  --gbdf_grs --GBDTS147   Process TS147 model (No match of Procedure code GBDF GRS) - Required format")
        print("  --wgs_csbd --all     Process all discovered WGS_CSBD models")
        print("  --wgs_nyk --all     Process all discovered WGS_NYK models")
        print("  --gbdf_mcr --all     Process all discovered GBDF MCR models")
        print("  --list    List all available TS models")
        print("\nUse --help for more information.")
        sys.exit(1)
    
    # STAGE 4.6: MODEL PROCESSING EXECUTION
    # ====================================
    # Process selected models
    # Determine model type for Excel reporting and Postman enable from .env
    model_type = None
    if args.wgs_csbd:
        model_type = "WGS_CSBD"
    elif args.wgs_nyk:
        model_type = "WGS_NYK"
    elif args.gbdf_mcr:
        model_type = "GBDF_MCR"
    elif args.gbdf_grs:
        model_type = "GBDF_GRS"

    # Postman: controlled only by .env per-collection flag (true/false)
    postman_enabled_for_type = True
    if model_type == "WGS_CSBD":
        postman_enabled_for_type = POSTMAN_ENABLED_WGS_CSBD
    elif model_type == "WGS_NYK":
        postman_enabled_for_type = POSTMAN_ENABLED_WGS_KERNAL
    elif model_type == "GBDF_MCR":
        postman_enabled_for_type = POSTMAN_ENABLED_GBDF_MCR
    elif model_type == "GBDF_GRS":
        postman_enabled_for_type = POSTMAN_ENABLED_GBDF_GRS
    generate_postman = postman_enabled_for_type
    if not postman_enabled_for_type and model_type:
        env_key = {"WGS_CSBD": "ENABLE_POSTMAN_WGS_CSBD", "WGS_NYK": "ENABLE_POSTMAN_WGS_KERNAL",
                   "GBDF_MCR": "ENABLE_POSTMAN_GBDF_MCR", "GBDF_GRS": "ENABLE_POSTMAN_GBDF_GRS"}.get(model_type)
        print(f"[INFO] Postman generation is DISABLED for {model_type} (from .env: {env_key}=false)")

    # Check if report generation is disabled via command line or .env file
    enable_reporting = REPORT_GENERATION_ENABLED and not args.no_report
    
    # Create separate Excel reporter for this model type (only if reporting is enabled)
    excel_reporter = None
    if enable_reporting:
        excel_reporter = create_excel_reporter_for_processing(model_type)
        env_setting = os.getenv('ENABLE_REPORT_GENERATION', 'true')
        print(f"[INFO] Report generation is ENABLED (from .env: ENABLE_REPORT_GENERATION={env_setting})")
    else:
        if args.no_report:
            print("[INFO] Report generation is DISABLED (--no-report flag)")
        elif not REPORT_GENERATION_ENABLED:
            env_setting = os.getenv('ENABLE_REPORT_GENERATION', 'not set')
            if env_setting.lower() in ('false', '0', 'no', 'off'):
                print(f"[INFO] Report generation is DISABLED (from .env: ENABLE_REPORT_GENERATION={env_setting})")
            else:
                print("[INFO] Report generation is DISABLED (report_generate.py not available)")
    
    print(f"\nSTARTING Processing {len(models_to_process)} model(s)...")
    print("=" * 60)
    
    total_processed = 0
    successful_models = []
    
    for i, model_config in enumerate(models_to_process, 1):
        edit_id = model_config["edit_id"]
        code = model_config["code"]
        source_dir = model_config["source_dir"]
        dest_dir = model_config["dest_dir"]
        postman_collection_name = model_config["postman_collection_name"]
        ts_number = model_config.get("ts_number", "??")
        
        print(f"\nINFO Processing Model {i}/{len(models_to_process)}: TS_{ts_number} ({edit_id}_{code})")
        print("-" * 40)
        
        try:
            renamed_files = rename_files(
                edit_id=edit_id,
                code=code,
                source_dir=source_dir,
                dest_dir=dest_dir,
                generate_postman=generate_postman,
                postman_collection_name=postman_collection_name,
                postman_file_name=model_config.get('postman_file_name'),
                excel_reporter=excel_reporter
            )
            
            # Apply refdb value replacement if --refdb flag is set
            if args.refdb and renamed_files:
                print(f"\nINFO Applying refdb value replacement for TS_{ts_number}...")
                try:
                    # Determine refdb model type based on model_type
                    refdb_model = None
                    if model_type == "WGS_CSBD":
                        refdb_model = "wgs_csbd"
                    elif model_type == "WGS_NYK":
                        refdb_model = "wgs_kernal"
                    elif model_type == "GBDF_MCR":
                        refdb_model = "gbdf_mcr"
                    elif model_type == "GBDF_GRS":
                        refdb_model = "gbdf_grs"
                    
                    if refdb_model and not is_refdb_model_enabled(refdb_model):
                        print(f"INFO Refdb is disabled for {refdb_model} (check ENABLE_REFDB_* in .env). Skipping refdb replacement.")
                    elif refdb_model:
                        # Load refdb values from refdb_values.json
                        refdb_replacements = load_default_values(refdb_model)
                        
                        # Process the destination directory with refdb values
                        dest_path = Path(dest_dir)
                        if dest_path.exists():
                            successful_refdb, failed_refdb = process_directory(
                                directory=dest_path,
                                replacements=refdb_replacements,
                                recursive=True,
                                backup=False,  # Don't create backups during main processing
                                model=refdb_model
                            )
                            if successful_refdb > 0:
                                print(f"SUCCESS Refdb: Successfully processed {successful_refdb} file(s) with refdb values")
                            if failed_refdb > 0:
                                print(f"WARNING Refdb: {failed_refdb} file(s) failed refdb processing")
                        else:
                            print(f"WARNING Refdb: Destination directory not found: {dest_dir}")
                    else:
                        print(f"WARNING Refdb: Model type '{model_type}' is not a refdb-supported model")
                        print(f"   Supported refdb models: WGS_CSBD (CSBDTS_46, CSBDTS_47, CSBDTS_59, CSBDTS_75), WGS_NYK (NYKTS_123, NYKTS_149), GBDF_MCR (GBDTS_XX), GBDF_GRS (GBDTS_XX)")
                except Exception as refdb_error:
                    print(f"WARNING Refdb processing failed: {refdb_error}")
                    # Continue with normal processing even if refdb fails
            
            if renamed_files:
                print(f"SUCCESS Model TS_{ts_number} ({edit_id}_{code}): Successfully processed {len(renamed_files)} files")
                successful_models.append({
                    "ts_number": ts_number,
                    "edit_id": edit_id,
                    "code": code,
                    "files_count": len(renamed_files)
                })
                total_processed += len(renamed_files)
            else:
                print(f"WARNING  Model TS_{ts_number} ({edit_id}_{code}): No files were processed")
                
        except Exception as e:
            print(f"ERROR Model TS_{ts_number} ({edit_id}_{code}): Failed with error - {e}")
    
    # STAGE 4.7: FINAL SUMMARY REPORT
    # ===============================
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Models processed: {len(models_to_process)}")
    print(f"Successful models: {len(successful_models)}")
    print(f"Total files processed: {total_processed}")
    
    if successful_models:
        print(f"\nSUCCESS SUCCESSFUL MODELS:")
        for model in successful_models:
            print(f"   - TS_{model['ts_number']} ({model['edit_id']}_{model['code']}): {model['files_count']} files")
        
        if generate_postman:
            print(f"\nCOLLECTION POSTMAN COLLECTIONS GENERATED:")
            print("To use these collections:")
            print("1. Open Postman")
            print("2. Click 'Import'")
            print("3. Select the collection files from 'postman_collections' folder")
            print("4. Start testing your APIs!")
    
    if total_processed > 0:
        print(f"\nCELEBRATION Successfully processed {total_processed} files!")
        print("Files are now ready for API testing with Postman.")
        
        # Generate Excel timing report for single model processing (only if enabled)
        if enable_reporting and excel_reporter:
            generate_excel_timing_report(excel_reporter, model_type=model_type)
    else:
        print("\nERROR No files were processed.")


if __name__ == "__main__":
    main()
