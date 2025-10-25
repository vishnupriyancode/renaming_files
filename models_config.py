# Configuration file for multiple models
# This file now supports both static configurations and dynamic discovery

import os
from dynamic_models import discover_ts_folders, get_model_by_ts_number, get_all_models

# Static model configurations (for backward compatibility)
STATIC_MODELS_CONFIG = {
    "wgs_csbd": [
    {
        "ts_number": "01",
        "edit_id": "RULEEM000001",
        "code": "W04",
        "source_dir": "source_folder/WGS_CSBD/TS_01_Covid_WGS_CSBD_RULEEM000001_W04_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_01_Covid_WGS_CSBD_RULEEM000001_W04_dis/regression",
        "postman_collection_name": "TS_01_Covid_Collection",
        "postman_file_name": "covid_wgs_csbd_RULEEM000001_W04.json"
    },
    {
        "ts_number": "02",
        "edit_id": "RULELATE000001",
        "code": "00W17",
        "source_dir": "source_folder/WGS_CSBD/TS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_dis/regression",
        "postman_collection_name": "TS_02_Laterality_Collection",
        "postman_file_name": "laterality_wgs_csbd_RULELATE000001_00W17.json"
    },
    {
        "ts_number": "03",
        "edit_id": "RULEREVE000005",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_dis/regression",
        "postman_collection_name": "TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000005_00W28.json"
    },
    {
        "ts_number": "04",
        "edit_id": "RULEREVE000004",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_WGS_CSBD_RULEREVE000004_00W28_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_WGS_CSBD_RULEREVE000004_00W28_dis/regression",
        "postman_collection_name": "TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000004_00W28.json"
    },
    {
        "ts_number": "05",
        "edit_id": "RULEREVE000003",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_WGS_CSBD_RULEREVE000003_00W28_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_WGS_CSBD_RULEREVE000003_00W28_dis/regression",
        "postman_collection_name": "TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000003_00W28.json"
    },
    {
        "ts_number": "06",
        "edit_id": "RULEREVE000002",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_WGS_CSBD_RULEREVE000002_00W28_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_WGS_CSBD_RULEREVE000002_00W28_dis/regression",
        "postman_collection_name": "TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000002_00W28.json"
    },
    {
        "ts_number": "07",
        "edit_id": "RULEREVE000001",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_WGS_CSBD_RULEREVE000001_00W28_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_WGS_CSBD_RULEREVE000001_00W28_dis/regression",
        "postman_collection_name": "TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000001_00W28.json"
    },
    {
        "ts_number": "08",
        "edit_id": "RULELAB0000009",
        "code": "00W13",
        "source_dir": "source_folder/WGS_CSBD/TS_08_Lab panel Model_WGS_CSBD_RULELAB0000009_00W13_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_08_Lab panel Model_WGS_CSBD_RULELAB0000009_00W13_dis/regression",
        "postman_collection_name": "TS_08_Lab panel Model_Collection",
        "postman_file_name": "lab_wgs_csbd_RULELAB0000009_00W13.json"
    },
    {
        "ts_number": "09",
        "edit_id": "RULEDEVI000003",
        "code": "00W13",
        "source_dir": "source_folder/WGS_CSBD/TS_09_Device Dependent Procedures(R1)-1B_WGS_CSBD_RULEDEVI000003_00W13_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_09_Device Dependent Procedures(R1)-1B_WGS_CSBD_RULEDEVI000003_00W13_dis/regression",
        "postman_collection_name": "TS_09_Device Dependent Procedures_Collection",
        "postman_file_name": "device_wgs_csbd_RULEDEVI000003_00W13.json"
    },
    {
        "ts_number": "10",
        "edit_id": "RULERECO000001",
        "code": "00W34",
        "source_dir": "source_folder/WGS_CSBD/TS_10_Recovery Room Reimbursement_WGS_CSBD_RULERECO000001_00W34_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_10_Recovery Room Reimbursement_WGS_CSBD_RULERECO000001_00W34_dis/regression",
        "postman_collection_name": "TS_10_Recovery Room Reimbursement_Collection",
        "postman_file_name": "recovery_wgs_csbd_RULERECO000001_00W34.json"
    },
    {
        "ts_number": "11",
        "edit_id": "RULERECO000003",
        "code": "00W26",
        "source_dir": "source_folder/WGS_CSBD/TS_11_Revenue Code to HCPCS Xwalk-1B_WGS_CSBD_RULERECO000003_00W26_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_11_Revenue Code to HCPCS Xwalk-1B_WGS_CSBD_RULERECO000003_00W26_dis/regression",
        "postman_collection_name": "TS_11_Revenue Code to HCPCS Xwalk-1B_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULERECO000003_00W26.json"
    },
    {
        "ts_number": "12",
        "edit_id": "RULEINCI000001",
        "code": "00W34",
        "source_dir": "source_folder/WGS_CSBD/TS_12_Incidentcal Services Facility_WGS_CSBD_RULEINCI000001_00W34_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_12_Incidentcal Services Facility_WGS_CSBD_RULEINCI000001_00W34_dis/regression",
        "postman_collection_name": "TS_12_Incidentcal Services Facility_Collection",
        "postman_file_name": "incidentcal_wgs_csbd_RULEINCI000001_00W34.json"
    },
    {
        "ts_number": "13",
        "edit_id": "RULERCE0000006",
        "code": "00W06",
        "source_dir": "source_folder/WGS_CSBD/TS_13_Revenue model CR v3_WGS_CSBD_RULERCE0000006_00W06_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_13_Revenue model CR v3_WGS_CSBD_RULERCE0000006_00W06_dis/regression",
        "postman_collection_name": "TS_13_Revenue model CR v3_Collection",
        "postman_file_name": "revenue_model_wgs_csbd_RULERCE0000006_00W06.json"
    },
    {
        "ts_number": "14",
        "edit_id": "RULERCE000001",
        "code": "00W26",
        "source_dir": "source_folder/WGS_CSBD/TS_14_HCPCS to Revenue Code Xwalk_WGS_CSBD_RULERCE000001_00W26_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_14_HCPCS to Revenue Code Xwalk_WGS_CSBD_RULERCE000001_00W26_dis/regression",
        "postman_collection_name": "TS_14_HCPCS to Revenue Code Xwalk_Collection",
        "postman_file_name": "hcpcs_wgs_csbd_RULERCE000001_00W26.json"
    },
    {
        "ts_number": "15",
        "edit_id": "RULERCE000005",
        "code": "00W06",
        "source_dir": "source_folder/WGS_CSBD/TS_15_revenue model_WGS_CSBD_RULERCE000005_00W06_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_15_revenue model_WGS_CSBD_RULERCE000005_00W06_dis/regression",
        "postman_collection_name": "TS_15_revenue model_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULERCE000005_00W06.json"
    },
    {
        "ts_number": "46",
        "edit_id": "RULEEMSD000002",
        "code": "00W09",
        "source_dir": "source_folder/WGS_CSBD/TS_46_Multiple E&M Same day_WGS_CSBD_RULEEMSD000002_00W09_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_46_Multiple E&M Same day_WGS_CSBD_RULEEMSD000002_00W09_dis/regression",
        "postman_collection_name": "TS_46_Multiple E&M Same day_Collection",
        "postman_file_name": "multiple_em_wgs_csbd_RULEEMSD000002_00W09.json"
    },
    {
        "ts_number": "20",
        "edit_id": "RULERBWR000001",
        "code": "00W30",
        "source_dir": "source_folder/WGS_CSBD/TS_20_RadioservicesbilledwithoutRadiopharma_WGS_CSBD_RULERBWR000001_00W30_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_20_RadioservicesbilledwithoutRadiopharma_WGS_CSBD_RULERBWR000001_00W30_dis/regression",
        "postman_collection_name": "TS_20_RadioservicesbilledwithoutRadiopharma_Collection",
        "postman_file_name": "radioservices_wgs_csbd_RULERBWR000001_00W30.json"
    },
    {
        "ts_number": "47",
        "edit_id": "RULEMBOS000001",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/TS_47_Multiple Billing of Obstetrical Services_WGS_CSBD_RULEMBOS000001_00W28_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/TS_47_Multiple Billing of Obstetrical Services_WGS_CSBD_RULEMBOS000001_00W28_dis/regression",
        "postman_collection_name": "TS_47_Multiple Billing of Obstetrical Services_Collection",
        "postman_file_name": "multiple_billing_obstetrical_wgs_csbd_RULEMBOS000001_00W28.json"
    },
    {
        "ts_number": "48",
        "edit_id": "RULERCTH00001",
        "code": "00W26",
        "source_dir": "source_folder/WGS_CSBD/CSBD_TS_48_Revenue code to HCPCS Alignment edit_WGS_CSBD_RULERCTH00001_00W26_sur/regression",
        "dest_dir": "renaming_jsons/WGS_CSBD/CSBD_TS_48_Revenue code to HCPCS Alignment edit_WGS_CSBD_RULERCTH00001_00W26_dis/regression",
        "postman_collection_name": "CSBD_TS_48_Revenue code to HCPCS Alignment edit_Collection",
        "postman_file_name": "revenue_hcpcs_alignment_wgs_csbd_RULERCTH00001_00W26.json"
    }
    ],
    "gbdf_mcr": [
        {
            "ts_number": "47",
            "edit_id": "RULEEM000001",
            "code": "v04",
            "source_dir": "source_folder/GBDF/TS_47_Covid_gbdf_mcr_RULEEM000001_v04_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_47_Covid_gbdf_mcr_RULEEM000001_v04_dis/regression",
            "postman_collection_name": "TS_47_Covid_gbdf_mcr_Collection",
            "postman_file_name": "covid_gbdf_mcr_RULEEM000001_v04.json"
        },
        {
            "ts_number": "48",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_48_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_48_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/regression",
            "postman_collection_name": "TS_48_Multiple E&M Same day_gbdf_mcr_Collection",
            "postman_file_name": "multiple_em_gbdf_mcr_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "138",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_138_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_138_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/regression",
            "postman_collection_name": "TS_138_Multiple E&M Same day_gbdf_mcr_Collection",
            "postman_file_name": "multiple_em_gbdf_mcr_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "140",
            "edit_id": "RULENDCUOM000001",
            "code": "v41",
            "source_dir": "source_folder/GBDF/TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_RULENDCUOM000001_v41_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_RULENDCUOM000001_v41_dis/regression",
            "postman_collection_name": "TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_Collection",
            "postman_file_name": "ndc_uom_gbdf_mcr_RULENDCUOM000001_v41.json"
        },
        {
            "ts_number": "144",
            "edit_id": "RULENEBU000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_RULENEBU000001_v18_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_RULENEBU000001_v18_dis/regression",
            "postman_collection_name": "TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_Collection",
            "postman_file_name": "nebulizer_gbdf_mcr_RULENEBU000001_v18.json"
        },
        {
            "ts_number": "146",
            "edit_id": "RULENMP000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_146_No match of Procedure code_gbdf_mcr_RULENMP000001_v18_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_146_No match of Procedure code_gbdf_mcr_RULENMP000001_v18_dis/regression",
            "postman_collection_name": "TS_146_No match of Procedure code_gbdf_mcr_Collection",
            "postman_file_name": "no_match_procedure_gbdf_mcr_RULENMP000001_v18.json"
        },
        {
            "ts_number": "60",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_60_Unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_v17_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_60_Unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_v17_dis/regression",
            "postman_collection_name": "TS_60_Unspecified_dx_code_outpt_gbdf_mcr_Collection",
            "postman_file_name": "unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_v17.json"
        }
    ],
    "gbdf_grs": [
        {
            "ts_number": "49",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_49_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_49_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/regression",
            "postman_collection_name": "TS_49_Multiple E&M Same day_gbdf_grs_Collection",
            "postman_file_name": "multiple_em_gbdf_grs_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "139",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_139_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_139_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/regression",
            "postman_collection_name": "TS_139_Multiple E&M Same day_gbdf_grs_Collection",
            "postman_file_name": "multiple_em_gbdf_grs_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "141",
            "edit_id": "RULENDCUOM000001",
            "code": "v41",
            "source_dir": "source_folder/GBDF/TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_RULENDCUOM000001_v41_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_RULENDCUOM000001_v41_dis/regression",
            "postman_collection_name": "TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_Collection",
            "postman_file_name": "ndc_uom_gbdf_grs_RULENDCUOM000001_v41.json"
        },
        {
            "ts_number": "145",
            "edit_id": "RULENEBU000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_RULENEBU000001_v18_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_RULENEBU000001_v18_dis/regression",
            "postman_collection_name": "TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_Collection",
            "postman_file_name": "nebulizer_gbdf_grs_RULENEBU000001_v18.json"
        },
        {
            "ts_number": "147",
            "edit_id": "RULENMP000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_147_No match of Procedure code_gbdf_grs_RULENMP000001_v18_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_147_No match of Procedure code_gbdf_grs_RULENMP000001_v18_dis/regression",
            "postman_collection_name": "TS_147_No match of Procedure code_gbdf_grs_Collection",
            "postman_file_name": "no_match_procedure_gbdf_grs_RULENMP000001_v18.json"
        },
        {
            "ts_number": "59",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_59_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_59_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17_dis/regression",
            "postman_collection_name": "TS_59_Unspecified_dx_code_outpt_gbdf_grs_Collection",
            "postman_file_name": "unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17.json"
        },
        {
            "ts_number": "61",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_61_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_61_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_dis/regression",
            "postman_collection_name": "TS_61_Unspecified_dx_code_prof_gbdf_grs_Collection",
            "postman_file_name": "unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17.json"
        },
        {
            "ts_number": "62",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_62_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_sur/regression",
            "dest_dir": "renaming_jsons/GBDF/TS_62_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_dis/regression",
            "postman_collection_name": "TS_62_Unspecified_dx_code_prof_gbdf_grs_Collection",
            "postman_file_name": "unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17.json"
        }
    ]
}

# Dynamic model discovery
def get_models_config(use_dynamic=True, use_wgs_csbd_destination=False, use_gbdf_mcr=False, use_gbdf_grs=False):
    """
    Get model configurations using dynamic discovery or static config.
    
    Args:
        use_dynamic: If True, use dynamic discovery; if False, use static config
        use_wgs_csbd_destination: If True, use WGS_CSBD as destination folder instead of renaming_jsons
        use_gbdf_mcr: If True, use GBDF MCR models instead of WGS_CSBD
        use_gbdf_grs: If True, use GBDF GRS models instead of WGS_CSBD
        
    Returns:
        List of model configurations
    """
    if use_dynamic:
        try:
            if use_gbdf_mcr:
                # Use dynamic discovery for GBDF MCR
                discovered_models = discover_ts_folders("source_folder/GBDF", False)
                if discovered_models:
                    print(f"Dynamic discovery found {len(discovered_models)} GBDF MCR models")
                    return discovered_models
                else:
                    print("No GBDF MCR models found via dynamic discovery, falling back to static config")
                    return STATIC_MODELS_CONFIG.get("gbdf_mcr", [])
            elif use_gbdf_grs:
                # Use dynamic discovery for GBDF GRS
                discovered_models = discover_ts_folders("source_folder/GBDF", False)
                if discovered_models:
                    print(f"Dynamic discovery found {len(discovered_models)} GBDF GRS models")
                    return discovered_models
                else:
                    print("No GBDF GRS models found via dynamic discovery, falling back to static config")
                    return STATIC_MODELS_CONFIG.get("gbdf_grs", [])
            else:
                # Use dynamic discovery for WGS_CSBD
                discovered_models = discover_ts_folders("source_folder/WGS_CSBD", True)
                if discovered_models:
                    print(f"Dynamic discovery found {len(discovered_models)} WGS_CSBD models")
                    return discovered_models
                else:
                    print("No WGS_CSBD models found via dynamic discovery, falling back to static config")
                    return STATIC_MODELS_CONFIG.get("wgs_csbd", [])
        except Exception as e:
            print(f"Dynamic discovery failed: {e}, falling back to static config")
            if use_gbdf_mcr:
                return STATIC_MODELS_CONFIG.get("gbdf_mcr", [])
            elif use_gbdf_grs:
                return STATIC_MODELS_CONFIG.get("gbdf_grs", [])
            else:
                return STATIC_MODELS_CONFIG.get("wgs_csbd", [])
    else:
        if use_gbdf_mcr:
            return STATIC_MODELS_CONFIG.get("gbdf_mcr", [])
        elif use_gbdf_grs:
            return STATIC_MODELS_CONFIG.get("gbdf_grs", [])
        else:
            return STATIC_MODELS_CONFIG.get("wgs_csbd", [])

def get_model_by_ts(ts_number):
    """
    Get a specific model by TS number using dynamic discovery.
    
    Args:
        ts_number: TS number (e.g., "01", "02", "03")
        
    Returns:
        Model configuration dict or None if not found
    """
    try:
        return get_model_by_ts_number(ts_number, "source_folder/WGS_CSBD")
    except Exception as e:
        print(f"Error getting model for TS_{ts_number}: {e}")
        return None

# For backward compatibility, keep MODELS_CONFIG as a property
MODELS_CONFIG = get_models_config(use_dynamic=True)

# Global settings
GENERATE_POSTMAN_COLLECTIONS = True
VERBOSE_OUTPUT = True
