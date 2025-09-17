# Configuration file for multiple models
# This file now supports both static configurations and dynamic discovery

import os
from dynamic_models import discover_ts_folders, get_model_by_ts_number, get_all_models

# Static model configurations (for backward compatibility)
STATIC_MODELS_CONFIG = [
    {
        "edit_id": "rvn001",
        "code": "00W5",
        "source_dir": "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_sur/regression",
        "dest_dir": "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_dis/regression",
        "postman_collection_name": "TS_1_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn001_00w5.json"
    },
    {
        "edit_id": "rvn002",
        "code": "00W6",
        "source_dir": "TS_02_REVENUE_WGS_CSBD_rvn002_00W6_sur/regression",
        "dest_dir": "renaming_jsons/TS_02_REVENUE_WGS_CSBD_rvn002_00W6_dis/regression",
        "postman_collection_name": "TS_2_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn002_00w6.json"
    },
    {
        "edit_id": "rvn003",
        "code": "00W7",
        "source_dir": "TS_03_REVENUE_WGS_CSBD_rvn003_00W7_sur/regression",
        "dest_dir": "renaming_jsons/TS_03_REVENUE_WGS_CSBD_rvn003_00W7_dis/regression",
        "postman_collection_name": "TS_3_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn003_00w7.json"
    },
    {
        "edit_id": "rvn004",
        "code": "00W8", 
        "source_dir": "TS_04_REVENUE_WGS_CSBD_rvn004_00W8_sur/regression",
        "dest_dir": "renaming_jsons/TS_04_REVENUE_WGS_CSBD_rvn004_00W8_dis/regression",
        "postman_collection_name": "TS_4_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn004_00w8.json"
    },
    {
        "edit_id": "rvn005",
        "code": "00W9", 
        "source_dir": "TS_05_REVENUE_WGS_CSBD_rvn005_00W9_sur/regression",
        "dest_dir": "renaming_jsons/TS_05_REVENUE_WGS_CSBD_rvn005_00W9_dis/regression",
        "postman_collection_name": "TS_5_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn005_00w9.json"
    },
    {
        "edit_id": "rvn006",
        "code": "00W10", 
        "source_dir": "TS_06_REVENUE_WGS_CSBD_rvn006_00W10_sur/regression",
        "dest_dir": "renaming_jsons/TS_06_REVENUE_WGS_CSBD_rvn006_00W10_dis/regression",
        "postman_collection_name": "TS_6_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn006_00w10.json"
    },
    {
        "edit_id": "rvn011",
        "code": "00W11",
        "source_dir": "TS_07_REVENUE_WGS_CSBD_rvn011_00W11_sur/regression",
        "dest_dir": "renaming_jsons/TS_07_REVENUE_WGS_CSBD_rvn011_00W11_dis/regression",
        "postman_collection_name": "TS_7_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn011_00w11.json"
    },
    {
        "edit_id": "rvn012",
        "code": "00W12",
        "source_dir": "TS_13_REVENUE_WGS_CSBD_rvn012_00W12_sur/regression",
        "dest_dir": "renaming_jsons/TS_13_REVENUE_WGS_CSBD_rvn012_00W12_dis/regression",
        "postman_collection_name": "TS_13_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn012_00w12.json"
    },
    {
        "edit_id": "rvn013",
        "code": "00W13",
        "source_dir": "TS_50_REVENUE_WGS_CSBD_rvn013_00W13_sur/regression",
        "dest_dir": "renaming_jsons/TS_50_REVENUE_WGS_CSBD_rvn013_00W13_dis/regression",
        "postman_collection_name": "TS_50_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn013_00w13.json"
    },
    {
        "edit_id": "rvn014",
        "code": "00W14",
        "source_dir": "TS_100_REVENUE_WGS_CSBD_rvn014_00W14_sur/regression",
        "dest_dir": "renaming_jsons/TS_100_REVENUE_WGS_CSBD_rvn014_00W14_dis/regression",
        "postman_collection_name": "TS_100_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn014_00w14.json"
    },
    {
        "edit_id": "rvn015",
        "code": "00W15",
        "source_dir": "TS_120_REVENUE_WGS_CSBD_rvn015_00W15_sur/regression",
        "dest_dir": "renaming_jsons/TS_120_REVENUE_WGS_CSBD_rvn015_00W15_dis/regression",
        "postman_collection_name": "TS_120_collection",
        "postman_file_name": "revenue_wgs_csbd_rvn015_00w15.json"
    }
]

# Dynamic model discovery
def get_models_config(use_dynamic=True):
    """
    Get model configurations using dynamic discovery or static config.
    
    Args:
        use_dynamic: If True, use dynamic discovery; if False, use static config
        
    Returns:
        List of model configurations
    """
    if use_dynamic:
        try:
            # Use dynamic discovery
            discovered_models = discover_ts_folders()
            if discovered_models:
                print(f"✅ Dynamic discovery found {len(discovered_models)} models")
                return discovered_models
            else:
                print("⚠️  No models found via dynamic discovery, falling back to static config")
                return STATIC_MODELS_CONFIG
        except Exception as e:
            print(f"⚠️  Dynamic discovery failed: {e}, falling back to static config")
            return STATIC_MODELS_CONFIG
    else:
        return STATIC_MODELS_CONFIG

def get_model_by_ts(ts_number):
    """
    Get a specific model by TS number using dynamic discovery.
    
    Args:
        ts_number: TS number (e.g., "01", "02", "03")
        
    Returns:
        Model configuration dict or None if not found
    """
    try:
        return get_model_by_ts_number(ts_number)
    except Exception as e:
        print(f"❌ Error getting model for TS_{ts_number}: {e}")
        return None

# For backward compatibility, keep MODELS_CONFIG as a property
MODELS_CONFIG = get_models_config(use_dynamic=True)

# Global settings
GENERATE_POSTMAN_COLLECTIONS = True
VERBOSE_OUTPUT = True
