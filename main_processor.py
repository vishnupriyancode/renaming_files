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
            "market": "EX",   # market -> EX
            "date": "EX"      # date -> EX
        }
    }
    
    # Auto-generate paths if not provided
    if source_dir is None:
        source_dir = f"TS_01_REVENUE_WGS_CSBD_{edit_id}_{code}_payloads_sur/regression"
    
    if dest_dir is None:
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
            
            # Source and destination paths
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, new_filename)
            
            try:
                # Copy the file to destination with new name
                shutil.copy2(source_path, dest_path)
                print(f"✓ Successfully copied and renamed: {filename} → {new_filename}")
                
                # Remove the original file
                os.remove(source_path)
                print(f"✓ Removed original file: {filename}")
                
                renamed_files.append(new_filename)
                
            except Exception as e:
                print(f"✗ Error processing {filename}: {e}")
                
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
            
            # Source and destination paths
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, new_filename)
            
            try:
                # Copy the file to destination with new name
                shutil.copy2(source_path, dest_path)
                print(f"✓ Successfully copied and renamed: {filename} → {new_filename}")
                
                # Remove the original file
                os.remove(source_path)
                print(f"✓ Removed original file: {filename}")
                
                renamed_files.append(new_filename)
                
            except Exception as e:
                print(f"✗ Error processing {filename}: {e}")
                
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
                    print(f"✓ Successfully moved: {filename}")
                    
                    # Remove the original file
                    os.remove(source_path)
                    print(f"✓ Removed original file: {filename}")
                    
                    renamed_files.append(new_filename)
                    
                except Exception as e:
                    print(f"✗ Error processing {filename}: {e}")
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
            # Initialize Postman generator
            generator = PostmanCollectionGenerator(
                source_dir="renaming_jsons",
                output_dir="postman_collections"
            )
            
            # Extract collection name from destination directory if not provided
            if postman_collection_name is None:
                # Extract from dest_dir path
                dest_path_parts = dest_dir.split(os.sep)
                for part in dest_path_parts:
                    if part.startswith("TS_") and "_payloads_dis" in part:
                        postman_collection_name = part.replace("_payloads_dis", "")
                        break
                
                # Fallback to auto-generated name if not found
                if postman_collection_name is None:
                    postman_collection_name = f"TS_01_REVENUE_WGS_CSBD_{edit_id}_{code}"
            
            # Get custom filename from model config if available
            custom_filename = postman_file_name
            
            # Generate collection
            collection_path = generator.generate_postman_collection(postman_collection_name, custom_filename)
            
            if collection_path:
                print(f"✅ Postman collection generated: {collection_path}")
                print(f"📦 Collection name: {postman_collection_name}")
                print("\n🎯 Ready for API testing!")
                print("=" * 60)
                print("To use this collection:")
                print("1. Open Postman")
                print("2. Click 'Import'")
                print(f"3. Select the file: {collection_path}")
                print("4. Start testing your APIs!")
            else:
                print("❌ Failed to generate Postman collection")
                
        except Exception as e:
            print(f"❌ Error generating Postman collection: {e}")
    
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
            "source_dir": "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/regression",
            "dest_dir": "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis/regression",
            "postman_collection_name": "TS_01_REVENUE_WGS_CSBD_rvn001_00W5"
        },
        {
            "edit_id": "rvn002", 
            "code": "00W6",
            "source_dir": "TS_01_REVENUE_WGS_CSBD_rvn002_00W6_payloads_sur/regression",
            "dest_dir": "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn002_00W6_payloads_dis/regression",
            "postman_collection_name": "TS_01_REVENUE_WGS_CSBD_rvn002_00W6"
        }
    ]
    """
    
    print("🚀 Starting Multi-Model Processing")
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
        
        print(f"\n📋 Processing Model {i}/{len(models_config)}")
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
                print(f"✅ Model {edit_id}_{code}: Successfully processed {len(renamed_files)} files")
                successful_models.append({
                    "edit_id": edit_id,
                    "code": code,
                    "files_count": len(renamed_files),
                    "files": renamed_files
                })
                total_processed += len(renamed_files)
            else:
                print(f"⚠️  Model {edit_id}_{code}: No files were processed")
                failed_models.append({
                    "edit_id": edit_id,
                    "code": code,
                    "reason": "No files found or processed"
                })
                
        except Exception as e:
            print(f"❌ Model {edit_id}_{code}: Failed with error - {e}")
            failed_models.append({
                "edit_id": edit_id,
                "code": code,
                "reason": str(e)
            })
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 PROCESSING SUMMARY")
    print("=" * 80)
    print(f"Total models processed: {len(models_config)}")
    print(f"Successful models: {len(successful_models)}")
    print(f"Failed models: {len(failed_models)}")
    print(f"Total files processed: {total_processed}")
    
    if successful_models:
        print(f"\n✅ SUCCESSFUL MODELS:")
        for model in successful_models:
            print(f"   • {model['edit_id']}_{model['code']}: {model['files_count']} files")
    
    if failed_models:
        print(f"\n❌ FAILED MODELS:")
        for model in failed_models:
            print(f"   • {model['edit_id']}_{model['code']}: {model['reason']}")
    
    print("\n🎯 All models processed!")
    return successful_models, failed_models


def main():
    """Main function with comprehensive command line interface."""
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Main Processor - Rename files and generate Postman collections for TS models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process specific TS models
  python main_processor.py --TS07    # Process TS07 model
  python main_processor.py --TS100   # Process TS100 model  
  python main_processor.py --TS120   # Process TS120 model
  python main_processor.py --TS13    # Process TS13 model
  python main_processor.py --TS50    # Process TS50 model
  python main_processor.py --TS130   # Process TS130 model
  
  # Process all discovered models
  python main_processor.py --all     # Process all discovered models
  
  # List available models
  python main_processor.py --list    # List all available TS models
  
  # Skip Postman generation
  python main_processor.py --TS07 --no-postman
  
  # Process with custom parameters
  python main_processor.py --edit-id rvn001 --code 00W5 --source-dir custom/path
        """
    )
    
    # Add model-specific arguments for available models
    parser.add_argument("--TS07", action="store_true", 
                       help="Process TS07 model")
    parser.add_argument("--TS100", action="store_true", 
                       help="Process TS100 model")
    parser.add_argument("--TS120", action="store_true", 
                       help="Process TS120 model")
    parser.add_argument("--TS13", action="store_true", 
                       help="Process TS13 model")
    parser.add_argument("--TS50", action="store_true", 
                       help="Process TS50 model")
    parser.add_argument("--TS130", action="store_true", 
                       help="Process TS130 model")
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
        models_config = get_models_config(use_dynamic=True)
        print("✅ Configuration loaded with dynamic discovery")
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("Please ensure models_config.py and dynamic_models.py exist.")
        sys.exit(1)
    
    # Handle --list option
    if args.list:
        print("\n📋 AVAILABLE TS MODELS")
        print("=" * 50)
        if models_config:
            for model in models_config:
                print(f"TS_{model['ts_number']}: {model['edit_id']}_{model['code']}")
                print(f"  📁 Source: {model['source_dir']}")
                print(f"  📁 Dest:   {model['dest_dir']}")
                print()
        else:
            print("❌ No TS models found")
        sys.exit(0)
    
    # Handle custom parameters
    if args.edit_id and args.code:
        print(f"\n🔧 Processing custom model: {args.edit_id}_{args.code}")
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
                print(f"✅ Custom model {args.edit_id}_{args.code}: Successfully processed {len(renamed_files)} files")
            else:
                print(f"⚠️  Custom model {args.edit_id}_{args.code}: No files were processed")
                
        except Exception as e:
            print(f"❌ Custom model {args.edit_id}_{args.code}: Failed with error - {e}")
            sys.exit(1)
        
        sys.exit(0)
    
    # Determine which models to process
    models_to_process = []
    
    # Handle specific TS numbers for available models
    if args.TS07:
        ts07_model = next((model for model in models_config if model.get("ts_number") == "07"), None)
        if ts07_model:
            models_to_process.append(ts07_model)
        else:
            print("❌ Error: TS07 model not found!")
            sys.exit(1)
    
    if args.TS100:
        ts100_model = next((model for model in models_config if model.get("ts_number") == "100"), None)
        if ts100_model:
            models_to_process.append(ts100_model)
        else:
            print("❌ Error: TS100 model not found!")
            sys.exit(1)
    
    if args.TS120:
        ts120_model = next((model for model in models_config if model.get("ts_number") == "120"), None)
        if ts120_model:
            models_to_process.append(ts120_model)
        else:
            print("❌ Error: TS120 model not found!")
            sys.exit(1)
    
    if args.TS13:
        ts13_model = next((model for model in models_config if model.get("ts_number") == "13"), None)
        if ts13_model:
            models_to_process.append(ts13_model)
        else:
            print("❌ Error: TS13 model not found!")
            sys.exit(1)
    
    if args.TS50:
        ts50_model = next((model for model in models_config if model.get("ts_number") == "50"), None)
        if ts50_model:
            models_to_process.append(ts50_model)
        else:
            print("❌ Error: TS50 model not found!")
            sys.exit(1)
    
    if args.TS130:
        ts130_model = next((model for model in models_config if model.get("ts_number") == "130"), None)
        if ts130_model:
            models_to_process.append(ts130_model)
        else:
            print("❌ Error: TS130 model not found!")
            sys.exit(1)
    
    if args.all:
        models_to_process = models_config
        print(f"✅ Processing all {len(models_config)} discovered models")
    
    # If no specific model is selected, show help
    if not models_to_process:
        print("❌ Error: No model specified!")
        print("\nPlease specify which model to process:")
        print("  --TS07    Process TS07 model")
        print("  --TS100   Process TS100 model")
        print("  --TS120   Process TS120 model")
        print("  --TS13    Process TS13 model")
        print("  --TS50    Process TS50 model")
        print("  --TS130   Process TS130 model")
        print("  --all     Process all discovered models")
        print("  --list    List all available TS models")
        print("\nUse --help for more information.")
        sys.exit(1)
    
    # Process selected models
    generate_postman = not args.no_postman
    
    print(f"\n🚀 Processing {len(models_to_process)} model(s)...")
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
        
        print(f"\n📋 Processing Model {i}/{len(models_to_process)}: TS_{ts_number} ({edit_id}_{code})")
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
                print(f"✅ Model TS_{ts_number} ({edit_id}_{code}): Successfully processed {len(renamed_files)} files")
                successful_models.append({
                    "ts_number": ts_number,
                    "edit_id": edit_id,
                    "code": code,
                    "files_count": len(renamed_files)
                })
                total_processed += len(renamed_files)
            else:
                print(f"⚠️  Model TS_{ts_number} ({edit_id}_{code}): No files were processed")
                
        except Exception as e:
            print(f"❌ Model TS_{ts_number} ({edit_id}_{code}): Failed with error - {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Models processed: {len(models_to_process)}")
    print(f"Successful models: {len(successful_models)}")
    print(f"Total files processed: {total_processed}")
    
    if successful_models:
        print(f"\n✅ SUCCESSFUL MODELS:")
        for model in successful_models:
            print(f"   • TS_{model['ts_number']} ({model['edit_id']}_{model['code']}): {model['files_count']} files")
        
        if generate_postman:
            print(f"\n📦 POSTMAN COLLECTIONS GENERATED:")
            print("To use these collections:")
            print("1. Open Postman")
            print("2. Click 'Import'")
            print("3. Select the collection files from 'postman_collections' folder")
            print("4. Start testing your APIs!")
    
    if total_processed > 0:
        print(f"\n🎉 Successfully processed {total_processed} files!")
        print("Files are now ready for API testing with Postman.")
    else:
        print("\n❌ No files were processed.")


if __name__ == "__main__":
    main()
