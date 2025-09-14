#!/usr/bin/env python3
"""
Script to process multiple models with different edit_id and code values.
This script handles renaming files and generating Postman collections for multiple models.
"""

import os
from rename_files_with_postman import rename_files


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
    """Main function with configuration loaded from models_config.py."""
    
    try:
        from models_config import MODELS_CONFIG, GENERATE_POSTMAN_COLLECTIONS
        models_config = MODELS_CONFIG
        generate_postman = GENERATE_POSTMAN_COLLECTIONS
        print("✅ Configuration loaded from models_config.py")
    except ImportError:
        print("⚠️  models_config.py not found, using default configuration")
        # Fallback configuration
        models_config = [
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
        generate_postman = True
    
    # Process all models
    successful_models, failed_models = process_multiple_models(
        models_config=models_config,
        generate_postman=generate_postman
    )
    
    # Additional instructions
    if successful_models:
        print(f"\n📦 POSTMAN COLLECTIONS GENERATED:")
        print("To use these collections:")
        print("1. Open Postman")
        print("2. Click 'Import'")
        print("3. Select the collection files from 'postman_collections' folder")
        print("4. Start testing your APIs!")
        
        print(f"\n📁 GENERATED COLLECTIONS:")
        for model in successful_models:
            collection_name = f"TS_01_REVENUE_WGS_CSBD_{model['edit_id']}_{model['code']}"
            print(f"   • {collection_name}")


if __name__ == "__main__":
    main()
