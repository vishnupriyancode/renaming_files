# Configuration file for multiple models
# This file now supports both static configurations and dynamic discovery

import os
from dynamic_models import discover_ts_folders, get_model_by_ts_number, get_all_models

# Static model configurations (for backward compatibility)
STATIC_MODELS_CONFIG = [
    {
        "ts_number": "01",
        "edit_id": "RULEEM000001",
        "code": "W04",
        "source_dir": "source_folder/TS_01_Covid_WGS_CSBD_RULEEM000001_W04_sur/regression",
        "dest_dir": "renaming_jsons/TS_01_Covid_WGS_CSBD_RULEEM000001_W04_dis/regression",
        "postman_collection_name": "TS_01_Covid_Collection",
        "postman_file_name": "covid_wgs_csbd_RULEEM000001_w04.json"
    },
    {
        "ts_number": "02",
        "edit_id": "RULELATE000001",
        "code": "00W17",
        "source_dir": "source_folder/TS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_sur/regression",
        "dest_dir": "renaming_jsons/TS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_dis/regression",
        "postman_collection_name": "TS_02_Laterality_Collection",
        "postman_file_name": "laterality_wgs_csbd_RULELATE000001_00w17.json"
    },
    {
        "ts_number": "03",
        "edit_id": "RULEREVE000005",
        "code": "00W28",
        "source_dir": "source_folder/TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_sur/regression",
        "dest_dir": "renaming_jsons/TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_dis/regression",
        "postman_collection_name": "TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000005_00w28.json"
    },
    {
        "ts_number": "04",
        "edit_id": "RULEREVE000004",
        "code": "00W28",
        "source_dir": "source_folder/TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_WGS_CSBD_RULEREVE000004_00W28_sur/regression",
        "dest_dir": "renaming_jsons/TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_WGS_CSBD_RULEREVE000004_00W28_dis/regression",
        "postman_collection_name": "TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000004_00w28.json"
    },
    {
        "ts_number": "05",
        "edit_id": "RULEREVE000003",
        "code": "00W28",
        "source_dir": "source_folder/TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_WGS_CSBD_RULEREVE000003_00W28_sur/regression",
        "dest_dir": "renaming_jsons/TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_WGS_CSBD_RULEREVE000003_00W28_dis/regression",
        "postman_collection_name": "TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000003_00w28.json"
    },
    {
        "ts_number": "06",
        "edit_id": "RULEREVE000002",
        "code": "00W28",
        "source_dir": "source_folder/TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_WGS_CSBD_RULEREVE000002_00W28_sur/regression",
        "dest_dir": "renaming_jsons/TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_WGS_CSBD_RULEREVE000002_00W28_dis/regression",
        "postman_collection_name": "TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000002_00w28.json"
    },
    {
        "ts_number": "07",
        "edit_id": "RULEREVE000001",
        "code": "00W28",
        "source_dir": "source_folder/TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_WGS_CSBD_RULEREVE000001_00W28_sur/regression",
        "dest_dir": "renaming_jsons/TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_WGS_CSBD_RULEREVE000001_00W28_dis/regression",
        "postman_collection_name": "TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000001_00w28.json"
    },
    {
        "ts_number": "08",
        "edit_id": "RULELAB0000009",
        "code": "00W13",
        "source_dir": "source_folder/TS_08_Lab panel Model_WGS_CSBD_RULELAB0000009_00W13_sur/regression",
        "dest_dir": "renaming_jsons/TS_08_Lab panel Model_WGS_CSBD_RULELAB0000009_00W13_dis/regression",
        "postman_collection_name": "TS_08_Lab panel Model_Collection",
        "postman_file_name": "lab_wgs_csbd_RULELAB0000009_00w13.json"
    },
    {
        "ts_number": "09",
        "edit_id": "RULEDEVI000003",
        "code": "00W13",
        "source_dir": "source_folder/TS_09_Device Dependent Procedures(R1)-1B_WGS_CSBD_RULEDEVI000003_00W13_sur/regression",
        "dest_dir": "renaming_jsons/TS_09_Device Dependent Procedures(R1)-1B_WGS_CSBD_RULEDEVI000003_00W13_dis/regression",
        "postman_collection_name": "TS_09_Device Dependent Procedures_Collection",
        "postman_file_name": "device_wgs_csbd_RULEDEVI000003_00w13.json"
    },
    {
        "ts_number": "10",
        "edit_id": "RULERECO000001",
        "code": "00W34",
        "source_dir": "source_folder/TS_10_Recovery Room Reimbursement_WGS_CSBD_RULERECO000001_00W34_sur/regression",
        "dest_dir": "renaming_jsons/TS_10_Recovery Room Reimbursement_WGS_CSBD_RULERECO000001_00W34_dis/regression",
        "postman_collection_name": "TS_10_Recovery Room Reimbursement_Collection",
        "postman_file_name": "recovery_wgs_csbd_RULERECO000001_00w34.json"
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
