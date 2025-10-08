#!/usr/bin/env python3
"""
Main Processor - Consolidated file for renaming files and generating Postman collections.
This file combines the functionality of:
- rename_files_with_postman.py (main processing logic)
- process_multiple_models.py (batch processing)
- rename_files.py (simple interface wrapper)

Supports both single model processing and batch processing of multiple models.
"""

import os
import re
import shutil
import sys
import subprocess
import argparse
from postman_generator import PostmanCollectionGenerator


def rename_files(edit_id="rvn001", code="00W5", source_dir=None, dest_dir=None, generate_postman=True, postman_collection_name=None, postman_file_name=None):
    """Rename files and optionally generate Postman collection for a specific model.
    
    Args:
        edit_id: The edit ID (e.g., "rvn001", "rvn002")
        code: The code (e.g., "00W5", "00W6")
        source_dir: Source directory path (auto-generated if None)
        dest_dir: Destination directory path (auto-generated if None)
        generate_postman: If True, generate Postman collection after renaming
        postman_collection_name: Name for the Postman collection
        postman_file_name: Custom filename for the Postman collection JSON file
    """
    
    # Mapping for suffixes based on the expected output format
    suffix_mapping = {
        "positive": {
            "deny": "LR",    # deny -> LR
        },
        "negative": {
            "bypass": "NR",  # bypass -> NR
        },
        "Exclusion": {
            "exclusion": "EX",   # exclusion -> EX
        }
    }
    
    # Auto-generate paths if not provided
    if source_dir is None:
        source_dir = f"source_folder/WGS_CSBD/TS_01_REVENUE_WGS_CSBD_{edit_id}_{code}_payloads_sur/regression"
    
    if dest_dir is None:
        # Default to renaming_jsons for backward compatibility
        dest_dir = f"renaming_jsons/TS_01_REVENUE_WGS_CSBD_{edit_id}_{code}_payloads_dis/regression"
    
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} not found!")
        return
    
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Get all JSON files in the source directory
    json_files = [f for f in os.listdir(source_dir) if f.endswith('.json')]
    
    print("Files to be renamed and moved:")
    print("=" * 60)
    
    renamed_files = []
    
    for filename in json_files:
        # Parse the current filename
        parts = filename.split('#')
        
        if len(parts) == 3:
            # Handle 3-part template: TC#XX_XXXXX#suffix.json
            tc_part = parts[0]  # TC
            tc_id_part = parts[1]  # 01_12345
            suffix = parts[2].replace('.json', '')  # deny, bypass, market
            
            # Get the correct suffix mapping for the new template
            mapped_suffix = suffix
            for category in suffix_mapping.values():
                if suffix in category:
                    mapped_suffix = category[suffix]
                    break
            
            # Create new filename according to new template: TC#XX_XXXXX#rvn001#00W5#LR.json
            new_filename = f"{tc_part}#{tc_id_part}#{edit_id}#{code}#{mapped_suffix}.json"
            
            print(f"Current: {filename}")
            print(f"Converting to new template...")
            print(f"New:     {new_filename}")
            print(f"Moving to: {dest_dir}")
            print("-" * 40)
            
            # Source and destination paths - normalize paths for Windows compatibility
            source_path = os.path.normpath(os.path.join(source_dir, filename))
            dest_path = os.path.normpath(os.path.join(dest_dir, new_filename))
            
            try:
                # Copy the file to destination with new name
                # Use shutil.copy2 for cross-platform compatibility
                shutil.copy2(source_path, dest_path)
                print(f"Successfully copied and renamed: {filename} -> {new_filename}")
                
                # Remove the original file
                os.remove(source_path)
                print(f"Removed original file: {filename}")
                
                renamed_files.append(new_filename)
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
        elif len(parts) == 4:
            # Handle 4-part template: TC#XX_XXXXX#edit_id#suffix.json
            tc_part = parts[0]  # TC
            tc_id_part = parts[1]  # 01_12345
            file_edit_id = parts[2]  # rvn001
            suffix = parts[3].replace('.json', '')  # deny, bypass, market
            
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
                
                # Remove the original file
                os.remove(source_path)
                print(f"Removed original file: {filename}")
                
                renamed_files.append(new_filename)
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
        elif len(parts) == 5:
            # Handle 5-part template: TC#XX_XXXXX#edit_id#code#suffix.json (already converted)
            tc_part = parts[0]  # TC
            tc_id_part = parts[1]  # 01_12345
            file_edit_id = parts[2]  # rvn001
            file_code = parts[3]  # 00W5
            suffix = parts[4].replace('.json', '')  # LR, NR, EX
            
            # Check if this file matches our target model
            if file_edit_id == edit_id and file_code == code:
                # File is already in correct format, just move it
                new_filename = filename  # Keep the same name
                
                print(f"Current: {filename}")
                print(f"Already in correct format, moving as-is...")
                print(f"Moving to: {dest_dir}")
                print("-" * 40)
                
                # Source and destination paths
                source_path = os.path.join(source_dir, filename)
                dest_path = os.path.join(dest_dir, new_filename)
                
                try:
                    # Copy the file to destination
                    shutil.copy2(source_path, dest_path)
                    print(f"Successfully moved: {filename}")
                    
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
    
    # Generate Postman collection if requested
    if generate_postman and renamed_files:
        print("\n" + "=" * 60)
        print("Generating Postman collection...")
        print("-" * 40)
        
        try:
            # Initialize Postman generator with specific model directory
            # Use appropriate subdirectory when processing models
            output_dir = "postman_collections"
            if "WGS_CSBD" in dest_dir:
                output_dir = "postman_collections/WGS_CSBD"
            elif "GBDF" in dest_dir:
                output_dir = "postman_collections/GBDF"
            
            generator = PostmanCollectionGenerator(
                source_dir=dest_dir,  # Use the specific model's destination directory
                output_dir=output_dir
            )
            
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
            
            # Generate collection
            collection_path = generator.generate_postman_collection(postman_collection_name, custom_filename)
            
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
    
    return renamed_files


def process_multiple_models(models_config, generate_postman=True):
    """
    Process multiple models with their respective configurations.
    
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
    
    print("Starting Multi-Model Processing")
    print("=" * 80)
    
    total_processed = 0
    successful_models = []
    failed_models = []
    
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
                postman_collection_name=postman_collection_name
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
    return successful_models, failed_models


def main():
    """Main function with comprehensive command line interface."""
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Main Processor - Rename files and generate Postman collections for TS models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process specific TS models (WGS_CSBD flag required)
  python main_processor.py --wgs_csbd --TS01    # Process TS01 model (Covid)
  python main_processor.py --wgs_csbd --TS02    # Process TS02 model (Laterality Policy)
  python main_processor.py --wgs_csbd --TS07    # Process TS07 model
  python main_processor.py --wgs_csbd --TS10    # Process TS10 model
  
  # Process GBDF MCR models (GBDF MCR flag required)
  python main_processor.py --gbdf_mcr --TS47    # Process TS47 model (Covid GBDF MCR)
  
  # Process all discovered models
  python main_processor.py --wgs_csbd --all     # Process all discovered WGS_CSBD models
  python main_processor.py --gbdf_mcr --all     # Process all discovered GBDF MCR models
  
  # List available models
  python main_processor.py --list    # List all available TS models
  
  # Skip Postman generation
  python main_processor.py --wgs_csbd --TS07 --no-postman
  python main_processor.py --gbdf_mcr --TS47 --no-postman
  
  # Process with custom parameters
  python main_processor.py --edit-id rvn001 --code 00W5 --source-dir custom/path
        """
    )
    
    # Add WGS_CSBD flag
    parser.add_argument("--wgs_csbd", action="store_true", 
                       help="Process WGS_CSBD models (required for TS model processing)")
    
    # Add GBDF MCR flag
    parser.add_argument("--gbdf_mcr", action="store_true", 
                       help="Process GBDF MCR models (required for GBDF model processing)")
    
    # Add model-specific arguments for available models
    parser.add_argument("--TS01", action="store_true", 
                       help="Process TS01 model (Covid)")
    parser.add_argument("--TS02", action="store_true", 
                       help="Process TS02 model (Laterality Policy)")
    parser.add_argument("--TS10", action="store_true", 
                       help="Process TS10 model")
    parser.add_argument("--TS03", action="store_true", 
                       help="Process TS03 model (Revenue code Services not payable on Facility claim Sub Edit 5)")
    parser.add_argument("--TS04", action="store_true", 
                       help="Process TS04 model (Revenue code Services not payable on Facility claim - Sub Edit 4)")
    parser.add_argument("--TS05", action="store_true", 
                       help="Process TS05 model (Revenue code Services not payable on Facility claim Sub Edit 3)")
    parser.add_argument("--TS06", action="store_true", 
                       help="Process TS06 model (Revenue code Services not payable on Facility claim Sub Edit 2)")
    parser.add_argument("--TS07", action="store_true", 
                       help="Process TS07 model (Revenue code Services not payable on Facility claim Sub Edit 1)")
    parser.add_argument("--TS08", action="store_true", 
                       help="Process TS08 model (Lab panel Model)")
    parser.add_argument("--TS09", action="store_true", 
                       help="Process TS09 model (Device Dependent Procedures)")
    parser.add_argument("--TS11", action="store_true", 
                       help="Process TS11 model (Revenue Code to HCPCS Xwalk-1B)")
    parser.add_argument("--TS12", action="store_true", 
                       help="Process TS12 model (Incidentcal Services Facility)")
    parser.add_argument("--TS13", action="store_true", 
                       help="Process TS13 model (Revenue model CR v3)")
    parser.add_argument("--TS14", action="store_true", 
                       help="Process TS14 model (HCPCS to Revenue Code Xwalk)")
    parser.add_argument("--TS15", action="store_true", 
                       help="Process TS15 model (revenue model)")
    parser.add_argument("--TS46", action="store_true", 
                       help="Process TS46 model (Multiple E&M Same day)")
    parser.add_argument("--TS47", action="store_true", 
                       help="Process TS47 model (Covid GBDF MCR)")
    parser.add_argument("--all", action="store_true", 
                       help="Process all discovered models")
    parser.add_argument("--list", action="store_true", 
                       help="List all available TS models")
    parser.add_argument("--no-postman", action="store_true", 
                       help="Skip Postman collection generation")
    
    # Add custom parameter arguments
    parser.add_argument("--edit-id", type=str, help="Custom edit ID (e.g., rvn001)")
    parser.add_argument("--code", type=str, help="Custom code (e.g., 00W5)")
    parser.add_argument("--source-dir", type=str, help="Custom source directory path")
    parser.add_argument("--dest-dir", type=str, help="Custom destination directory path")
    parser.add_argument("--collection-name", type=str, help="Custom Postman collection name")
    
    args = parser.parse_args()
    
    # Load model configurations with dynamic discovery
    try:
        from models_config import get_models_config, get_model_by_ts
        models_config = get_models_config(use_dynamic=True, use_wgs_csbd_destination=args.wgs_csbd, use_gbdf_mcr=args.gbdf_mcr)
        print("Configuration loaded with dynamic discovery")
    except ImportError as e:
        print(f"Error: {e}")
        print("Please ensure models_config.py and dynamic_models.py exist.")
        sys.exit(1)
    
    # Handle --list option
    if args.list:
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
                generate_postman=not args.no_postman,
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
    
    # Determine which models to process
    models_to_process = []
    
    # Handle specific TS numbers for available models
    
    if args.TS01:
        ts01_model = next((model for model in models_config if model.get("ts_number") == "01"), None)
        if ts01_model:
            models_to_process.append(ts01_model)
        else:
            print("ERROR Error: TS01 model not found!")
            sys.exit(1)
    
    if args.TS02:
        ts02_model = next((model for model in models_config if model.get("ts_number") == "02"), None)
        if ts02_model:
            models_to_process.append(ts02_model)
        else:
            print("ERROR Error: TS02 model not found!")
            sys.exit(1)
    
    if args.TS10:
        ts10_model = next((model for model in models_config if model.get("ts_number") == "10"), None)
        if ts10_model:
            models_to_process.append(ts10_model)
        else:
            print("ERROR Error: TS10 model not found!")
            sys.exit(1)
    

    if args.TS04:
        ts04_model = next((model for model in models_config if model.get("ts_number") == "04"), None)
        if ts04_model:
            models_to_process.append(ts04_model)
        else:
            print("ERROR Error: TS04 model not found!")
            sys.exit(1)
    
    if args.TS03:
        ts03_model = next((model for model in models_config if model.get("ts_number") == "03"), None)
        if ts03_model:
            models_to_process.append(ts03_model)
        else:
            print("ERROR Error: TS03 model not found!")
            sys.exit(1)
    
    if args.TS05:
        ts05_model = next((model for model in models_config if model.get("ts_number") == "05"), None)
        if ts05_model:
            models_to_process.append(ts05_model)
        else:
            print("ERROR Error: TS05 model not found!")
            sys.exit(1)
    
    if args.TS06:
        ts06_model = next((model for model in models_config if model.get("ts_number") == "06"), None)
        if ts06_model:
            models_to_process.append(ts06_model)
        else:
            print("ERROR Error: TS06 model not found!")
            sys.exit(1)
    
    if args.TS07:
        ts07_model = next((model for model in models_config if model.get("ts_number") == "07"), None)
        if ts07_model:
            models_to_process.append(ts07_model)
        else:
            print("ERROR Error: TS07 model not found!")
            sys.exit(1)
    
    if args.TS08:
        ts08_model = next((model for model in models_config if model.get("ts_number") == "08"), None)
        if ts08_model:
            models_to_process.append(ts08_model)
        else:
            print("ERROR Error: TS08 model not found!")
            sys.exit(1)
    
    if args.TS09:
        ts09_model = next((model for model in models_config if model.get("ts_number") == "09"), None)
        if ts09_model:
            models_to_process.append(ts09_model)
        else:
            print("ERROR Error: TS09 model not found!")
            sys.exit(1)
    
    if args.TS11:
        ts11_model = next((model for model in models_config if model.get("ts_number") == "11"), None)
        if ts11_model:
            models_to_process.append(ts11_model)
        else:
            print("ERROR Error: TS11 model not found!")
            sys.exit(1)
    
    if args.TS12:
        ts12_model = next((model for model in models_config if model.get("ts_number") == "12"), None)
        if ts12_model:
            models_to_process.append(ts12_model)
        else:
            print("ERROR Error: TS12 model not found!")
            sys.exit(1)
    
    if args.TS13:
        ts13_model = next((model for model in models_config if model.get("ts_number") == "13"), None)
        if ts13_model:
            models_to_process.append(ts13_model)
        else:
            print("ERROR Error: TS13 model not found!")
            sys.exit(1)
    
    if args.TS14:
        ts14_model = next((model for model in models_config if model.get("ts_number") == "14"), None)
        if ts14_model:
            models_to_process.append(ts14_model)
        else:
            print("ERROR Error: TS14 model not found!")
            sys.exit(1)
    
    if args.TS15:
        ts15_model = next((model for model in models_config if model.get("ts_number") == "15"), None)
        if ts15_model:
            models_to_process.append(ts15_model)
        else:
            print("ERROR Error: TS15 model not found!")
            sys.exit(1)
    
    if args.TS46:
        ts46_model = next((model for model in models_config if model.get("ts_number") == "46"), None)
        if ts46_model:
            models_to_process.append(ts46_model)
        else:
            print("ERROR Error: TS46 model not found!")
            sys.exit(1)
    
    if args.TS47:
        # TS47 can be either WGS_CSBD or GBDF depending on the flag used
        if args.wgs_csbd:
            # Look for WGS_CSBD TS47 model
            ts47_model = next((model for model in models_config if model.get("ts_number") == "47"), None)
            if ts47_model:
                models_to_process.append(ts47_model)
            else:
                print("ERROR Error: WGS_CSBD TS47 model not found!")
                sys.exit(1)
        elif args.gbdf_mcr:
            # Look for GBDF TS47 model
            gbdf_models = get_models_config(use_dynamic=True, use_gbdf_mcr=True)
            ts47_model = next((model for model in gbdf_models if model.get("ts_number") == "47"), None)
            if ts47_model:
                models_to_process.append(ts47_model)
            else:
                print("ERROR Error: GBDF TS47 model not found!")
                sys.exit(1)
        else:
            print("ERROR Error: TS47 requires either --wgs_csbd or --gbdf_mcr flag!")
            print("\nPlease specify which TS47 model to process:")
            print("  python main_processor.py --wgs_csbd --TS47    # Process WGS_CSBD TS47 model")
            print("  python main_processor.py --gbdf_mcr --TS47    # Process GBDF TS47 model")
            sys.exit(1)
    
    if args.all:
        models_to_process = models_config
        print(f"SUCCESS Processing all {len(models_config)} discovered models")
    
    # Check if appropriate flag is required for TS model processing
    wgs_csbd_models = any([args.TS01, args.TS02, args.TS03, args.TS04, args.TS05, 
                          args.TS06, args.TS07, args.TS08, args.TS09, args.TS10, 
                          args.TS11, args.TS12, args.TS13, args.TS14, args.TS15, args.TS46,
                          (args.TS47 and args.wgs_csbd)])  # TS47 is WGS_CSBD when wgs_csbd flag is used
    # TS47 can be either WGS_CSBD or GBDF depending on flag - only consider it GBDF if gbdf_mcr flag is used
    gbdf_mcr_models = args.TS47 and args.gbdf_mcr
    all_models = args.all
    
    if wgs_csbd_models and not args.wgs_csbd:
        print("ERROR Error: --wgs_csbd flag is required for WGS_CSBD TS model processing!")
        print("\nPlease use the --wgs_csbd flag with WGS_CSBD TS model commands:")
        print("  python main_processor.py --wgs_csbd --TS01    # Process TS01 model (Covid)")
        print("  python main_processor.py --wgs_csbd --TS02    # Process TS02 model (Laterality Policy)")
        print("  python main_processor.py --wgs_csbd --TS03    # Process TS03 model")
        print("  python main_processor.py --wgs_csbd --TS04    # Process TS04 model")
        print("  python main_processor.py --wgs_csbd --TS05    # Process TS05 model")
        print("  python main_processor.py --wgs_csbd --TS06    # Process TS06 model")
        print("  python main_processor.py --wgs_csbd --TS07    # Process TS07 model")
        print("  python main_processor.py --wgs_csbd --TS08    # Process TS08 model")
        print("  python main_processor.py --wgs_csbd --TS09    # Process TS09 model")
        print("  python main_processor.py --wgs_csbd --TS10    # Process TS10 model")
        print("  python main_processor.py --wgs_csbd --TS11    # Process TS11 model")
        print("  python main_processor.py --wgs_csbd --TS12    # Process TS12 model")
        print("  python main_processor.py --wgs_csbd --TS13    # Process TS13 model")
        print("  python main_processor.py --wgs_csbd --TS14    # Process TS14 model")
        print("  python main_processor.py --wgs_csbd --TS15    # Process TS15 model")
        print("  python main_processor.py --wgs_csbd --TS46    # Process TS46 model")
        print("  python main_processor.py --wgs_csbd --TS47    # Process WGS_CSBD TS47 model")
        print("  python main_processor.py --wgs_csbd --all     # Process all discovered models")
        print("\nUse --help for more information.")
        sys.exit(1)
    
    if gbdf_mcr_models and not args.gbdf_mcr:
        print("ERROR Error: --gbdf_mcr flag is required for GBDF MCR TS model processing!")
        print("\nPlease use the --gbdf_mcr flag with GBDF MCR TS model commands:")
        print("  python main_processor.py --gbdf_mcr --TS47    # Process GBDF TS47 model (Covid GBDF MCR)")
        print("\nUse --help for more information.")
        sys.exit(1)
    
    if all_models and not args.wgs_csbd and not args.gbdf_mcr:
        print("ERROR Error: Either --wgs_csbd or --gbdf_mcr flag is required for --all processing!")
        print("\nPlease specify which type of models to process:")
        print("  python main_processor.py --wgs_csbd --all     # Process all WGS_CSBD models")
        print("  python main_processor.py --gbdf_mcr --all     # Process all GBDF MCR models")
        print("\nUse --help for more information.")
        sys.exit(1)
    
    # If no specific model is selected, show help
    if not models_to_process:
        print("ERROR Error: No model specified!")
        print("\nPlease specify which model to process:")
        print("  --wgs_csbd --TS01    Process TS01 model (Covid)")
        print("  --wgs_csbd --TS02    Process TS02 model (Laterality Policy)")
        print("  --wgs_csbd --TS03    Process TS03 model (Revenue code Services not payable on Facility claim Sub Edit 5)")
        print("  --wgs_csbd --TS04    Process TS04 model (Revenue code Services not payable on Facility claim - Sub Edit 4)")
        print("  --wgs_csbd --TS05    Process TS05 model (Revenue code Services not payable on Facility claim Sub Edit 3)")
        print("  --wgs_csbd --TS06    Process TS06 model (Revenue code Services not payable on Facility claim Sub Edit 2)")
        print("  --wgs_csbd --TS07    Process TS07 model (Revenue code Services not payable on Facility claim Sub Edit 1)")
        print("  --wgs_csbd --TS08    Process TS08 model (Lab panel Model)")
        print("  --wgs_csbd --TS09    Process TS09 model (Device Dependent Procedures)")
        print("  --wgs_csbd --TS10    Process TS10 model")
        print("  --wgs_csbd --TS11    Process TS11 model (Revenue Code to HCPCS Xwalk-1B)")
        print("  --wgs_csbd --TS12    Process TS12 model (Incidentcal Services Facility)")
        print("  --wgs_csbd --TS13    Process TS13 model (Revenue model CR v3)")
        print("  --wgs_csbd --TS14    Process TS14 model (HCPCS to Revenue Code Xwalk)")
        print("  --wgs_csbd --TS15    Process TS15 model (revenue model)")
        print("  --wgs_csbd --TS46    Process TS46 model (Multiple E&M Same day)")
        print("  --gbdf_mcr --TS47    Process TS47 model (Covid GBDF MCR)")
        print("  --wgs_csbd --all     Process all discovered WGS_CSBD models")
        print("  --gbdf_mcr --all     Process all discovered GBDF MCR models")
        print("  --list    List all available TS models")
        print("\nUse --help for more information.")
        sys.exit(1)
    
    # Process selected models
    generate_postman = not args.no_postman
    
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
                postman_file_name=model_config.get('postman_file_name')
            )
            
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
    else:
        print("\nERROR No files were processed.")


if __name__ == "__main__":
    main()
