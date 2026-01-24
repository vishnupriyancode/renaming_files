# Configuration file for multiple models
# This file now supports both static configurations and dynamic discovery

import os
import json
from dynamic_models import discover_ts_folders, get_model_by_ts_number, get_all_models

# Static model configurations (for backward compatibility)
STATIC_MODELS_CONFIG = {
    "wgs_csbd": [
    {
        "ts_number": "01",
        "edit_id": "RULEEM000001",
        "code": "00W04",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_01_Covid_WGS_CSBD_RULEEM000001_00W04_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_01_Covid_WGS_CSBD_RULEEM000001_00W04_dis/payloads/regression",
        "postman_collection_name": "TS_01_Covid_Collection",
        "postman_file_name": "covid_wgs_csbd_RULEEM000001_00W04.json"
    },
    {
        "ts_number": "02",
        "edit_id": "RULELATE000001",
        "code": "00W17",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_dis/payloads/regression",
        "postman_collection_name": "TS_02_Laterality_Collection",
        "postman_file_name": "laterality_wgs_csbd_RULELATE000001_00W17.json"
    },
    {
        "ts_number": "03",
        "edit_id": "RULEREVE000005",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_dis/payloads/regression",
        "postman_collection_name": "TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000005_00W28.json"
    },
    {
        "ts_number": "04",
        "edit_id": "RULEREVE000004",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_04_Revenue code Services not payable on Facility claim Sub Edit 4_WGS_CSBD_RULEREVE000004_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_04_Revenue code Services not payable on Facility claim Sub Edit 4_WGS_CSBD_RULEREVE000004_00W28_dis/payloads/regression",
        "postman_collection_name": "TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000004_00W28.json"
    },
    {
        "ts_number": "05",
        "edit_id": "RULEREVE000003",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_05_Revenue code Services not payable on Facility claim Sub Edit 3_WGS_CSBD_RULEREVE000003_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_05_Revenue code Services not payable on Facility claim Sub Edit 3_WGS_CSBD_RULEREVE000003_00W28_dis/payloads/regression",
        "postman_collection_name": "TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000003_00W28.json"
    },
    {
        "ts_number": "06",
        "edit_id": "RULEREVE000002",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_06_Revenue code Services not payable on Facility claim Sub Edit 2_WGS_CSBD_RULEREVE000002_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_06_Revenue code Services not payable on Facility claim Sub Edit 2_WGS_CSBD_RULEREVE000002_00W28_dis/payloads/regression",
        "postman_collection_name": "TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000002_00W28.json"
    },
    {
        "ts_number": "07",
        "edit_id": "RULEREVE000001",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_07_Revenue code Services not payable on Facility claim Sub Edit 1_WGS_CSBD_RULEREVE000001_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_07_Revenue code Services not payable on Facility claim Sub Edit 1_WGS_CSBD_RULEREVE000001_00W28_dis/payloads/regression",
        "postman_collection_name": "TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULEREVE000001_00W28.json"
    },
    {
        "ts_number": "08",
        "edit_id": "RULELAB0000009",
        "code": "00W13",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_08_Lab panel Model_WGS_CSBD_RULELAB0000009_00W13_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_08_Lab panel Model_WGS_CSBD_RULELAB0000009_00W13_dis/payloads/regression",
        "postman_collection_name": "TS_08_Lab panel Model_Collection",
        "postman_file_name": "lab_wgs_csbd_RULELAB0000009_00W13.json"
    },
    {
        "ts_number": "09",
        "edit_id": "RULEDEVI000003",
        "code": "00W13",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_09_Device Dependent Procedures(R1)-1B_WGS_CSBD_RULEDEVI000003_00W13_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_09_Device Dependent Procedures(R1)-1B_WGS_CSBD_RULEDEVI000003_00W13_dis/payloads/regression",
        "postman_collection_name": "TS_09_Device Dependent Procedures_Collection",
        "postman_file_name": "device_wgs_csbd_RULEDEVI000003_00W13.json"
    },
    {
        "ts_number": "10",
        "edit_id": "RULERECO000001",
        "code": "00W34",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_10_Recovery Room Reimbursement_WGS_CSBD_RULERECO000001_00W34_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_10_Recovery Room Reimbursement_WGS_CSBD_RULERECO000001_00W34_dis/payloads/regression",
        "postman_collection_name": "TS_10_Recovery Room Reimbursement_Collection",
        "postman_file_name": "recovery_wgs_csbd_RULERECO000001_00W34.json"
    },
    {
        "ts_number": "11",
        "edit_id": "RULERECO000003",
        "code": "00W26",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_11_Revenue Code to HCPCS Xwalk-1B_WGS_CSBD_RULERECO000003_00W26_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_11_Revenue Code to HCPCS Xwalk-1B_WGS_CSBD_RULERECO000003_00W26_dis/payloads/regression",
        "postman_collection_name": "TS_11_Revenue Code to HCPCS Xwalk-1B_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULERECO000003_00W26.json"
    },
    {
        "ts_number": "12",
        "edit_id": "RULEINCI000001",
        "code": "00W34",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_12_Incidentcal Services Facility_WGS_CSBD_RULEINCI000001_00W34_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_12_Incidentcal Services Facility_WGS_CSBD_RULEINCI000001_00W34_dis/payloads/regression",
        "postman_collection_name": "TS_12_Incidentcal Services Facility_Collection",
        "postman_file_name": "incidentcal_wgs_csbd_RULEINCI000001_00W34.json"
    },
    {
        "ts_number": "13",
        "edit_id": "RULERCE0000006",
        "code": "00W06",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_13_Revenue model CR v3_WGS_CSBD_RULERCE0000006_00W06_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_13_Revenue model CR v3_WGS_CSBD_RULERCE0000006_00W06_dis/payloads/regression",
        "postman_collection_name": "TS_13_Revenue model CR v3_Collection",
        "postman_file_name": "revenue_model_wgs_csbd_RULERCE0000006_00W06.json"
    },
    {
        "ts_number": "14",
        "edit_id": "RULERCE000001",
        "code": "00W26",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_14_HCPCS to Revenue Code Xwalk_WGS_CSBD_RULERCE000001_00W26_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_14_HCPCS to Revenue Code Xwalk_WGS_CSBD_RULERCE000001_00W26_dis/payloads/regression",
        "postman_collection_name": "TS_14_HCPCS to Revenue Code Xwalk_Collection",
        "postman_file_name": "hcpcs_wgs_csbd_RULERCE000001_00W26.json"
    },
    {
        "ts_number": "15",
        "edit_id": "RULERCE000005",
        "code": "00W06",
        "source_dir": "source_folder/WGS_CSBD/TS_15_revenue model_WGS_CSBD_RULERCE000005_00W06_sur/regression",
        "dest_dir": "renaming_jsons/CSBDTS/TS_15_revenue model_WGS_CSBD_RULERCE000005_00W06_dis/regression",
        "postman_collection_name": "TS_15_revenue model_Collection",
        "postman_file_name": "revenue_wgs_csbd_RULERCE000005_00W06.json"
    },
    {
        "ts_number": "20",
        "edit_id": "RULERBWR000001",
        "code": "00W30",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_20_RadioservicesbilledwithoutRadiopharma_WGS_CSBD_RULERBWR000001_00W30_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_20_RadioservicesbilledwithoutRadiopharma_WGS_CSBD_RULERBWR000001_00W30_dis/payloads/regression",
        "postman_collection_name": "TS_20_RadioservicesbilledwithoutRadiopharma_Collection",
        "postman_file_name": "radioservices_wgs_csbd_RULERBWR000001_00W30.json"
    },
    {
        "ts_number": "46",
        "edit_id": "RULEEMSD000002",
        "code": "00W09",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_46_Multiple E&M Same day_WGS_CSBD_RULEEMSD000002_00W09_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_46_Multiple E&M Same day_WGS_CSBD_RULEEMSD000002_00W09_dis/payloads/regression",
        "postman_collection_name": "TS_46_Multiple E&M Same day_Collection",
        "postman_file_name": "multiple_em_wgs_csbd_RULEEMSD000002_00W09.json"
    },
    {
        "ts_number": "47",
        "edit_id": "RULEMBOS000001",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_47_Multiple Billing of Obstetrical Services_WGS_CSBD_RULEMBOS000001_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_47_Multiple Billing of Obstetrical Services_WGS_CSBD_RULEMBOS000001_00W28_dis/payloads/regression",
        "postman_collection_name": "TS_47_Multiple Billing of Obstetrical Services_Collection",
        "postman_file_name": "multiple_billing_obstetrical_wgs_csbd_RULEMBOS000001_00W28.json"
    },
    {
        "ts_number": "48",
        "edit_id": "RULERCTH00001",
        "code": "00W26",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_48_Revenue code to HCPCS Alignment edit_WGS_CSBD_RULERCTH00001_00W26_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_48_Revenue code to HCPCS Alignment edit_WGS_CSBD_RULERCTH00001_00W26_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_48_Revenue code to HCPCS Alignment edit_Collection",
        "postman_file_name": "revenue_code_to_hcpcs_alignment_edit_wgs_csbd_RULERCTH00001_00W26.json"
    },
    {
        "ts_number": "49",
        "edit_id": "RULEOBSER00001",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_49_Observation_Services_WGS_CSBD_RULEOBSER00001_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_49_Observation_Services_WGS_CSBD_RULEOBSER00001_00W28_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_49_Observation_Services_Collection",
        "postman_file_name": "observation_services_wgs_csbd_RULEOBSER00001_00W28.json"
    },
    {
        "ts_number": "50",
        "edit_id": "RULEOBSER00002",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_50_Observation_Services_WGS_CSBD_RULEOBSER00002_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_50_Observation_Services_WGS_CSBD_RULEOBSER00002_00W28_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_50_Observation_Services_Collection",
        "postman_file_name": "observation_services_wgs_csbd_RULEOBSER00002_00W28.json"
    },
    {
        "ts_number": "51",
        "edit_id": "RULEOBSER00003",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_51_Observation_Services_WGS_CSBD_RULEOBSER00003_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_51_Observation_Services_WGS_CSBD_RULEOBSER00003_00W28_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_51_Observation_Services_Collection",
        "postman_file_name": "observation_services_wgs_csbd_RULEOBSER00003_00W28.json"
    },
    {
        "ts_number": "52",
        "edit_id": "RULEOBSER00004",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_52_Observation_Services_WGS_CSBD_RULEOBSER00004_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_52_Observation_Services_WGS_CSBD_RULEOBSER00004_00W28_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_52_Observation_Services_Collection",
        "postman_file_name": "observation_services_wgs_csbd_RULEOBSER00004_00W28.json"
    },
    {
        "ts_number": "53",
        "edit_id": "RULEOBSER00005",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_53_Observation_Services_WGS_CSBD_RULEOBSER00005_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_53_Observation_Services_WGS_CSBD_RULEOBSER00005_00W28_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_53_Observation_Services_Collection",
        "postman_file_name": "observation_services_wgs_csbd_RULEOBSER00005_00W28.json"
    },
    {
        "ts_number": "54",
        "edit_id": "RULEOBSER00006",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_54_Observation_Services_WGS_CSBD_RULEOBSER00006_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_54_Observation_Services_WGS_CSBD_RULEOBSER00006_00W28_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_54_Observation_Services_Collection",
        "postman_file_name": "observation_services_wgs_csbd_RULEOBSER00006_00W28.json"
    },
    {
        "ts_number": "55",
        "edit_id": "RULEOBSER00007",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_55_Observation_Services_WGS_CSBD_RULEOBSER00007_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_55_Observation_Services_WGS_CSBD_RULEOBSER00007_00W28_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_55_Observation_Services_Collection",
        "postman_file_name": "observation_services_wgs_csbd_RULEOBSER00007_00W28.json"
    },
    {
        "ts_number": "56",
        "edit_id": "RULEOBSER00008",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_56_Observation_Services_WGS_CSBD_RULEOBSER00008_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_56_Observation_Services_WGS_CSBD_RULEOBSER00008_00W28_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_56_Observation_Services_Collection",
        "postman_file_name": "observation_services_wgs_csbd_RULEOBSER00008_00W28.json"
    },
    {
        "ts_number": "57",
        "edit_id": "RULERADDON00001",
        "code": "00W60",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_57_add_on without base_WGS_CSBD_RULERADDON00001_00W60_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_57_add_on without base_WGS_CSBD_RULERADDON00001_00W60_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_57_add_on without base_Collection",
        "postman_file_name": "add_on_without_base_wgs_csbd_RULERADDON00001_00W60.json"
    },
    {
        "ts_number": "58",
        "edit_id": "RULESUB4000001",
        "code": "00W28",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_58_Expansion_WGS_CSBD_RULESUB4000001_00W28_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_58_Expansion_WGS_CSBD_RULESUB4000001_00W28_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_58_Expansion_Collection",
        "postman_file_name": "expansion_on_sub_edit4_wgs_csbd_RULESUB4000001_00W28.json"
    }
    ],
    "gbdf_mcr": [
        {
            "ts_number": "47",
            "edit_id": "RULEEM000001",
            "code": "v04",
            "source_dir": "source_folder/GBDF/TS_47_Covid_gbdf_mcr_RULEEM000001_v04_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_47_Covid_gbdf_mcr_RULEEM000001_v04_dis/payloads/regression",
            "postman_collection_name": "TS_47_Covid_gbdf_mcr_Collection",
            "postman_file_name": "covid_gbdf_mcr_RULEEM000001_v04.json"
        },
        {
            "ts_number": "48",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_48_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_48_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/payloads/regression",
            "postman_collection_name": "TS_48_Multiple E&M Same day_gbdf_mcr_Collection",
            "postman_file_name": "multiple_em_gbdf_mcr_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "60",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_60_Unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_60_Unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_v17_dis/payloads/regression",
            "postman_collection_name": "TS_60_Unspecified_dx_code_outpt_gbdf_mcr_Collection",
            "postman_file_name": "unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_v17.json"
        },
        {
            "ts_number": "61",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_61_Unspecified_dx_code_prof_gbdf_mcr_RULEUSD00100_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_61_Unspecified_dx_code_prof_gbdf_mcr_RULEUSD00100_v17_dis/payloads/regression",
            "postman_collection_name": "TS_61_Unspecified_dx_code_prof_gbdf_mcr_Collection",
            "postman_file_name": "unspecified_dx_code_prof_gbdf_mcr_RULEUSD00100_v17.json"
        },
        {
            "ts_number": "70",
            "edit_id": "RULE00000376",
            "code": "v16",
            "source_dir": "source_folder/GBDF/GBDTS_70_InappropriatePrimaryDiagnosis_gbdf_mcr_RULE00000376_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_70_InappropriatePrimaryDiagnosis_gbdf_mcr_RULE00000376_v16_dis/payloads/regression",
            "postman_collection_name": "TS_70_InappropriatePrimaryDiagnosis_gbdf_mcr_Collection",
            "postman_file_name": "inappropriate_primary_diagnosis_gbdf_mcr_RULE00000376_v16.json"
        },
        {
            "ts_number": "138",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_138_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_138_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/payloads/regression",
            "postman_collection_name": "TS_138_Multiple E&M Same day_gbdf_mcr_Collection",
            "postman_file_name": "multiple_em_gbdf_mcr_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "140",
            "edit_id": "RULENDCUOM000001",
            "code": "v41",
            "source_dir": "source_folder/GBDF/TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_RULENDCUOM000001_v41_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_RULENDCUOM000001_v41_dis/payloads/regression",
            "postman_collection_name": "TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_Collection",
            "postman_file_name": "ndc_uom_gbdf_mcr_RULENDCUOM000001_v41.json"
        },
        {
            "ts_number": "144",
            "edit_id": "RULENEBU000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_RULENEBU000001_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_RULENEBU000001_v18_dis/payloads/regression",
            "postman_collection_name": "TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_Collection",
            "postman_file_name": "nebulizer_gbdf_mcr_RULENEBU000001_v18.json"
        },
        {
            "ts_number": "146",
            "edit_id": "RULENMP000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_146_No match of Procedure code_gbdf_mcr_RULENMP000001_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_146_No match of Procedure code_gbdf_mcr_RULENMP000001_v18_dis/payloads/regression",
            "postman_collection_name": "TS_146_No match of Procedure code_gbdf_mcr_Collection",
            "postman_file_name": "no_match_procedure_gbdf_mcr_RULENMP000001_v18.json"
        }
    ],
    "gbdf_grs": [
        {
            "ts_number": "49",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_49_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_49_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/payloads/regression",
            "postman_collection_name": "TS_49_Multiple E&M Same day_gbdf_grs_Collection",
            "postman_file_name": "multiple_em_gbdf_grs_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "59",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_59_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_59_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17_dis/payloads/regression",
            "postman_collection_name": "TS_59_Unspecified_dx_code_outpt_gbdf_grs_Collection",
            "postman_file_name": "unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17.json"
        },
        {
            "ts_number": "61",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_61_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_61_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_dis/payloads/regression",
            "postman_collection_name": "TS_61_Unspecified_dx_code_prof_gbdf_grs_Collection",
            "postman_file_name": "unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17.json"
        },
        {
            "ts_number": "62",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_62_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_62_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_dis/payloads/regression",
            "postman_collection_name": "TS_62_Unspecified_dx_code_prof_gbdf_grs_Collection",
            "postman_file_name": "unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17.json"
        },
        {
            "ts_number": "139",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_139_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_139_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/payloads/regression",
            "postman_collection_name": "TS_139_Multiple E&M Same day_gbdf_grs_Collection",
            "postman_file_name": "multiple_em_gbdf_grs_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "141",
            "edit_id": "RULENDCUOM000001",
            "code": "v41",
            "source_dir": "source_folder/GBDF/TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_RULENDCUOM000001_v41_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_RULENDCUOM000001_v41_dis/payloads/regression",
            "postman_collection_name": "TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_Collection",
            "postman_file_name": "ndc_uom_gbdf_grs_RULENDCUOM000001_v41.json"
        },
        {
            "ts_number": "145",
            "edit_id": "RULENEBU000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_RULENEBU000001_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_RULENEBU000001_v18_dis/payloads/regression",
            "postman_collection_name": "TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_Collection",
            "postman_file_name": "nebulizer_gbdf_grs_RULENEBU000001_v18.json"
        },
        {
            "ts_number": "147",
            "edit_id": "RULENMP000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_147_No match of Procedure code_gbdf_grs_RULENMP000001_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_147_No match of Procedure code_gbdf_grs_RULENMP000001_v18_dis/payloads/regression",
            "postman_collection_name": "TS_147_No match of Procedure code_gbdf_grs_Collection",
            "postman_file_name": "no_match_procedure_gbdf_grs_RULENMP000001_v18.json"
        }
    ],
    "wgs_kernal": [
        {
            "ts_number": "122",
            "edit_id": "RULERCTH00001",
            "code": "00W26",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_122_Revenue code to HCPCS Alignment edit_WGS_NYK_RULERCTH00001_00W26_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_122_Revenue code to HCPCS Alignment edit_WGS_NYK_RULERCTH00001_00W26_dis/payloads/regression",
            "postman_collection_name": "NYKTS_122_Revenue code to HCPCS Alignment edit_Collection",
            "postman_file_name": "revenue_code_to_hcpcs_alignment_edit_wgs_nyk_RULERCTH00001_00W26.json"
        },
        {
            "ts_number": "123",
            "edit_id": "RULEOBSER00001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_123_Observation_Services_WGS_NYK_RULEOBSER00001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_123_Observation_Services_WGS_NYK_RULEOBSER00001_00W28_dis/payloads/regression",
            "postman_collection_name": "NYKTS_123_Observation_Services_Collection",
            "postman_file_name": "observation_services_wgs_nyk_RULEOBSER00001_00W28.json"
        },
        {
            "ts_number": "124",
            "edit_id": "RULEOBSER00002",
            "code": "00W28",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_124_Observation_Services_WGS_NYK_RULEOBSER00002_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_124_Observation_Services_WGS_NYK_RULEOBSER00002_00W28_dis/payloads/regression",
            "postman_collection_name": "NYKTS_124_Observation_Services_Collection",
            "postman_file_name": "observation_services_wgs_nyk_RULEOBSER00002_00W28.json"
        },
        {
            "ts_number": "125",
            "edit_id": "RULEOBSER00003",
            "code": "00W28",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_125_Observation_Services_WGS_NYK_RULEOBSER00003_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_125_Observation_Services_WGS_NYK_RULEOBSER00003_00W28_dis/payloads/regression",
            "postman_collection_name": "NYKTS_125_Observation_Services_Collection",
            "postman_file_name": "observation_services_wgs_nyk_RULEOBSER00003_00W28.json"
        },
        {
            "ts_number": "126",
            "edit_id": "RULEOBSER00004",
            "code": "00W28",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_126_Observation_Services_WGS_NYK_RULEOBSER00004_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_126_Observation_Services_WGS_NYK_RULEOBSER00004_00W28_dis/payloads/regression",
            "postman_collection_name": "NYKTS_126_Observation_Services_Collection",
            "postman_file_name": "observation_services_wgs_nyk_RULEOBSER00004_00W28.json"
        },
        {
            "ts_number": "127",
            "edit_id": "RULEOBSER00005",
            "code": "00W28",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_127_Observation_Services_WGS_NYK_RULEOBSER00005_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_127_Observation_Services_WGS_NYK_RULEOBSER00005_00W28_dis/payloads/regression",
            "postman_collection_name": "NYKTS_127_Observation_Services_Collection",
            "postman_file_name": "observation_services_wgs_nyk_RULEOBSER00005_00W28.json"
        },
        {
            "ts_number": "128",
            "edit_id": "RULEOBSER00006",
            "code": "00W28",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_128_Observation_Services_WGS_NYK_RULEOBSER00006_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_128_Observation_Services_WGS_NYK_RULEOBSER00006_00W28_dis/payloads/regression",
            "postman_collection_name": "NYKTS_128_Observation_Services_Collection",
            "postman_file_name": "observation_services_wgs_nyk_RULEOBSER00006_00W28.json"
        },
        {
            "ts_number": "129",
            "edit_id": "RULEOBSER00007",
            "code": "00W28",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_129_Observation_Services_WGS_NYK_RULEOBSER00007_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_129_Observation_Services_WGS_NYK_RULEOBSER00007_00W28_dis/payloads/regression",
            "postman_collection_name": "NYKTS_129_Observation_Services_Collection",
            "postman_file_name": "observation_services_wgs_nyk_RULEOBSER00007_00W28.json"
        },
        {
            "ts_number": "130",
            "edit_id": "RULEOBSER00008",
            "code": "00W28",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_130_Observation_Services_WGS_NYK_RULEOBSER00008_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_130_Observation_Services_WGS_NYK_RULEOBSER00008_00W28_dis/payloads/regression",
            "postman_collection_name": "NYKTS_130_Observation_Services_Collection",
            "postman_file_name": "observation_services_wgs_nyk_RULEOBSER00008_00W28.json"
        },
        {
            "ts_number": "132",
            "edit_id": "RULERADDON00001",
            "code": "00W60",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_132_add_on without base_WGS_NYK_RULERADDON00001_00W60_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_132_add_on without base_WGS_NYK_RULERADDON00001_00W60_dis/payloads/regression",
            "postman_collection_name": "NYKTS_132_add_on without base_Collection",
            "postman_file_name": "add_on_without_base_wgs_nyk_RULERADDON00001_00W60.json"
        }
    ]
}

# Dynamic model discovery
def get_models_config(use_dynamic=True, use_wgs_csbd_destination=False, use_gbdf_mcr=False, use_gbdf_grs=False, use_wgs_nyk=False):
    """
    Get model configurations using dynamic discovery or static config.

    Args:
        use_dynamic: If True, use dynamic discovery; if False, use static config
        use_wgs_csbd_destination: If True, use WGS_CSBD as destination folder instead of renaming_jsons
        use_gbdf_mcr: If True, use GBDF MCR models instead of WGS_CSBD
        use_gbdf_grs: If True, use GBDF GRS models instead of WGS_CSBD
        use_wgs_nyk: If True, use WGS_NYK models instead of WGS_CSBD

    Returns:
        List of model configurations
    """
    if use_dynamic:
        try:
            if use_wgs_nyk:
                # Use dynamic discovery for WGS_NYK
                discovered_models = discover_ts_folders("source_folder/WGS_Kernal", False)
                if discovered_models:
                    print(f"Dynamic discovery found {len(discovered_models)} WGS_NYK models")
                    return discovered_models
                else:
                    print("No WGS_NYK models found via dynamic discovery, falling back to static config")
                    return STATIC_MODELS_CONFIG.get("wgs_kernal", [])
            elif use_gbdf_mcr:
                # Use dynamic discovery for GBDF MCR
                discovered_models = discover_ts_folders("source_folder/GBDF", False)
                # Filter for MCR models only (exclude GRS)
                # Use source_dir as primary check since it always exists and contains the folder path
                # Also check folder_name as fallback for robustness
                mcr_models = [
                    m for m in discovered_models 
                    if ("gbdf_mcr" in m.get("source_dir", "").lower() or "gbdf_mcr" in m.get("folder_name", "").lower())
                    and "gbdf_grs" not in m.get("source_dir", "").lower() 
                    and "gbdf_grs" not in m.get("folder_name", "").lower()
                ]
                if mcr_models:
                    print(f"Dynamic discovery found {len(mcr_models)} GBDF MCR models")
                    return mcr_models
                else:
                    print("No GBDF MCR models found via dynamic discovery, falling back to static config")
                    return STATIC_MODELS_CONFIG.get("gbdf_mcr", [])
            elif use_gbdf_grs:
                # Use dynamic discovery for GBDF GRS
                discovered_models = discover_ts_folders("source_folder/GBDF", False)
                # Filter for GRS models only
                # Use source_dir as primary check since it always exists and contains the folder path
                # Also check folder_name as fallback for robustness
                grs_models = [
                    m for m in discovered_models 
                    if "gbdf_grs" in m.get("source_dir", "").lower() or "gbdf_grs" in m.get("folder_name", "").lower()
                ]
                if grs_models:
                    print(f"Dynamic discovery found {len(grs_models)} GBDF GRS models")
                    return grs_models
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
            if use_wgs_nyk:
                return STATIC_MODELS_CONFIG.get("wgs_kernal", [])
            elif use_gbdf_mcr:
                return STATIC_MODELS_CONFIG.get("gbdf_mcr", [])
            elif use_gbdf_grs:
                return STATIC_MODELS_CONFIG.get("gbdf_grs", [])
            else:
                return STATIC_MODELS_CONFIG.get("wgs_csbd", [])
    else:
        if use_wgs_nyk:
            return STATIC_MODELS_CONFIG.get("wgs_kernal", [])
        elif use_gbdf_mcr:
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


def apply_header_footer_to_json(file_path):
    """
    Apply header and footer structure to JSON files.
    Wraps the existing JSON content with header and footer metadata.
    
    This function ALWAYS ensures the header/footer structure is present,
    even if the file already has it (to ensure consistency).
    
    Header structure:
    - adhoc: "true"
    - analyticId: " "
    - hints: ["congnitive_claims_async"]
    - payload: {existing JSON content}
    
    Footer structure:
    - responseRequired: "false"
    - meta-src-envrmt: "IMST"
    - meta-transid: "20220117181853TMBL20359Cl893580999"
    
    Args:
        file_path: Path to the JSON file to transform
        
    Returns:
        bool: True if transformation was successful, False otherwise
    """
    try:
        # Read the existing JSON content
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        
        # Check if the file already has the correct structure
        has_correct_structure = (isinstance(existing_data, dict) and 
                                "adhoc" in existing_data and 
                                "payload" in existing_data and 
                                "responseRequired" in existing_data and
                                "meta-src-envrmt" in existing_data and
                                "meta-transid" in existing_data)
        
        # Header and footer structure (always use these values)
        header_footer = {
            "adhoc": "true",
            "analyticId": " ",
            "hints": ["congnitive_claims_async"],
            "responseRequired": "false",
            "meta-src-envrmt": "IMST",
            "meta-transid": "20220117181853TMBL20359Cl893580999"
        }
        
        # Always ensure header/footer structure is correct
        if has_correct_structure:
            # File has structure, but ensure all header/footer fields are correct
            new_structure = {
                "adhoc": header_footer["adhoc"],
                "analyticId": header_footer["analyticId"],
                "hints": header_footer["hints"],
                "payload": existing_data.get("payload", existing_data),  # Use existing payload or entire data
                "responseRequired": header_footer["responseRequired"],
                "meta-src-envrmt": header_footer["meta-src-envrmt"],
                "meta-transid": header_footer["meta-transid"]
            }
            
            # Preserve any additional fields that might exist
            for key, value in existing_data.items():
                if key not in ["adhoc", "analyticId", "hints", "payload", "responseRequired", "meta-src-envrmt", "meta-transid"]:
                    new_structure[key] = value
            
            # Write the updated structure back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(new_structure, f, indent=2, ensure_ascii=False)
            print(f"[INFO] Updated header/footer structure in: {file_path}")
        else:
            # File doesn't have correct structure, wrap existing data in payload
            new_structure = {
                "adhoc": header_footer["adhoc"],
                "analyticId": header_footer["analyticId"],
                "hints": header_footer["hints"],
                "payload": existing_data,  # The existing JSON becomes the payload
                "responseRequired": header_footer["responseRequired"],
                "meta-src-envrmt": header_footer["meta-src-envrmt"],
                "meta-transid": header_footer["meta-transid"]
            }
            
            # Write the transformed JSON back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(new_structure, f, indent=2, ensure_ascii=False)
            print(f"[SUCCESS] Applied header/footer to: {file_path}")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"[ERROR] Error parsing JSON in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Error applying header/footer to {file_path}: {e}")
        return False


def apply_header_footer_to_renaming_jsons():
    """
    Apply header and footer to all JSON files in renaming_jsons folder
    for WGS_CSBD and WGS_Kernal models.
    
    This function recursively finds all JSON files in:
    - renaming_jsons/CSBDTS/**
    - renaming_jsons/NYKTS/**
    
    and applies the header/footer structure to each file.
    
    Returns:
        dict: Statistics about processed files
    """
    base_dir = "renaming_jsons"
    processed_count = 0
    skipped_count = 0
    error_count = 0
    
    # Directories to process
    target_dirs = [
        os.path.join(base_dir, "WGS_CSBD"),
        os.path.join(base_dir, "WGS_KERNAL")
    ]
    
    print("=" * 60)
    print("Applying header/footer to JSON files")
    print("=" * 60)
    
    for target_dir in target_dirs:
        if not os.path.exists(target_dir):
            print(f"[WARNING] Directory not found: {target_dir}")
            continue
        
        print(f"\nProcessing directory: {target_dir}")
        print("-" * 60)
        
        # Recursively find all JSON files
        for root, dirs, files in os.walk(target_dir):
            for filename in files:
                if filename.endswith('.json'):
                    file_path = os.path.join(root, filename)
                    
                    # Apply header/footer (function will handle both new and existing structures)
                    if apply_header_footer_to_json(file_path):
                        processed_count += 1
                    else:
                        error_count += 1
    
    print("\n" + "=" * 60)
    print("Header/Footer Application Summary")
    print("=" * 60)
    print(f"Processed: {processed_count} files")
    print(f"Skipped (already correct): {skipped_count} files")
    print(f"Errors: {error_count} files")
    print("=" * 60)
    
    return {
        "processed": processed_count,
        "skipped": skipped_count,
        "errors": error_count
    }


# Main section - allows running this script directly to apply header/footer
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Header/Footer Application for WGS_CSBD and WGS_Kernal Models")
    print("=" * 60)
    print("\nThis script will apply header and footer structure to all JSON files")
    print("in renaming_jsons/WGS_CSBD and renaming_jsons/WGS_KERNAL directories.\n")
    
    # Apply header/footer to all JSON files
    stats = apply_header_footer_to_renaming_jsons()
    
    print(f"\n✓ Process completed successfully!")
    print(f"  - Processed: {stats['processed']} files")
    print(f"  - Skipped: {stats['skipped']} files")
    print(f"  - Errors: {stats['errors']} files")
