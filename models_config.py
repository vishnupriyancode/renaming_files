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
    },
    {
        "ts_number": "59",
        "edit_id": "RULESUB4000001",
        "code": "00W00",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_59_Wgs_WGS_CSBD_RULESUB4000001_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_59_Wgs_WGS_CSBD_RULESUB4000001_00W00_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_59_Wgs_Collection",
        "postman_file_name": "wgs_csbd_expansion_on_sub_edit4_RULESUB4000001_00W00.json"
    },
    {
        "ts_number": "60",
        "edit_id": "RULEINPCC00001",
        "code": "00W45",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_60_Inpatient_WGS_CSBD_RULEINPCC00001_00W45_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_60_Inpatient_WGS_CSBD_RULEINPCC00001_00W45_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_60_Inpatient_Collection",
        "postman_file_name": "inpatient_neonatal_and_pediatric_critical_care_iprep_332_wgs_csbd_RULEINPCC00001_00W45.json"
    },
    {
        "ts_number": "61",
        "edit_id": "RULEOPBS000001",
        "code": "00W15",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_61_Op_WGS_CSBD_RULEOPBS000001_00W15_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_61_Op_WGS_CSBD_RULEOPBS000001_00W15_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_61_Op_Collection",
        "postman_file_name": "op_facility_bundled_services_wgs_csbd_RULEOPBS000001_00W15.json"
    },
    {
        "ts_number": "62",
        "edit_id": "RULEANES000001",
        "code": "00W32",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_62_Anesthesia_WGS_CSBD_RULEANES000001_00W32_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_62_Anesthesia_WGS_CSBD_RULEANES000001_00W32_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_62_Anesthesia_Collection",
        "postman_file_name": "anesthesia_billed_time_units_wgs_csbd_RULEANES000001_00W32.json"
    },
    {
        "ts_number": "63",
        "edit_id": "RULEBDLG000004",
        "code": "00W15",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_63_Bundled_WGS_CSBD_RULEBDLG000004_00W15_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_63_Bundled_WGS_CSBD_RULEBDLG000004_00W15_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_63_Bundled_Collection",
        "postman_file_name": "bundled_services_logic_4_wgs_csbd_RULEBDLG000004_00W15.json"
    },
    {
        "ts_number": "64",
        "edit_id": "RULECLIA00001",
        "code": "00W00",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_64_Clia_WGS_CSBD_RULECLIA00001_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_64_Clia_WGS_CSBD_RULECLIA00001_00W00_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_64_Clia_Collection",
        "postman_file_name": "clia_edit_wgs_csbd_l92l95l94l93l90l91_RULECLIA00001_00W00.json"
    },
    {
        "ts_number": "65",
        "edit_id": "RULEJWME000001",
        "code": "00W59",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_65_Medical_WGS_CSBD_RULEJWME000001_00W59_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_65_Medical_WGS_CSBD_RULEJWME000001_00W59_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_65_Medical_Collection",
        "postman_file_name": "medical_injectable_edits_jw_modifier_i_352_wgs_csbd_RULEJWME000001_00W59.json"
    },
    {
        "ts_number": "66",
        "edit_id": "RULEMFTM000001",
        "code": "00W31",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_66_Missing_WGS_CSBD_RULEMFTM000001_00W31_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_66_Missing_WGS_CSBD_RULEMFTM000001_00W31_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_66_Missing_Collection",
        "postman_file_name": "missing_required_finger_or_toe_anatomical_modifier_iprep_310_wgs_csbd_RULEMFTM000001_00W31.json"
    },
    {
        "ts_number": "67",
        "edit_id": "RULENCCIPTP001",
        "code": "00W10",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_67_Ncci_WGS_CSBD_RULENCCIPTP001_00W10_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_67_Ncci_WGS_CSBD_RULENCCIPTP001_00W10_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_67_Ncci_Collection",
        "postman_file_name": "ncci_ptp_outpt_facility_iprep_271_wgs_csbd_RULENCCIPTP001_00W10.json"
    },
    {
        "ts_number": "68",
        "edit_id": "RULENDC000001",
        "code": "00W40",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_68_Ndc_WGS_CSBD_RULENDC000001_00W40_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_68_Ndc_WGS_CSBD_RULENDC000001_00W40_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_68_Ndc_Collection",
        "postman_file_name": "ndc_validation_edit_expansion_iprep_296_wgs_csbd_RULENDC000001_00W40.json"
    },
    {
        "ts_number": "70",
        "edit_id": "RULERCRO000001",
        "code": "00W34",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_70_Correct_WGS_CSBD_RULERCRO000001_00W34_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_70_Correct_WGS_CSBD_RULERCRO000001_00W34_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_70_Correct_Collection",
        "postman_file_name": "correct_coding_recovery_room_reimbursement_iprep_241_wgs_csbd_RULERCRO000001_00W34.json"
    },
    {
        "ts_number": "71",
        "edit_id": "RULERCTH000001",
        "code": "00W26",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_71_Revenue_WGS_CSBD_RULERCTH000001_00W26_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_71_Revenue_WGS_CSBD_RULERCTH000001_00W26_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_71_Revenue_Collection",
        "postman_file_name": "revenue_code_to_hcpcs_alignment_edit_iprep_205_wgs_csbd_RULERCTH000001_00W26.json"
    },
    {
        "ts_number": "73",
        "edit_id": "RULEUNAC000001",
        "code": "00W16",
        "source_dir": "source_folder/WGS_CSBD/CSBDTS_73_Unacceptable_WGS_CSBD_RULEUNAC000001_00W16_sur/payloads/regression",
        "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_73_Unacceptable_WGS_CSBD_RULEUNAC000001_00W16_dis/payloads/regression",
        "postman_collection_name": "CSBDTS_73_Unacceptable_Collection",
        "postman_file_name": "unacceptable_principal_diagnosis_wgs_csbd_RULEUNAC000001_00W16.json"
    },
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
        "ts_number": "49",
        "edit_id": "RULELATE000001",
        "code": "v17",
        "source_dir": "source_folder/GBDF/GBDTS_49_Laterality_gbdf_mcr_RULELATE000001_v17_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_49_Laterality_gbdf_mcr_RULELATE000001_v17_dis/payloads/regression",
        "postman_collection_name": "GBDTS_49_Laterality_Collection",
        "postman_file_name": "laterality_policy_diagnosis_to_diagnosis_gbd_facets_mcr_RULELATE000001_v17.json"
    },
    {
        "ts_number": "50",
        "edit_id": "PSMEM000001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/GBDTS_50_Psm_gbdf_mcr_PSMEM000001_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_50_Psm_gbdf_mcr_PSMEM000001_00W00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_50_Psm_Collection",
        "postman_file_name": "psm_edits_established_patients_ep_gbd_facets_mcr_PSMEM000001_00W00.json"
    },
    {
        "ts_number": "52",
        "edit_id": "PSMEM000002",
        "code": "v00",
        "source_dir": "source_folder/GBDF/GBDTS_52_Psm_gbdf_mcr_PSMEM000002_v00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_52_Psm_gbdf_mcr_PSMEM000002_v00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_52_Psm_Collection",
        "postman_file_name": "psm_edit_for_new_patient_visit_type_np_gbd_facets_mcr_PSMEM000002_v00.json"
    },
    {
        "ts_number": "54",
        "edit_id": "PSMEM000003",
        "code": "v00",
        "source_dir": "source_folder/GBDF/GBDTS_54_Psm_gbdf_mcr_PSMEM000003_v00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_54_Psm_gbdf_mcr_PSMEM000003_v00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_54_Psm_Collection",
        "postman_file_name": "psm_edits_for_emergency_department_personnel_ed_gbd_facets_mcr_PSMEM000003_v00.json"
    },
    {
        "ts_number": "56",
        "edit_id": "PSMEM000004",
        "code": "v00",
        "source_dir": "source_folder/GBDF/GBDTS_56_Psm_gbdf_mcr_PSMEM000004_v00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_56_Psm_gbdf_mcr_PSMEM000004_v00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_56_Psm_Collection",
        "postman_file_name": "psm_edits_for_emergency_department_facility_er_gbd_facets_mcr_PSMEM000004_v00.json"
    },
    {
        "ts_number": "58",
        "edit_id": "RULEMAN000004",
        "code": "v14",
        "source_dir": "source_folder/GBDF/GBDTS_58_Manifestation_gbdf_mcr_RULEMAN000004_v14_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_58_Manifestation_gbdf_mcr_RULEMAN000004_v14_dis/payloads/regression",
        "postman_collection_name": "GBDTS_58_Manifestation_Collection",
        "postman_file_name": "manifestation_codes_gbd_facets_mcr_RULEMAN000004_v14.json"
    },
    {
        "ts_number": "60",
        "edit_id": "RULEUSD00100_Outpt_GRS",
        "code": "v17",
        "source_dir": "source_folder/GBDF/GBDTS_60_Unspecified_gbdf_mcr_RULEUSD00100_Outpt_GRS_v17_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_60_Unspecified_gbdf_mcr_RULEUSD00100_Outpt_GRS_v17_dis/payloads/regression",
        "postman_collection_name": "GBDTS_60_Unspecified_Collection",
        "postman_file_name": "unspecified_dxcodes_outpt_mcr_gbd_facets_grs_RULEUSD00100_Outpt_GRS_v17.json"
    },
    {
        "ts_number": "62",
        "edit_id": "RULEUSD00100_Prof_MCR",
        "code": "v17",
        "source_dir": "source_folder/GBDF/GBDTS_62_Unspecified_gbdf_mcr_RULEUSD00100_Prof_MCR_v17_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_62_Unspecified_gbdf_mcr_RULEUSD00100_Prof_MCR_v17_dis/payloads/regression",
        "postman_collection_name": "GBDTS_62_Unspecified_Collection",
        "postman_file_name": "unspecified_dxcodes_prof_mcr_gbd_facets_mcr_RULEUSD00100_Prof_MCR_v17.json"
    },
    {
        "ts_number": "63",
        "edit_id": "RULEAMBU000001",
        "code": "v37",
        "source_dir": "source_folder/GBDF/GBDTS_63_Shadow_gbdf_mcr_Ambulance Mileage without Base Transport Paid IPREP 192_v37_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_63_Shadow_gbdf_mcr_Ambulance Mileage without Base Transport Paid IPREP 192_v37_dis/payloads/regression",
        "postman_collection_name": "GBDTS_63_Shadow_Collection",
        "postman_file_name": "shadow_ruleambu000001_mcr_v37_edits_group9_Ambulance Mileage without Base Transport Paid IPREP 192_v37.json"
    },
    {
        "ts_number": "65",
        "edit_id": "RULEAMBU000001",
        "code": "v37",
        "source_dir": "source_folder/GBDF/GBDTS_65_Gbdf_gbdf_mcr_Ambulance Mileage without Base Transport Paid IPREP 192_v37_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_65_Gbdf_gbdf_mcr_Ambulance Mileage without Base Transport Paid IPREP 192_v37_dis/payloads/regression",
        "postman_collection_name": "GBDTS_65_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_shadow_ruleambu000001_mmp_v37_edits_group9_Ambulance Mileage without Base Transport Paid IPREP 192_v37.json"
    },
    {
        "ts_number": "66",
        "edit_id": "RULE00000022",
        "code": "v19",
        "source_dir": "source_folder/GBDF/GBDTS_66_Gbdf_gbdf_mcr_RULE00000022_v19_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_66_Gbdf_gbdf_mcr_RULE00000022_v19_dis/payloads/regression",
        "postman_collection_name": "GBDTS_66_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_inaccurate_laterality_edit_gbd_facets_mmp_RULE00000022_v19.json"
    },
    {
        "ts_number": "67",
        "edit_id": "RULE00000022",
        "code": "v19",
        "source_dir": "source_folder/GBDF/GBDTS_67_Inaccurate_gbdf_mcr_RULE00000022_v19_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_67_Inaccurate_gbdf_mcr_RULE00000022_v19_dis/payloads/regression",
        "postman_collection_name": "GBDTS_67_Inaccurate_Collection",
        "postman_file_name": "inaccurate_laterality_edit_gbd_facets_mcr_RULE00000022_v19.json"
    },
    {
        "ts_number": "72",
        "edit_id": "RULEALWA000001",
        "code": "v31",
        "source_dir": "source_folder/GBDF/GBDTS_72_Always_gbdf_mcr_RULEALWA000001_v31_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_72_Always_gbdf_mcr_RULEALWA000001_v31_dis/payloads/regression",
        "postman_collection_name": "GBDTS_72_Always_Collection",
        "postman_file_name": "always_therapy_missing_modifiers_gbd_facets_mcr_RULEALWA000001_v31.json"
    },
    {
        "ts_number": "73",
        "edit_id": "RULEEXCL000001",
        "code": "v27",
        "source_dir": "source_folder/GBDF/GBDTS_73_Gbdf_gbdf_mcr_RULEEXCL000001_v27_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_73_Gbdf_gbdf_mcr_RULEEXCL000001_v27_dis/payloads/regression",
        "postman_collection_name": "GBDTS_73_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_excludes_1_notes_gbd_facets_mmp_RULEEXCL000001_v27.json"
    },
    {
        "ts_number": "75",
        "edit_id": "RULEEXCL000001",
        "code": "v27",
        "source_dir": "source_folder/GBDF/GBDTS_75_Excludes_gbdf_mcr_RULEEXCL000001_v27_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_75_Excludes_gbdf_mcr_RULEEXCL000001_v27_dis/payloads/regression",
        "postman_collection_name": "GBDTS_75_Excludes_Collection",
        "postman_file_name": "excludes_1_notes_gbd_facets_mcr_RULEEXCL000001_v27.json"
    },
    {
        "ts_number": "123",
        "edit_id": "RULEANES000001",
        "code": "v32",
        "source_dir": "source_folder/GBDF/GBDTS_123_Anesthesia_gbdf_mcr_RULEANES000001_v32_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_123_Anesthesia_gbdf_mcr_RULEANES000001_v32_dis/payloads/regression",
        "postman_collection_name": "GBDTS_123_Anesthesia_Collection",
        "postman_file_name": "anesthesia_billed_time_units_gbd_facets_mcr_RULEANES000001_v32.json"
    },
    {
        "ts_number": "125",
        "edit_id": "RULECLIA00001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/GBDTS_125_Clia_gbdf_mcr_RULECLIA00001_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_125_Clia_gbdf_mcr_RULECLIA00001_00W00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_125_Clia_Collection",
        "postman_file_name": "clia_edit_for_gbd_mcr_gbd_facets_mcr_r92r95r93r90r94r91_RULECLIA00001_00W00.json"
    },
    {
        "ts_number": "126",
        "edit_id": "RULECLIA00001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/GBDTS_126_Clia_gbdf_mcr_RULECLIA00001_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_126_Clia_gbdf_mcr_RULECLIA00001_00W00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_126_Clia_Collection",
        "postman_file_name": "clia_edit_for_gbd_mcr_gbd_facets_grs_r92r95r93r90r94r91_RULECLIA00001_00W00.json"
    },
    {
        "ts_number": "127",
        "edit_id": "RULEIPVT000001",
        "code": "v38",
        "source_dir": "source_folder/GBDF/GBDTS_127_Gbdf_gbdf_mcr_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-Facets-MCR_v38_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_127_Gbdf_gbdf_mcr_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-Facets-MCR_v38_dis/payloads/regression",
        "postman_collection_name": "GBDTS_127_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-Facets-MCR_v38.json"
    },
    {
        "ts_number": "129",
        "edit_id": "RULEIMMU000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/GBDTS_129_Gbdf_gbdf_mcr_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-Facets-MCR_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_129_Gbdf_gbdf_mcr_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-Facets-MCR_v08_dis/payloads/regression",
        "postman_collection_name": "GBDTS_129_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-Facets-MCR_v08.json"
    },
    {
        "ts_number": "131",
        "edit_id": "RULEKNEE000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/GBDTS_131_Gbdf_gbdf_mcr_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-Facets-MCR_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_131_Gbdf_gbdf_mcr_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-Facets-MCR_v08_dis/payloads/regression",
        "postman_collection_name": "GBDTS_131_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-Facets-MCR_v08.json"
    },
    {
        "ts_number": "134",
        "edit_id": "RULEJWME000001",
        "code": "v59",
        "source_dir": "source_folder/GBDF/GBDTS_134_Gbdf_gbdf_mcr_RULEJWME000001 Medical Injectable Edits JW Modifier I-352 GBD-Facets-MCR_v59_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_134_Gbdf_gbdf_mcr_RULEJWME000001 Medical Injectable Edits JW Modifier I-352 GBD-Facets-MCR_v59_dis/payloads/regression",
        "postman_collection_name": "GBDTS_134_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEJWME000001 Medical Injectable Edits JW Modifier I-352 GBD-Facets-MCR_v59.json"
    },
    {
        "ts_number": "136",
        "edit_id": "RULEEM0000012",
        "code": "v07",
        "source_dir": "source_folder/GBDF/GBDTS_136_Gbdf_gbdf_mcr_RULEEM0000012 MNP Model GBD-Facets-MCR_v07_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_136_Gbdf_gbdf_mcr_RULEEM0000012 MNP Model GBD-Facets-MCR_v07_dis/payloads/regression",
        "postman_collection_name": "GBDTS_136_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEEM0000012 MNP Model GBD-Facets-MCR_v07.json"
    },
    {
        "ts_number": "138",
        "edit_id": "RULEEMSD000002",
        "code": "v09",
        "source_dir": "source_folder/GBDF/GBDTS_138_Gbdf_gbdf_mcr_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-Facets-MCR_v09_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_138_Gbdf_gbdf_mcr_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-Facets-MCR_v09_dis/payloads/regression",
        "postman_collection_name": "GBDTS_138_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-Facets-MCR_v09.json"
    },
    {
        "ts_number": "140",
        "edit_id": "RULENDCUOM000001",
        "code": "v41",
        "source_dir": "source_folder/GBDF/GBDTS_140_Gbdf_gbdf_mcr_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-Facets-MCR_v41_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_140_Gbdf_gbdf_mcr_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-Facets-MCR_v41_dis/payloads/regression",
        "postman_collection_name": "GBDTS_140_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-Facets-MCR_v41.json"
    },
    {
        "ts_number": "142",
        "edit_id": "RULENDC000001",
        "code": "v40",
        "source_dir": "source_folder/GBDF/GBDTS_142_Gbdf_gbdf_mcr_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-Facets-MCR_v40_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_142_Gbdf_gbdf_mcr_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-Facets-MCR_v40_dis/payloads/regression",
        "postman_collection_name": "GBDTS_142_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-Facets-MCR_v40.json"
    },
    {
        "ts_number": "144",
        "edit_id": "RULENEBU000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/GBDTS_144_Gbdf_gbdf_mcr_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-Facets-MCR_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_144_Gbdf_gbdf_mcr_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-Facets-MCR_v08_dis/payloads/regression",
        "postman_collection_name": "GBDTS_144_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-Facets-MCR_v08.json"
    },
    {
        "ts_number": "146",
        "edit_id": "RULENMP000001",
        "code": "v18",
        "source_dir": "source_folder/GBDF/GBDTS_146_Gbdf_gbdf_mcr_RULENMP000001 No match of Procedure code GBD-Facets-MCR_v18_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_146_Gbdf_gbdf_mcr_RULENMP000001 No match of Procedure code GBD-Facets-MCR_v18_dis/payloads/regression",
        "postman_collection_name": "GBDTS_146_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULENMP000001 No match of Procedure code GBD-Facets-MCR_v18.json"
    },
    {
        "ts_number": "148",
        "edit_id": "RULEOSTO000001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/GBDTS_148_Gbdf_gbdf_mcr_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-MCR v08_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_148_Gbdf_gbdf_mcr_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-MCR v08_00W00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_148_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-MCR v08_00W00.json"
    },
    {
        "ts_number": "150",
        "edit_id": "RULETRAC000001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/GBDTS_150_Gbdf_gbdf_mcr_RULETRAC000001 Trach Supply A52492​ IPREP-132 GBD-Facets-MCR v08_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_150_Gbdf_gbdf_mcr_RULETRAC000001 Trach Supply A52492​ IPREP-132 GBD-Facets-MCR v08_00W00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_150_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULETRAC000001 Trach Supply A52492​ IPREP-132 GBD-Facets-MCR v08_00W00.json"
    },
    {
        "ts_number": "152",
        "edit_id": "RULERCRO000001",
        "code": "v34",
        "source_dir": "source_folder/GBDF/GBDTS_152_Gbdf_gbdf_mcr_RULERCRO000001 Correct_Coding_Recovery_room GBD-Facets-MCR_v34_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_152_Gbdf_gbdf_mcr_RULERCRO000001 Correct_Coding_Recovery_room GBD-Facets-MCR_v34_dis/payloads/regression",
        "postman_collection_name": "GBDTS_152_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULERCRO000001 Correct_Coding_Recovery_room GBD-Facets-MCR_v34.json"
    },
    {
        "ts_number": "154",
        "edit_id": "RULEIPDXE00001",
        "code": "v16",
        "source_dir": "source_folder/GBDF/GBDTS_154_Gbdf_gbdf_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_MCR_v16_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_154_Gbdf_gbdf_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_MCR_v16_dis/payloads/regression",
        "postman_collection_name": "GBDTS_154_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_MCR_v16.json"
    },
    {
        "ts_number": "155",
        "edit_id": "RULEIPDXE00001",
        "code": "v16",
        "source_dir": "source_folder/GBDF/GBDTS_155_Gbdf_gbdf_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_GRS_v16_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_155_Gbdf_gbdf_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_GRS_v16_dis/payloads/regression",
        "postman_collection_name": "GBDTS_155_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_GRS_v16.json"
    },
    {
        "ts_number": "156",
        "edit_id": "RULEGENE000001",
        "code": "v25",
        "source_dir": "source_folder/GBDF/GBDTS_156_Geneticstesting_gbdf_mcr_RULEGENE000001_v25_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_156_Geneticstesting_gbdf_mcr_RULEGENE000001_v25_dis/payloads/regression",
        "postman_collection_name": "GBDTS_156_Geneticstesting_Collection",
        "postman_file_name": "geneticstesting_gbd_facets_mcr_RULEGENE000001_v25.json"
    },
    {
        "ts_number": "159",
        "edit_id": "RULERCWP000001",
        "code": "v06",
        "source_dir": "source_folder/GBDF/GBDTS_159_Mcr_gbdf_mcr_RULERCWP000001-Revenue Code without Procedure_v06_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_159_Mcr_gbdf_mcr_RULERCWP000001-Revenue Code without Procedure_v06_dis/payloads/regression",
        "postman_collection_name": "GBDTS_159_Mcr_Collection",
        "postman_file_name": "mcr_RULERCWP000001-Revenue Code without Procedure_v06.json"
    },
    {
        "ts_number": "161",
        "edit_id": "RULEPMAM000001",
        "code": "v31",
        "source_dir": "source_folder/GBDF/GBDTS_161_Mcr_gbdf_mcr_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_161_Mcr_gbdf_mcr_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31_dis/payloads/regression",
        "postman_collection_name": "GBDTS_161_Mcr_Collection",
        "postman_file_name": "mcr_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31.json"
    },
    {
        "ts_number": "162",
        "edit_id": "PSMEM000003_algo",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/GBDTS_162_Gbdf_gbdf_mcr_PSMEM000003_algo_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_162_Gbdf_gbdf_mcr_PSMEM000003_algo_00W00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_162_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_psm_edits_for_emergency_PSMEM000003_algo_00W00.json"
    },
    {
        "ts_number": "164",
        "edit_id": "PSMEM000004_algo",
        "code": "v00",
        "source_dir": "source_folder/GBDF/GBDTS_164_Psm_gbdf_mcr_PSMEM000004_algo_v00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_164_Psm_gbdf_mcr_PSMEM000004_algo_v00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_164_Psm_Collection",
        "postman_file_name": "psm_edits_for_emergency_department_facility_new_algo_mcr_PSMEM000004_algo_v00.json"
    },
    {
        "ts_number": "166",
        "edit_id": "RULEEM000002_refdb",
        "code": "v05",
        "source_dir": "source_folder/GBDF/GBDTS_166_Sick_gbdf_mcr_RULEEM000002_refdb_v05_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_166_Sick_gbdf_mcr_RULEEM000002_refdb_v05_dis/payloads/regression",
        "postman_collection_name": "GBDTS_166_Sick_Collection",
        "postman_file_name": "sick_well_unbundle_mcr_RULEEM000002_refdb_v05.json"
    },
    {
        "ts_number": "127",
        "edit_id": "RULEIPVT000001",
        "code": "v38",
        "source_dir": "source_folder/GBDF/GBDTS_127_Gbdf_gbdf_mcr_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-FaceGBDTS-MCR_v38_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_127_Gbdf_gbdf_mcr_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-FaceGBDTS-MCR_v38_dis/payloads/regression",
        "postman_collection_name": "GBDTS_127_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-FaceGBDTS-MCR_v38.json"
    },
    {
        "ts_number": "129",
        "edit_id": "RULEIMMU000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/GBDTS_129_Gbdf_gbdf_mcr_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-FaceGBDTS-MCR_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_129_Gbdf_gbdf_mcr_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-FaceGBDTS-MCR_v08_dis/payloads/regression",
        "postman_collection_name": "GBDTS_129_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-FaceGBDTS-MCR_v08.json"
    },
    {
        "ts_number": "131",
        "edit_id": "RULEKNEE000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/GBDTS_131_Gbdf_gbdf_mcr_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-FaceGBDTS-MCR_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_131_Gbdf_gbdf_mcr_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-FaceGBDTS-MCR_v08_dis/payloads/regression",
        "postman_collection_name": "GBDTS_131_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-FaceGBDTS-MCR_v08.json"
    },
    {
        "ts_number": "134",
        "edit_id": "RULEJWME000001",
        "code": "v59",
        "source_dir": "source_folder/GBDF/GBDTS_134_Gbdf_gbdf_mcr_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBD-FaceGBDTS-MCR_v59_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_134_Gbdf_gbdf_mcr_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBD-FaceGBDTS-MCR_v59_dis/payloads/regression",
        "postman_collection_name": "GBDTS_134_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBD-FaceGBDTS-MCR_v59.json"
    },
    {
        "ts_number": "136",
        "edit_id": "RULEEM0000012",
        "code": "v07",
        "source_dir": "source_folder/GBDF/GBDTS_136_Gbdf_gbdf_mcr_RULEEM0000012 MNP Model GBD-FaceGBDTS-MCR_v07_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_136_Gbdf_gbdf_mcr_RULEEM0000012 MNP Model GBD-FaceGBDTS-MCR_v07_dis/payloads/regression",
        "postman_collection_name": "GBDTS_136_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEEM0000012 MNP Model GBD-FaceGBDTS-MCR_v07.json"
    },
    {
        "ts_number": "138",
        "edit_id": "RULEEMSD000002",
        "code": "v09",
        "source_dir": "source_folder/GBDF/GBDTS_138_Gbdf_gbdf_mcr_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-FaceGBDTS-MCR_v09_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_138_Gbdf_gbdf_mcr_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-FaceGBDTS-MCR_v09_dis/payloads/regression",
        "postman_collection_name": "GBDTS_138_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-FaceGBDTS-MCR_v09.json"
    },
    {
        "ts_number": "140",
        "edit_id": "RULENDCUOM000001",
        "code": "v41",
        "source_dir": "source_folder/GBDF/GBDTS_140_Gbdf_gbdf_mcr_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-FaceGBDTS-MCR_v41_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_140_Gbdf_gbdf_mcr_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-FaceGBDTS-MCR_v41_dis/payloads/regression",
        "postman_collection_name": "GBDTS_140_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-FaceGBDTS-MCR_v41.json"
    },
    {
        "ts_number": "142",
        "edit_id": "RULENDC000001",
        "code": "v40",
        "source_dir": "source_folder/GBDF/GBDTS_142_Gbdf_gbdf_mcr_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-FaceGBDTS-MCR_v40_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_142_Gbdf_gbdf_mcr_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-FaceGBDTS-MCR_v40_dis/payloads/regression",
        "postman_collection_name": "GBDTS_142_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-FaceGBDTS-MCR_v40.json"
    },
    {
        "ts_number": "144",
        "edit_id": "RULENEBU000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/GBDTS_144_Gbdf_gbdf_mcr_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-FaceGBDTS-MCR_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_144_Gbdf_gbdf_mcr_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-FaceGBDTS-MCR_v08_dis/payloads/regression",
        "postman_collection_name": "GBDTS_144_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-FaceGBDTS-MCR_v08.json"
    },
    {
        "ts_number": "146",
        "edit_id": "RULENMP000001",
        "code": "v18",
        "source_dir": "source_folder/GBDF/GBDTS_146_Gbdf_gbdf_mcr_RULENMP000001 No match of Procedure code GBD-FaceGBDTS-MCR_v18_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_146_Gbdf_gbdf_mcr_RULENMP000001 No match of Procedure code GBD-FaceGBDTS-MCR_v18_dis/payloads/regression",
        "postman_collection_name": "GBDTS_146_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULENMP000001 No match of Procedure code GBD-FaceGBDTS-MCR_v18.json"
    },
    {
        "ts_number": "148",
        "edit_id": "RULEOSTO000001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/GBDTS_148_Gbdf_gbdf_mcr_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-FaceGBDTS-MCR v08_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_148_Gbdf_gbdf_mcr_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-FaceGBDTS-MCR v08_00W00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_148_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-FaceGBDTS-MCR v08_00W00.json"
    },
    {
        "ts_number": "150",
        "edit_id": "RULETRAC000001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/GBDTS_150_Gbdf_gbdf_mcr_RULETRAC000001 Trach Supply A52492 IPREP-132 GBD-FaceGBDTS-MCR v08_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_150_Gbdf_gbdf_mcr_RULETRAC000001 Trach Supply A52492 IPREP-132 GBD-FaceGBDTS-MCR v08_00W00_dis/payloads/regression",
        "postman_collection_name": "GBDTS_150_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULETRAC000001 Trach Supply A52492 IPREP-132 GBD-FaceGBDTS-MCR v08_00W00.json"
    },
    {
        "ts_number": "152",
        "edit_id": "RULERCRO000001",
        "code": "v34",
        "source_dir": "source_folder/GBDF/GBDTS_152_Gbdf_gbdf_mcr_RULERCRO000001 Correct_Coding_Recovery_room GBD-FaceGBDTS-MCR_v34_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_152_Gbdf_gbdf_mcr_RULERCRO000001 Correct_Coding_Recovery_room GBD-FaceGBDTS-MCR_v34_dis/payloads/regression",
        "postman_collection_name": "GBDTS_152_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULERCRO000001 Correct_Coding_Recovery_room GBD-FaceGBDTS-MCR_v34.json"
    },
    {
        "ts_number": "154",
        "edit_id": "RULEIPDXE00001",
        "code": "v16",
        "source_dir": "source_folder/GBDF/GBDTS_154_Gbdf_gbdf_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_FceGBDTS_MCR_v16_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_154_Gbdf_gbdf_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_FceGBDTS_MCR_v16_dis/payloads/regression",
        "postman_collection_name": "GBDTS_154_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_edit_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_FceGBDTS_MCR_v16.json"
    },
    {
        "ts_number": "155",
        "edit_id": "RULEIPDXE00001",
        "code": "v16",
        "source_dir": "source_folder/GBDF/GBDTS_155_Gbdf_gbdf_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_FceGBDTS_GRS_v16_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/GBDTS_155_Gbdf_gbdf_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_FceGBDTS_GRS_v16_dis/payloads/regression",
        "postman_collection_name": "GBDTS_155_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_FceGBDTS_GRS_v16.json"
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
            "ts_number": "59",
            "edit_id": "RULEUSD00100",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_59_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_59_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17_dis/payloads/regression",
            "postman_collection_name": "TS_59_Unspecified_dx_code_outpt_gbdf_grs_Collection",
            "postman_file_name": "unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17.json"
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
        "ts_number": "47",
        "edit_id": "RULEEM000001",
        "code": "v04",
        "source_dir": "source_folder/GBDF/TS_47_Covid_gbdf_grs_RULEEM000001_v04_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_47_Covid_gbdf_grs_RULEEM000001_v04_dis/payloads/regression",
        "postman_collection_name": "TS_47_Covid_Collection",
        "postman_file_name": "covid_model_gbd_facets_grs_RULEEM000001_v04.json"
    },
    {
        "ts_number": "48",
        "edit_id": "RULELATE000001",
        "code": "v17",
        "source_dir": "source_folder/GBDF/TS_48_Laterality_gbdf_grs_RULELATE000001_v17_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_48_Laterality_gbdf_grs_RULELATE000001_v17_dis/payloads/regression",
        "postman_collection_name": "TS_48_Laterality_Collection",
        "postman_file_name": "laterality_policy_diagnosis_to_diagnosis_gbd_facets_grs_RULELATE000001_v17.json"
    },
    {
        "ts_number": "51",
        "edit_id": "PSMEM000001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/TS_51_Psm_gbdf_grs_PSMEM000001_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_51_Psm_gbdf_grs_PSMEM000001_00W00_dis/payloads/regression",
        "postman_collection_name": "TS_51_Psm_Collection",
        "postman_file_name": "psm_edits_established_patients_ep_gbd_facets_grs_PSMEM000001_00W00.json"
    },
    {
        "ts_number": "53",
        "edit_id": "PSMEM000002",
        "code": "v00",
        "source_dir": "source_folder/GBDF/TS_53_Psm_gbdf_grs_PSMEM000002_v00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_53_Psm_gbdf_grs_PSMEM000002_v00_dis/payloads/regression",
        "postman_collection_name": "TS_53_Psm_Collection",
        "postman_file_name": "psm_edit_for_new_patient_visit_type_np_gbd_facets_grs_PSMEM000002_v00.json"
    },
    {
        "ts_number": "55",
        "edit_id": "PSMEM000003",
        "code": "v00",
        "source_dir": "source_folder/GBDF/TS_55_Psm_gbdf_grs_PSMEM000003_v00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_55_Psm_gbdf_grs_PSMEM000003_v00_dis/payloads/regression",
        "postman_collection_name": "TS_55_Psm_Collection",
        "postman_file_name": "psm_edits_for_emergency_department_personnel_ed_gbd_facets_grs_PSMEM000003_v00.json"
    },
    {
        "ts_number": "57",
        "edit_id": "PSMEM000004",
        "code": "v00",
        "source_dir": "source_folder/GBDF/TS_57_Psm_gbdf_grs_PSMEM000004_v00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_57_Psm_gbdf_grs_PSMEM000004_v00_dis/payloads/regression",
        "postman_collection_name": "TS_57_Psm_Collection",
        "postman_file_name": "psm_edits_for_emergency_department_facility_er_gbd_facets_grs_PSMEM000004_v00.json"
    },
    {
        "ts_number": "59",
        "edit_id": "RULEUSD00100_Outpt_GRS",
        "code": "v17",
        "source_dir": "source_folder/GBDF/TS_59_Unspecified_gbdf_grs_RULEUSD00100_Outpt_GRS_v17_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_59_Unspecified_gbdf_grs_RULEUSD00100_Outpt_GRS_v17_dis/payloads/regression",
        "postman_collection_name": "TS_59_Unspecified_Collection",
        "postman_file_name": "unspecified_dxcodes_outpt_grs_gbd_facets_grs_RULEUSD00100_Outpt_GRS_v17.json"
    },
    {
        "ts_number": "61",
        "edit_id": "RULEUSD00100_Prof_GRS",
        "code": "v17",
        "source_dir": "source_folder/GBDF/TS_61_Unspecified_gbdf_grs_RULEUSD00100_Prof_GRS_v17_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_61_Unspecified_gbdf_grs_RULEUSD00100_Prof_GRS_v17_dis/payloads/regression",
        "postman_collection_name": "TS_61_Unspecified_Collection",
        "postman_file_name": "unspecified_dxcodes_prof_grs_gbd_facets_grs_RULEUSD00100_Prof_GRS_v17.json"
    },
    {
        "ts_number": "64",
        "edit_id": "RULEAMBU000001",
        "code": "v37",
        "source_dir": "source_folder/GBDF/TS_64_Shadow_gbdf_grs_Ambulance Mileage without Base Transport Paid IPREP 192_v37_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_64_Shadow_gbdf_grs_Ambulance Mileage without Base Transport Paid IPREP 192_v37_dis/payloads/regression",
        "postman_collection_name": "TS_64_Shadow_Collection",
        "postman_file_name": "shadow_ruleambu000001_grs_v37_edits_group9_Ambulance Mileage without Base Transport Paid IPREP 192_v37.json"
    },
    {
        "ts_number": "68",
        "edit_id": "RULE00000022",
        "code": "v19",
        "source_dir": "source_folder/GBDF/TS_68_Inaccurate_gbdf_grs_RULE00000022_v19_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_68_Inaccurate_gbdf_grs_RULE00000022_v19_dis/payloads/regression",
        "postman_collection_name": "TS_68_Inaccurate_Collection",
        "postman_file_name": "inaccurate_laterality_edit_gbd_facets_grs_RULE00000022_v19.json"
    },
    {
        "ts_number": "69",
        "edit_id": "RULE00000376",
        "code": "v16",
        "source_dir": "source_folder/GBDF/TS_69_Inappropriate_gbdf_grs_RULE00000376_v16_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_69_Inappropriate_gbdf_grs_RULE00000376_v16_dis/payloads/regression",
        "postman_collection_name": "TS_69_Inappropriate_Collection",
        "postman_file_name": "inappropriate_primary_diagnosis_gbd_facets_grs_RULE00000376_v16.json"
    },
    {
        "ts_number": "71",
        "edit_id": "RULEALWA000001",
        "code": "v31",
        "source_dir": "source_folder/GBDF/TS_71_Always_gbdf_grs_RULEALWA000001_v31_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_71_Always_gbdf_grs_RULEALWA000001_v31_dis/payloads/regression",
        "postman_collection_name": "TS_71_Always_Collection",
        "postman_file_name": "always_therapy_missing_modifiers_gbd_facets_grs_RULEALWA000001_v31.json"
    },
    {
        "ts_number": "74",
        "edit_id": "RULEEXCL000001",
        "code": "v27",
        "source_dir": "source_folder/GBDF/TS_74_Excludes_gbdf_grs_RULEEXCL000001_v27_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_74_Excludes_gbdf_grs_RULEEXCL000001_v27_dis/payloads/regression",
        "postman_collection_name": "TS_74_Excludes_Collection",
        "postman_file_name": "excludes_1_notes_gbd_facets_grs_RULEEXCL000001_v27.json"
    },
    {
        "ts_number": "122",
        "edit_id": "RULEGENE000001",
        "code": "v25",
        "source_dir": "source_folder/GBDF/TS_122_Geneticstesting_gbdf_grs_RULEGENE000001_v25_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_122_Geneticstesting_gbdf_grs_RULEGENE000001_v25_dis/payloads/regression",
        "postman_collection_name": "TS_122_Geneticstesting_Collection",
        "postman_file_name": "geneticstesting_gbd_facets_grs_RULEGENE000001_v25.json"
    },
    {
        "ts_number": "124",
        "edit_id": "RULEANES000001",
        "code": "v32",
        "source_dir": "source_folder/GBDF/TS_124_Anesthesia_gbdf_grs_RULEANES000001_v32_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_124_Anesthesia_gbdf_grs_RULEANES000001_v32_dis/payloads/regression",
        "postman_collection_name": "TS_124_Anesthesia_Collection",
        "postman_file_name": "anesthesia_billed_time_units_gbd_facets_grs_RULEANES000001_v32.json"
    },
    {
        "ts_number": "128",
        "edit_id": "RULEIPVT000001",
        "code": "v38",
        "source_dir": "source_folder/GBDF/TS_128_Gbdf_gbdf_grs_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-Facets-GRS_v38_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_128_Gbdf_gbdf_grs_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-Facets-GRS_v38_dis/payloads/regression",
        "postman_collection_name": "TS_128_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-Facets-GRS_v38.json"
    },
    {
        "ts_number": "130",
        "edit_id": "RULEIMMU000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/TS_130_Gbdf_gbdf_grs_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-Facets-GRS_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_130_Gbdf_gbdf_grs_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-Facets-GRS_v08_dis/payloads/regression",
        "postman_collection_name": "TS_130_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-Facets-GRS_v08.json"
    },
    {
        "ts_number": "132",
        "edit_id": "RULEKNEE000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/TS_132_Gbdf_gbdf_grs_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-Facets-GRS_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_132_Gbdf_gbdf_grs_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-Facets-GRS_v08_dis/payloads/regression",
        "postman_collection_name": "TS_132_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-Facets-GRS_v08.json"
    },
    {
        "ts_number": "133",
        "edit_id": "RULEMAN000004",
        "code": "v14",
        "source_dir": "source_folder/GBDF/TS_133_Manifestation_gbdf_grs_RULEMAN000004_v14_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_133_Manifestation_gbdf_grs_RULEMAN000004_v14_dis/payloads/regression",
        "postman_collection_name": "TS_133_Manifestation_Collection",
        "postman_file_name": "manifestation_codes_gbd_facets_grs_RULEMAN000004_v14.json"
    },
    {
        "ts_number": "135",
        "edit_id": "RULEJWME000001",
        "code": "v59",
        "source_dir": "source_folder/GBDF/TS_135_Gbdf_gbdf_grs_RULEJWME000001 Medical Injectable Edits JW Modifier I-352 GBD-Facets-GRS_v59_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_135_Gbdf_gbdf_grs_RULEJWME000001 Medical Injectable Edits JW Modifier I-352 GBD-Facets-GRS_v59_dis/payloads/regression",
        "postman_collection_name": "TS_135_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEJWME000001 Medical Injectable Edits JW Modifier I-352 GBD-Facets-GRS_v59.json"
    },
    {
        "ts_number": "137",
        "edit_id": "RULEEM0000012",
        "code": "v07",
        "source_dir": "source_folder/GBDF/TS_137_Gbdf_gbdf_grs_RULEEM0000012 MNP Model GBD-Facets-GRS_v07_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_137_Gbdf_gbdf_grs_RULEEM0000012 MNP Model GBD-Facets-GRS_v07_dis/payloads/regression",
        "postman_collection_name": "TS_137_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEEM0000012 MNP Model GBD-Facets-GRS_v07.json"
    },
    {
        "ts_number": "139",
        "edit_id": "RULEEMSD000002",
        "code": "v09",
        "source_dir": "source_folder/GBDF/TS_139_Gbdf_gbdf_grs_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-Facets-GRS_v09_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_139_Gbdf_gbdf_grs_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-Facets-GRS_v09_dis/payloads/regression",
        "postman_collection_name": "TS_139_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-Facets-GRS_v09.json"
    },
    {
        "ts_number": "141",
        "edit_id": "RULENDCUOM000001",
        "code": "v41",
        "source_dir": "source_folder/GBDF/TS_141_Gbdf_gbdf_grs_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-Facets-GRS_v41_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_141_Gbdf_gbdf_grs_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-Facets-GRS_v41_dis/payloads/regression",
        "postman_collection_name": "TS_141_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-Facets-GRS_v41.json"
    },
    {
        "ts_number": "143",
        "edit_id": "RULENDC000001",
        "code": "v40",
        "source_dir": "source_folder/GBDF/TS_143_Gbdf_gbdf_grs_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-Facets-GRS_v40_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_143_Gbdf_gbdf_grs_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-Facets-GRS_v40_dis/payloads/regression",
        "postman_collection_name": "TS_143_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-Facets-GRS_v40.json"
    },
    {
        "ts_number": "145",
        "edit_id": "RULENEBU000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/TS_145_Gbdf_gbdf_grs_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-Facets-GRS_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_145_Gbdf_gbdf_grs_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-Facets-GRS_v08_dis/payloads/regression",
        "postman_collection_name": "TS_145_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-Facets-GRS_v08.json"
    },
    {
        "ts_number": "147",
        "edit_id": "RULENMP000001",
        "code": "v18",
        "source_dir": "source_folder/GBDF/TS_147_Gbdf_gbdf_grs_RULENMP000001 No match of Procedure code GBD-Facets-GRS_v18_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_147_Gbdf_gbdf_grs_RULENMP000001 No match of Procedure code GBD-Facets-GRS_v18_dis/payloads/regression",
        "postman_collection_name": "TS_147_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULENMP000001 No match of Procedure code GBD-Facets-GRS_v18.json"
    },
    {
        "ts_number": "149",
        "edit_id": "RULEOSTO000001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/TS_149_Gbdf_gbdf_grs_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-GRS v08_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_149_Gbdf_gbdf_grs_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-GRS v08_00W00_dis/payloads/regression",
        "postman_collection_name": "TS_149_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-GRS v08_00W00.json"
    },
    {
        "ts_number": "151",
        "edit_id": "RULETRAC000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/TS_151_Gbdf_gbdf_grs_RULETRAC000001 Trach Supply A52492​ IPREP-132 GBD-Facets-GRS_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_151_Gbdf_gbdf_grs_RULETRAC000001 Trach Supply A52492​ IPREP-132 GBD-Facets-GRS_v08_dis/payloads/regression",
        "postman_collection_name": "TS_151_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULETRAC000001 Trach Supply A52492​ IPREP-132 GBD-Facets-GRS_v08.json"
    },
    {
        "ts_number": "153",
        "edit_id": "RULERCRO000001",
        "code": "v34",
        "source_dir": "source_folder/GBDF/TS_153_Gbdf_gbdf_grs_RULERCRO000001 Correct_Coding_Recovery_room GBD-Facets-GRS_v34_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_153_Gbdf_gbdf_grs_RULERCRO000001 Correct_Coding_Recovery_room GBD-Facets-GRS_v34_dis/payloads/regression",
        "postman_collection_name": "TS_153_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULERCRO000001 Correct_Coding_Recovery_room GBD-Facets-GRS_v34.json"
    },
    {
        "ts_number": "157",
        "edit_id": "RULEIPDXH00001",
        "code": "v16",
        "source_dir": "source_folder/GBDF/TS_157_Gbdf_gbdf_grs_RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBD-Facets-GRS_v16_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_157_Gbdf_gbdf_grs_RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBD-Facets-GRS_v16_dis/payloads/regression",
        "postman_collection_name": "TS_157_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBD-Facets-GRS_v16.json"
    },
    {
        "ts_number": "158",
        "edit_id": "RULERCWP000001",
        "code": "v06",
        "source_dir": "source_folder/GBDF/TS_158_Grs_gbdf_grs_RULERCWP000001-Revenue Code without Procedure_v06_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_158_Grs_gbdf_grs_RULERCWP000001-Revenue Code without Procedure_v06_dis/payloads/regression",
        "postman_collection_name": "TS_158_Grs_Collection",
        "postman_file_name": "grs_RULERCWP000001-Revenue Code without Procedure_v06.json"
    },
    {
        "ts_number": "160",
        "edit_id": "RULEPMAM000001",
        "code": "v31",
        "source_dir": "source_folder/GBDF/TS_160_Grs_gbdf_grs_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_160_Grs_gbdf_grs_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31_dis/payloads/regression",
        "postman_collection_name": "TS_160_Grs_Collection",
        "postman_file_name": "grs_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31.json"
    },
    {
        "ts_number": "163",
        "edit_id": "PSMEM000003_algo",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/TS_163_Gbdf_gbdf_grs_PSMEM000003_algo_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_163_Gbdf_gbdf_grs_PSMEM000003_algo_00W00_dis/payloads/regression",
        "postman_collection_name": "TS_163_Gbdf_Collection",
        "postman_file_name": "gbdf_mcr_psm_edits_for_emergency_PSMEM000003_algo_00W00.json"
    },
    {
        "ts_number": "165",
        "edit_id": "PSMEM000004_algo",
        "code": "v00",
        "source_dir": "source_folder/GBDF/TS_165_Psm_gbdf_grs_PSMEM000004_algo_v00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_165_Psm_gbdf_grs_PSMEM000004_algo_v00_dis/payloads/regression",
        "postman_collection_name": "TS_165_Psm_Collection",
        "postman_file_name": "psm_edits_for_emergency_department_facility_new_algo_grs_PSMEM000004_algo_v00.json"
    },
    {
        "ts_number": "167",
        "edit_id": "RULEEM000002_refdb",
        "code": "v05",
        "source_dir": "source_folder/GBDF/TS_167_Sick_gbdf_grs_RULEEM000002_refdb_v05_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_167_Sick_gbdf_grs_RULEEM000002_refdb_v05_dis/payloads/regression",
        "postman_collection_name": "TS_167_Sick_Collection",
        "postman_file_name": "sick_well_unbundle_grs_RULEEM000002_refdb_v05.json"
    },
    {
        "ts_number": "128",
        "edit_id": "RULEIPVT000001",
        "code": "v38",
        "source_dir": "source_folder/GBDF/TS_128_Gbdf_gbdf_grs_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-FaceGBDTS-GRS_v38_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_128_Gbdf_gbdf_grs_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-FaceGBDTS-GRS_v38_dis/payloads/regression",
        "postman_collection_name": "TS_128_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBD-FaceGBDTS-GRS_v38.json"
    },
    {
        "ts_number": "130",
        "edit_id": "RULEIMMU000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/TS_130_Gbdf_gbdf_grs_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-FaceGBDTS-GRS_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_130_Gbdf_gbdf_grs_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-FaceGBDTS-GRS_v08_dis/payloads/regression",
        "postman_collection_name": "TS_130_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBD-FaceGBDTS-GRS_v08.json"
    },
    {
        "ts_number": "132",
        "edit_id": "RULEKNEE000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/TS_132_Gbdf_gbdf_grs_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-FaceGBDTS-GRS_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_132_Gbdf_gbdf_grs_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-FaceGBDTS-GRS_v08_dis/payloads/regression",
        "postman_collection_name": "TS_132_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBD-FaceGBDTS-GRS_v08.json"
    },
    {
        "ts_number": "135",
        "edit_id": "RULEJWME000001",
        "code": "v59",
        "source_dir": "source_folder/GBDF/TS_135_Gbdf_gbdf_grs_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBD-FaceGBDTS-GRS_v59_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_135_Gbdf_gbdf_grs_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBD-FaceGBDTS-GRS_v59_dis/payloads/regression",
        "postman_collection_name": "TS_135_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBD-FaceGBDTS-GRS_v59.json"
    },
    {
        "ts_number": "137",
        "edit_id": "RULEEM0000012",
        "code": "v07",
        "source_dir": "source_folder/GBDF/TS_137_Gbdf_gbdf_grs_RULEEM0000012 MNP Model GBD-FaceGBDTS-GRS_v07_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_137_Gbdf_gbdf_grs_RULEEM0000012 MNP Model GBD-FaceGBDTS-GRS_v07_dis/payloads/regression",
        "postman_collection_name": "TS_137_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEEM0000012 MNP Model GBD-FaceGBDTS-GRS_v07.json"
    },
    {
        "ts_number": "139",
        "edit_id": "RULEEMSD000002",
        "code": "v09",
        "source_dir": "source_folder/GBDF/TS_139_Gbdf_gbdf_grs_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-FaceGBDTS-GRS_v09_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_139_Gbdf_gbdf_grs_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-FaceGBDTS-GRS_v09_dis/payloads/regression",
        "postman_collection_name": "TS_139_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBD-FaceGBDTS-GRS_v09.json"
    },
    {
        "ts_number": "141",
        "edit_id": "RULENDCUOM000001",
        "code": "v41",
        "source_dir": "source_folder/GBDF/TS_141_Gbdf_gbdf_grs_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-FaceGBDTS-GRS_v41_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_141_Gbdf_gbdf_grs_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-FaceGBDTS-GRS_v41_dis/payloads/regression",
        "postman_collection_name": "TS_141_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBD-FaceGBDTS-GRS_v41.json"
    },
    {
        "ts_number": "143",
        "edit_id": "RULENDC000001",
        "code": "v40",
        "source_dir": "source_folder/GBDF/TS_143_Gbdf_gbdf_grs_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-FaceGBDTS-GRS_v40_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_143_Gbdf_gbdf_grs_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-FaceGBDTS-GRS_v40_dis/payloads/regression",
        "postman_collection_name": "TS_143_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBD-FaceGBDTS-GRS_v40.json"
    },
    {
        "ts_number": "145",
        "edit_id": "RULENEBU000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/TS_145_Gbdf_gbdf_grs_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-FaceGBDTS-GRS_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_145_Gbdf_gbdf_grs_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-FaceGBDTS-GRS_v08_dis/payloads/regression",
        "postman_collection_name": "TS_145_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULENEBU000001 Nebulizer A52466 IPREP-132 GBD-FaceGBDTS-GRS_v08.json"
    },
    {
        "ts_number": "147",
        "edit_id": "RULENMP000001",
        "code": "v18",
        "source_dir": "source_folder/GBDF/TS_147_Gbdf_gbdf_grs_RULENMP000001 No match of Procedure code GBD-FaceGBDTS-GRS_v18_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_147_Gbdf_gbdf_grs_RULENMP000001 No match of Procedure code GBD-FaceGBDTS-GRS_v18_dis/payloads/regression",
        "postman_collection_name": "TS_147_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULENMP000001 No match of Procedure code GBD-FaceGBDTS-GRS_v18.json"
    },
    {
        "ts_number": "149",
        "edit_id": "RULEOSTO000001",
        "code": "00W00",
        "source_dir": "source_folder/GBDF/TS_149_Gbdf_gbdf_grs_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-FaceGBDTS-GRS v08_00W00_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_149_Gbdf_gbdf_grs_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-FaceGBDTS-GRS v08_00W00_dis/payloads/regression",
        "postman_collection_name": "TS_149_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-FaceGBDTS-GRS v08_00W00.json"
    },
    {
        "ts_number": "151",
        "edit_id": "RULETRAC000001",
        "code": "v08",
        "source_dir": "source_folder/GBDF/TS_151_Gbdf_gbdf_grs_RULETRAC000001 Trach Supply A52492 IPREP-132 GBD-FaceGBDTS-GRS_v08_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_151_Gbdf_gbdf_grs_RULETRAC000001 Trach Supply A52492 IPREP-132 GBD-FaceGBDTS-GRS_v08_dis/payloads/regression",
        "postman_collection_name": "TS_151_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULETRAC000001 Trach Supply A52492 IPREP-132 GBD-FaceGBDTS-GRS_v08.json"
    },
    {
        "ts_number": "153",
        "edit_id": "RULERCRO000001",
        "code": "v34",
        "source_dir": "source_folder/GBDF/TS_153_Gbdf_gbdf_grs_RULERCRO000001 Correct_Coding_Recovery_room GBD-FaceGBDTS-GRS_v34_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_153_Gbdf_gbdf_grs_RULERCRO000001 Correct_Coding_Recovery_room GBD-FaceGBDTS-GRS_v34_dis/payloads/regression",
        "postman_collection_name": "TS_153_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULERCRO000001 Correct_Coding_Recovery_room GBD-FaceGBDTS-GRS_v34.json"
    },
    {
        "ts_number": "157",
        "edit_id": "RULEIPDXH00001",
        "code": "v16",
        "source_dir": "source_folder/GBDF/TS_157_Gbdf_gbdf_grs_RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBD-FaceGBDTS-GRS_v16_sur/payloads/regression",
        "dest_dir": "renaming_jsons/GBDTS/TS_157_Gbdf_gbdf_grs_RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBD-FaceGBDTS-GRS_v16_dis/payloads/regression",
        "postman_collection_name": "TS_157_Gbdf_Collection",
        "postman_file_name": "gbdf_grs_edit_RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBD-FaceGBDTS-GRS_v16.json"
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

# For backward compatibility, lazily resolve MODELS_CONFIG on access
def __getattr__(name):
    if name == "MODELS_CONFIG":
        return get_models_config(use_dynamic=True)
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

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
