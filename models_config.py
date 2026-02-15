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
            "edit_id": "RULESUB4000001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_02_Expansion_WGS_CSBD_RULESUB4000001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_02_Expansion_WGS_CSBD_RULESUB4000001_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_02_Expansion_Collection",
            "postman_file_name": "expansion_on_sub_edit_4_iprep_117_iprep_313_wgs_csbd_RULESUB4000001_00W28.json"
        },
        {
            "ts_number": "03",
            "edit_id": "RULEOPBS000001",
            "code": "00W15",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_03_Op_WGS_CSBD_RULEOPBS000001_00W15_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_03_Op_WGS_CSBD_RULEOPBS000001_00W15_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_03_Op_Collection",
            "postman_file_name": "op_facility_bundled_services_wgs_csbd_RULEOPBS000001_00W15.json"
        },
        {
            "ts_number": "04",
            "edit_id": "RULEANES000001",
            "code": "00W32",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_04_Anesthesia_WGS_CSBD_RULEANES000001_00W32_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_04_Anesthesia_WGS_CSBD_RULEANES000001_00W32_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_04_Anesthesia_Collection",
            "postman_file_name": "anesthesia_billed_time_units_wgs_csbd_RULEANES000001_00W32.json"
        },
        {
            "ts_number": "05",
            "edit_id": "RULEBDLG000004",
            "code": "00W15",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_05_Bundled_WGS_CSBD_RULEBDLG000004_00W15_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_05_Bundled_WGS_CSBD_RULEBDLG000004_00W15_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_05_Bundled_Collection",
            "postman_file_name": "bundled_services_logic_4_iprep_213_wgs_csbd_RULEBDLG000004_00W15.json"
        },
        {
            "ts_number": "06",
            "edit_id": "RULECLIA00001",
            "code": "00W00",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_06_Clia_WGS_CSBD_RULECLIA00001_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_06_Clia_WGS_CSBD_RULECLIA00001_00W00_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_06_Clia_Collection",
            "postman_file_name": "clia_edit_wgs_csbd_l92l95l94l93l90l91_RULECLIA00001_00W00.json"
        },
        {
            "ts_number": "07",
            "edit_id": "RULEJWME000001",
            "code": "00W59",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_07_Medical_WGS_CSBD_RULEJWME000001_00W59_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_07_Medical_WGS_CSBD_RULEJWME000001_00W59_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_07_Medical_Collection",
            "postman_file_name": "medical_injectable_edits_jw_modifier_i_352_wgs_csbd_RULEJWME000001_00W59.json"
        },
        {
            "ts_number": "08",
            "edit_id": "RULEMFTM000001",
            "code": "00W31",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_08_Missing_WGS_CSBD_RULEMFTM000001_00W31_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_08_Missing_WGS_CSBD_RULEMFTM000001_00W31_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_08_Missing_Collection",
            "postman_file_name": "missing_required_finger_or_toe_anatomical_modifier_iprep_310_wgs_csbd_RULEMFTM000001_00W31.json"
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
            "ts_number": "09",
            "edit_id": "RULENCCIPTP001",
            "code": "00W10",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_09_Ncci_WGS_CSBD_RULENCCIPTP001_00W10_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_09_Ncci_WGS_CSBD_RULENCCIPTP001_00W10_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_09_Ncci_Collection",
            "postman_file_name": "ncci_ptp_outpt_facility_iprep_271_wgs_csbd_RULENCCIPTP001_00W10.json"
        },
        {
            "ts_number": "10",
            "edit_id": "RULENDC000001",
            "code": "00W40",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_10_Ndc_WGS_CSBD_RULENDC000001_00W40_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_10_Ndc_WGS_CSBD_RULENDC000001_00W40_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_10_Ndc_Collection",
            "postman_file_name": "ndc_validation_edit_expansion_iprep_296_wgs_csbd_RULENDC000001_00W40.json"
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
            "ts_number": "11",
            "edit_id": "RULERCRO000001",
            "code": "00W34",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_11_Correct_WGS_CSBD_RULERCRO000001_00W34_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_11_Correct_WGS_CSBD_RULERCRO000001_00W34_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_11_Correct_Collection",
            "postman_file_name": "correct_coding_recovery_room_reimbursement_iprep_241_wgs_csbd_RULERCRO000001_00W34.json"
        },
        {
            "ts_number": "12",
            "edit_id": "RULERCTH000001",
            "code": "00W26",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_12_Revenue_WGS_CSBD_RULERCTH000001_00W26_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_12_Revenue_WGS_CSBD_RULERCTH000001_00W26_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_12_Revenue_Collection",
            "postman_file_name": "revenue_code_to_hcpcs_alignment_edit_iprep_205_wgs_csbd_RULERCTH000001_00W26.json"
        },
        {
            "ts_number": "13",
            "edit_id": "RULEUNAC000001",
            "code": "00W16",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_13_Unacceptable_WGS_CSBD_RULEUNAC000001_00W16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_13_Unacceptable_WGS_CSBD_RULEUNAC000001_00W16_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_13_Unacceptable_Collection",
            "postman_file_name": "unacceptable_principal_diagnosis_wgs_csbd_RULEUNAC000001_00W16.json"
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
            "ts_number": "14",
            "edit_id": "RULEEM0000012 MNP Model",
            "code": "00W00",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_14_Wgs_WGS_CSBD_RULEEM0000012 MNP Model_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_14_Wgs_WGS_CSBD_RULEEM0000012 MNP Model_00W00_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_14_Wgs_Collection",
            "postman_file_name": "wgs_csbd_w07_RULEEM0000012 MNP Model_00W00.json"
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
            "ts_number": "15",
            "edit_id": "RULELATE000001",
            "code": "00W17",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_15_Laterality_WGS_CSBD_RULELATE000001_00W17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_15_Laterality_WGS_CSBD_RULELATE000001_00W17_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_15_Laterality_Collection",
            "postman_file_name": "laterality_policy_diagnosis_to_diagnosis_wgs_csbd_RULELATE000001_00W17.json"
        },
        {
            "ts_number": "16",
            "edit_id": "RULEREVE000005",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_16_Revenue_WGS_CSBD_RULEREVE000005_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_16_Revenue_WGS_CSBD_RULEREVE000005_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_16_Revenue_Collection",
            "postman_file_name": "revenue_code_services_not_payable_on_facility_claim_sub_edit_5_wgs_csbd_RULEREVE000005_00W28.json"
        },
        {
            "ts_number": "17",
            "edit_id": "RULEREVE000004",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_17_Revenue_WGS_CSBD_RULEREVE000004_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_17_Revenue_WGS_CSBD_RULEREVE000004_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_17_Revenue_Collection",
            "postman_file_name": "revenue_code_services_not_payable_on_facility_claim_sub_edit_4_wgs_csbd_RULEREVE000004_00W28.json"
        },
        {
            "ts_number": "18",
            "edit_id": "RULEREVE000003",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_18_Revenue_WGS_CSBD_RULEREVE000003_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_18_Revenue_WGS_CSBD_RULEREVE000003_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_18_Revenue_Collection",
            "postman_file_name": "revenue_code_services_not_payable_on_facility_claim_sub_edit_3_wgs_csbd_RULEREVE000003_00W28.json"
        },
        {
            "ts_number": "19",
            "edit_id": "RULEREVE000001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_19_Revenue_WGS_CSBD_RULEREVE000001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_19_Revenue_WGS_CSBD_RULEREVE000001_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_19_Revenue_Collection",
            "postman_file_name": "revenue_code_services_not_payable_on_facility_claim_sub_edit_2_wgs_csbd_RULEREVE000001_00W28.json"
        },
        {
            "ts_number": "20",
            "edit_id": "RULEREVE000002",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_20_Revenue_WGS_CSBD_RULEREVE000002_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_20_Revenue_WGS_CSBD_RULEREVE000002_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_20_Revenue_Collection",
            "postman_file_name": "revenue_code_services_not_payable_on_facility_claim_sub_edit_1_wgs_csbd_RULEREVE000002_00W28.json"
        },
        {
            "ts_number": "21",
            "edit_id": "RULELAB0000009",
            "code": "00W13",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_21_Lab_WGS_CSBD_RULELAB0000009_00W13_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_21_Lab_WGS_CSBD_RULELAB0000009_00W13_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_21_Lab_Collection",
            "postman_file_name": "lab_panel_model_wgs_csbd_RULELAB0000009_00W13.json"
        },
        {
            "ts_number": "22",
            "edit_id": "RULEDEVI000003",
            "code": "00W36",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_22_Device_WGS_CSBD_RULEDEVI000003_00W36_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_22_Device_WGS_CSBD_RULEDEVI000003_00W36_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_22_Device_Collection",
            "postman_file_name": "device_dependent_proceduresr1_1b_wgs_csbd_RULEDEVI000003_00W36.json"
        },
        {
            "ts_number": "23",
            "edit_id": "RULERECO000001",
            "code": "00W34",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_23_Recovery_WGS_CSBD_RULERECO000001_00W34_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_23_Recovery_WGS_CSBD_RULERECO000001_00W34_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_23_Recovery_Collection",
            "postman_file_name": "recovery_room_reimbursement_wgs_csbd_RULERECO000001_00W34.json"
        },
        {
            "ts_number": "24",
            "edit_id": "RULEBEHA000003",
            "code": "00W26",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_24_Revenue_WGS_CSBD_RULEBEHA000003_00W26_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_24_Revenue_WGS_CSBD_RULEBEHA000003_00W26_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_24_Revenue_Collection",
            "postman_file_name": "revenue_code_to_hcpcs_xwalk_1b_wgs_csbd_RULEBEHA000003_00W26.json"
        },
        {
            "ts_number": "25",
            "edit_id": "RULEINCI000001",
            "code": "00W34",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_25_Incidental_WGS_CSBD_RULEINCI000001_00W34_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_25_Incidental_WGS_CSBD_RULEINCI000001_00W34_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_25_Incidental_Collection",
            "postman_file_name": "incidental_services_facility_wgs_csbd_RULEINCI000001_00W34.json"
        },
        {
            "ts_number": "26",
            "edit_id": "RULERCE0000006",
            "code": "00W06",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_26_Revenue_WGS_CSBD_RULERCE0000006_00W06_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_26_Revenue_WGS_CSBD_RULERCE0000006_00W06_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_26_Revenue_Collection",
            "postman_file_name": "revenue_model_cr_v3_wgs_csbd_RULERCE0000006_00W06.json"
        },
        {
            "ts_number": "27",
            "edit_id": "RULEBEHA000001",
            "code": "00W26",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_27_Hcpcs_WGS_CSBD_RULEBEHA000001_00W26_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_27_Hcpcs_WGS_CSBD_RULEBEHA000001_00W26_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_27_Hcpcs_Collection",
            "postman_file_name": "hcpcs_to_revenue_code_xwalk_wgs_csbd_RULEBEHA000001_00W26.json"
        },
        {
            "ts_number": "28",
            "edit_id": "RULERCE0000005",
            "code": "00W06",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_28_Revenue_WGS_CSBD_RULERCE0000005_00W06_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_28_Revenue_WGS_CSBD_RULERCE0000005_00W06_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_28_Revenue_Collection",
            "postman_file_name": "revenue_model_iprep_108_wgs_csbd_RULERCE0000005_00W06.json"
        },
        {
            "ts_number": "29",
            "edit_id": "RULEEM000002_refdb",
            "code": "00W05",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_29_Sick_WGS_CSBD_RULEEM000002_refdb_00W05_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_29_Sick_WGS_CSBD_RULEEM000002_refdb_00W05_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_29_Sick_Collection",
            "postman_file_name": "sick_well_unbundle_refdb_wgs_csbd_RULEEM000002_refdb_00W05.json"
        },
        {
            "ts_number": "30",
            "edit_id": "RULEMUTU000001",
            "code": "00W33",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_30_Mutually_WGS_CSBD_RULEMUTU000001_00W33_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_30_Mutually_WGS_CSBD_RULEMUTU000001_00W33_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_30_Mutually_Collection",
            "postman_file_name": "mutually_exclusive_places_of_service_wgs_csbd_RULEMUTU000001_00W33.json"
        },
        {
            "ts_number": "31",
            "edit_id": "RULEEMSD000001",
            "code": "00W09",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_31_Multiple_WGS_CSBD_RULEEMSD000001_00W09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_31_Multiple_WGS_CSBD_RULEEMSD000001_00W09_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_31_Multiple_Collection",
            "postman_file_name": "multiple_em_same_day_wgs_csbd_RULEEMSD000001_00W09.json"
        },
        {
            "ts_number": "32",
            "edit_id": "RULERBWR000001",
            "code": "00W30",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_32_Radiology_WGS_CSBD_RULERBWR000001_00W30_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_32_Radiology_WGS_CSBD_RULERBWR000001_00W30_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_32_Radiology_Collection",
            "postman_file_name": "radiology_services_billed_without_radiopharmaceuticals_wgs_csbd_RULERBWR000001_00W30.json"
        },
        {
            "ts_number": "33",
            "edit_id": "RULEMAN000004",
            "code": "00W14",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_33_Manifestation_WGS_CSBD_RULEMAN000004_00W14_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_33_Manifestation_WGS_CSBD_RULEMAN000004_00W14_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_33_Manifestation_Collection",
            "postman_file_name": "manifestation_codes_wgs_csbd_RULEMAN000004_00W14.json"
        },
        {
            "ts_number": "34",
            "edit_id": "RULESS00000011",
            "code": "00W11",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_34_Supplies_WGS_CSBD_RULESS00000011_00W11_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_34_Supplies_WGS_CSBD_RULESS00000011_00W11_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_34_Supplies_Collection",
            "postman_file_name": "supplies_billed_as_implants_wgs_csbd_RULESS00000011_00W11.json"
        },
        {
            "ts_number": "35",
            "edit_id": "RULESUPP000001",
            "code": "00W11",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_35_Supplies_WGS_CSBD_RULESUPP000001_00W11_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_35_Supplies_WGS_CSBD_RULESUPP000001_00W11_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_35_Supplies_Collection",
            "postman_file_name": "supplies_billed_as_implants_wgs_csbd_RULESUPP000001_00W11.json"
        },
        {
            "ts_number": "36",
            "edit_id": "RULEDRCM000001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_36_Diagnostic_WGS_CSBD_RULEDRCM000001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_36_Diagnostic_WGS_CSBD_RULEDRCM000001_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_36_Diagnostic_Collection",
            "postman_file_name": "diagnostic_radiopharmaceuticals_and_contrast_materials_wgs_csbd_RULEDRCM000001_00W28.json"
        },
        {
            "ts_number": "37",
            "edit_id": "RULEALWA000001",
            "code": "00W31",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_37_Always_WGS_CSBD_RULEALWA000001_00W31_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_37_Always_WGS_CSBD_RULEALWA000001_00W31_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_37_Always_Collection",
            "postman_file_name": "always_therapy_missing_modifiers_wgs_csbd_RULEALWA000001_00W31.json"
        },
        {
            "ts_number": "38",
            "edit_id": "RULEPROF000001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_38_Professional_WGS_CSBD_RULEPROF000001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_38_Professional_WGS_CSBD_RULEPROF000001_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_38_Professional_Collection",
            "postman_file_name": "professional_anesthesia_modifiers_wgs_csbd_RULEPROF000001_00W28.json"
        },
        {
            "ts_number": "39",
            "edit_id": "RULENONP000001",
            "code": "00W30",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_39_Non_WGS_CSBD_RULENONP000001_00W30_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_39_Non_WGS_CSBD_RULENONP000001_00W30_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_39_Non_Collection",
            "postman_file_name": "non_patient_lab_service_wgs_csbd_RULENONP000001_00W30.json"
        },
        {
            "ts_number": "40",
            "edit_id": "RULE00000022",
            "code": "00W19",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_40_Inaccurate_WGS_CSBD_RULE00000022_00W19_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_40_Inaccurate_WGS_CSBD_RULE00000022_00W19_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_40_Inaccurate_Collection",
            "postman_file_name": "inaccurate_laterality_edit_wgs_csbd_RULE00000022_00W19.json"
        },
        {
            "ts_number": "41",
            "edit_id": "RULEFACI000001",
            "code": "00W24",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_41_Facility_WGS_CSBD_RULEFACI000001_00W24_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_41_Facility_WGS_CSBD_RULEFACI000001_00W24_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_41_Facility_Collection",
            "postman_file_name": "facility_modifier_wgs_csbd_RULEFACI000001_00W24.json"
        },
        {
            "ts_number": "42",
            "edit_id": "RULEUSD00100_Outpt",
            "code": "00W17",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_42_Unspecified_WGS_CSBD_RULEUSD00100_Outpt_00W17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_42_Unspecified_WGS_CSBD_RULEUSD00100_Outpt_00W17_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_42_Unspecified_Collection",
            "postman_file_name": "unspecified_dxcodes_csbd_outpt_wgs_csbd_RULEUSD00100_Outpt_00W17.json"
        },
        {
            "ts_number": "43",
            "edit_id": "RULEUSD00100_prof",
            "code": "00W17",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_43_Unspecified_WGS_CSBD_RULEUSD00100_prof_00W17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_43_Unspecified_WGS_CSBD_RULEUSD00100_prof_00W17_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_43_Unspecified_Collection",
            "postman_file_name": "unspecified_dxcodes_wgs_csbd_RULEUSD00100_prof_00W17.json"
        },
        {
            "ts_number": "44",
            "edit_id": "PSMEM000001",
            "code": "00W00",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_44_Psm_WGS_CSBD_PSMEM000001_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_44_Psm_WGS_CSBD_PSMEM000001_00W00_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_44_Psm_Collection",
            "postman_file_name": "psm_edits_established_patients_ep_wgs_csbd_PSMEM000001_00W00.json"
        },
        {
            "ts_number": "45",
            "edit_id": "PSMEM000002",
            "code": "00W00",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_45_Psm_WGS_CSBD_PSMEM000002_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_45_Psm_WGS_CSBD_PSMEM000002_00W00_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_45_Psm_Collection",
            "postman_file_name": "psm_edit_for_new_patient_visit_type_np_wgs_csbd_PSMEM000002_00W00.json"
        },
        {
            "ts_number": "46",
            "edit_id": "PSMEM000003",
            "code": "00W00",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_46_Psm_WGS_CSBD_PSMEM000003_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_46_Psm_WGS_CSBD_PSMEM000003_00W00_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_46_Psm_Collection",
            "postman_file_name": "psm_edits_for_emergency_department_personnel_ed_wgs_csbd_PSMEM000003_00W00.json"
        },
        {
            "ts_number": "47",
            "edit_id": "PSMEM000004",
            "code": "00W00",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_47_Psm_WGS_CSBD_PSMEM000004_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_47_Psm_WGS_CSBD_PSMEM000004_00W00_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_47_Psm_Collection",
            "postman_file_name": "psm_edits_for_emergency_department_facility_er_wgs_csbd_PSMEM000004_00W00.json"
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
            "ts_number": "48",
            "edit_id": "RULEAMBU000001",
            "code": "00W37",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_48_Ambulance_WGS_CSBD_RULEAMBU000001_00W37_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_48_Ambulance_WGS_CSBD_RULEAMBU000001_00W37_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_48_Ambulance_Collection",
            "postman_file_name": "ambulance_mileage_without_base_transport_paid_iprep_192_wgs_csbd_RULEAMBU000001_00W37.json"
        },
        {
            "ts_number": "49",
            "edit_id": "RULESNDX000001",
            "code": "00W35",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_49_Secondary_WGS_CSBD_RULESNDX000001_00W35_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_49_Secondary_WGS_CSBD_RULESNDX000001_00W35_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_49_Secondary_Collection",
            "postman_file_name": "secondary_dxs_may_not_be_primary_dxs_group4_wgs_csbd_RULESNDX000001_00W35.json"
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
            "ts_number": "50",
            "edit_id": "RULEIPVT000001",
            "code": "00W38",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_50_Immunization_WGS_CSBD_RULEIPVT000001_00W38_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_50_Immunization_WGS_CSBD_RULEIPVT000001_00W38_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_50_Immunization_Collection",
            "postman_file_name": "immunization_procedure_code_without_vaccinetoxoid_group4_wgs_csbd_RULEIPVT000001_00W38.json"
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
            "ts_number": "51",
            "edit_id": "RULEPMAM000001",
            "code": "00W00",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_51_Iprep_WGS_CSBD_RULEPMAM000001_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_51_Iprep_WGS_CSBD_RULEPMAM000001_00W00_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_51_Iprep_Collection",
            "postman_file_name": "iprep_58_procedures_with_missing_anatomical_modifiers_wgs_csbd_RULEPMAM000001_00W00.json"
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
            "ts_number": "52",
            "edit_id": "RULEBDLG000001",
            "code": "00W15",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_52_Iprep_WGS_CSBD_RULEBDLG000001_00W15_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_52_Iprep_WGS_CSBD_RULEBDLG000001_00W15_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_52_Iprep_Collection",
            "postman_file_name": "iprep_122_bundled_services_venous_access_port_wgs_csbd_RULEBDLG000001_00W15.json"
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
            "ts_number": "53",
            "edit_id": "RULEBDLG000007",
            "code": "00W15",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_53_Iprep_WGS_CSBD_RULEBDLG000007_00W15_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_53_Iprep_WGS_CSBD_RULEBDLG000007_00W15_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_53_Iprep_Collection",
            "postman_file_name": "iprep_214_bundles_logic_7_wgs_csbd_RULEBDLG000007_00W15.json"
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
            "ts_number": "54",
            "edit_id": "RULEBDLG000016",
            "code": "00W15",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_54_Iprep_WGS_CSBD_RULEBDLG000016_00W15_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_54_Iprep_WGS_CSBD_RULEBDLG000016_00W15_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_54_Iprep_Collection",
            "postman_file_name": "iprep_215_bundles_logic_16_wgs_csbd_RULEBDLG000016_00W15.json"
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
            "ts_number": "55",
            "edit_id": "RULENDCUOM000001",
            "code": "00W41",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_55_Ndc_WGS_CSBD_RULENDCUOM000001_00W41_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_55_Ndc_WGS_CSBD_RULENDCUOM000001_00W41_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_55_Ndc_Collection",
            "postman_file_name": "ndc_uom_validation_edit_expansion_iprep_328_wgs_csbd_RULENDCUOM000001_00W41.json"
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
            "ts_number": "56",
            "edit_id": "PSMEM000004_Algo",
            "code": "00W00",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_56_Psm_WGS_CSBD_PSMEM000004_Algo_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_56_Psm_WGS_CSBD_PSMEM000004_Algo_00W00_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_56_Psm_Collection",
            "postman_file_name": "psm_edits_for_emergency_department_facility_new_algo_iprep_364_wgs_csbd_PSMEM000004_Algo_00W00.json"
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
            "ts_number": "57",
            "edit_id": "RULEMBOS000001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_57_Multiple_WGS_CSBD_RULEMBOS000001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_57_Multiple_WGS_CSBD_RULEMBOS000001_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_57_Multiple_Collection",
            "postman_file_name": "multiple_billing_of_obstetrical_services_iprep_278_wgs_csbd_RULEMBOS000001_00W28.json"
        },
        {
            "ts_number": "58",
            "edit_id": "RULEOBSER00001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_58_Observation_WGS_CSBD_RULEOBSER00001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_58_Observation_WGS_CSBD_RULEOBSER00001_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_58_Observation_Collection",
            "postman_file_name": "observation_services_iprep_142_sub_edit_1_wgs_csbd_RULEOBSER00001_00W28.json"
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
            "ts_number": "59",
            "edit_id": "RULEOBSER00002_Observation Services IPREP-142 sub-edit-2",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_59_Wgs_WGS_CSBD_RULEOBSER00002_Observation Services IPREP-142 sub-edit-2_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_59_Wgs_WGS_CSBD_RULEOBSER00002_Observation Services IPREP-142 sub-edit-2_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_59_Wgs_Collection",
            "postman_file_name": "wgs_csbd_RULEOBSER00002_Observation Services IPREP-142 sub-edit-2_00W28.json"
        },
        {
            "ts_number": "60",
            "edit_id": "RULEOBSER00003_Observation Services IPREP-142 sub-edit-3",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_60_Wgs_WGS_CSBD_RULEOBSER00003_Observation Services IPREP-142 sub-edit-3_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_60_Wgs_WGS_CSBD_RULEOBSER00003_Observation Services IPREP-142 sub-edit-3_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_60_Wgs_Collection",
            "postman_file_name": "wgs_csbd_RULEOBSER00003_Observation Services IPREP-142 sub-edit-3_00W28.json"
        },
        {
            "ts_number": "61",
            "edit_id": "RULEOBSER00004_Observation Services IPREP-142 sub-edit-4",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_61_Wgs_WGS_CSBD_RULEOBSER00004_Observation Services IPREP-142 sub-edit-4_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_61_Wgs_WGS_CSBD_RULEOBSER00004_Observation Services IPREP-142 sub-edit-4_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_61_Wgs_Collection",
            "postman_file_name": "wgs_csbd_RULEOBSER00004_Observation Services IPREP-142 sub-edit-4_00W28.json"
        },
        {
            "ts_number": "62",
            "edit_id": "RULEOBSER00005_Observation Services IPREP-142 sub-edit-5",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_62_Wgs_WGS_CSBD_RULEOBSER00005_Observation Services IPREP-142 sub-edit-5_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_62_Wgs_WGS_CSBD_RULEOBSER00005_Observation Services IPREP-142 sub-edit-5_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_62_Wgs_Collection",
            "postman_file_name": "wgs_csbd_RULEOBSER00005_Observation Services IPREP-142 sub-edit-5_00W28.json"
        },
        {
            "ts_number": "63",
            "edit_id": "RULEOBSER00006_Observation Services IPREP-142 sub-edit-6",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_63_Wgs_WGS_CSBD_RULEOBSER00006_Observation Services IPREP-142 sub-edit-6_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_63_Wgs_WGS_CSBD_RULEOBSER00006_Observation Services IPREP-142 sub-edit-6_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_63_Wgs_Collection",
            "postman_file_name": "wgs_csbd_RULEOBSER00006_Observation Services IPREP-142 sub-edit-6_00W28.json"
        },
        {
            "ts_number": "64",
            "edit_id": "RULEOBSER00007_Observation Services IPREP-142 sub-edit-7",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_64_Wgs_WGS_CSBD_RULEOBSER00007_Observation Services IPREP-142 sub-edit-7_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_64_Wgs_WGS_CSBD_RULEOBSER00007_Observation Services IPREP-142 sub-edit-7_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_64_Wgs_Collection",
            "postman_file_name": "wgs_csbd_RULEOBSER00007_Observation Services IPREP-142 sub-edit-7_00W28.json"
        },
        {
            "ts_number": "65",
            "edit_id": "RULEOBSER00008_Observation Services IPREP-142 sub-edit-8",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_65_Wgs_WGS_CSBD_RULEOBSER00008_Observation Services IPREP-142 sub-edit-8_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_65_Wgs_WGS_CSBD_RULEOBSER00008_Observation Services IPREP-142 sub-edit-8_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_65_Wgs_Collection",
            "postman_file_name": "wgs_csbd_RULEOBSER00008_Observation Services IPREP-142 sub-edit-8_00W28.json"
        },
        {
            "ts_number": "66",
            "edit_id": "RULEADDON00001 IPREP-53 Add-on without Base - CPT Sourcing",
            "code": "00W60",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_66_Wgs_WGS_CSBD_RULEADDON00001 IPREP-53 Add-on without Base - CPT Sourcing_00W60_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_66_Wgs_WGS_CSBD_RULEADDON00001 IPREP-53 Add-on without Base - CPT Sourcing_00W60_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_66_Wgs_Collection",
            "postman_file_name": "wgs_csbd_RULEADDON00001 IPREP-53 Add-on without Base - CPT Sourcing_00W60.json"
        },
        {
            "ts_number": "67",
            "edit_id": "PSMEM000003_Algo",
            "code": "00W00",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_67_Psm_WGS_CSBD_PSMEM000003_Algo_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_67_Psm_WGS_CSBD_PSMEM000003_Algo_00W00_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_67_Psm_Collection",
            "postman_file_name": "psm_edits_for_emergency_department_facility_new_algo_iprep_364_wgs_csbd_PSMEM000003_Algo_00W00.json"
        },
        {
            "ts_number": "68",
            "edit_id": "RULEANTP000001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_68_Antepartum_WGS_CSBD_RULEANTP000001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_68_Antepartum_WGS_CSBD_RULEANTP000001_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_68_Antepartum_Collection",
            "postman_file_name": "antepartum_services_iprep_337_wgs_csbd_RULEANTP000001_00W28.json"
        },
        {
            "ts_number": "69",
            "edit_id": "RULEINPCC00001",
            "code": "00W45",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_69_Inpatient_WGS_CSBD_RULEINPCC00001_00W45_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_69_Inpatient_WGS_CSBD_RULEINPCC00001_00W45_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_69_Inpatient_Collection",
            "postman_file_name": "inpatient_neonatal_and_pediatric_critical_care_iprep_332_wgs_csbd_RULEINPCC00001_00W45.json"
        },
        {
            "ts_number": "70",
            "edit_id": "RULEPREV000001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_70_Preventative_WGS_CSBD_RULEPREV000001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_70_Preventative_WGS_CSBD_RULEPREV000001_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_70_Preventative_Collection",
            "postman_file_name": "preventative_medicine_and_screening_iprep_362_wgs_csbd_RULEPREV000001_00W28.json"
        },
        {
            "ts_number": "71",
            "edit_id": "RULEOCCH000001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_71_Outpatient_WGS_CSBD_RULEOCCH000001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_71_Outpatient_WGS_CSBD_RULEOCCH000001_00W28_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_71_Outpatient_Collection",
            "postman_file_name": "outpatient_critical_care_to_home_iprep_371_wgs_csbd_RULEOCCH000001_00W28.json"
        },
        {
            "ts_number": "72",
            "edit_id": "RULERECO000003",
            "code": "00W34",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_72_Recovery_WGS_CSBD_RULERECO000003_00W34_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_72_Recovery_WGS_CSBD_RULERECO000003_00W34_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_72_Recovery_Collection",
            "postman_file_name": "recovery_room_rimbursement_iperp_125_wgs_csbd_RULERECO000003_00W34.json"
        },
        {
            "ts_number": "73",
            "edit_id": "RULEEMSD000002",
            "code": "00W09",
            "source_dir": "source_folder/WGS_CSBD/CSBDTS_73_Multiple_WGS_CSBD_RULEEMSD000002_00W09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_73_Multiple_WGS_CSBD_RULEEMSD000002_00W09_dis/payloads/regression",
            "postman_collection_name": "CSBDTS_73_Multiple_Collection",
            "postman_file_name": "multiple_em_same_day_2nd_pass_iprep_224_wgs_csbd_RULEEMSD000002_00W09.json"
        }
    ],
    "gbdf_mcr": [
        {
            "ts_number": "47",
            "edit_id": "RULEEM000001",
            "code": "v04",
            "source_dir": "source_folder/GBDF/TS_47_Covid_gbd_mcr_RULEEM000001_v04_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_47_Covid_gbd_mcr_RULEEM000001_v04_dis/payloads/regression",
            "postman_collection_name": "TS_47_Covid_gbd_mcr_Collection",
            "postman_file_name": "covid_gbd_mcr_RULEEM000001_v04.json"
        },
        {
            "ts_number": "50",
            "edit_id": "RULELATE000001",
            "code": "v17",
            "source_dir": "source_folder/GBDF/GBDTS_50_Laterality_gbd_mcr_RULELATE000001_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_50_Laterality_gbd_mcr_RULELATE000001_v17_dis/payloads/regression",
            "postman_collection_name": "GBDTS_50_Laterality_Collection",
            "postman_file_name": "laterality_policy_diagnosis_to_diagnosis_gbdts_gbd_mcr_RULELATE000001_v17.json"
        },
        {
            "ts_number": "51",
            "edit_id": "PSMEM000001",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/GBDTS_51_Psm_gbd_mcr_PSMEM000001_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_51_Psm_gbd_mcr_PSMEM000001_00W00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_51_Psm_Collection",
            "postman_file_name": "psm_edigbdts_established_patiengbdts_ep_gbdts_gbd_mcr_PSMEM000001_00W00.json"
        },
        {
            "ts_number": "53",
            "edit_id": "PSMEM000002",
            "code": "v00",
            "source_dir": "source_folder/GBDF/GBDTS_53_Psm_gbd_mcr_PSMEM000002_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_53_Psm_gbd_mcr_PSMEM000002_v00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_53_Psm_Collection",
            "postman_file_name": "psm_edit_for_new_patient_visit_type_np_gbdts_gbd_mcr_PSMEM000002_v00.json"
        },
        {
            "ts_number": "55",
            "edit_id": "PSMEM000003",
            "code": "v00",
            "source_dir": "source_folder/GBDF/GBDTS_55_Psm_gbd_mcr_PSMEM000003_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_55_Psm_gbd_mcr_PSMEM000003_v00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_55_Psm_Collection",
            "postman_file_name": "psm_edigbdts_for_emergency_department_personnel_ed_gbdts_gbd_mcr_PSMEM000003_v00.json"
        },
        {
            "ts_number": "57",
            "edit_id": "PSMEM000004",
            "code": "v00",
            "source_dir": "source_folder/GBDF/GBDTS_57_Psm_gbd_mcr_PSMEM000004_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_57_Psm_gbd_mcr_PSMEM000004_v00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_57_Psm_Collection",
            "postman_file_name": "psm_edigbdts_for_emergency_department_facility_er_gbdts_gbd_mcr_PSMEM000004_v00.json"
        },
        {
            "ts_number": "59",
            "edit_id": "RULEMAN000004",
            "code": "v14",
            "source_dir": "source_folder/GBDF/GBDTS_59_Manifestation_gbd_mcr_RULEMAN000004_v14_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_59_Manifestation_gbd_mcr_RULEMAN000004_v14_dis/payloads/regression",
            "postman_collection_name": "GBDTS_59_Manifestation_Collection",
            "postman_file_name": "manifestation_codes_gbdts_gbd_mcr_RULEMAN000004_v14.json"
        },
        {
            "ts_number": "60",
            "edit_id": "RULEUSD00100_Outpt_MCR",
            "code": "v17",
            "source_dir": "source_folder/GBDF/GBDTS_60_Unspecified_gbd_mcr_RULEUSD00100_Outpt_MCR_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_60_Unspecified_gbd_mcr_RULEUSD00100_Outpt_MCR_v17_dis/payloads/regression",
            "postman_collection_name": "GBDTS_60_Unspecified_Collection",
            "postman_file_name": "unspecified_dxcodes_outpt_gbd_mcr_RULEUSD00100_Outpt_MCR_v17.json"
        },
        {
            "ts_number": "62",
            "edit_id": "RULEUSD00100_outpt_MCR",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_62_Unspecified_dx_code_outpt_gbd_mcr_RULEUSD00100_outpt_MCR_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_62_Unspecified_dx_code_outpt_gbd_mcr_RULEUSD00100_outpt_MCR_v17_dis/payloads/regression",
            "postman_collection_name": "TS_62_Unspecified_dx_code_outpt_gbd_mcr_Collection",
            "postman_file_name": "unspecified_dx_code_outpt_gbd_mcr_RULEUSD00100_outpt_MCR_v17.json"
        },
        {
            "ts_number": "63",
            "edit_id": "RULEUSD00100_Prof_MCR",
            "code": "v17",
            "source_dir": "source_folder/GBDF/GBDTS_63_Unspecified_gbd_mcr_RULEUSD00100_Prof_MCR_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_63_Unspecified_gbd_mcr_RULEUSD00100_Prof_MCR_v17_dis/payloads/regression",
            "postman_collection_name": "GBDTS_63_Unspecified_Collection",
            "postman_file_name": "unspecified_dxcodes_prof_mcr_gbdts_gbd_mcr_RULEUSD00100_Prof_MCR_v17.json"
        },
        {
            "ts_number": "64",
            "edit_id": "RULE00000022",
            "code": "v19",
            "source_dir": "source_folder/GBDF/GBDTS_64_Gbdf_gbd_mcr_RULE00000022_v19_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_64_Gbdf_gbd_mcr_RULE00000022_v19_dis/payloads/regression",
            "postman_collection_name": "GBDTS_64_Gbdf_Collection",
            "postman_file_name": "gbdf_mcr_inaccurate_laterality_edit_gbd_mmp_RULE00000022_v19.json"
        },
        {
            "ts_number": "67",
            "edit_id": "RULE00000022",
            "code": "v19",
            "source_dir": "source_folder/GBDF/GBDTS_67_Inaccurate_gbd_mcr_RULE00000022_v19_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_67_Inaccurate_gbd_mcr_RULE00000022_v19_dis/payloads/regression",
            "postman_collection_name": "GBDTS_67_Inaccurate_Collection",
            "postman_file_name": "inaccurate_laterality_edit_gbd_facets_mcr_RULE00000022_v19.json"
        },
        {
            "ts_number": "68",
            "edit_id": "RULE00000376",
            "code": "v16",
            "source_dir": "source_folder/GBDF/GBDTS_68_Inappropriate_gbd_mcr_RULE00000376_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_68_Inappropriate_gbd_mcr_RULE00000376_v16_dis/payloads/regression",
            "postman_collection_name": "GBDTS_68_Inappropriate_Collection",
            "postman_file_name": "inappropriate_primary_diagnosis_gbdts_gbd_mcr_RULE00000376_v16.json"
        },
        {
            "ts_number": "70",
            "edit_id": "RULEALWA000001",
            "code": "v31",
            "source_dir": "source_folder/GBDF/GBDTS_70_Always_gbd_mcr_RULEALWA000001_v31_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_70_Always_gbd_mcr_RULEALWA000001_v31_dis/payloads/regression",
            "postman_collection_name": "GBDTS_70_Always_Collection",
            "postman_file_name": "always_therapy_missing_modifiers_gbdts_gbd_mcr_RULEALWA000001_v31.json"
        },
        {
            "ts_number": "73",
            "edit_id": "RULEEXCL000001",
            "code": "v27",
            "source_dir": "source_folder/GBDF/GBDTS_73_Excludes_gbd_mcr_RULEEXCL000001_v27_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_73_Excludes_gbd_mcr_RULEEXCL000001_v27_dis/payloads/regression",
            "postman_collection_name": "GBDTS_73_Excludes_Collection",
            "postman_file_name": "excludes_1_notes_gbd_mcr_RULEEXCL000001_v27.json"
        },
        {
            "ts_number": "75",
            "edit_id": "RULEEXCL000001",
            "code": "v27",
            "source_dir": "source_folder/GBDF/GBDTS_75_Excludes_gbd_mcr_RULEEXCL000001_v27_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_75_Excludes_gbd_mcr_RULEEXCL000001_v27_dis/payloads/regression",
            "postman_collection_name": "GBDTS_75_Excludes_Collection",
            "postman_file_name": "excludes_1_notes_gbd_facets_mcr_RULEEXCL000001_v27.json"
        },
        {
            "ts_number": "75",
            "edit_id": "RULEANES000001",
            "code": "v32",
            "source_dir": "source_folder/GBDF/GBDTS_75_Anesthesia_gbd_mcr_RULEANES000001_v32_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_75_Anesthesia_gbd_mcr_RULEANES000001_v32_dis/payloads/regression",
            "postman_collection_name": "GBDTS_75_Anesthesia_Collection",
            "postman_file_name": "anesthesia_billed_time_unigbdts_gbdts_gbd_mcr_RULEANES000001_v32.json"
        },
        {
            "ts_number": "77",
            "edit_id": "RULECLIA00001",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/GBDTS_77_Clia_gbd_mcr_RULECLIA00001_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_77_Clia_gbd_mcr_RULECLIA00001_00W00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_77_Clia_Collection",
            "postman_file_name": "clia_edit_gbd_mcr_r92r95r93r90r94r91_RULECLIA00001_00W00.json"
        },
        {
            "ts_number": "79",
            "edit_id": "RULEAMBU000001",
            "code": "v37",
            "source_dir": "source_folder/GBDF/GBDTS_79_Ambulance_gbd_mcr_RULEAMBU000001_v37_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_79_Ambulance_gbd_mcr_RULEAMBU000001_v37_dis/payloads/regression",
            "postman_collection_name": "GBDTS_79_Ambulance_Collection",
            "postman_file_name": "ambulance_mileage_without_base_transport_paid_gbd_mcr_RULEAMBU000001_v37.json"
        },
        {
            "ts_number": "81",
            "edit_id": "RULEAMBU000001",
            "code": "v37",
            "source_dir": "source_folder/GBDF/GBDTS_81_Gbdf_gbd_mcr_RULEAMBU000001_v37_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_81_Gbdf_gbd_mcr_RULEAMBU000001_v37_dis/payloads/regression",
            "postman_collection_name": "GBDTS_81_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_ambulance_mileage_without_base_transport_paid_gbd_mmp_RULEAMBU000001_v37.json"
        },
        {
            "ts_number": "81",
            "edit_id": "Ambulance Mileage without Base Transport Paid IPREP 192",
            "code": "v37",
            "source_dir": "source_folder/GBDF/GBDTS_81_Gbdf_gbd_mcr_Ambulance Mileage without Base Transport Paid IPREP 192_v37_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_81_Gbdf_gbd_mcr_Ambulance Mileage without Base Transport Paid IPREP 192_v37_dis/payloads/regression",
            "postman_collection_name": "GBDTS_81_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_shadow_ruleambu000001_mmp_Ambulance Mileage without Base Transport Paid IPREP 192_v37.json"
        },
        {
            "ts_number": "82",
            "edit_id": "RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBDTS-FaceGBDTS-MCR",
            "code": "v38",
            "source_dir": "source_folder/GBDF/GBDTS_82_Gbdf_gbd_mcr_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBDTS-FaceGBDTS-MCR_v38_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_82_Gbdf_gbd_mcr_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBDTS-FaceGBDTS-MCR_v38_dis/payloads/regression",
            "postman_collection_name": "GBDTS_82_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBDTS-FaceGBDTS-MCR_v38.json"
        },
        {
            "ts_number": "82",
            "edit_id": "RULEIPVT000001",
            "code": "v38",
            "source_dir": "source_folder/GBDF/GBDTS_82_Immunization_gbd_mcr_RULEIPVT000001_v38_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_82_Immunization_gbd_mcr_RULEIPVT000001_v38_dis/payloads/regression",
            "postman_collection_name": "GBDTS_82_Immunization_Collection",
            "postman_file_name": "immunization_procedure_code_without_vaccinetoxoid_gbd_mcr_RULEIPVT000001_v38.json"
        },
        {
            "ts_number": "84",
            "edit_id": "RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBDTS-FaceGBDTS-MCR",
            "code": "v08",
            "source_dir": "source_folder/GBDF/GBDTS_84_Gbdf_gbd_mcr_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBDTS-FaceGBDTS-MCR_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_84_Gbdf_gbd_mcr_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBDTS-FaceGBDTS-MCR_v08_dis/payloads/regression",
            "postman_collection_name": "GBDTS_84_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBDTS-FaceGBDTS-MCR_v08.json"
        },
        {
            "ts_number": "84",
            "edit_id": "RULEIMMU000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/GBDTS_84_Immuno_gbd_mcr_RULEIMMU000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_84_Immuno_gbd_mcr_RULEIMMU000001_v08_dis/payloads/regression",
            "postman_collection_name": "GBDTS_84_Immuno_Collection",
            "postman_file_name": "immuno_drugs_a52474_gbd_mcr_RULEIMMU000001_v08.json"
        },
        {
            "ts_number": "86",
            "edit_id": "RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBDTS-FaceGBDTS-MCR",
            "code": "v08",
            "source_dir": "source_folder/GBDF/GBDTS_86_Gbdf_gbd_mcr_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBDTS-FaceGBDTS-MCR_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_86_Gbdf_gbd_mcr_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBDTS-FaceGBDTS-MCR_v08_dis/payloads/regression",
            "postman_collection_name": "GBDTS_86_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBDTS-FaceGBDTS-MCR_v08.json"
        },
        {
            "ts_number": "86",
            "edit_id": "RULEKNEE000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/GBDTS_86_Knee_gbd_mcr_RULEKNEE000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_86_Knee_gbd_mcr_RULEKNEE000001_v08_dis/payloads/regression",
            "postman_collection_name": "GBDTS_86_Knee_Collection",
            "postman_file_name": "knee_orthosis_a52465_gbd_mcr_RULEKNEE000001_v08.json"
        },
        {
            "ts_number": "89",
            "edit_id": "RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBDTS-FaceGBDTS-MCR",
            "code": "v59",
            "source_dir": "source_folder/GBDF/GBDTS_89_Gbdf_gbd_mcr_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBDTS-FaceGBDTS-MCR_v59_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_89_Gbdf_gbd_mcr_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBDTS-FaceGBDTS-MCR_v59_dis/payloads/regression",
            "postman_collection_name": "GBDTS_89_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBDTS-FaceGBDTS-MCR_v59.json"
        },
        {
            "ts_number": "89",
            "edit_id": "RULEJWME000001",
            "code": "v59",
            "source_dir": "source_folder/GBDF/GBDTS_89_Medical_gbd_mcr_RULEJWME000001_v59_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_89_Medical_gbd_mcr_RULEJWME000001_v59_dis/payloads/regression",
            "postman_collection_name": "GBDTS_89_Medical_Collection",
            "postman_file_name": "medical_injectable_jw_modifier_edit_gbd_mcr_RULEJWME000001_v59.json"
        },
        {
            "ts_number": "91",
            "edit_id": "RULEEM0000012 MNP Model GBDTS-FaceGBDTS-MCR",
            "code": "v07",
            "source_dir": "source_folder/GBDF/GBDTS_91_Gbdf_gbd_mcr_RULEEM0000012 MNP Model GBDTS-FaceGBDTS-MCR_v07_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_91_Gbdf_gbd_mcr_RULEEM0000012 MNP Model GBDTS-FaceGBDTS-MCR_v07_dis/payloads/regression",
            "postman_collection_name": "GBDTS_91_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEEM0000012 MNP Model GBDTS-FaceGBDTS-MCR_v07.json"
        },
        {
            "ts_number": "91",
            "edit_id": "RULEEM0000012",
            "code": "v07",
            "source_dir": "source_folder/GBDF/GBDTS_91_Mnp_gbd_mcr_RULEEM0000012_v07_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_91_Mnp_gbd_mcr_RULEEM0000012_v07_dis/payloads/regression",
            "postman_collection_name": "GBDTS_91_Mnp_Collection",
            "postman_file_name": "mnp_model_gbd_mcr_RULEEM0000012_v07.json"
        },
        {
            "ts_number": "93",
            "edit_id": "RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBDTS-FaceGBDTS-MCR",
            "code": "v09",
            "source_dir": "source_folder/GBDF/GBDTS_93_Gbdf_gbd_mcr_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBDTS-FaceGBDTS-MCR_v09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_93_Gbdf_gbd_mcr_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBDTS-FaceGBDTS-MCR_v09_dis/payloads/regression",
            "postman_collection_name": "GBDTS_93_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBDTS-FaceGBDTS-MCR_v09.json"
        },
        {
            "ts_number": "94",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/GBDTS_94_Multiple_gbd_mcr_RULEEMSD000002_v09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_94_Multiple_gbd_mcr_RULEEMSD000002_v09_dis/payloads/regression",
            "postman_collection_name": "GBDTS_94_Multiple_Collection",
            "postman_file_name": "multiple_em_same_day_2nd_pass_gbd_mcr_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "95",
            "edit_id": "RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBDTS-FaceGBDTS-MCR",
            "code": "v41",
            "source_dir": "source_folder/GBDF/GBDTS_95_Gbdf_gbd_mcr_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBDTS-FaceGBDTS-MCR_v41_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_95_Gbdf_gbd_mcr_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBDTS-FaceGBDTS-MCR_v41_dis/payloads/regression",
            "postman_collection_name": "GBDTS_95_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBDTS-FaceGBDTS-MCR_v41.json"
        },
        {
            "ts_number": "95",
            "edit_id": "RULENDCUOM000001",
            "code": "v41",
            "source_dir": "source_folder/GBDF/GBDTS_95_Ndc_gbd_mcr_RULENDCUOM000001_v41_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_95_Ndc_gbd_mcr_RULENDCUOM000001_v41_dis/payloads/regression",
            "postman_collection_name": "GBDTS_95_Ndc_Collection",
            "postman_file_name": "ndc_uom_validation_edit_expansion_gbd_mcr_RULENDCUOM000001_v41.json"
        },
        {
            "ts_number": "97",
            "edit_id": "RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBDTS-FaceGBDTS-MCR",
            "code": "v40",
            "source_dir": "source_folder/GBDF/GBDTS_97_Gbdf_gbd_mcr_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBDTS-FaceGBDTS-MCR_v40_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_97_Gbdf_gbd_mcr_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBDTS-FaceGBDTS-MCR_v40_dis/payloads/regression",
            "postman_collection_name": "GBDTS_97_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBDTS-FaceGBDTS-MCR_v40.json"
        },
        {
            "ts_number": "97",
            "edit_id": "RULENDC000001",
            "code": "v40",
            "source_dir": "source_folder/GBDF/GBDTS_97_Ndc_gbd_mcr_RULENDC000001_v40_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_97_Ndc_gbd_mcr_RULENDC000001_v40_dis/payloads/regression",
            "postman_collection_name": "GBDTS_97_Ndc_Collection",
            "postman_file_name": "ndc_validation_edit_expansion_gbd_mcr_RULENDC000001_v40.json"
        },
        {
            "ts_number": "99",
            "edit_id": "RULENEBU000001 Nebulizer A52466 IPREP-132 GBDTS-FaceGBDTS-MCR",
            "code": "v08",
            "source_dir": "source_folder/GBDF/GBDTS_99_Gbdf_gbd_mcr_RULENEBU000001 Nebulizer A52466 IPREP-132 GBDTS-FaceGBDTS-MCR_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_99_Gbdf_gbd_mcr_RULENEBU000001 Nebulizer A52466 IPREP-132 GBDTS-FaceGBDTS-MCR_v08_dis/payloads/regression",
            "postman_collection_name": "GBDTS_99_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULENEBU000001 Nebulizer A52466 IPREP-132 GBDTS-FaceGBDTS-MCR_v08.json"
        },
        {
            "ts_number": "101",
            "edit_id": "RULENMP000001 No match of Procedure code GBDTS-FaceGBDTS-MCR",
            "code": "v18",
            "source_dir": "source_folder/GBDF/GBDTS_101_Gbdf_gbd_mcr_RULENMP000001 No match of Procedure code GBDTS-FaceGBDTS-MCR_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_101_Gbdf_gbd_mcr_RULENMP000001 No match of Procedure code GBDTS-FaceGBDTS-MCR_v18_dis/payloads/regression",
            "postman_collection_name": "GBDTS_101_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULENMP000001 No match of Procedure code GBDTS-FaceGBDTS-MCR_v18.json"
        },
        {
            "ts_number": "101",
            "edit_id": "RULENMP000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/GBDTS_101_No_gbd_mcr_RULENMP000001_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_101_No_gbd_mcr_RULENMP000001_v18_dis/payloads/regression",
            "postman_collection_name": "GBDTS_101_No_Collection",
            "postman_file_name": "no_match_of_procedure_code_gbd_mcr_RULENMP000001_v18.json"
        },
        {
            "ts_number": "103",
            "edit_id": "RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBDTS-FaceGBDTS-MCR v08",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/GBDTS_103_Gbdf_gbd_mcr_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBDTS-FaceGBDTS-MCR v08_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_103_Gbdf_gbd_mcr_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBDTS-FaceGBDTS-MCR v08_00W00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_103_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBDTS-FaceGBDTS-MCR v08_00W00.json"
        },
        {
            "ts_number": "105",
            "edit_id": "RULETRAC000001 Trach Supply A52492 IPREP-132 GBDTS-FaceGBDTS-MCR v08",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/GBDTS_105_Gbdf_gbd_mcr_RULETRAC000001 Trach Supply A52492 IPREP-132 GBDTS-FaceGBDTS-MCR v08_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_105_Gbdf_gbd_mcr_RULETRAC000001 Trach Supply A52492 IPREP-132 GBDTS-FaceGBDTS-MCR v08_00W00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_105_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULETRAC000001 Trach Supply A52492 IPREP-132 GBDTS-FaceGBDTS-MCR v08_00W00.json"
        },
        {
            "ts_number": "107",
            "edit_id": "RULERCRO000001 Correct_Coding_Recovery_room GBDTS-FaceGBDTS-MCR",
            "code": "v34",
            "source_dir": "source_folder/GBDF/GBDTS_107_Gbdf_gbd_mcr_RULERCRO000001 Correct_Coding_Recovery_room GBDTS-FaceGBDTS-MCR_v34_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_107_Gbdf_gbd_mcr_RULERCRO000001 Correct_Coding_Recovery_room GBDTS-FaceGBDTS-MCR_v34_dis/payloads/regression",
            "postman_collection_name": "GBDTS_107_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULERCRO000001 Correct_Coding_Recovery_room GBDTS-FaceGBDTS-MCR_v34.json"
        },
        {
            "ts_number": "107",
            "edit_id": "RULERCRO000001",
            "code": "v34",
            "source_dir": "source_folder/GBDF/GBDTS_107_Correct_gbd_mcr_RULERCRO000001_v34_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_107_Correct_gbd_mcr_RULERCRO000001_v34_dis/payloads/regression",
            "postman_collection_name": "GBDTS_107_Correct_Collection",
            "postman_file_name": "correct_coding_recovery_room_gbd_mcr_RULERCRO000001_v34.json"
        },
        {
            "ts_number": "109",
            "edit_id": "RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBDTS_FceGBDTS_MCR",
            "code": "v16",
            "source_dir": "source_folder/GBDF/GBDTS_109_Gbdf_gbd_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBDTS_FceGBDTS_MCR_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_109_Gbdf_gbd_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBDTS_FceGBDTS_MCR_v16_dis/payloads/regression",
            "postman_collection_name": "GBDTS_109_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBDTS_FceGBDTS_MCR_v16.json"
        },
        {
            "ts_number": "110",
            "edit_id": "RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBDTS_FceGBDTS_GRS",
            "code": "v16",
            "source_dir": "source_folder/GBDF/GBDTS_110_Gbdf_gbd_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBDTS_FceGBDTS_GRS_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_110_Gbdf_gbd_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBDTS_FceGBDTS_GRS_v16_dis/payloads/regression",
            "postman_collection_name": "GBDTS_110_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBDTS_FceGBDTS_GRS_v16.json"
        },
        {
            "ts_number": "111",
            "edit_id": "RULEGENE000001",
            "code": "v25",
            "source_dir": "source_folder/GBDF/GBDTS_111_Geneticstesting_gbd_mcr_RULEGENE000001_v25_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_111_Geneticstesting_gbd_mcr_RULEGENE000001_v25_dis/payloads/regression",
            "postman_collection_name": "GBDTS_111_Geneticstesting_Collection",
            "postman_file_name": "geneticstesting_gbdts_gbd_mcr_RULEGENE000001_v25.json"
        },
        {
            "ts_number": "114",
            "edit_id": "RULERCWP000001-Revenue Code without Procedure",
            "code": "v06",
            "source_dir": "source_folder/GBDF/GBDTS_114_Mcr_gbd_mcr_RULERCWP000001-Revenue Code without Procedure_v06_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_114_Mcr_gbd_mcr_RULERCWP000001-Revenue Code without Procedure_v06_dis/payloads/regression",
            "postman_collection_name": "GBDTS_114_Mcr_Collection",
            "postman_file_name": "mcr_RULERCWP000001-Revenue Code without Procedure_v06.json"
        },
        {
            "ts_number": "114",
            "edit_id": "RULERCWP000001",
            "code": "v06",
            "source_dir": "source_folder/GBDF/GBDTS_114_Revenue_gbd_mcr_RULERCWP000001_v06_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_114_Revenue_gbd_mcr_RULERCWP000001_v06_dis/payloads/regression",
            "postman_collection_name": "GBDTS_114_Revenue_Collection",
            "postman_file_name": "revenue_code_without_procedure_gbd_mcr_RULERCWP000001_v06.json"
        },
        {
            "ts_number": "116",
            "edit_id": "RULEPMAM000001 - PRocedures missing  Anatomical Modifier",
            "code": "v31",
            "source_dir": "source_folder/GBDF/GBDTS_116_Mcr_gbd_mcr_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_116_Mcr_gbd_mcr_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31_dis/payloads/regression",
            "postman_collection_name": "GBDTS_116_Mcr_Collection",
            "postman_file_name": "mcr_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31.json"
        },
        {
            "ts_number": "116",
            "edit_id": "RULEPMAM000001",
            "code": "v31",
            "source_dir": "source_folder/GBDF/GBDTS_116_Procedures_gbd_mcr_RULEPMAM000001_v31_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_116_Procedures_gbd_mcr_RULEPMAM000001_v31_dis/payloads/regression",
            "postman_collection_name": "GBDTS_116_Procedures_Collection",
            "postman_file_name": "procedures_missing_anatomical_modifier_gbd_mcr_RULEPMAM000001_v31.json"
        },
        {
            "ts_number": "117",
            "edit_id": "PSMEM000003_algo",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/GBDTS_117_Gbdf_gbd_mcr_PSMEM000003_algo_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_117_Gbdf_gbd_mcr_PSMEM000003_algo_00W00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_117_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_psm_edigbdts_for_emergency_PSMEM000003_algo_00W00.json"
        },
        {
            "ts_number": "119",
            "edit_id": "PSMEM000004_algo",
            "code": "v00",
            "source_dir": "source_folder/GBDF/GBDTS_119_Psm_gbd_mcr_PSMEM000004_algo_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_119_Psm_gbd_mcr_PSMEM000004_algo_v00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_119_Psm_Collection",
            "postman_file_name": "psm_edigbdts_for_emergency_department_facility_new_algo_mcr_PSMEM000004_algo_v00.json"
        },
        {
            "ts_number": "122",
            "edit_id": "RULEEM000002_refdb",
            "code": "v05",
            "source_dir": "source_folder/GBDF/GBDTS_122_Sick_gbd_mcr_RULEEM000002_refdb_v05_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_122_Sick_gbd_mcr_RULEEM000002_refdb_v05_dis/payloads/regression",
            "postman_collection_name": "GBDTS_122_Sick_Collection",
            "postman_file_name": "sick_well_unbundle_grs_mcr_RULEEM000002_refdb_v05.json"
        },
        {
            "ts_number": "126",
            "edit_id": "RULECLIA00001",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/GBDTS_126_Clia_gbd_mcr_RULECLIA00001_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_126_Clia_gbd_mcr_RULECLIA00001_00W00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_126_Clia_Collection",
            "postman_file_name": "clia_edit_for_gbd_mcr_gbd_facets_grs_r92r95r93r90r94r91_RULECLIA00001_00W00.json"
        },
        {
            "ts_number": "144",
            "edit_id": "RULENEBU000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_144_Nebulizer A52466 IPERP-132_gbd_mcr_RULENEBU000001_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_144_Nebulizer A52466 IPERP-132_gbd_mcr_RULENEBU000001_v18_dis/payloads/regression",
            "postman_collection_name": "TS_144_Nebulizer A52466 IPERP-132_gbd_mcr_Collection",
            "postman_file_name": "nebulizer_gbd_mcr_RULENEBU000001_v18.json"
        },
        {
            "ts_number": "148",
            "edit_id": "RULEOSTO000001",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/GBDTS_148_Gbdf_gbd_mcr_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-MCR v08_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_148_Gbdf_gbd_mcr_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-MCR v08_00W00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_148_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-MCR v08_00W00.json"
        },
        {
            "ts_number": "150",
            "edit_id": "RULETRAC000001",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/GBDTS_150_Gbdf_gbd_mcr_RULETRAC000001 Trach Supply A52492​ IPREP-132 GBD-Facets-MCR v08_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_150_Gbdf_gbd_mcr_RULETRAC000001 Trach Supply A52492​ IPREP-132 GBD-Facets-MCR v08_00W00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_150_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULETRAC000001 Trach Supply A52492​ IPREP-132 GBD-Facets-MCR v08_00W00.json"
        },
        {
            "ts_number": "154",
            "edit_id": "RULEIPDXE00001",
            "code": "v16",
            "source_dir": "source_folder/GBDF/GBDTS_154_Gbdf_gbd_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_MCR_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_154_Gbdf_gbd_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_MCR_v16_dis/payloads/regression",
            "postman_collection_name": "GBDTS_154_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_edit_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_MCR_v16.json"
        },
        {
            "ts_number": "155",
            "edit_id": "RULEIPDXE00001",
            "code": "v16",
            "source_dir": "source_folder/GBDF/GBDTS_155_Gbdf_gbd_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_GRS_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_155_Gbdf_gbd_mcr_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_GRS_v16_dis/payloads/regression",
            "postman_collection_name": "GBDTS_155_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEIPDXE00001 IPREP-115 Inappropriate Primary Dxs-Expansion _GBD_Fcets_GRS_v16.json"
        },
        {
            "ts_number": "170",
            "edit_id": "Ambulance Mileage without Base Transport Paid IPREP 192",
            "code": "v37",
            "source_dir": "source_folder/GBDF/GBDTS_170_Gbdf_gbd_mcr_Ambulance Mileage without Base Transport Paid IPREP 192_v37_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_170_Gbdf_gbd_mcr_Ambulance Mileage without Base Transport Paid IPREP 192_v37_dis/payloads/regression",
            "postman_collection_name": "GBDTS_170_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_shadow_ruleambu000001_mmp_v37_edigbdts_group9_Ambulance Mileage without Base Transport Paid IPREP 192_v37.json"
        },
        {
            "ts_number": "171",
            "edit_id": "RULEUSD00100_PROF_MCR",
            "code": "v17",
            "source_dir": "source_folder/GBDF/GBDTS_171_Unspecified_gbd_mcr_RULEUSD00100_PROF_MCR_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_171_Unspecified_gbd_mcr_RULEUSD00100_PROF_MCR_v17_dis/payloads/regression",
            "postman_collection_name": "GBDTS_171_Unspecified_Collection",
            "postman_file_name": "unspecified_dxcodes_outpt_gbd_mcr_RULEUSD00100_PROF_MCR_v17.json"
        },
        {
            "ts_number": "172",
            "edit_id": "RULENEBU000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/GBDTS_172_Nebulizer_gbd_mcr_RULENEBU000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_172_Nebulizer_gbd_mcr_RULENEBU000001_v08_dis/payloads/regression",
            "postman_collection_name": "GBDTS_172_Nebulizer_Collection",
            "postman_file_name": "nebulizer_a52466_gbd_mcr_RULENEBU000001_v08.json"
        },
        {
            "ts_number": "173",
            "edit_id": "RULEOSTO000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/GBDTS_173_Ostomy_gbd_mcr_RULEOSTO000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_173_Ostomy_gbd_mcr_RULEOSTO000001_v08_dis/payloads/regression",
            "postman_collection_name": "GBDTS_173_Ostomy_Collection",
            "postman_file_name": "ostomy_supplies_a52487_gbd_mcr_RULEOSTO000001_v08.json"
        },
        {
            "ts_number": "174",
            "edit_id": "RULETRAC000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/GBDTS_174_Trach_gbd_mcr_RULETRAC000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_174_Trach_gbd_mcr_RULETRAC000001_v08_dis/payloads/regression",
            "postman_collection_name": "GBDTS_174_Trach_Collection",
            "postman_file_name": "trach_supply_a52492_gbd_mcr_v08_RULETRAC000001_v08.json"
        },
        {
            "ts_number": "175",
            "edit_id": "PSMEM000003_algo",
            "code": "v00",
            "source_dir": "source_folder/GBDF/GBDTS_175_Psm_gbd_mcr_PSMEM000003_algo_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/GBDTS_175_Psm_gbd_mcr_PSMEM000003_algo_v00_dis/payloads/regression",
            "postman_collection_name": "GBDTS_175_Psm_Collection",
            "postman_file_name": "psm_for_emergency_department_personnel_new_algo_gbd_mcr_PSMEM000003_algo_v00.json"
        }
    ],
    "gbdf_grs": [
        {
            "ts_number": "48",
            "edit_id": "RULEEM000001",
            "code": "v04",
            "source_dir": "source_folder/GBDF/TS_48_Covid_gbd_grs_RULEEM000001_v04_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_48_Covid_gbd_grs_RULEEM000001_v04_dis/payloads/regression",
            "postman_collection_name": "TS_48_Covid_Collection",
            "postman_file_name": "covid_model_gbdts_gbd_grs_RULEEM000001_v04.json"
        },
        {
            "ts_number": "49",
            "edit_id": "RULELATE000001",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_49_Laterality_gbd_grs_RULELATE000001_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_49_Laterality_gbd_grs_RULELATE000001_v17_dis/payloads/regression",
            "postman_collection_name": "TS_49_Laterality_Collection",
            "postman_file_name": "laterality_policy_diagnosis_to_diagnosis_gbdts_gbd_grs_RULELATE000001_v17.json"
        },
        {
            "ts_number": "52",
            "edit_id": "PSMEM000001",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/TS_52_Psm_gbd_grs_PSMEM000001_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_52_Psm_gbd_grs_PSMEM000001_00W00_dis/payloads/regression",
            "postman_collection_name": "TS_52_Psm_Collection",
            "postman_file_name": "psm_edigbdts_established_patiengbdts_ep_gbdts_gbd_grs_PSMEM000001_00W00.json"
        },
        {
            "ts_number": "54",
            "edit_id": "PSMEM000002",
            "code": "v00",
            "source_dir": "source_folder/GBDF/TS_54_Psm_gbd_grs_PSMEM000002_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_54_Psm_gbd_grs_PSMEM000002_v00_dis/payloads/regression",
            "postman_collection_name": "TS_54_Psm_Collection",
            "postman_file_name": "psm_edit_for_new_patient_visit_type_np_gbdts_gbd_grs_PSMEM000002_v00.json"
        },
        {
            "ts_number": "56",
            "edit_id": "PSMEM000003",
            "code": "v00",
            "source_dir": "source_folder/GBDF/TS_56_Psm_gbd_grs_PSMEM000003_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_56_Psm_gbd_grs_PSMEM000003_v00_dis/payloads/regression",
            "postman_collection_name": "TS_56_Psm_Collection",
            "postman_file_name": "psm_edigbdts_for_emergency_department_personnel_ed_gbdts_gbd_grs_PSMEM000003_v00.json"
        },
        {
            "ts_number": "58",
            "edit_id": "PSMEM000004",
            "code": "v00",
            "source_dir": "source_folder/GBDF/TS_58_Psm_gbd_grs_PSMEM000004_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_58_Psm_gbd_grs_PSMEM000004_v00_dis/payloads/regression",
            "postman_collection_name": "TS_58_Psm_Collection",
            "postman_file_name": "psm_edigbdts_for_emergency_department_facility_er_gbdts_gbd_grs_PSMEM000004_v00.json"
        },
        {
            "ts_number": "61",
            "edit_id": "RULEUSD00100_Outpt_GRS",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_61_Unspecified_gbd_grs_RULEUSD00100_Outpt_GRS_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_61_Unspecified_gbd_grs_RULEUSD00100_Outpt_GRS_v17_dis/payloads/regression",
            "postman_collection_name": "TS_61_Unspecified_Collection",
            "postman_file_name": "unspecified_dxcodes_outpt_gbd_grs_RULEUSD00100_Outpt_GRS_v17.json"
        },
        {
            "ts_number": "62",
            "edit_id": "RULEUSD00100_Prof_GRS",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_62_Unspecified_gbd_grs_RULEUSD00100_Prof_GRS_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_62_Unspecified_gbd_grs_RULEUSD00100_Prof_GRS_v17_dis/payloads/regression",
            "postman_collection_name": "TS_62_Unspecified_Collection",
            "postman_file_name": "unspecified_dxcodes_prof_grs_gbdts_gbd_grs_RULEUSD00100_Prof_GRS_v17.json"
        },
        {
            "ts_number": "63",
            "edit_id": "RULEUSD00100_PROF_GRS",
            "code": "v17",
            "source_dir": "source_folder/GBDF/TS_63_Unspecified_gbd_grs_RULEUSD00100_PROF_GRS_v17_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_63_Unspecified_gbd_grs_RULEUSD00100_PROF_GRS_v17_dis/payloads/regression",
            "postman_collection_name": "TS_63_Unspecified_Collection",
            "postman_file_name": "unspecified_dxcodes_outpt_gbd_grs_RULEUSD00100_PROF_GRS_v17.json"
        },
        {
            "ts_number": "66",
            "edit_id": "RULE00000022",
            "code": "v19",
            "source_dir": "source_folder/GBDF/TS_66_Inaccurate_gbd_grs_RULE00000022_v19_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_66_Inaccurate_gbd_grs_RULE00000022_v19_dis/payloads/regression",
            "postman_collection_name": "TS_66_Inaccurate_Collection",
            "postman_file_name": "inaccurate_laterality_edit_gbdts_gbd_grs_RULE00000022_v19.json"
        },
        {
            "ts_number": "67",
            "edit_id": "RULE00000376",
            "code": "v16",
            "source_dir": "source_folder/GBDF/TS_67_Inappropriate_gbd_grs_RULE00000376_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_67_Inappropriate_gbd_grs_RULE00000376_v16_dis/payloads/regression",
            "postman_collection_name": "TS_67_Inappropriate_Collection",
            "postman_file_name": "inappropriate_primary_diagnosis_gbdts_gbd_grs_RULE00000376_v16.json"
        },
        {
            "ts_number": "69",
            "edit_id": "RULEALWA000001",
            "code": "v31",
            "source_dir": "source_folder/GBDF/TS_69_Always_gbd_grs_RULEALWA000001_v31_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_69_Always_gbd_grs_RULEALWA000001_v31_dis/payloads/regression",
            "postman_collection_name": "TS_69_Always_Collection",
            "postman_file_name": "always_therapy_missing_modifiers_gbdts_gbd_grs_RULEALWA000001_v31.json"
        },
        {
            "ts_number": "72",
            "edit_id": "RULEEXCL000001",
            "code": "v27",
            "source_dir": "source_folder/GBDF/TS_72_Excludes_gbd_grs_RULEEXCL000001_v27_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_72_Excludes_gbd_grs_RULEEXCL000001_v27_dis/payloads/regression",
            "postman_collection_name": "TS_72_Excludes_Collection",
            "postman_file_name": "excludes_1_notes_gbdts_gbd_grs_RULEEXCL000001_v27.json"
        },
        {
            "ts_number": "74",
            "edit_id": "RULEGENE000001",
            "code": "v25",
            "source_dir": "source_folder/GBDF/TS_74_Geneticstesting_gbd_grs_RULEGENE000001_v25_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_74_Geneticstesting_gbd_grs_RULEGENE000001_v25_dis/payloads/regression",
            "postman_collection_name": "TS_74_Geneticstesting_Collection",
            "postman_file_name": "geneticstesting_gbdts_gbd_grs_RULEGENE000001_v25.json"
        },
        {
            "ts_number": "76",
            "edit_id": "RULEANES000001",
            "code": "v32",
            "source_dir": "source_folder/GBDF/TS_76_Anesthesia_gbd_grs_RULEANES000001_v32_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_76_Anesthesia_gbd_grs_RULEANES000001_v32_dis/payloads/regression",
            "postman_collection_name": "TS_76_Anesthesia_Collection",
            "postman_file_name": "anesthesia_billed_time_unigbdts_gbdts_gbd_grs_RULEANES000001_v32.json"
        },
        {
            "ts_number": "78",
            "edit_id": "RULECLIA00001",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/TS_78_Clia_gbd_grs_RULECLIA00001_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_78_Clia_gbd_grs_RULECLIA00001_00W00_dis/payloads/regression",
            "postman_collection_name": "TS_78_Clia_Collection",
            "postman_file_name": "clia_edit_gbd_grs_r92r95r93r90r94r91_RULECLIA00001_00W00.json"
        },
        {
            "ts_number": "80",
            "edit_id": "RULEAMBU000001",
            "code": "v37",
            "source_dir": "source_folder/GBDF/TS_80_Ambulance_gbd_grs_RULEAMBU000001_v37_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_80_Ambulance_gbd_grs_RULEAMBU000001_v37_dis/payloads/regression",
            "postman_collection_name": "TS_80_Ambulance_Collection",
            "postman_file_name": "ambulance_mileage_without_base_transport_paid_gbd_grs_RULEAMBU000001_v37.json"
        },
        {
            "ts_number": "80",
            "edit_id": "Ambulance Mileage without Base Transport Paid IPREP 192",
            "code": "v37",
            "source_dir": "source_folder/GBDF/TS_80_Shadow_gbd_grs_Ambulance Mileage without Base Transport Paid IPREP 192_v37_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_80_Shadow_gbd_grs_Ambulance Mileage without Base Transport Paid IPREP 192_v37_dis/payloads/regression",
            "postman_collection_name": "TS_80_Shadow_Collection",
            "postman_file_name": "shadow_ruleambu000001_grs_Ambulance Mileage without Base Transport Paid IPREP 192_v37.json"
        },
        {
            "ts_number": "83",
            "edit_id": "RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBDTS-FaceGBDTS-GRS",
            "code": "v38",
            "source_dir": "source_folder/GBDF/TS_83_Gbdf_gbd_grs_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBDTS-FaceGBDTS-GRS_v38_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_83_Gbdf_gbd_grs_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBDTS-FaceGBDTS-GRS_v38_dis/payloads/regression",
            "postman_collection_name": "TS_83_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEIPVT000001 Immunization Procedure code without Vaccine/Toxoid GBDTS-FaceGBDTS-GRS_v38.json"
        },
        {
            "ts_number": "83",
            "edit_id": "RULEIPVT000001",
            "code": "v38",
            "source_dir": "source_folder/GBDF/TS_83_Immunization_gbd_grs_RULEIPVT000001_v38_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_83_Immunization_gbd_grs_RULEIPVT000001_v38_dis/payloads/regression",
            "postman_collection_name": "TS_83_Immunization_Collection",
            "postman_file_name": "immunization_procedure_code_without_vaccinetoxoid_gbd_grs_RULEIPVT000001_v38.json"
        },
        {
            "ts_number": "85",
            "edit_id": "RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBDTS-FaceGBDTS-GRS",
            "code": "v08",
            "source_dir": "source_folder/GBDF/TS_85_Gbdf_gbd_grs_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBDTS-FaceGBDTS-GRS_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_85_Gbdf_gbd_grs_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBDTS-FaceGBDTS-GRS_v08_dis/payloads/regression",
            "postman_collection_name": "TS_85_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEIMMU000001 Immuno Drugs A52474 IPREP-132 GBDTS-FaceGBDTS-GRS_v08.json"
        },
        {
            "ts_number": "85",
            "edit_id": "RULEIMMU000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/TS_85_Immuno_gbd_grs_RULEIMMU000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_85_Immuno_gbd_grs_RULEIMMU000001_v08_dis/payloads/regression",
            "postman_collection_name": "TS_85_Immuno_Collection",
            "postman_file_name": "immuno_drugs_a52474_gbd_grs_RULEIMMU000001_v08.json"
        },
        {
            "ts_number": "87",
            "edit_id": "RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBDTS-FaceGBDTS-GRS",
            "code": "v08",
            "source_dir": "source_folder/GBDF/TS_87_Gbdf_gbd_grs_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBDTS-FaceGBDTS-GRS_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_87_Gbdf_gbd_grs_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBDTS-FaceGBDTS-GRS_v08_dis/payloads/regression",
            "postman_collection_name": "TS_87_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEKNEE000001 Knee Orthosis A52465 IPREP-132 GBDTS-FaceGBDTS-GRS_v08.json"
        },
        {
            "ts_number": "87",
            "edit_id": "RULEKNEE000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/TS_87_Knee_gbd_grs_RULEKNEE000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_87_Knee_gbd_grs_RULEKNEE000001_v08_dis/payloads/regression",
            "postman_collection_name": "TS_87_Knee_Collection",
            "postman_file_name": "knee_orthosis_a52465_gbd_grs_RULEKNEE000001_v08.json"
        },
        {
            "ts_number": "88",
            "edit_id": "RULEMAN000004",
            "code": "v14",
            "source_dir": "source_folder/GBDF/TS_88_Manifestation_gbd_grs_RULEMAN000004_v14_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_88_Manifestation_gbd_grs_RULEMAN000004_v14_dis/payloads/regression",
            "postman_collection_name": "TS_88_Manifestation_Collection",
            "postman_file_name": "manifestation_codes_gbdts_gbd_grs_RULEMAN000004_v14.json"
        },
        {
            "ts_number": "90",
            "edit_id": "RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBDTS-FaceGBDTS-GRS",
            "code": "v59",
            "source_dir": "source_folder/GBDF/TS_90_Gbdf_gbd_grs_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBDTS-FaceGBDTS-GRS_v59_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_90_Gbdf_gbd_grs_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBDTS-FaceGBDTS-GRS_v59_dis/payloads/regression",
            "postman_collection_name": "TS_90_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEJWME000001 Medical Injectable EdiGBDTS JW Modifier I-352 GBDTS-FaceGBDTS-GRS_v59.json"
        },
        {
            "ts_number": "90",
            "edit_id": "RULEJWME000001",
            "code": "v59",
            "source_dir": "source_folder/GBDF/TS_90_Medical_gbd_grs_RULEJWME000001_v59_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_90_Medical_gbd_grs_RULEJWME000001_v59_dis/payloads/regression",
            "postman_collection_name": "TS_90_Medical_Collection",
            "postman_file_name": "medical_injectable_jw_modifier_edit_gbd_grs_RULEJWME000001_v59.json"
        },
        {
            "ts_number": "92",
            "edit_id": "RULEEM0000012 MNP Model GBDTS-FaceGBDTS-GRS",
            "code": "v07",
            "source_dir": "source_folder/GBDF/TS_92_Gbdf_gbd_grs_RULEEM0000012 MNP Model GBDTS-FaceGBDTS-GRS_v07_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_92_Gbdf_gbd_grs_RULEEM0000012 MNP Model GBDTS-FaceGBDTS-GRS_v07_dis/payloads/regression",
            "postman_collection_name": "TS_92_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEEM0000012 MNP Model GBDTS-FaceGBDTS-GRS_v07.json"
        },
        {
            "ts_number": "92",
            "edit_id": "RULEEM0000012",
            "code": "v07",
            "source_dir": "source_folder/GBDF/TS_92_Mnp_gbd_grs_RULEEM0000012_v07_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_92_Mnp_gbd_grs_RULEEM0000012_v07_dis/payloads/regression",
            "postman_collection_name": "TS_92_Mnp_Collection",
            "postman_file_name": "mnp_model_gbd_grs_RULEEM0000012_v07.json"
        },
        {
            "ts_number": "94",
            "edit_id": "RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBDTS-FaceGBDTS-GRS",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_94_Gbdf_gbd_grs_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBDTS-FaceGBDTS-GRS_v09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_94_Gbdf_gbd_grs_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBDTS-FaceGBDTS-GRS_v09_dis/payloads/regression",
            "postman_collection_name": "TS_94_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEEMSD000002 Multiple E&M Same Day (2nd pass) GBDTS-FaceGBDTS-GRS_v09.json"
        },
        {
            "ts_number": "96",
            "edit_id": "RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBDTS-FaceGBDTS-GRS",
            "code": "v41",
            "source_dir": "source_folder/GBDF/TS_96_Gbdf_gbd_grs_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBDTS-FaceGBDTS-GRS_v41_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_96_Gbdf_gbd_grs_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBDTS-FaceGBDTS-GRS_v41_dis/payloads/regression",
            "postman_collection_name": "TS_96_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULENDCUOM000001 NDC UOM Validation Edit Expansion IPREP-328 GBDTS-FaceGBDTS-GRS_v41.json"
        },
        {
            "ts_number": "96",
            "edit_id": "RULENDCUOM000001",
            "code": "v41",
            "source_dir": "source_folder/GBDF/TS_96_Ndc_gbd_grs_RULENDCUOM000001_v41_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_96_Ndc_gbd_grs_RULENDCUOM000001_v41_dis/payloads/regression",
            "postman_collection_name": "TS_96_Ndc_Collection",
            "postman_file_name": "ndc_uom_validation_edit_expansion_gbd_grs_RULENDCUOM000001_v41.json"
        },
        {
            "ts_number": "98",
            "edit_id": "RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBDTS-FaceGBDTS-GRS",
            "code": "v40",
            "source_dir": "source_folder/GBDF/TS_98_Gbdf_gbd_grs_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBDTS-FaceGBDTS-GRS_v40_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_98_Gbdf_gbd_grs_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBDTS-FaceGBDTS-GRS_v40_dis/payloads/regression",
            "postman_collection_name": "TS_98_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULENDC000001 NDC Validation Edit Expansion IPREP-296 GBDTS-FaceGBDTS-GRS_v40.json"
        },
        {
            "ts_number": "98",
            "edit_id": "RULENDC000001",
            "code": "v40",
            "source_dir": "source_folder/GBDF/TS_98_Ndc_gbd_grs_RULENDC000001_v40_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_98_Ndc_gbd_grs_RULENDC000001_v40_dis/payloads/regression",
            "postman_collection_name": "TS_98_Ndc_Collection",
            "postman_file_name": "ndc_validation_edit_expansion_gbd_grs_RULENDC000001_v40.json"
        },
        {
            "ts_number": "100",
            "edit_id": "RULENEBU000001 Nebulizer A52466 IPREP-132 GBDTS-FaceGBDTS-GRS",
            "code": "v08",
            "source_dir": "source_folder/GBDF/TS_100_Gbdf_gbd_grs_RULENEBU000001 Nebulizer A52466 IPREP-132 GBDTS-FaceGBDTS-GRS_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_100_Gbdf_gbd_grs_RULENEBU000001 Nebulizer A52466 IPREP-132 GBDTS-FaceGBDTS-GRS_v08_dis/payloads/regression",
            "postman_collection_name": "TS_100_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULENEBU000001 Nebulizer A52466 IPREP-132 GBDTS-FaceGBDTS-GRS_v08.json"
        },
        {
            "ts_number": "102",
            "edit_id": "RULENMP000001 No match of Procedure code GBDTS-FaceGBDTS-GRS",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_102_Gbdf_gbd_grs_RULENMP000001 No match of Procedure code GBDTS-FaceGBDTS-GRS_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_102_Gbdf_gbd_grs_RULENMP000001 No match of Procedure code GBDTS-FaceGBDTS-GRS_v18_dis/payloads/regression",
            "postman_collection_name": "TS_102_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULENMP000001 No match of Procedure code GBDTS-FaceGBDTS-GRS_v18.json"
        },
        {
            "ts_number": "102",
            "edit_id": "RULENMP000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_102_No_gbd_grs_RULENMP000001_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_102_No_gbd_grs_RULENMP000001_v18_dis/payloads/regression",
            "postman_collection_name": "TS_102_No_Collection",
            "postman_file_name": "no_match_of_procedure_code_gbd_grs_RULENMP000001_v18.json"
        },
        {
            "ts_number": "104",
            "edit_id": "RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBDTS-FaceGBDTS-GRS v08",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/TS_104_Gbdf_gbd_grs_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBDTS-FaceGBDTS-GRS v08_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_104_Gbdf_gbd_grs_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBDTS-FaceGBDTS-GRS v08_00W00_dis/payloads/regression",
            "postman_collection_name": "TS_104_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBDTS-FaceGBDTS-GRS v08_00W00.json"
        },
        {
            "ts_number": "106",
            "edit_id": "RULETRAC000001 Trach Supply A52492 IPREP-132 GBDTS-FaceGBDTS-GRS",
            "code": "v08",
            "source_dir": "source_folder/GBDF/TS_106_Gbdf_gbd_grs_RULETRAC000001 Trach Supply A52492 IPREP-132 GBDTS-FaceGBDTS-GRS_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_106_Gbdf_gbd_grs_RULETRAC000001 Trach Supply A52492 IPREP-132 GBDTS-FaceGBDTS-GRS_v08_dis/payloads/regression",
            "postman_collection_name": "TS_106_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULETRAC000001 Trach Supply A52492 IPREP-132 GBDTS-FaceGBDTS-GRS_v08.json"
        },
        {
            "ts_number": "106",
            "edit_id": "RULETRAC000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/TS_106_Trach_gbd_grs_RULETRAC000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_106_Trach_gbd_grs_RULETRAC000001_v08_dis/payloads/regression",
            "postman_collection_name": "TS_106_Trach_Collection",
            "postman_file_name": "trach_supply_a52492_gbd_grs_v08_RULETRAC000001_v08.json"
        },
        {
            "ts_number": "108",
            "edit_id": "RULERCRO000001 Correct_Coding_Recovery_room GBDTS-FaceGBDTS-GRS",
            "code": "v34",
            "source_dir": "source_folder/GBDF/TS_108_Gbdf_gbd_grs_RULERCRO000001 Correct_Coding_Recovery_room GBDTS-FaceGBDTS-GRS_v34_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_108_Gbdf_gbd_grs_RULERCRO000001 Correct_Coding_Recovery_room GBDTS-FaceGBDTS-GRS_v34_dis/payloads/regression",
            "postman_collection_name": "TS_108_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULERCRO000001 Correct_Coding_Recovery_room GBDTS-FaceGBDTS-GRS_v34.json"
        },
        {
            "ts_number": "108",
            "edit_id": "RULERCRO000001",
            "code": "v34",
            "source_dir": "source_folder/GBDF/TS_108_Correct_gbd_grs_RULERCRO000001_v34_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_108_Correct_gbd_grs_RULERCRO000001_v34_dis/payloads/regression",
            "postman_collection_name": "TS_108_Correct_Collection",
            "postman_file_name": "correct_coding_recovery_room_gbd_grs_RULERCRO000001_v34.json"
        },
        {
            "ts_number": "110",
            "edit_id": "RULEIPDXE00001",
            "code": "v16",
            "source_dir": "source_folder/GBDF/TS_110_Inappropriate_gbd_grs_RULEIPDXE00001_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_110_Inappropriate_gbd_grs_RULEIPDXE00001_v16_dis/payloads/regression",
            "postman_collection_name": "TS_110_Inappropriate_Collection",
            "postman_file_name": "inappropriate_primary_dxs_expansion_gbd_grs_RULEIPDXE00001_v16.json"
        },
        {
            "ts_number": "112",
            "edit_id": "RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBDTS-FaceGBDTS-GRS",
            "code": "v16",
            "source_dir": "source_folder/GBDF/TS_112_Gbdf_gbd_grs_RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBDTS-FaceGBDTS-GRS_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_112_Gbdf_gbd_grs_RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBDTS-FaceGBDTS-GRS_v16_dis/payloads/regression",
            "postman_collection_name": "TS_112_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEIPDXH00001 Inappropriate_Primary_DX_PROF_HEADER_GBDTS-FaceGBDTS-GRS_v16.json"
        },
        {
            "ts_number": "112",
            "edit_id": "RULEIPDXH00001",
            "code": "v16",
            "source_dir": "source_folder/GBDF/TS_112_Inappropriate_gbd_grs_RULEIPDXH00001_v16_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_112_Inappropriate_gbd_grs_RULEIPDXH00001_v16_dis/payloads/regression",
            "postman_collection_name": "TS_112_Inappropriate_Collection",
            "postman_file_name": "inappropriate_primary_dx_prof_header_gbd_grs_RULEIPDXH00001_v16.json"
        },
        {
            "ts_number": "113",
            "edit_id": "RULERCWP000001-Revenue Code without Procedure",
            "code": "v06",
            "source_dir": "source_folder/GBDF/TS_113_Grs_gbd_grs_RULERCWP000001-Revenue Code without Procedure_v06_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_113_Grs_gbd_grs_RULERCWP000001-Revenue Code without Procedure_v06_dis/payloads/regression",
            "postman_collection_name": "TS_113_Grs_Collection",
            "postman_file_name": "grs_RULERCWP000001-Revenue Code without Procedure_v06.json"
        },
        {
            "ts_number": "113",
            "edit_id": "RULERCWP000001",
            "code": "v06",
            "source_dir": "source_folder/GBDF/TS_113_Revenue_gbd_grs_RULERCWP000001_v06_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_113_Revenue_gbd_grs_RULERCWP000001_v06_dis/payloads/regression",
            "postman_collection_name": "TS_113_Revenue_Collection",
            "postman_file_name": "revenue_code_without_procedure_gbd_grs_RULERCWP000001_v06.json"
        },
        {
            "ts_number": "115",
            "edit_id": "RULEPMAM000001 - PRocedures missing  Anatomical Modifier",
            "code": "v31",
            "source_dir": "source_folder/GBDF/TS_115_Grs_gbd_grs_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_115_Grs_gbd_grs_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31_dis/payloads/regression",
            "postman_collection_name": "TS_115_Grs_Collection",
            "postman_file_name": "grs_RULEPMAM000001 - PRocedures missing  Anatomical Modifier_v31.json"
        },
        {
            "ts_number": "115",
            "edit_id": "RULEPMAM000001",
            "code": "v31",
            "source_dir": "source_folder/GBDF/TS_115_Procedures_gbd_grs_RULEPMAM000001_v31_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_115_Procedures_gbd_grs_RULEPMAM000001_v31_dis/payloads/regression",
            "postman_collection_name": "TS_115_Procedures_Collection",
            "postman_file_name": "procedures_missing_anatomical_modifier_gbd_grs_RULEPMAM000001_v31.json"
        },
        {
            "ts_number": "118",
            "edit_id": "PSMEM000003_algo",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/TS_118_Gbdf_gbd_grs_PSMEM000003_algo_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_118_Gbdf_gbd_grs_PSMEM000003_algo_00W00_dis/payloads/regression",
            "postman_collection_name": "TS_118_Gbdf_Collection",
            "postman_file_name": "gbd_mcr_psm_edigbdts_for_emergency_PSMEM000003_algo_00W00.json"
        },
        {
            "ts_number": "120",
            "edit_id": "PSMEM000004_algo",
            "code": "v00",
            "source_dir": "source_folder/GBDF/TS_120_Psm_gbd_grs_PSMEM000004_algo_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_120_Psm_gbd_grs_PSMEM000004_algo_v00_dis/payloads/regression",
            "postman_collection_name": "TS_120_Psm_Collection",
            "postman_file_name": "psm_edigbdts_for_emergency_department_facility_new_algo_grs_PSMEM000004_algo_v00.json"
        },
        {
            "ts_number": "122",
            "edit_id": "RULEEM000002_refdb",
            "code": "v05",
            "source_dir": "source_folder/GBDF/TS_122_Sick_gbd_grs_RULEEM000002_refdb_v05_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_122_Sick_gbd_grs_RULEEM000002_refdb_v05_dis/payloads/regression",
            "postman_collection_name": "TS_122_Sick_Collection",
            "postman_file_name": "sick_well_unbundle_grs_RULEEM000002_refdb_v05.json"
        },
        {
            "ts_number": "139",
            "edit_id": "RULEEMSD000002",
            "code": "v09",
            "source_dir": "source_folder/GBDF/TS_139_Multiple E&M Same day_gbd_grs_RULEEMSD000002_v09_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_139_Multiple E&M Same day_gbd_grs_RULEEMSD000002_v09_dis/payloads/regression",
            "postman_collection_name": "TS_139_Multiple E&M Same day_gbd_grs_Collection",
            "postman_file_name": "multiple_em_gbd_grs_RULEEMSD000002_v09.json"
        },
        {
            "ts_number": "145",
            "edit_id": "RULENEBU000001",
            "code": "v18",
            "source_dir": "source_folder/GBDF/TS_145_Nebulizer A52466 IPERP-132_gbd_grs_RULENEBU000001_v18_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_145_Nebulizer A52466 IPERP-132_gbd_grs_RULENEBU000001_v18_dis/payloads/regression",
            "postman_collection_name": "TS_145_Nebulizer A52466 IPERP-132_gbd_grs_Collection",
            "postman_file_name": "nebulizer_gbd_grs_RULENEBU000001_v18.json"
        },
        {
            "ts_number": "149",
            "edit_id": "RULEOSTO000001",
            "code": "00W00",
            "source_dir": "source_folder/GBDF/TS_149_Gbdf_gbd_grs_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-GRS v08_00W00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_149_Gbdf_gbd_grs_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-GRS v08_00W00_dis/payloads/regression",
            "postman_collection_name": "TS_149_Gbdf_Collection",
            "postman_file_name": "gbd_grs_edit_RULEOSTO000001 Ostomy Supplies A52487 IPREP-132 GBD-Facets-GRS v08_00W00.json"
        },
        {
            "ts_number": "150",
            "edit_id": "RULENEBU000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/TS_150_Nebulizer_gbd_grs_RULENEBU000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_150_Nebulizer_gbd_grs_RULENEBU000001_v08_dis/payloads/regression",
            "postman_collection_name": "TS_150_Nebulizer_Collection",
            "postman_file_name": "nebulizer_a52466_gbd_grs_RULENEBU000001_v08.json"
        },
        {
            "ts_number": "151",
            "edit_id": "RULEOSTO000001",
            "code": "v08",
            "source_dir": "source_folder/GBDF/TS_151_Ostomy_gbd_grs_RULEOSTO000001_v08_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_151_Ostomy_gbd_grs_RULEOSTO000001_v08_dis/payloads/regression",
            "postman_collection_name": "TS_151_Ostomy_Collection",
            "postman_file_name": "ostomy_supplies_a52487_gbd_grs_RULEOSTO000001_v08.json"
        },
        {
            "ts_number": "152",
            "edit_id": "PSMEM000003_algo",
            "code": "v00",
            "source_dir": "source_folder/GBDF/TS_152_Psm_gbd_grs_PSMEM000003_algo_v00_sur/payloads/regression",
            "dest_dir": "renaming_jsons/GBDTS/TS_152_Psm_gbd_grs_PSMEM000003_algo_v00_dis/payloads/regression",
            "postman_collection_name": "TS_152_Psm_Collection",
            "postman_file_name": "psm_for_emergency_department_personnel_new_algo_gbd_grs_PSMEM000003_algo_v00.json"
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
        },
        {
            "ts_number": "150",
            "edit_id": "RULEINPCC00001",
            "code": "00W45",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_150_Inpatient_WGS_NYK_RULEINPCC00001_00W45_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_150_Inpatient_WGS_NYK_RULEINPCC00001_00W45_dis/payloads/regression",
            "postman_collection_name": "NYKTS_150_Inpatient_Collection",
            "postman_file_name": "inpatient_neonatal_and_pediatric_critical_care_iprep_332_wgs_nyk_RULEINPCC00001_00W45.json"
        },
        {
            "ts_number": "151",
            "edit_id": "RULEPREV000001",
            "code": "00W28",
            "source_dir": "source_folder/WGS_Kernal/NYKTS_151_Preventative_WGS_NYK_RULEPREV000001_00W28_sur/payloads/regression",
            "dest_dir": "renaming_jsons/NYKTS/NYKTS_151_Preventative_WGS_NYK_RULEPREV000001_00W28_dis/payloads/regression",
            "postman_collection_name": "NYKTS_151_Preventative_Collection",
            "postman_file_name": "preventative_medicine_and_screening_iprep_362_wgs_nyk_RULEPREV000001_00W28.json"
        }
    ]
}

# Dynamic model discovery
def get_models_config(use_dynamic=True, use_wgs_csbd_destination=False, use_gbd_mcr=False, use_gbd_grs=False, use_wgs_nyk=False):
    """
    Get model configurations using dynamic discovery or static config.

    Args:
        use_dynamic: If True, use dynamic discovery; if False, use static config
        use_wgs_csbd_destination: If True, use WGS_CSBD as destination folder instead of renaming_jsons
        use_gbd_mcr: If True, use GBDF MCR models instead of WGS_CSBD
        use_gbd_grs: If True, use GBDF GRS models instead of WGS_CSBD
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
            elif use_gbd_mcr:
                # Use dynamic discovery for GBDF MCR
                discovered_models = discover_ts_folders("source_folder/GBDF", False)
                # Filter for MCR models only (exclude GRS)
                # Use source_dir as primary check since it always exists and contains the folder path
                # Also check folder_name as fallback for robustness
                mcr_models = [
                    m for m in discovered_models 
                    if ("gbd_mcr" in m.get("source_dir", "").lower() or "gbd_mcr" in m.get("folder_name", "").lower())
                    and "gbd_grs" not in m.get("source_dir", "").lower() 
                    and "gbd_grs" not in m.get("folder_name", "").lower()
                ]
                if mcr_models:
                    print(f"Dynamic discovery found {len(mcr_models)} GBDF MCR models")
                    return mcr_models
                else:
                    print("No GBDF MCR models found via dynamic discovery, falling back to static config")
                    return STATIC_MODELS_CONFIG.get("gbd_mcr", [])
            elif use_gbd_grs:
                # Use dynamic discovery for GBDF GRS
                discovered_models = discover_ts_folders("source_folder/GBDF", False)
                # Filter for GRS models only
                # Use source_dir as primary check since it always exists and contains the folder path
                # Also check folder_name as fallback for robustness
                grs_models = [
                    m for m in discovered_models 
                    if "gbd_grs" in m.get("source_dir", "").lower() or "gbd_grs" in m.get("folder_name", "").lower()
                ]
                if grs_models:
                    print(f"Dynamic discovery found {len(grs_models)} GBDF GRS models")
                    return grs_models
                else:
                    print("No GBDF GRS models found via dynamic discovery, falling back to static config")
                    return STATIC_MODELS_CONFIG.get("gbd_grs", [])
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
            elif use_gbd_mcr:
                return STATIC_MODELS_CONFIG.get("gbd_mcr", [])
            elif use_gbd_grs:
                return STATIC_MODELS_CONFIG.get("gbd_grs", [])
            else:
                return STATIC_MODELS_CONFIG.get("wgs_csbd", [])
    else:
        if use_wgs_nyk:
            return STATIC_MODELS_CONFIG.get("wgs_kernal", [])
        elif use_gbd_mcr:
            return STATIC_MODELS_CONFIG.get("gbd_mcr", [])
        elif use_gbd_grs:
            return STATIC_MODELS_CONFIG.get("gbd_grs", [])
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


def apply_header_footer_to_json(file_path, is_wgs_kernal=False):
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
    - meta-transid: WGS_Kernal uses "20240705012036TMBLMMY437A003580999CS90TIMBER01",
                   WGS_CSBD uses "20220117181853TMBL20359Cl893580999"
    - protegrity / Protigrity: "false" (for WGS_Kernal and WGS_CSBD models)
    
    Args:
        file_path: Path to the JSON file to transform
        is_wgs_kernal: If True, use WGS_Kernal meta-transid; else use WGS_CSBD meta-transid
        
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
        
        # meta-transid: WGS_Kernal uses dedicated value; WGS_CSBD uses legacy value
        meta_transid = "20240705012036TMBLMMY437A003580999CS90TIMBER01" if is_wgs_kernal else "20220117181853TMBL20359Cl893580999"
        # Header and footer structure (always use these values)
        header_footer = {
            "adhoc": "true",
            "analyticId": " ",
            "hints": ["congnitive_claims_async"],
            "responseRequired": "false",
            "meta-src-envrmt": "IMST",
            "meta-transid": meta_transid,
            "protegrity": "false",
            "Protigrity": "false"
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
                "meta-transid": header_footer["meta-transid"],
                "protegrity": header_footer["protegrity"],
                "Protigrity": header_footer["Protigrity"]
            }
            
            # Preserve any additional fields that might exist
            for key, value in existing_data.items():
                if key not in ["adhoc", "analyticId", "hints", "payload", "responseRequired", "meta-src-envrmt", "meta-transid", "protegrity", "Protigrity"]:
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
                "meta-transid": header_footer["meta-transid"],
                "protegrity": header_footer["protegrity"],
                "Protigrity": header_footer["Protigrity"]
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
        is_wgs_kernal = "WGS_KERNAL" in target_dir.upper()
        for root, dirs, files in os.walk(target_dir):
            for filename in files:
                if filename.endswith('.json'):
                    file_path = os.path.join(root, filename)
                    
                    # Apply header/footer (function will handle both new and existing structures)
                    if apply_header_footer_to_json(file_path, is_wgs_kernal=is_wgs_kernal):
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
