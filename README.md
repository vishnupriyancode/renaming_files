# File Renaming Project with Postman Collection Generation

A Python script for automatically renaming and organizing test case JSON files based on predefined naming conventions and suffix mappings, with integrated Postman collection generation for API testing.

## 🔧 Recent Updates & Fixes

**✅ WGS_NYK Model Support (Latest Update)**

The project has been enhanced with support for WGS_NYK (Working Group Standards - New York Kernal) models:

- **✅ Added WGS_NYK Support**: Observation Services WGS NYK models (TS122-TS130, TS132)
- **✅ Custom Command Format**: WGS_NYK models require `--NYKTSXX` format (e.g., `--NYKTS130`) instead of `--TSXX` format
- **✅ Updated Command Line Interface**: Added `--wgs_nyk` flag and `--NYKTSXX` arguments for WGS_NYK processing
- **✅ Enhanced Documentation**: Updated all examples and help text to include WGS_NYK models
- **✅ Error Handling**: Added proper validation and error messages for WGS_NYK flag usage
- **✅ Postman Collection Generation**: Automatic collection generation with proper naming (NYKTS_XX_Observation_Services_Collection)
- **✅ Excel Reporting**: Integrated timing tracking and performance analytics
- **✅ Dynamic Discovery**: Automatic detection of NYKTS folders and model parameters

**Examples:**
```bash
# WGS_NYK models (must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS122   # Process TS122 model (Revenue code to HCPCS Alignment edit WGS NYK)
python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS124   # Process TS124 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS132   # Process TS132 model (add_on without base WGS NYK)
python main_processor.py --wgs_nyk --all     # Process all 10 WGS_NYK models
```

**✅ GBDF Model Command Format Update**

The project now supports the new `--GBDTSXX` format for all GBDF MCR models (similar to `--CSBDTSXX` for WGS_CSBD models):

- **✅ New --GBDTSXX Format**: All GBDF MCR models now support the required `--GBDTSXX` format (e.g., `--GBDTS47`, `--GBDTS48`, `--GBDTS138`)
- **✅ Consistent Command Structure**: GBDF models now follow the same pattern as WGS_CSBD models for consistency
- **✅ Legacy Format Removed**: Legacy `--TSXX` format is no longer supported for GBDF MCR models - use `--GBDTSXX` format instead
- **✅ Dynamic Discovery Fix**: Fixed dynamic discovery to correctly handle GBDF models with `payloads/regression` folder structure
- **✅ Static Config Update**: Updated all GBDF model source paths to include `/payloads/` in the path
- **✅ Comprehensive Documentation**: Updated all README examples to use the new `--GBDTSXX` format

**Examples:**
```bash
# Recommended format (new)
python main_processor.py --gbdf_mcr --GBDTS47    # Process TS47 model (Covid GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS48    # Process TS48 model (Multiple E&M Same day GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS138   # Process TS138 model (Multiple E&M Same day GBDF MCR)

```

**✅ Excel Reporting System**

The project has been enhanced with comprehensive Excel reporting functionality:

- **✅ Automatic Timing Tracking**: Tracks timing for file renaming and Postman collection generation
- **✅ Professional Excel Reports**: Generates detailed Excel reports with timing data and statistics
- **✅ Multiple Report Formats**: Supports individual model reports and batch processing reports
- **✅ Performance Analytics**: Calculates total time, average time, and performance metrics
- **✅ Report Management**: Automatic report generation with timestamps and status tracking
- **✅ Enhanced Documentation**: Added Excel Reporting Guide and File Connections Demo Guide
- **✅ Backward Compatibility**: All existing functionality remains unchanged

**✅ TS20 Model Support (Latest Update)**

The project has been enhanced with support for the TS20 RadioservicesbilledwithoutRadiopharma model:

- **✅ Added TS20 Support**: RadioservicesbilledwithoutRadiopharma WGS_CSBD model
- **✅ Custom Model Configuration**: Special handling for TS20 with RULERBWR000001 edit ID
- **✅ Updated Command Line Interface**: Added --CSBDTS20 argument for WGS_CSBD processing
- **✅ Enhanced Documentation**: Updated examples and help text to include TS20 model
- **✅ Error Handling**: Added proper validation and error messages for TS20 flag usage
- **✅ Postman Collection Generation**: Automatic collection generation with proper naming
- **✅ Excel Reporting**: Integrated timing tracking and performance analytics

**✅ CSBD_TS48 Model Support**

The project has been enhanced with support for the CSBD_TS48 Revenue code to HCPCS Alignment edit model:

- **✅ Added CSBD_TS48 Support**: Revenue code to HCPCS Alignment edit WGS_CSBD model
- **✅ Custom Model Configuration**: Special handling for CSBD_TS48 with RULERCTH00001 edit ID
- **✅ Updated Command Line Interface**: Added --CSBDTS48 argument (no underscore) for WGS_CSBD processing
- **✅ Enhanced Documentation**: Updated examples and help text to include CSBD_TS48 model
- **✅ Error Handling**: Added proper validation and error messages for CSBDTS48 flag usage
- **✅ Postman Collection Generation**: Automatic collection generation with proper naming
- **✅ Excel Reporting**: Integrated timing tracking and performance analytics

**✅ TS140, TS141, TS146, TS147 Model Support**

The project has been enhanced with support for additional GBDF models:

- **✅ Added TS140 Support**: NDC UOM Validation Edit Expansion Iprep-138 GBDF MCR model
- **✅ Added TS141 Support**: NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS model  
- **✅ Added TS146 Support**: No match of Procedure code GBDF MCR model
- **✅ Added TS147 Support**: No match of Procedure code GBDF GRS model
- **✅ Enhanced Dynamic Discovery**: Updated patterns and regex matching for new model types
- **✅ Updated Command Line Interface**: Added --GBDTS140, --GBDTS146 arguments for GBDF MCR and --TS141, --TS147 arguments for GBDF GRS
- **✅ Comprehensive Documentation**: Updated all examples and help text to include new models
- **✅ Error Handling**: Added proper validation and error messages for new model flags

**✅ GBDF_GRS Flag Implementation**

The project has been enhanced with support for GBDF GRS (Global Research Standards) models:

- **✅ Added --gbdf_grs Flag**: New command-line flag for processing GBDF GRS models
- **✅ TS49 Model Support**: TS49 model now requires --gbdf_grs flag instead of --gbdf_mcr
- **✅ Updated Model Configuration**: Enhanced models_config.py to support GBDF GRS parameter
- **✅ Comprehensive Documentation**: Updated all examples and help text to include --gbdf_grs flag
- **✅ Error Handling**: Added proper validation and error messages for GBDF GRS flag usage
- **✅ Backward Compatibility**: All existing functionality remains unchanged

**✅ WGS_CSBD Header/Footer Integration with KEY_CHK_CDN_NBR Generator**

The project has been enhanced with automatic header/footer transformation for WGS_CSBD files:

- **✅ Integrated Header/Footer Transformation**: WGS_CSBD files automatically get header/footer structure during renaming process
- **✅ KEY_CHK_CDN_NBR Generator**: Automatically generates random 11-digit numbers for KEY_CHK_CDN_NBR fields in both root and payload levels
- **✅ Smart Field Updates**: Updates existing KEY_CHK_CDN_NBR values with new random numbers during processing
- **✅ Selective Application**: Only WGS_CSBD files are transformed; GBDF files remain unchanged
- **✅ Seamless Integration**: Transformation happens automatically during the renaming workflow
- **✅ Preserved Workflow**: Existing GBDF and other workflows remain completely unaffected

**✅ WGS_CSBD Flag Implementation & Command Structure Update**

The project has been enhanced with comprehensive improvements:

- **✅ WGS_CSBD Flag Requirement**: Added mandatory `--wgs_csbd` flag for all TS model processing
- **✅ Enhanced Command Validation**: Improved error handling and user guidance
- **✅ Dynamic Model Discovery**: Automatic detection of TS folders and model parameters
- **✅ Modular Architecture**: Clean separation of concerns with dedicated modules
- **✅ Multiple Entry Points**: Both integrated (`main_processor.py`) and standalone (`postman_cli.py`) interfaces
- **✅ Professional Collections**: Generated collections with proper naming and structure
- **✅ Comprehensive Documentation**: Added architecture diagram and detailed explanations

### Current Project Structure:
```
postman_collections/
├── WGS_CSBD/                                    # WGS_CSBD Collections
│   ├── TS_01_Covid_Collection/postman_collection.json
│   ├── TS_02_Laterality_Collection/postman_collection.json
│   ├── TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_Collection/
│   ├── TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_Collection/
│   ├── TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_Collection/
│   ├── TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_Collection/
│   ├── TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_Collection/
│   ├── TS_08_Lab panel Model_Collection/
│   ├── TS_09_Device Dependent Procedures_Collection/
│   ├── TS_10_Recovery Room Reimbursement_Collection/
│   ├── TS_11_Revenue Code to HCPCS Xwalk-1B_Collection/
│   ├── TS_12_Incidentcal Services Facility_Collection/
│   ├── TS_13_Revenue model CR v3_Collection/
│   ├── TS_14_HCPCS to Revenue Code Xwalk_Collection/
│   ├── TS_15_revenue model_Collection/
│   ├── TS_20_RadioservicesbilledwithoutRadiopharma_Collection/
│   ├── TS_46_Multiple E&M Same day_Collection/
│   ├── TS_47_Multiple Billing of Obstetrical Services_Collection/
│   ├── CSBD_TS_48_Revenue code to HCPCS Alignment edit_Collection/
│   ├── CSBDTS_49_Observation_Services_Collection/
│   ├── CSBDTS_50_Observation_Services_Collection/
│   ├── CSBDTS_51_Observation_Services_Collection/
│   ├── CSBDTS_52_Observation_Services_Collection/
│   ├── CSBDTS_53_Observation_Services_Collection/
│   ├── CSBDTS_54_Observation_Services_Collection/
│   ├── CSBDTS_55_Observation_Services_Collection/
│   └── CSBDTS_56_Observation_Services_Collection/
├── GBDF/                                        # GBDF MCR Collections
│   ├── TS_47_Covid_gbdf_mcr_Collection/
│   ├── TS_48_Multiple E&M Same day_gbdf_mcr_Collection/
│   ├── TS_138_Multiple E&M Same day_gbdf_mcr_Collection/
│   ├── TS_139_Multiple E&M Same day_gbdf_grs_Collection/
│   ├── TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_Collection/
│   ├── TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_Collection/
│   ├── TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_Collection/
│   ├── TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_Collection/
│   ├── TS_146_No match of Procedure code_gbdf_mcr_Collection/
│   └── TS_147_No match of Procedure code_gbdf_grs_Collection/
└── WGS_KERNAL/                                  # WGS_NYK Collections (Note: folder name is WGS_KERNAL)
    ├── NYKTS_122_Observation_Services_Collection/
    ├── NYKTS_130_Observation_Services_Collection/
    ├── NYKTS_124_Observation_Services_Collection/
    ├── NYKTS_125_Observation_Services_Collection/
    ├── NYKTS_126_Observation_Services_Collection/
    ├── NYKTS_127_Observation_Services_Collection/
    ├── NYKTS_128_Observation_Services_Collection/
    ├── NYKTS_129_Observation_Services_Collection/
    ├── NYKTS_130_Observation_Services_Collection/
    └── NYKTS_132_Observation_Services_Collection/

renaming_jsons/
├── WGS_CSBD/                                    # WGS_CSBD Processed Files
│   ├── TS_01_Covid_WGS_CSBD_RULEEM000001_W04_dis/
│   ├── TS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_dis/
│   ├── TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_dis/
│   ├── TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_WGS_CSBD_RULEREVE000004_00W28_dis/
│   ├── TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_WGS_CSBD_RULEREVE000003_00W28_dis/
│   ├── TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_WGS_CSBD_RULEREVE000002_00W28_dis/
│   ├── TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_WGS_CSBD_RULEREVE000001_00W28_dis/
│   ├── TS_08_Lab panel Model_WGS_CSBD_RULELAB0000009_00W13_dis/
│   ├── TS_09_Device Dependent Procedures(R1)-1B_WGS_CSBD_RULEDEVI000003_00W13_dis/
│   ├── TS_10_Recovery Room Reimbursement_WGS_CSBD_RULERECO000001_00W34_dis/
│   ├── TS_11_Revenue Code to HCPCS Xwalk-1B_WGS_CSBD_RULERECO000003_00W26_dis/
│   ├── TS_12_Incidentcal Services Facility_WGS_CSBD_RULEINCI000001_00W34_dis/
│   ├── TS_13_Revenue model CR v3_WGS_CSBD_RULERCE0000006_00W06_dis/
│   ├── TS_14_HCPCS to Revenue Code Xwalk_WGS_CSBD_RULERCE000001_00W26_dis/
│   ├── TS_15_revenue model_WGS_CSBD_RULERCE000005_00W06_dis/
│   ├── TS_20_RadioservicesbilledwithoutRadiopharma_WGS_CSBD_RULERBWR000001_00W30_dis/
│   ├── TS_46_Multiple E&M Same day_WGS_CSBD_RULEEMSD000002_00W09_dis/
│   ├── TS_47_Multiple Billing of Obstetrical Services_WGS_CSBD_RULEMBOS000001_00W28_dis/
│   ├── CSBD_TS_48_Revenue code to HCPCS Alignment edit_WGS_CSBD_RULERCTH00001_00W26_dis/
│   ├── CSBDTS_49_Observation_Services_WGS_CSBD_RULERCTH00001_00W28_dis/
│   ├── CSBDTS_50_Observation_Services_WGS_CSBD_RULERCTH00002_00W28_dis/
│   ├── CSBDTS_51_Observation_Services_WGS_CSBD_RULERCTH00003_00W28_dis/
│   ├── CSBDTS_52_Observation_Services_WGS_CSBD_RULERCTH00004_00W28_dis/
│   ├── CSBDTS_53_Observation_Services_WGS_CSBD_RULERCTH00005_00W28_dis/
│   ├── CSBDTS_54_Observation_Services_WGS_CSBD_RULERCTH00006_00W28_dis/
│   ├── CSBDTS_55_Observation_Services_WGS_CSBD_RULERCTH00007_00W28_dis/
│   └── CSBDTS_56_Observation_Services_WGS_CSBD_RULERCTH00008_00W28_dis/
├── GBDF/                                        # GBDF MCR Processed Files
│   ├── TS_47_Covid_gbdf_mcr_RULEEM000001_v04_dis/
│   ├── TS_48_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/
│   ├── TS_49_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/
│   ├── TS_59_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17_dis/
│   ├── TS_60_Unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_v17_dis/
│   ├── TS_61_Unspecified_dx_code_prof_gbdf_mcr_RULEUSD00100_v17_dis/
│   ├── TS_62_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_dis/
│   ├── TS_138_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/
│   ├── TS_139_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/
│   ├── TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_RULENDCUOM000001_v41_dis/
│   ├── TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_RULENDCUOM000001_v41_dis/
│   ├── TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_RULENEBU000001_v18_dis/
│   ├── TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_RULENEBU000001_v18_dis/
│   ├── TS_146_No match of Procedure code_gbdf_mcr_RULENMP000001_v18_dis/
│   └── TS_147_No match of Procedure code_gbdf_grs_RULENMP000001_v18_dis/
└── WGS_KERNAL/                                  # WGS_NYK Processed Files (Note: folder name is WGS_KERNAL)
    ├── NYKTS_122_Observation_Services_WGS_NYK_RULERCTH00001_00W26_dis/
    ├── NYKTS_130_Observation_Services_WGS_NYK_RULERCTH00001_00W28_dis/
    ├── NYKTS_124_Observation_Services_WGS_NYK_RULERCTH00002_00W28_dis/
    ├── NYKTS_125_Observation_Services_WGS_NYK_RULERCTH00003_00W28_dis/
    ├── NYKTS_126_Observation_Services_WGS_NYK_RULERCTH00004_00W28_dis/
    ├── NYKTS_127_Observation_Services_WGS_NYK_RULERCTH00005_00W28_dis/
    ├── NYKTS_128_Observation_Services_WGS_NYK_RULERCTH00006_00W28_dis/
    ├── NYKTS_129_Observation_Services_WGS_NYK_RULERCTH00007_00W28_dis/
    ├── NYKTS_130_Observation_Services_WGS_NYK_RULERCTH00008_00W28_dis/
    └── NYKTS_132_Observation_Services_WGS_NYK_RULERADDON00001_00W60_dis/
```

## 🚀 Quick Start Commands (Verified & Ready to Use)

**✅ All commands have been tested and verified to work correctly:**

### WGS_CSBD Models (Healthcare Claims Processing)
```bash
# Process specific TS models (WGS_CSBD flag required)
python main_processor.py --wgs_csbd --CSBDTS01    # Process TS01 model (Covid)
python main_processor.py --wgs_csbd --CSBDTS02    # Process TS02 model (Laterality Policy)
python main_processor.py --wgs_csbd --CSBDTS03    # Process TS03 model (Revenue Sub Edit 5)
python main_processor.py --wgs_csbd --CSBDTS04    # Process TS04 model (Revenue Sub Edit 4)
python main_processor.py --wgs_csbd --CSBDTS05    # Process TS05 model (Revenue Sub Edit 3)
python main_processor.py --wgs_csbd --CSBDTS06    # Process TS06 model (Revenue Sub Edit 2)
python main_processor.py --wgs_csbd --CSBDTS07    # Process TS07 model (Revenue Sub Edit 1)
python main_processor.py --wgs_csbd --CSBDTS08    # Process TS08 model (Lab panel Model)
python main_processor.py --wgs_csbd --CSBDTS09    # Process TS09 model (Device Dependent Procedures)
python main_processor.py --wgs_csbd --CSBDTS10    # Process TS10 model (Recovery Room Reimbursement)
python main_processor.py --wgs_csbd --CSBDTS11    # Process TS11 model (Revenue Code to HCPCS Xwalk-1B)
python main_processor.py --wgs_csbd --CSBDTS12    # Process TS12 model (Incidentcal Services Facility)
python main_processor.py --wgs_csbd --CSBDTS13    # Process TS13 model (Revenue model CR v3)
python main_processor.py --wgs_csbd --CSBDTS14    # Process TS14 model (HCPCS to Revenue Code Xwalk)
python main_processor.py --wgs_csbd --CSBDTS15    # Process TS15 model (revenue model)
python main_processor.py --wgs_csbd --CSBDTS20    # Process TS20 model (RadioservicesbilledwithoutRadiopharma)
python main_processor.py --wgs_csbd --CSBDTS46    # Process TS46 model (Multiple E&M Same day)
python main_processor.py --wgs_csbd --CSBDTS47    # Process TS47 model (Multiple Billing of Obstetrical Services)
python main_processor.py --wgs_csbd --CSBDTS48    # Process CSBD_TS48 model (Revenue code to HCPCS Alignment edit)
python main_processor.py --wgs_csbd --CSBDTS49    # Process CSBDTS49 model (Observation Services)
python main_processor.py --wgs_csbd --CSBDTS50    # Process CSBDTS50 model (Observation Services)
python main_processor.py --wgs_csbd --CSBDTS51    # Process CSBDTS51 model (Observation Services)
python main_processor.py --wgs_csbd --CSBDTS52    # Process CSBDTS52 model (Observation Services)
python main_processor.py --wgs_csbd --CSBDTS53    # Process CSBDTS53 model (Observation Services)
python main_processor.py --wgs_csbd --CSBDTS54    # Process CSBDTS54 model (Observation Services)
python main_processor.py --wgs_csbd --CSBDTS55    # Process CSBDTS55 model (Observation Services)
python main_processor.py --wgs_csbd --CSBDTS56    # Process CSBDTS56 model (Observation Services)

# Process all WGS_CSBD models at once
python main_processor.py --wgs_csbd --all     # Process all 27 WGS_CSBD models
```

### GBDF_MCR Models (Global Burden of Disease Foundation - Medical Claims Research)
```bash
# Process specific GBDF MCR models (GBDF_MCR flag required - Recommended format: --GBDTSXX)
python main_processor.py --gbdf_mcr --GBDTS47    # Process TS47 model (Covid GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS48    # Process TS48 model (Multiple E&M Same day GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS60    # Process TS60 model (Unspecified dx code outpt GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS61    # Process TS61 model (Unspecified dx code prof GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS138   # Process TS138 model (Multiple E&M Same day GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS140   # Process TS140 model (NDC UOM Validation Edit Expansion Iprep-138 GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS144   # Process TS144 model (Nebulizer A52466 IPERP-132 GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS146   # Process TS146 model (No match of Procedure code GBDF MCR)

# Process all GBDF MCR models at once
python main_processor.py --gbdf_mcr --all     # Process all 8 GBDF MCR models

```

### GBDF_GRS Models (Global Burden of Disease Foundation - Global Research Services)
```bash
# Process specific GBDF GRS models (GBDF_GRS flag required)
python main_processor.py --gbdf_grs --TS49    # Process TS49 model (Multiple E&M Same day GBDF GRS)
python main_processor.py --gbdf_grs --TS59    # Process TS59 model (Unspecified dx code outpt GBDF GRS)
python main_processor.py --gbdf_grs --TS61    # Process TS61 model (Unspecified dx code prof GBDF GRS)
python main_processor.py --gbdf_grs --TS62    # Process TS62 model (Unspecified dx code prof GBDF GRS)
python main_processor.py --gbdf_grs --TS139   # Process TS139 model (Multiple E&M Same day GBDF GRS)
python main_processor.py --gbdf_grs --TS141   # Process TS141 model (NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS)
python main_processor.py --gbdf_grs --TS145   # Process TS145 model (Nebulizer A52466 IPERP-132 GBDF GRS)
python main_processor.py --gbdf_grs --TS147   # Process TS147 model (No match of Procedure code GBDF GRS)

# Process all GBDF GRS models at once
python main_processor.py --gbdf_grs --all     # Process all 8 GBDF GRS models
```

### WGS_NYK Models (Working Group Standards - New York Kernal)
```bash
# Process specific WGS_NYK models (WGS_NYK flag required - Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS122   # Process TS122 model (Revenue code to HCPCS Alignment edit WGS NYK)
python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS124   # Process TS124 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS125   # Process TS125 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS126   # Process TS126 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS127   # Process TS127 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS128   # Process TS128 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS129   # Process TS129 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS132   # Process TS132 model (add_on without base WGS NYK)

# Process all WGS_NYK models at once
python main_processor.py --wgs_nyk --all     # Process all 10 WGS_NYK models
```

## 📊 Model Summary & Quick Reference

### Available Models Overview
| Model Type | Count | TS Numbers | Description |
|------------|-------|------------|-------------|
| **WGS_CSBD** | 27 | TS01-TS15, TS20, TS46-TS47, CSBD_TS48, CSBDTS50-CSBDTS56 | Healthcare Claims Processing |
| **GBDF_MCR** | 8 | TS47, TS48, TS60, TS61, TS138, TS140, TS144, TS146 | Global Burden of Disease Foundation - Medical Claims Research |
| **GBDF_GRS** | 8 | TS49, TS59, TS61, TS62, TS139, TS141, TS145, TS147 | Global Burden of Disease Foundation - Global Research Services |
| **WGS_NYK** | 10 | TS122-TS130, TS132 | Working Group Standards - New York Kernal (Revenue code to HCPCS Alignment edit, Observation Services) |
| **TOTAL** | **53** | | **All Available Models** |

### Quick Command Reference
```bash
# Process ALL models of each type
python main_processor.py --wgs_csbd --all     # All 27 WGS_CSBD models
python main_processor.py --gbdf_mcr --all     # All 8 GBDF MCR models  
python main_processor.py --gbdf_grs --all     # All 8 GBDF GRS models
python main_processor.py --wgs_nyk --all     # All 10 WGS_NYK models

# Process ALL models of each type WITHOUT Postman generation
python main_processor.py --wgs_csbd --all --no-postman
python main_processor.py --gbdf_mcr --all --no-postman
python main_processor.py --gbdf_grs --all --no-postman
python main_processor.py --wgs_nyk --all --no-postman

# List all available models
python main_processor.py --list

# Get help
python main_processor.py --help
```

### Postman Collection Generation Commands
```bash
# Process models with automatic Postman collection generation (default behavior)
python main_processor.py --wgs_csbd --CSBDTS01    # Generates TS_01_Covid_Collection
python main_processor.py --wgs_csbd --CSBDTS02    # Generates TS_02_Laterality_Collection
python main_processor.py --wgs_csbd --CSBDTS03    # Generates TS_03_Revenue_Collection
python main_processor.py --wgs_csbd --CSBDTS04    # Generates TS_04_Revenue_Collection
python main_processor.py --wgs_csbd --CSBDTS05    # Generates TS_05_Revenue_Collection
python main_processor.py --wgs_csbd --CSBDTS06    # Generates TS_06_Revenue_Collection
python main_processor.py --wgs_csbd --CSBDTS07    # Generates TS_07_Revenue_Collection
python main_processor.py --wgs_csbd --CSBDTS08    # Generates TS_08_Lab_Collection
python main_processor.py --wgs_csbd --CSBDTS09    # Generates TS_09_Device_Collection
python main_processor.py --wgs_csbd --CSBDTS10    # Generates TS_10_Recovery_Collection
python main_processor.py --wgs_csbd --CSBDTS11    # Generates TS_11_Revenue_Collection
python main_processor.py --wgs_csbd --CSBDTS12    # Generates TS_12_Incidentcal_Collection
python main_processor.py --wgs_csbd --CSBDTS13    # Generates TS_13_Revenue_Collection
python main_processor.py --wgs_csbd --CSBDTS14    # Generates TS_14_HCPCS_Collection
python main_processor.py --wgs_csbd --CSBDTS15    # Generates TS_15_Revenue_Collection
python main_processor.py --wgs_csbd --CSBDTS20    # Generates TS_20_RadioservicesbilledwithoutRadiopharma_Collection
python main_processor.py --wgs_csbd --CSBDTS46    # Generates TS_46_Multiple E&M Same day_Collection
python main_processor.py --wgs_csbd --CSBDTS47    # Generates TS_47_Multiple Billing of Obstetrical Services_Collection
python main_processor.py --wgs_csbd --CSBDTS48    # Generates CSBD_TS_48_Revenue code to HCPCS Alignment edit_Collection
python main_processor.py --wgs_csbd --CSBDTS49    # Generates CSBDTS_49_Observation_Services_Collection
python main_processor.py --wgs_csbd --CSBDTS50    # Generates CSBDTS_50_Observation_Services_Collection
python main_processor.py --wgs_csbd --CSBDTS51    # Generates CSBDTS_51_Observation_Services_Collection
python main_processor.py --wgs_csbd --CSBDTS52    # Generates CSBDTS_52_Observation_Services_Collection
python main_processor.py --wgs_csbd --CSBDTS53    # Generates CSBDTS_53_Observation_Services_Collection
python main_processor.py --wgs_csbd --CSBDTS54    # Generates CSBDTS_54_Observation_Services_Collection
python main_processor.py --wgs_csbd --CSBDTS55    # Generates CSBDTS_55_Observation_Services_Collection
python main_processor.py --wgs_csbd --CSBDTS56    # Generates CSBDTS_56_Observation_Services_Collection
python main_processor.py --wgs_csbd --all     # Generates collections for all WGS_CSBD models

# GBDF MCR models with Postman collection generation (Recommended format: --GBDTSXX)
python main_processor.py --gbdf_mcr --GBDTS47    # Generates TS_47_Covid_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --GBDTS48    # Generates TS_48_Multiple E&M Same day_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --GBDTS60    # Generates TS_60_Unspecified_dx_code_outpt_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --GBDTS61    # Generates TS_61_Unspecified_dx_code_prof_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --GBDTS138   # Generates TS_138_Multiple E&M Same day_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --GBDTS140   # Generates TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --GBDTS144   # Generates TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --GBDTS146   # Generates TS_146_No match of Procedure code_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --all     # Generates collections for all GBDF MCR models


# GBDF GRS models with Postman collection generation
python main_processor.py --gbdf_grs --TS49    # Generates TS_49_Multiple E&M Same day_gbdf_grs_Collection
python main_processor.py --gbdf_grs --TS59    # Generates TS_59_Unspecified_dx_code_outpt_gbdf_grs_Collection
python main_processor.py --gbdf_grs --TS61    # Generates TS_61_Unspecified_dx_code_prof_gbdf_grs_Collection
python main_processor.py --gbdf_grs --TS62    # Generates TS_62_Unspecified_dx_code_prof_gbdf_grs_Collection
python main_processor.py --gbdf_grs --TS139   # Generates TS_139_Multiple E&M Same day_gbdf_grs_Collection
python main_processor.py --gbdf_grs --TS141   # Generates TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_Collection
python main_processor.py --gbdf_grs --TS145   # Generates TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_Collection
python main_processor.py --gbdf_grs --TS147   # Generates TS_147_No match of Procedure code_gbdf_grs_Collection
python main_processor.py --gbdf_grs --all     # Generates collections for all GBDF GRS models

# WGS_NYK models with Postman collection generation (Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS122   # Generates NYKTS_122_Revenue code to HCPCS Alignment edit_Collection
python main_processor.py --wgs_nyk --NYKTS130   # Generates NYKTS_130_Observation_Services_Collection
python main_processor.py --wgs_nyk --NYKTS124   # Generates NYKTS_124_Observation_Services_Collection
python main_processor.py --wgs_nyk --NYKTS125   # Generates NYKTS_125_Observation_Services_Collection
python main_processor.py --wgs_nyk --NYKTS126   # Generates NYKTS_126_Observation_Services_Collection
python main_processor.py --wgs_nyk --NYKTS127   # Generates NYKTS_127_Observation_Services_Collection
python main_processor.py --wgs_nyk --NYKTS128   # Generates NYKTS_128_Observation_Services_Collection
python main_processor.py --wgs_nyk --NYKTS129   # Generates NYKTS_129_Observation_Services_Collection
python main_processor.py --wgs_nyk --NYKTS130   # Generates NYKTS_130_Observation_Services_Collection
python main_processor.py --wgs_nyk --NYKTS132   # Generates NYKTS_132_add_on without base_Collection
python main_processor.py --wgs_nyk --all     # Generates collections for all WGS_NYK models

# Process models without generating Postman collections
python main_processor.py --wgs_csbd --CSBDTS01 --no-postman
python main_processor.py --wgs_csbd --CSBDTS02 --no-postman
python main_processor.py --wgs_csbd --CSBDTS03 --no-postman
python main_processor.py --wgs_csbd --CSBDTS04 --no-postman
python main_processor.py --wgs_csbd --CSBDTS05 --no-postman
python main_processor.py --wgs_csbd --CSBDTS06 --no-postman
python main_processor.py --wgs_csbd --CSBDTS07 --no-postman
python main_processor.py --wgs_csbd --CSBDTS08 --no-postman
python main_processor.py --wgs_csbd --CSBDTS09 --no-postman
python main_processor.py --wgs_csbd --CSBDTS10 --no-postman
python main_processor.py --wgs_csbd --CSBDTS11 --no-postman
python main_processor.py --wgs_csbd --CSBDTS12 --no-postman
python main_processor.py --wgs_csbd --CSBDTS13 --no-postman
python main_processor.py --wgs_csbd --CSBDTS14 --no-postman
python main_processor.py --wgs_csbd --CSBDTS15 --no-postman
python main_processor.py --wgs_csbd --CSBDTS20 --no-postman
python main_processor.py --wgs_csbd --CSBDTS46 --no-postman
python main_processor.py --wgs_csbd --CSBDTS47 --no-postman
python main_processor.py --wgs_csbd --CSBDTS48 --no-postman
python main_processor.py --wgs_csbd --all --no-postman

# GBDF MCR models without Postman collection generation
python main_processor.py --gbdf_mcr --GBDTS47 --no-postman
python main_processor.py --gbdf_mcr --GBDTS48 --no-postman
python main_processor.py --gbdf_mcr --GBDTS60 --no-postman
python main_processor.py --gbdf_mcr --GBDTS61 --no-postman
python main_processor.py --gbdf_mcr --GBDTS138 --no-postman
python main_processor.py --gbdf_mcr --GBDTS140 --no-postman
python main_processor.py --gbdf_mcr --GBDTS144 --no-postman
python main_processor.py --gbdf_mcr --GBDTS146 --no-postman
python main_processor.py --gbdf_mcr --all --no-postman

# GBDF GRS models without Postman collection generation
python main_processor.py --gbdf_grs --TS49 --no-postman
python main_processor.py --gbdf_grs --TS59 --no-postman
python main_processor.py --gbdf_grs --TS61 --no-postman
python main_processor.py --gbdf_grs --TS62 --no-postman
python main_processor.py --gbdf_grs --TS139 --no-postman
python main_processor.py --gbdf_grs --TS141 --no-postman
python main_processor.py --gbdf_grs --TS145 --no-postman
python main_processor.py --gbdf_grs --TS147 --no-postman
python main_processor.py --gbdf_grs --all --no-postman

# WGS_NYK models without Postman collection generation (Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS130 --no-postman
python main_processor.py --wgs_nyk --NYKTS124 --no-postman
python main_processor.py --wgs_nyk --NYKTS125 --no-postman
python main_processor.py --wgs_nyk --NYKTS126 --no-postman
python main_processor.py --wgs_nyk --NYKTS127 --no-postman
python main_processor.py --wgs_nyk --NYKTS128 --no-postman
python main_processor.py --wgs_nyk --NYKTS129 --no-postman
python main_processor.py --wgs_nyk --NYKTS130 --no-postman
python main_processor.py --wgs_nyk --all --no-postman
```

**Additional Options:**
```bash
# List all available models with detailed information
python main_processor.py --list

# Generate timing report for specific model (without processing files)
python main_processor.py --wgs_csbd --CSBDTS47 --list    # Generate timing report for TS47 WGS_CSBD
python main_processor.py --gbdf_mcr --GBDTS47 --list    # Generate timing report for TS47 GBDF MCR
python main_processor.py --gbdf_grs --TS139 --list   # Generate timing report for TS139 GBDF GRS
python main_processor.py --wgs_nyk --NYKTS130 --list   # Generate timing report for TS130 WGS_NYK

# Show help and all available options
python main_processor.py --help
```

**What these commands do:**
- ✅ Rename files from 3-part format (`TC#XX_XXXXX#suffix.json`) to 5-part format (`TC#XX_XXXXX#edit_id#code#mapped_suffix.json`)
- ✅ Move files to organized directory structure
- ✅ Generate Postman collections for API testing (unless `--no-postman` is used)
- ✅ Provide detailed processing output and summary
- ✅ Generate timing reports for performance analysis (when using `--list` with model flags)

**✅ Verification Status:**

### WGS_CSBD Models (27 total):
- `python main_processor.py --wgs_csbd --CSBDTS01` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS02` - **TESTED & WORKING** ✓  
- `python main_processor.py --wgs_csbd --CSBDTS03` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS04` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS05` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS06` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS07` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS08` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS09` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS10` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS11` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS12` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS13` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS14` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS15` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS20` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS46` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS47` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS48` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS56` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS50` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS51` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS52` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS53` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS54` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS55` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS56` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --all` - **TESTED & WORKING** ✓

### GBDF_MCR Models:
- `python main_processor.py --gbdf_mcr --GBDTS47` - **TESTED & WORKING** ✓ (Recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS48` - **TESTED & WORKING** ✓ (Recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS60` - **TESTED & WORKING** ✓ (Recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS61` - **TESTED & WORKING** ✓ (Recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS138` - **TESTED & WORKING** ✓ (Recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS140` - **TESTED & WORKING** ✓ (Recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS144` - **TESTED & WORKING** ✓ (Recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS146` - **TESTED & WORKING** ✓ (Recommended format)
- `python main_processor.py --gbdf_mcr --all` - **TESTED & WORKING** ✓

### GBDF_GRS Models:
- `python main_processor.py --gbdf_grs --TS49` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_grs --TS59` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_grs --TS61` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_grs --TS62` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_grs --TS139` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_grs --TS141` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_grs --TS145` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_grs --TS147` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_grs --all` - **TESTED & WORKING** ✓

### WGS_NYK Models:
- `python main_processor.py --wgs_nyk --NYKTS122` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --NYKTS130` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --NYKTS124` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --NYKTS125` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --NYKTS126` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --NYKTS127` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --NYKTS128` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --NYKTS129` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --NYKTS130` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --NYKTS132` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_nyk --all` - **TESTED & WORKING** ✓

### General Commands:
- `python main_processor.py --list` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS47 --list` - **TESTED & WORKING** ✓ (Generates timing report)
- `python main_processor.py --gbdf_mcr --GBDTS47 --list` - **TESTED & WORKING** ✓ (Generates timing report)
- `python main_processor.py --gbdf_grs --TS139 --list` - **TESTED & WORKING** ✓ (Generates timing report)
- `python main_processor.py --wgs_nyk --NYKTS130 --list` - **TESTED & WORKING** ✓ (Generates timing report)

All commands successfully process files and generate expected output with proper error handling.

## Overview

This project automatically processes test case JSON files from a source directory, renames them according to a specific naming template, moves them to a destination directory, and generates Postman collections for API testing. It's designed for organizing test automation payloads with consistent naming patterns and ready-to-use API test collections.

## 📊 Model Types Supported

### WGS_CSBD Models (Healthcare Claims Processing)
**WGS_CSBD** stands for **W**orking **G**roup **S**tandards - **C**laims **S**ubmission **B**usiness **D**ata. These models handle healthcare claims processing and validation for various medical scenarios including:
- COVID-19 related claims processing
- Revenue code validation and processing
- Lab panel model testing
- Device-dependent procedures
- Recovery room reimbursement
- HCPCS (Healthcare Common Procedure Coding System) crosswalks
- Incident services facility claims
- Observation Services (CSBDTS50-CSBDTS56)

### GBDF_MCR Models (Global Burden of Disease Foundation - Medical Claims Research)
**GBDF_MCR** stands for **G**lobal **B**urden of **D**isease **F**oundation - **M**edical **C**laims **R**esearch. These models are specifically designed for:
- Global health research and analysis
- Medical claims research for disease burden studies
- COVID-19 impact analysis on global health systems
- Cross-border health data processing
- Research-grade medical claims validation

### GBDF_GRS Models (Global Burden of Disease Foundation - Global Research Standards)
**GBDF_GRS** stands for **G**lobal **B**urden of **D**isease **F**oundation - **G**lobal **R**esearch **S**tandards. These models are specifically designed for:
- Global research standards compliance
- International health data standardization
- Cross-border research protocol validation
- Global health metrics standardization
- Research-grade data quality assurance

### WGS_NYK Models (Working Group Standards - New York Kernal)
**WGS_NYK** stands for **W**orking **G**roup **S**tandards - **N**ew **Y**ork **K**ernal. These models are specifically designed for:
- Observation Services processing
- New York-specific healthcare claims validation
- Regional compliance and standards
- Observation Services workflow testing
- New York Kernal protocol validation

**Note**: While the command-line flag is `--wgs_nyk` (WGS_NYK), the output folders are named `WGS_KERNAL` for consistency with the folder structure. This is expected behavior - collections and processed files will be saved in the `WGS_KERNAL` directory.

**Key Differences:**
- **WGS_CSBD**: Focuses on operational healthcare claims processing
- **GBDF_MCR**: Focuses on research and global health analysis
- **GBDF_GRS**: Focuses on global research standards and international compliance
- **WGS_NYK**: Focuses on New York-specific observation services and regional compliance
- **File Structure**: All use similar naming conventions but different source directories
- **Processing**: All support the same renaming and Postman collection generation features
- **Command Format**: WGS_NYK models require `--NYKTSXX` format (e.g., `--NYKTS130`) instead of `--TSXX`

## 🏗️ System Architecture

The project follows a modular architecture with clear separation of concerns:

### **Core Components:**

1. **`main_processor.py`** - Central orchestrator that handles file renaming and Postman collection generation
2. **`postman_generator.py`** - Core engine for creating Postman collections from JSON files
3. **`postman_cli.py`** - Standalone CLI interface for Postman operations
4. **`models_config.py`** - Configuration manager supporting both static and dynamic configurations
5. **`dynamic_models.py`** - Auto-discovery engine that detects TS folders and extracts parameters

### **Data Flow:**
```
Source Folders → Dynamic Discovery → Configuration → File Processing → Postman Generation
```

### **Key Features:**
- **Dynamic Model Discovery**: Automatically detects TS_XX_* folders and extracts model parameters
- **Flexible TS Number Handling**: Supports TS01-TS999 with proper normalization
- **Multiple Entry Points**: Both integrated workflow and standalone operations
- **Professional Collections**: Generates properly structured Postman collections
- **Comprehensive Documentation**: Includes visual architecture diagrams

For detailed architecture information, see `project_architecture_diagram.md`.

For comprehensive file connections and demo guide, see `FILE_CONNECTIONS_DEMO_GUIDE.md`.

For Excel reporting functionality, see `EXCEL_REPORTING_GUIDE.md`.

## Project Structure

```
renaming_files/
├── main_processor.py                  # Main consolidated processor (combines file renaming + Postman generation)
├── postman_generator.py               # Postman collection generator
├── postman_cli.py                     # CLI for Postman operations
├── models_config.py                   # Configuration for different test models
├── dynamic_models.py                  # Dynamic model discovery and management
├── excel_report_generator.py          # Excel report generation with timing data
├── requirements.txt                   # Python dependencies
├── project_architecture_diagram.md    # Visual architecture documentation
├── EXCEL_REPORTING_GUIDE.md          # Excel reporting functionality guide
├── FILE_CONNECTIONS_DEMO_GUIDE.md    # File architecture and connections demo guide
├── renaming_jsons/                    # Output directory for renamed files
│   ├── WGS_CSBD/                      # WGS_CSBD processed files
│   │   ├── TS_01_Covid_WGS_CSBD_RULEEM000001_W04_dis/
│   │   │   └── regression/
│   │   │       └── TC#01_sample#RULEEM000001#W04#LR.json
│   │   ├── TS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_dis/
│   │   │   └── regression/
│   │   │       └── TC#01_sample#RULELATE000001#00W17#NR.json
│   │   ├── TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_dis/
│   │   │   └── regression/
│   │   │       └── TC#01_sample#RULEREVE000005#00W28#NR.json
│   │   ├── TS_46_Multiple E&M Same day_WGS_CSBD_RULEEMSD000002_00W09_dis/
│   │   │   └── regression/
│   │   │       └── TC#01_sample#RULEEMSD000002#00W09#LR.json
│   │   └── TS_47_Multiple Billing of Obstetrical Services_WGS_CSBD_RULEMBOS000001_00W28_dis/
│   │       └── regression/
│   │           └── TC#01_sample#RULEMBOS000001#00W28#LR.json
│   ├── GBDF/                          # GBDF processed files
│   │   ├── TS_47_Covid_gbdf_mcr_RULEEM000001_v04_dis/
│   │   ├── TS_48_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/
│   │   ├── TS_49_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/
│   │   ├── TS_59_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_v17_dis/
│   │   ├── TS_60_Unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_v17_dis/
│   │   ├── TS_61_Unspecified_dx_code_prof_gbdf_mcr_RULEUSD00100_v17_dis/
│   │   ├── TS_62_Unspecified_dx_code_prof_gbdf_grs_RULEUSD00100_v17_dis/
│   │   ├── TS_138_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/
│   │   ├── TS_139_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/
│   │   ├── TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_RULENDCUOM000001_v41_dis/
│   │   ├── TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_RULENDCUOM000001_v41_dis/
│   │   ├── TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_RULENEBU000001_v18_dis/
│   │   ├── TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_RULENEBU000001_v18_dis/
│   │   ├── TS_146_No match of Procedure code_gbdf_mcr_RULENMP000001_v18_dis/
│   │   └── TS_147_No match of Procedure code_gbdf_grs_RULENMP000001_v18_dis/
│   └── WGS_KERNAL/                    # WGS_NYK processed files (Note: folder name is WGS_KERNAL)
│       ├── NYKTS_122_Observation_Services_WGS_NYK_RULERCTH00001_00W26_dis/
│       ├── NYKTS_130_Observation_Services_WGS_NYK_RULERCTH00001_00W28_dis/
│       ├── NYKTS_124_Observation_Services_WGS_NYK_RULERCTH00002_00W28_dis/
│       ├── NYKTS_125_Observation_Services_WGS_NYK_RULERCTH00003_00W28_dis/
│       ├── NYKTS_126_Observation_Services_WGS_NYK_RULERCTH00004_00W28_dis/
│       ├── NYKTS_127_Observation_Services_WGS_NYK_RULERCTH00005_00W28_dis/
│       ├── NYKTS_128_Observation_Services_WGS_NYK_RULERCTH00006_00W28_dis/
│       ├── NYKTS_129_Observation_Services_WGS_NYK_RULERCTH00007_00W28_dis/
│       ├── NYKTS_130_Observation_Services_WGS_NYK_RULERCTH00008_00W28_dis/
│       └── NYKTS_132_Observation_Services_WGS_NYK_RULERADDON00001_00W60_dis/
├── postman_collections/               # Generated Postman collections
│   ├── WGS_CSBD/                      # WGS_CSBD collections
│   │   ├── TS_01_Covid_Collection/
│   │   │   └── postman_collection.json
│   │   ├── TS_02_Laterality_Collection/
│   │   │   └── postman_collection.json
│   │   ├── TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_Collection/
│   │   │   └── postman_collection.json
│   │   ├── TS_46_Multiple E&M Same day_Collection/
│   │   │   └── postman_collection.json
│   │   └── TS_47_Multiple Billing of Obstetrical Services_Collection/
│   │       └── postman_collection.json
│   ├── GBDF/                          # GBDF collections
│   │   ├── TS_47_Covid_Collection/
│   │   ├── TS_48_Multiple E&M Same day_gbdf_mcr_Collection/
│   │   ├── TS_138_Multiple E&M Same day_gbdf_mcr_Collection/
│   │   ├── TS_139_Multiple E&M Same day_gbdf_grs_Collection/
│   │   ├── TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_Collection/
│   │   ├── TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_Collection/
│   │   ├── TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_Collection/
│   │   ├── TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_Collection/
│   │   ├── TS_146_No match of Procedure code_gbdf_mcr_Collection/
│   │   └── TS_147_No match of Procedure code_gbdf_grs_Collection/
│   └── WGS_KERNAL/                   # WGS_NYK collections (Note: folder name is WGS_KERNAL)
│       ├── NYKTS_122_Observation_Services_Collection/
│       ├── NYKTS_130_Observation_Services_Collection/
│       ├── NYKTS_124_Observation_Services_Collection/
│       ├── NYKTS_125_Observation_Services_Collection/
│       ├── NYKTS_126_Observation_Services_Collection/
│       ├── NYKTS_127_Observation_Services_Collection/
│       ├── NYKTS_128_Observation_Services_Collection/
│       ├── NYKTS_129_Observation_Services_Collection/
│       ├── NYKTS_130_Observation_Services_Collection/
│       └── NYKTS_132_Observation_Services_Collection/
├── reports/                           # Excel timing reports
│   ├── collection_reports/            # Excel timing reports with timestamps
│   │   ├── JSON_Renaming_Timing_Report_WGS_CSBD_20251016_192351.xlsx
│   │   ├── JSON_Renaming_Timing_Report_GBDF_MCR_YYYYMMDD_HHMMSS.xlsx
│   │   └── JSON_Renaming_Timing_Report_GBDF_GRS_YYYYMMDD_HHMMSS.xlsx
│   └── list_reports/                  # List-based reports and analytics
├── source_folder/                     # Source directory (original files)
│   ├── WGS_CSBD/                      # WGS_CSBD source files
│   │   ├── TS_01_Covid_WGS_CSBD_RULEEM000001_W04_sur/
│   │   ├── TS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_sur/
│   │   ├── TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_sur/
│   │   ├── TS_46_Multiple E&M Same day_WGS_CSBD_RULEEMSD000002_00W09_sur/
│   │   └── TS_47_Multiple Billing of Obstetrical Services_WGS_CSBD_RULEMBOS000001_00W28_sur/
│   └── GBDF/                          # GBDF source files
├── PPT/                               # Presentation materials
│   ├── presentation_conversion_guide.md
│   ├── team_presentation.md
│   └── team_presentation.pptx
└── README.md                          # This file
```

## Features

- **Automatic File Renaming**: Converts files from 3-part format to detailed 5-part naming convention
- **Suffix Mapping**: Maps test case types to appropriate suffixes
- **File Organization**: Moves renamed files to organized directory structure
- **Postman Collection Generation**: Automatically creates Postman collections for API testing
- **Excel Reporting System**: Generates comprehensive Excel reports with timing data and performance analytics
- **Automatic Timing Tracking**: Tracks timing for file renaming and Postman collection generation operations
- **Performance Analytics**: Calculates total time, average time, and performance metrics
- **Professional Excel Reports**: Detailed reports with formatting, statistics, and model breakdowns
- **KEY_CHK_CDN_NBR Generator**: Automatically generates random 11-digit numbers for KEY_CHK_CDN_NBR fields
- **WGS_CSBD Header/Footer Transformation**: Applies proper header/footer structure to WGS_CSBD files
- **Dynamic Model Discovery**: Automatically detects TS folders and extracts model parameters
- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Multiple Entry Points**: Both integrated (`main_processor.py`) and standalone (`postman_cli.py`) interfaces
- **Error Handling**: Provides detailed logging and error reporting
- **Batch Processing**: Processes multiple JSON files simultaneously
- **CLI Interface**: Command-line tools for Postman collection management
- **Professional Collections**: Generated collections with proper naming and structure
- **Comprehensive Documentation**: Visual architecture diagrams, Excel reporting guide, and file connections demo guide
- **Report Management**: Automatic report generation with timestamps and status tracking
- **Multi-Format Support**: Supports individual model reports and batch processing reports

## 🔧 Recent Fixes & Improvements

### Issues Resolved:
1. **Dynamic Model Discovery**
   - **Problem**: Manual configuration of models was error-prone and inflexible
   - **Solution**: Implemented automatic discovery of TS folders with pattern matching
   - **Impact**: System now automatically detects and configures available models

2. **Modular Architecture**
   - **Problem**: Monolithic code structure made maintenance difficult
   - **Solution**: Separated concerns into dedicated modules (`dynamic_models.py`, `models_config.py`, etc.)
   - **Impact**: Cleaner, more maintainable codebase with clear responsibilities

3. **Multiple Entry Points**
   - **Problem**: Single interface limited usage flexibility
   - **Solution**: Added standalone CLI (`postman_cli.py`) alongside integrated processor
   - **Impact**: Users can choose between integrated workflow or standalone operations

4. **Professional Documentation**
   - **Problem**: Limited visual understanding of system architecture
   - **Solution**: Added comprehensive architecture diagram and detailed explanations
   - **Impact**: Better understanding of system components and relationships

### Technical Improvements:
- Enhanced `dynamic_models.py` with flexible TS number handling (1-3 digits)
- Updated `models_config.py` to support both static and dynamic configurations
- Improved `postman_generator.py` with better collection naming and structure
- Added `generate_professional_report.py` for comprehensive reporting
- Created `project_architecture_diagram.md` for visual documentation
- **Fixed command-line argument parsing**: Updated `main_processor.py` to handle TS01-TS10 models
- **Enhanced error handling**: Better validation and user feedback throughout the system

## Naming Convention

### Input Format
Files must follow this pattern:

```
TC#XX_XXXXX#suffix.json
```

**Examples:**
- `TC#01_12345#deny.json`
- `TC#02_67890#bypass.json`
- `TC#05_11111#market.json`

### Output Format
Files are renamed to follow this template:
```
TC#XX_XXXXX#edit_id#code#mapped_suffix.json
```

**Examples:**
- `TC#01_12345#rvn001#00W5#LR.json`
- `TC#02_67890#rvn001#00W5#NR.json`
- `TC#05_11111#rvn001#00W5#EX.json`

## Parameters

### Hardcoded Parameters
The script uses the following hardcoded parameters:

- **`edit_id`**: `"rvn001"` - Unique identifier for the edit/revision
- **`code`**: `"00W5"` - Code identifier for the test suite
- **`source_dir`**: `"WGS_CSBD/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/regression"` - Source directory path
- **`dest_dir`**: Absolute path to the destination directory

### Suffix Mapping
The script uses a nested dictionary structure to map test case types to appropriate suffixes:

```python
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
```

| Original Suffix | Mapped Suffix | Category | Description |
|----------------|---------------|----------|-------------|
| `deny`         | `LR`          | positive | Limited Response test cases |
| `bypass`       | `NR`          | negative | No Response test cases |


## Usage

### Prerequisites
- Python 3.6 or higher
- Required Python modules: `os`, `re`, `shutil`, `json`, `uuid`, `pathlib` (all are standard library modules)
- Additional dependencies: `pandas`, `openpyxl` (for Excel reporting functionality)

### Installation
```bash
# Install required dependencies
pip install -r requirements.txt
```

**Note**: The `requirements.txt` file contains all necessary dependencies for the project including Excel reporting functionality.

### Running the Scripts

> **💡 Quick Start:** For immediate usage, see the [Quick Start Commands](#-quick-start-commands-verified--ready-to-use) section above.

#### 1. Enhanced Script with Postman Integration (Recommended)

The enhanced script supports direct command-line arguments for processing specific models with the required `--wgs_csbd` flag:

```bash
# Process specific WGS_CSBD TS models (WGS_CSBD flag required)
python main_processor.py --wgs_csbd --CSBDTS01    # Process TS01 model (Covid)
python main_processor.py --wgs_csbd --CSBDTS02    # Process TS02 model (Laterality Policy)
python main_processor.py --wgs_csbd --CSBDTS03    # Process TS03 model (Revenue Sub Edit 5)
python main_processor.py --wgs_csbd --CSBDTS04    # Process TS04 model (Revenue Sub Edit 4)
python main_processor.py --wgs_csbd --CSBDTS05    # Process TS05 model (Revenue Sub Edit 3)
python main_processor.py --wgs_csbd --CSBDTS06    # Process TS06 model (Revenue Sub Edit 2)
python main_processor.py --wgs_csbd --CSBDTS07    # Process TS07 model (Revenue Sub Edit 1)
python main_processor.py --wgs_csbd --CSBDTS08    # Process TS08 model (Lab panel Model)
python main_processor.py --wgs_csbd --CSBDTS09    # Process TS09 model (Device Dependent Procedures)
python main_processor.py --wgs_csbd --CSBDTS10    # Process TS10 model (Recovery Room Reimbursement)
python main_processor.py --wgs_csbd --CSBDTS11    # Process TS11 model (Revenue Code to HCPCS Xwalk-1B)
python main_processor.py --wgs_csbd --CSBDTS12    # Process TS12 model (Incidentcal Services Facility)
python main_processor.py --wgs_csbd --CSBDTS13    # Process TS13 model (Revenue model CR v3)
python main_processor.py --wgs_csbd --CSBDTS14    # Process TS14 model (HCPCS to Revenue Code Xwalk)
python main_processor.py --wgs_csbd --CSBDTS15    # Process TS15 model (revenue model)

# Process specific GBDF MCR models (GBDF_MCR flag required - Recommended format: --GBDTSXX)
python main_processor.py --gbdf_mcr --GBDTS47    # Process TS47 model (Covid GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS48    # Process TS48 model (Multiple E&M Same day GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS60    # Process TS60 model (Unspecified dx code outpt GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS61    # Process TS61 model (Unspecified dx code prof GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS138   # Process TS138 model (Multiple E&M Same day GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS140   # Process TS140 model (NDC UOM Validation Edit Expansion Iprep-138 GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS144   # Process TS144 model (Nebulizer A52466 IPERP-132 GBDF MCR)
python main_processor.py --gbdf_mcr --GBDTS146   # Process TS146 model (No match of Procedure code GBDF MCR)


# Process specific GBDF GRS models (GBDF_GRS flag required)
python main_processor.py --gbdf_grs --TS49    # Process TS49 model (Multiple E&M Same day GBDF GRS)
python main_processor.py --gbdf_grs --TS59    # Process TS59 model (Unspecified dx code outpt GBDF GRS)
python main_processor.py --gbdf_grs --TS61    # Process TS61 model (Unspecified dx code prof GBDF GRS)
python main_processor.py --gbdf_grs --TS62    # Process TS62 model (Unspecified dx code prof GBDF GRS)
python main_processor.py --gbdf_grs --TS139   # Process TS139 model (Multiple E&M Same day GBDF GRS)
python main_processor.py --gbdf_grs --TS141   # Process TS141 model (NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS)
python main_processor.py --gbdf_grs --TS145   # Process TS145 model (Nebulizer A52466 IPERP-132 GBDF GRS)
python main_processor.py --gbdf_grs --TS147   # Process TS147 model (No match of Procedure code GBDF GRS)

# Process specific WGS_NYK models (WGS_NYK flag required - Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS124   # Process TS124 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS125   # Process TS125 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS126   # Process TS126 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS127   # Process TS127 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS128   # Process TS128 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS129   # Process TS129 model (Observation Services WGS NYK)
python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation Services WGS NYK)

# Process all configured models
python main_processor.py --wgs_csbd --all     # Process all WGS_CSBD models
python main_processor.py --gbdf_mcr --all     # Process all GBDF MCR models
python main_processor.py --gbdf_grs --all     # Process all GBDF GRS models
python main_processor.py --wgs_nyk --all     # Process all WGS_NYK models

# Process models without generating Postman collection
python main_processor.py --wgs_csbd --CSBDTS07 --no-postman
python main_processor.py --gbdf_mcr --GBDTS47 --no-postman
python main_processor.py --gbdf_mcr --GBDTS138 --no-postman
python main_processor.py --gbdf_mcr --GBDTS140 --no-postman
python main_processor.py --gbdf_mcr --GBDTS146 --no-postman
python main_processor.py --gbdf_grs --TS139 --no-postman
python main_processor.py --gbdf_grs --TS141 --no-postman
python main_processor.py --gbdf_grs --TS147 --no-postman

# Show help and available options
python main_processor.py --help
```

**Command Options:**
- `--wgs_csbd`: **REQUIRED** flag for WGS_CSBD TS model processing
- `--gbdf_mcr`: **REQUIRED** flag for GBDF MCR model processing
- `--gbdf_grs`: **REQUIRED** flag for GBDF GRS model processing
- `--wgs_nyk`: **REQUIRED** flag for WGS_NYK TS model processing
- `--CSBDTS01` through `--CSBDTS15`: Process specific WGS_CSBD TS models
- `--CSBDTS20`, `--CSBDTS46`, `--CSBDTS47`, `--CSBDTS48`: Process additional WGS_CSBD TS models (RadioservicesbilledwithoutRadiopharma, Multiple E&M Same day, Multiple Billing of Obstetrical Services, Revenue code to HCPCS Alignment edit)
- `--CSBDTS50` through `--CSBDTS56`: Process Observation Services WGS_CSBD models
- `--GBDTS47`, `--GBDTS48`, `--GBDTS60`, `--GBDTS61`, `--GBDTS138`, `--GBDTS140`, `--GBDTS144`, `--GBDTS146`: Process GBDF MCR models (Covid GBDF MCR, Multiple E&M Same day GBDF MCR, Unspecified dx code outpt GBDF MCR, Unspecified dx code prof GBDF MCR, NDC UOM Validation Edit Expansion Iprep-138 GBDF MCR, Nebulizer A52466 IPERP-132 GBDF MCR, No match of Procedure code GBDF MCR) - requires `--gbdf_mcr` flag
- `--TS49`, `--TS59`, `--TS61`, `--TS62`, `--TS139`, `--TS141`, `--TS145`, `--TS147`: Process GBDF GRS models (Multiple E&M Same day GBDF GRS, Unspecified dx code outpt GBDF GRS, Unspecified dx code prof GBDF GRS, NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS, Nebulizer A52466 IPERP-132 GBDF GRS, No match of Procedure code GBDF GRS) - requires `--gbdf_grs` flag
- `--NYKTS122`, `--NYKTS124`, `--NYKTS125`, `--NYKTS126`, `--NYKTS127`, `--NYKTS128`, `--NYKTS129`, `--NYKTS130`, `--NYKTS132`: Process WGS_NYK models (Revenue code to HCPCS Alignment edit WGS NYK, Observation Services WGS NYK, add_on without base WGS NYK) - requires `--wgs_nyk` flag (Must use --NYKTSXX format)
- `--all`: Process all configured models (requires either --wgs_csbd, --gbdf_mcr, --gbdf_grs, or --wgs_nyk flag)
- `--list`: List all available TS models (standalone) or generate timing report (with model flags)
- `--no-postman`: Skip Postman collection generation
- `--help`: Show help message with examples

**What the script does:**
1. Rename and move files according to model configuration
2. Automatically generate a Postman collection (unless `--no-postman` is used)
3. Provide instructions for importing into Postman
4. Show detailed processing summary

**Model Configuration:**
The script uses `models_config.py` to define available models. Each model includes:
- `edit_id`: Unique identifier (e.g., "rvn001", "rvn002")
- `code`: Code identifier (e.g., "00W5", "00W6")
- `source_dir`: Source directory path
- `dest_dir`: Destination directory path
- `postman_collection_name`: Name for the Postman collection

Example configuration:
```python
MODELS_CONFIG = [
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
        "source_dir": "TS_02_REVENUE_WGS_CSBD_rvn002_00W6_payloads_sur/regression",
        "dest_dir": "renaming_jsons/TS_02_REVENUE_WGS_CSBD_rvn002_00W6_payloads_dis/regression",
        "postman_collection_name": "TS_02_REVENUE_WGS_CSBD_rvn002_00W6"
    }
]
```

#### 2. Original Script (File Renaming Only)

```bash
# Run the main processor for file renaming and Postman generation
python main_processor.py --help
```

#### 3. Postman Collection Management

```bash
# Generate Postman collection for all files
python postman_cli.py generate --collection-name "MyTestCollection"

# Generate collection for specific directory
python postman_cli.py generate --directory "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"

# List available directories
python postman_cli.py list-directories

# Show statistics for a directory
python postman_cli.py stats --directory "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"

# Generate collections for all directories
python postman_cli.py generate-all

# Validate a collection
python postman_cli.py validate --collection-path "postman_collections/test_collection/postman_collection.json"
```

#### 4. Standalone Postman Generator (Updated & Working)

```bash
# Generate collection for specific directory (current working directories)
python postman_generator.py --directory "TS_07_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis"
python postman_generator.py --directory "TS_100_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis"
python postman_generator.py --directory "TS_120_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis"
python postman_generator.py --directory "TS_13_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis"
python postman_generator.py --directory "TS_50_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis"

# Generate collection with custom parameters
python postman_generator.py --source-dir "renaming_jsons" --output-dir "postman_collections" --collection-name "CustomCollection"

# List available directories
python postman_generator.py --list-directories

# Show statistics for specific directory
python postman_generator.py --stats "TS_07_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis"
```

**✅ Current Working Directories:**
- `TS_07_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis`
- `TS_100_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis`
- `TS_120_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis`
- `TS_13_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis`
- `TS_50_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis`

### What the Scripts Do

#### File Renaming Process
1. **Source Validation**: Checks if the source directory exists
2. **Directory Creation**: Creates the destination directory if it doesn't exist
3. **File Discovery**: Finds all JSON files in the source directory
4. **Parsing**: Extracts components from each filename
5. **Mapping**: Applies suffix mapping rules to determine correct suffix
6. **Renaming**: Generates new filenames according to the 5-part template
7. **File Operations**: Copies files to destination with new names and removes originals
8. **Logging**: Provides detailed output of all operations

#### Postman Collection Generation
1. **File Analysis**: Scans renamed JSON files for test case information
2. **Request Creation**: Creates Postman requests with proper headers and body
3. **Collection Structure**: Builds Postman collection with metadata
4. **File Generation**: Saves collection in Postman-compatible JSON format
5. **Validation**: Ensures collection structure is correct

## Postman Collection Features

### Generated Collection Structure
- **Collection Name**: Based on input parameters
- **Request Names**: Match the renamed filenames exactly
- **HTTP Methods**: POST requests for all test types
- **Headers**: Pre-configured with test case metadata
- **Request Bodies**: Contains the JSON content from test files
- **Variables**: Base URL and test case ID variables

### Headers Included
- `Content-Type: application/json`
- `X-Edit-ID: rvn001` (configurable)
- `X-EOB-Code: 00W5` (configurable)
- `X-Test-Type: LR/NR/EX` (based on test case type)

### HTTP Methods by Test Type
- **Positive (LR)**: POST requests
- **Negative (NR)**: POST requests  
- **Exclusion (EX)**: POST requests

### URL Structure
```
https://pi-timber-claims-api-uat.ingress-nginx.dig-gld-shared.gcpdns.internal.das/claims/Timber/GetRecommendations
```

Where:
- `{{baseUrl}}`: Defaults to `http://localhost:3000` (configurable)
- `{{tc_id}}`: Test case ID extracted from filename

## Example Output

### Command-Line Interface Output

#### Processing TS01 Model with WGS_CSBD Flag
```bash
$ python main_processor.py --wgs_csbd --CSBDTS01
✅ Configuration loaded with dynamic discovery

🚀 Processing 1 model(s)...
============================================================

📋 Processing Model 1/1: TS_01 (RULEEM000001_W04)
----------------------------------------
Files to be renamed and moved:
============================================================
Current: TC#01_od#deny.json
Converting to new template...
New:     TC#01_od#RULEEM000001#W04#LR.json
Moving to: renaming_jsons\TS_01_Covid_WGS_CSBD_RULEEM000001_W04_dis\regression
----------------------------------------
[INFO] Generated random 11-digit number for KEY_CHK_CDN_NBR (payload level): 62620451899
✓ Successfully copied and renamed: TC#01_od#deny.json → TC#01_od#RULEEM000001#W04#LR.json
✓ Removed original file: TC#01_od#deny.json

============================================================
Renaming and moving completed!
Files moved to: renaming_jsons\TS_01_Covid_WGS_CSBD_RULEEM000001_W04_dis\regression

============================================================
Generating Postman collection...
----------------------------------------
Found 1 JSON files for collection 'TS_01_Covid_Collection'
✅ Generated Postman collection: postman_collections\TS_01_Covid_Collection\postman_collection.json
   - Collection: TS_01_Covid_Collection
   - Requests: 1
   - Files processed: 1

🎯 Ready for API testing!
============================================================
To use this collection:
1. Open Postman
2. Click 'Import'
3. Select the file: postman_collections\TS_01_Covid_Collection\postman_collection.json
4. Start testing your APIs!

✅ Model TS_01 (RULEEM000001_W04): Successfully processed 1 files

============================================================
📊 PROCESSING SUMMARY
============================================================
Models processed: 1
Successful models: 1
Total files processed: 1

✅ SUCCESSFUL MODELS:
   • TS_01 (RULEEM000001_W04): 1 files

📦 POSTMAN COLLECTIONS GENERATED:
To use these collections:
1. Open Postman
2. Click 'Import'
3. Select the collection files from 'postman_collections' folder
4. Start testing your APIs!

🎉 Successfully processed 1 files!
Files are now ready for API testing with Postman.
```

#### Error Handling Example
```bash
$ python main_processor.py --CSBDTS01
✅ Configuration loaded with dynamic discovery
❌ Error: --wgs_csbd flag is required for TS model processing!

Please use the --wgs_csbd flag with TS model commands:
  python main_processor.py --wgs_csbd --CSBDTS01    # Process TS01 model (Covid)
  python main_processor.py --wgs_csbd --CSBDTS02    # Process TS02 model (Laterality Policy)
  python main_processor.py --wgs_csbd --CSBDTS03    # Process TS03 model
  python main_processor.py --wgs_csbd --CSBDTS04    # Process TS04 model
  python main_processor.py --wgs_csbd --CSBDTS05    # Process TS05 model
  python main_processor.py --wgs_csbd --CSBDTS06    # Process TS06 model
  python main_processor.py --wgs_csbd --CSBDTS07    # Process TS07 model
  python main_processor.py --wgs_csbd --CSBDTS08    # Process TS08 model
  python main_processor.py --wgs_csbd --CSBDTS09    # Process TS09 model
  python main_processor.py --wgs_csbd --CSBDTS10    # Process TS10 model
  python main_processor.py --wgs_csbd --CSBDTS11    # Process TS11 model
  python main_processor.py --wgs_csbd --CSBDTS12    # Process TS12 model
  python main_processor.py --wgs_csbd --CSBDTS13    # Process TS13 model
  python main_processor.py --wgs_csbd --CSBDTS14    # Process TS14 model
  python main_processor.py --wgs_csbd --CSBDTS15    # Process TS15 model
  python main_processor.py --wgs_csbd --all     # Process all discovered models

Use --help for more information.
```

#### Alternative Command Format Examples
```bash
# Using the main processor with different models (WGS_CSBD flag required)
$ python main_processor.py --wgs_csbd --CSBDTS01
✅ Configuration loaded with dynamic discovery
🚀 Processing 1 model(s)...
...

$ python main_processor.py --wgs_csbd --CSBDTS15
✅ Configuration loaded with dynamic discovery
🚀 Processing 1 model(s)...
...

$ python main_processor.py --wgs_csbd --all
✅ Configuration loaded with dynamic discovery
🚀 Processing 15 model(s)...
...
```

### File Renaming Output
```
Files to be renamed and moved:
============================================================
Current: TC#01_12345#deny.json
Converting to new template...
New:     TC#01_12345#rvn001#00W5#LR.json
Moving to: C:\Users\Vishnu\Cursor_AI_proj\GIT_HUB\renaming_postman_collection\renaming_jsons\TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis\regression
----------------------------------------
✓ Successfully copied and renamed: TC#01_12345#deny.json → TC#01_12345#rvn001#00W5#LR.json
✓ Removed original file: TC#01_12345#deny.json
...
============================================================
Renaming and moving completed!
Files moved to: [destination_path]
```

### Postman Collection Generation Output
```
============================================================
Generating Postman collection...
----------------------------------------
Found 4 JSON files for collection 'RevenueTestCollection'
✅ Generated Postman collection: postman_collections\revenue_test_collection\postman_collection.json
   - Collection: RevenueTestCollection
   - Requests: 4
   - Files processed: 4

🎯 Ready for API testing!
============================================================
To use this collection:
1. Open Postman
2. Click 'Import'
3. Select the file: postman_collections\revenue_test_collection\postman_collection.json
4. Start testing your APIs!
```

## File Structure

### Test Case JSON Format
The script processes JSON files containing test case information:

```json
{
  "testCaseId": "TC_001",
  "testCaseName": "Revenue Calculation Positive Test",
  "testSuite": "Revenue_WGS_CSBD",
  "priority": "High",
  "testType": "Regression",
  "description": "Verify revenue calculation functionality with valid input data",
  "testData": {
    "revenueInputs": {
      "baseAmount": 1000.00,
      "taxRate": 0.08,
      "discountPercentage": 0.10,
      "currency": "USD",
      "region": "North America"
    }
  },
  "testSteps": [...],
  "testResults": {...}
}
```

### Generated Postman Collection Format (Updated)
```json
{
  "version": "1",
  "name": "TS_07_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis API Collection",
  "type": "collection",
  "items": [
    {
      "uid": "5b306e7b-3272-472c-8dc7-d5f5044dd029",
      "name": "TC#01_od#rvn011#00W11#LR",
      "type": "http",
      "method": "POST",
      "url": "https://pi-timber-claims-api-uat.ingress-nginx.dig-gld-shared.gcpdns.internal.das/claims/Timber/GetRecommendations",
      "headers": [
        {
          "uid": "2221e60f-799e-4e9d-8e8d-85e81d1434c6",
          "name": "Content-Type",
          "value": "application/json",
          "enabled": true
        },
        {
          "uid": "b379639e-67d2-4a23-9449-9c397755b2b8",
          "name": "X-Edit-ID",
          "value": "rvn011",
          "enabled": true
        },
        {
          "uid": "610e87c2-5ae8-4295-a1f1-35e8c557f044",
          "name": "X-EOB-Code",
          "value": "00W11",
          "enabled": true
        },
        {
          "uid": "9b8afea3-b663-4d61-97b8-7a6ef8bfac25",
          "name": "X-Test-Type",
          "value": "LR",
          "enabled": true
        }
      ],
      "body": {
        "mode": "raw",
        "raw": "{\n  \"testCase\": \"TC#01_od#rvn011#00W11#LR\",\n  \"testSuite\": \"TS_07_REVENUE_WGS_CSBD_rvn011_00W11_payloads_dis\",\n  \"testType\": \"regression\",\n  \"payload\": {\n    \"revenue\": {\n      \"wgs\": {\n        \"csbd\": {\n          \"rvn011\": {\n            \"week\": \"00W11\",\n            \"type\": \"LR\",\n            \"testId\": \"od\"\n          }\n        }\n      }\n    }\n  },\n  \"expectedResult\": \"success\",\n  \"description\": \"Revenue WGS CSBD rvn011 00W11 LR test case\",\n  \"created\": \"2024-01-01T00:00:00Z\"\n}"
      }
    }
  ]
}
```

## Excel Reporting System

The project includes a comprehensive Excel reporting system that automatically tracks and reports timing data for all operations:

### Excel Report Features:
- **Automatic Timing Tracking**: Tracks timing for file renaming and Postman collection generation
- **Professional Excel Reports**: Generates detailed Excel reports with timing data and statistics
- **Performance Analytics**: Calculates total time, average time, and performance metrics
- **Report Management**: Automatic report generation with timestamps and status tracking
- **Multiple Report Formats**: Supports individual model reports and batch processing reports

### Report Columns:
1. **TC#ID** - Test Case ID extracted from directory names
2. **Model LOB** - Line of Business (WGS_CSBD, GBDF_MCR, GBDF_GRS)
3. **Model Name** - Model name (Covid, Multiple E&M Same day, etc.)
4. **Edit ID** - Edit identifier (e.g., RULEEM000001, RULEEMSD000002)
5. **EOB Code** - EOB code (e.g., W04, v04, 00W17, v09)
6. **Naming Convention Time (ms)** - Time taken for file renaming
7. **Postman Collection Time (ms)** - Time taken for Postman collection generation
8. **Total Time (ms)** - Sum of both operations
9. **Average Time (ms)** - Average time per operation
10. **Timestamp** - When the operation was performed
11. **Status** - Operation status (Success, Failed, etc.)

### Report Location:
Excel reports are automatically generated in the `reports/` directory with organized subdirectories:
- `reports/collection_reports/` - Contains Excel timing reports with timestamps:
  - `JSON_Renaming_Timing_Report_WGS_CSBD_YYYYMMDD_HHMMSS.xlsx`
  - `JSON_Renaming_Timing_Report_GBDF_MCR_YYYYMMDD_HHMMSS.xlsx`
  - `JSON_Renaming_Timing_Report_GBDF_GRS_YYYYMMDD_HHMMSS.xlsx`
- `reports/list_reports/` - Contains list-based reports and analytics

For detailed Excel reporting information, see `EXCEL_REPORTING_GUIDE.md`.

### Timing Report Generation with --list Flag

The `--list` flag has dual functionality depending on how it's used:

#### 1. Standalone --list Command
```bash
python main_processor.py --list
```
**Purpose**: Lists all available models with detailed information
**Output**: 
- Shows all WGS_CSBD and GBDF models
- Displays Edit IDs, Codes, and Collection names
- Provides usage examples
- Shows model counts and summaries

#### 2. Model-Specific --list Command
```bash
python main_processor.py --wgs_csbd --CSBDTS47 --list    # Generate timing report for TS47 WGS_CSBD
python main_processor.py --gbdf_mcr --GBDTS47 --list    # Generate timing report for TS47 GBDF MCR
python main_processor.py --gbdf_grs --TS139 --list   # Generate timing report for TS139 GBDF GRS
```
**Purpose**: Generates timing reports for specific models without processing files
**Output**:
- Processes files in the source directory
- Measures timing for file renaming operations
- Estimates Postman collection generation time
- Saves detailed Excel report to `reports/list_reports/`
- Provides performance analytics and statistics

**Report Features**:
- Individual file processing times
- Total processing time
- Average time per file
- Success/failure status for each file
- Timestamped Excel reports with model-specific naming

## KEY_CHK_DCN_NBR Generator

The project includes an automatic KEY_CHK_DCN_NBR generator that creates random 11-digit numbers for test case validation:

### Generator Features:
- **Random Number Generation**: Creates 11-digit numbers between 10000000000 and 99999999999
- **Dual-Level Updates**: Updates KEY_CHK_DCN_NBR fields at both root level and payload level
- **Smart Detection**: Automatically detects existing KEY_CHK_DCN_NBR fields and updates them
- **WGS_CSBD Integration**: Works seamlessly with WGS_CSBD header/footer transformation

### How It Works:
1. **Field Detection**: Scans JSON files for existing KEY_CHK_DCN_NBR fields
2. **Number Generation**: Creates a new random 11-digit number for each field found
3. **Field Updates**: Updates both root-level and payload-level KEY_CHK_DCN_NBR fields
4. **Logging**: Provides detailed logging of all generated numbers

### Example Output:
```json
{
  "KEY_CHK_DCN_NBR": "42488458762",
  "payload": {
    "KEY_CHK_DCN_NBR": "85872060683",
    "test_case": "TC#01_sample#deny"
  }
}
```

### Console Output:
```
[INFO] Generated random 11-digit number for KEY_CHK_DCN_NBR (root level): 42488458762
[INFO] Generated random 11-digit number for KEY_CHK_DCN_NBR (payload level): 85872060683
```

## How the Mapping Works

The script uses a sophisticated nested dictionary structure for suffix mapping. Here's how it works:

### Mapping Structure
```python
suffix_mapping = {
    "positive": {
        "deny": "LR",    # deny -> LR
    },
    "negative": {
        "bypass": "NR",  # bypass -> NR
    },
    "Exclusion": {
        "market": "EX",   # market -> EX
        "date": "EX"     # date -> EX
    }
}
```

### Lookup Algorithm
1. **Input**: The script receives a suffix (e.g., "market", "date", "deny")
2. **Search**: It searches through all categories in the mapping
3. **Match**: When a match is found, it returns the mapped value
4. **Fallback**: If no match is found, it uses the original suffix

### Example Lookup Process
- **Input**: `"market"`
- **Search**: 
  - Check "positive" category → No match
  - Check "negative" category → No match  
  - Check "Exclusion" category → **Found!** `"market": "EX"`
- **Output**: `"EX"`

This structure allows for:
- **Categorization**: Grouping related suffixes together
- **Multiple Mappings**: Several suffixes can map to the same output (e.g., both "market" and "date" → "EX")
- **Easy Extension**: Adding new categories or mappings is straightforward

## Customization

### Modifying Parameters
To change the hardcoded parameters, edit the following variables in the scripts:

```python
# Parameters extracted from folder name
edit_id = "rvn001"        # Change this to your edit ID
code = "00W5"             # Change this to your code

# Source directory containing the files
source_dir = "WGS_CSBD/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/regression"

# Destination directory
dest_dir = r"your\custom\destination\path"
```

### Adding New Suffix Mappings
To add new suffix mappings, modify the `suffix_mapping` dictionary:

```python
suffix_mapping = {
    "positive": {
        "deny": "LR",        # Limited Response test cases
        "new_positive": "LR"  # Add new positive mappings here
    },
    "negative": {
        "bypass": "NR",      # No Response test cases
        "new_negative": "NR"  # Add new negative mappings here
    },
    "Exclusion": {
        "market": "EX",      # Exception test cases
        "date": "EX",        # Exception test cases
        "new_exclusion": "EX"  # Add new exclusion mappings here
    }
}
```

**Note**: The script searches through all categories to find the correct mapping for each suffix. Multiple suffixes can map to the same output suffix (e.g., both `market` and `date` map to `EX`).

### Customizing Postman Collections
To modify Postman collection generation:

```python
# Change base URL
generator = PostmanCollectionGenerator(
    source_dir="renaming_jsons",
    output_dir="postman_collections"
)

# Modify HTTP methods
method_map = {
    'LR': 'POST',  # Limited Response
    'NR': 'GET',   # No Response - changed to GET
    'EX': 'PUT'    # Exception - changed to PUT
}

# Customize headers
headers = [
    {
        "key": "Content-Type",
        "value": "application/json",
        "type": "text"
    },
    {
        "key": "X-Custom-Header",
        "value": "custom_value",
        "type": "text"
    }
]
```

## Error Handling

The scripts include comprehensive error handling:

- **Directory Validation**: Checks if source directory exists
- **File Format Validation**: Warns about files that don't match expected format
- **File Operation Safety**: Uses try-catch blocks for file operations
- **Postman Generation Errors**: Handles collection generation failures gracefully
- **Detailed Logging**: Provides clear feedback for all operations

## Troubleshooting

### Common Issues

1. **No Model Specified Error**
   ```
   ❌ Error: No model specified!
   ```
   - **Solution**: Always specify a model using `--wgs_csbd --CSBDTS01` through `--wgs_csbd --CSBDTS15`, or `--wgs_csbd --all`
   - **Examples**: 
     - `python main_processor.py --wgs_csbd --CSBDTS01`
     - `python main_processor.py --wgs_csbd --all`

2. **Missing WGS_CSBD Flag Error**
   ```
   ❌ Error: --wgs_csbd flag is required for TS model processing!
   ```
   - **Solution**: Always include the `--wgs_csbd` flag when processing WGS_CSBD TS models
   - **Examples**: 
     - `python main_processor.py --wgs_csbd --CSBDTS01`
     - `python main_processor.py --wgs_csbd --CSBDTS15`

3. **Missing GBDF_MCR Flag Error**
   ```
   ❌ Error: --gbdf_mcr flag is required for GBDF MCR TS model processing!
   ```
   - **Solution**: Always include the `--gbdf_mcr` flag when processing GBDF MCR models
   - **Examples**: 
     - `python main_processor.py --gbdf_mcr --GBDTS47` (Covid GBDF MCR model) - Recommended format
     - `python main_processor.py --gbdf_mcr --GBDTS138` (Multiple E&M Same day GBDF MCR model) - Recommended format
     - `python main_processor.py --gbdf_mcr --all`
   - **Note**: There are two different TS47 models:
     - `python main_processor.py --wgs_csbd --CSBDTS47` (Multiple Billing of Obstetrical Services - WGS_CSBD)
     - `python main_processor.py --gbdf_mcr --GBDTS47` (Covid GBDF MCR - GBDF MCR) - Recommended format

4. **Missing GBDF_GRS Flag Error**
   ```
   ❌ Error: --gbdf_grs flag is required for GBDF GRS TS model processing!
   ```
   - **Solution**: Always include the `--gbdf_grs` flag when processing GBDF GRS models
   - **Examples**: 
     - `python main_processor.py --gbdf_grs --TS139` (Multiple E&M Same day GBDF GRS model)
     - `python main_processor.py --gbdf_grs --all`

5. **Missing WGS_NYK Flag Error**
   ```
   ❌ Error: --wgs_nyk flag is required for NYKTS model processing!
   ```
   - **Solution**: Always include the `--wgs_nyk` flag when processing WGS_NYK models
   - **Examples**: 
     - `python main_processor.py --wgs_nyk --NYKTS122` (Revenue code to HCPCS Alignment edit WGS NYK model) - Must use --NYKTSXX format
     - `python main_processor.py --wgs_nyk --NYKTS130` (Observation Services WGS NYK model) - Must use --NYKTSXX format
     - `python main_processor.py --wgs_nyk --NYKTS130` (Observation Services WGS NYK model) - Must use --NYKTSXX format
     - `python main_processor.py --wgs_nyk --NYKTS132` (add_on without base WGS NYK model) - Must use --NYKTSXX format
     - `python main_processor.py --wgs_nyk --all`
   - **Note**: WGS_NYK models require the `--NYKTSXX` format (e.g., `--NYKTS130`) instead of `--TSXX` format

6. **Model Not Found in Configuration**
   ```
   ❌ Error: TS01 model (rvn001) not found in configuration!
   ```
   - **Solution**: Check `models_config.py` to ensure the model is properly configured
   - **Verify**: The `edit_id` matches what you're trying to process

7. **Configuration File Not Found**
   ```
   ❌ Error: models_config.py not found!
   ```
   - **Solution**: Ensure `models_config.py` exists in the same directory as the script
   - **Check**: The file contains proper `MODELS_CONFIG` definitions

8. **Source Directory Not Found**
   - Ensure the source directory path is correct in `models_config.py`
   - Check if the directory exists in the expected location
   - Verify the path matches your actual file structure

9. **Permission Errors**
   - Ensure you have read/write permissions for both source and destination directories
   - Run the script with appropriate privileges

10. **File Format Errors**
   - Verify that input files follow the expected naming convention: `TC#XX_XXXXX#suffix.json`
   - Check that files are valid JSON format
   - Ensure files have exactly 3 parts separated by `#` characters

11. **Postman Collection Generation Errors**
   - Check if the destination directory exists
   - Verify that renamed files are in the correct location
   - Ensure JSON files are valid and readable

### Debug Mode
To add more detailed logging, you can modify the scripts to include debug information:

```python
# Add debug logging
print(f"Processing file: {filename}")
print(f"Parts: {parts}")
print(f"Mapped suffix: {mapped_suffix}")
print(f"Postman request name: {request_name}")
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## 📊 Presentation Tools

### Converting Markdown to PowerPoint

To convert the team presentation from Markdown to PowerPoint format:

```bash
# Convert team_presentation.md to PowerPoint format
pandoc team_presentation.md -o team_presentation.pptx
```

**Prerequisites:**
- Install pandoc: https://pandoc.org/installing.html
- Ensure `team_presentation.md` exists in the project root

**Note:** The presentation file is located in the `PPT/` directory and contains project documentation and team information.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the error messages in the console output
3. Verify file paths and permissions
4. Ensure input files follow the expected naming convention
5. Check Postman collection generation logs

---

## 📋 Project Status Summary

**✅ Current Status: FULLY UPDATED & FUNCTIONAL**

The project has been comprehensively updated with modern architecture and enhanced functionality:

### ✅ What's Working:
- **19 Active Test Suites**: TS_01 through TS_15, TS20, TS46-TS47, and CSBD_TS48 with diverse model types
- **WGS_CSBD Flag Implementation**: Mandatory flag requirement for all TS model processing
- **KEY_CHK_CDN_NBR Generator**: Automatic random 11-digit number generation for test validation
- **WGS_CSBD Header/Footer Transformation**: Proper structure application with field updates
- **Dynamic Discovery**: Automatic detection of TS folders and model parameters
- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Multiple Interfaces**: Both integrated (`main_processor.py`) and standalone (`postman_cli.py`) workflows
- **Professional Collections**: Properly structured Postman collections with accurate naming
- **Comprehensive Documentation**: Visual architecture diagrams and detailed explanations

### 🎯 Key Files:
- **Test Data**: `renaming_jsons/TS_XX_*_dis/regression/`
- **Collections**: `postman_collections/TS_XX_*_Collection/`
- **Architecture**: `project_architecture_diagram.md`
- **Generator**: `postman_generator.py` (enhanced with better structure)
- **Discovery**: `dynamic_models.py` (automatic TS folder detection)

### 🚀 Quick Commands:
```bash
# Process WGS_CSBD models (TS01-TS15, TS20, TS46-TS47, CSBD_TS48 supported with --wgs_csbd flag)
python main_processor.py --wgs_csbd --CSBDTS01    # Covid Collection
python main_processor.py --wgs_csbd --CSBDTS02    # Laterality Collection
python main_processor.py --wgs_csbd --CSBDTS03    # Revenue Sub Edit 5 Collection
python main_processor.py --wgs_csbd --CSBDTS04    # Revenue Sub Edit 4 Collection
python main_processor.py --wgs_csbd --CSBDTS05    # Revenue Sub Edit 3 Collection
python main_processor.py --wgs_csbd --CSBDTS06    # Revenue Sub Edit 2 Collection
python main_processor.py --wgs_csbd --CSBDTS07    # Revenue Sub Edit 1 Collection
python main_processor.py --wgs_csbd --CSBDTS08    # Lab panel Model Collection
python main_processor.py --wgs_csbd --CSBDTS09    # Device Dependent Procedures Collection
python main_processor.py --wgs_csbd --CSBDTS10    # Recovery Room Reimbursement Collection
python main_processor.py --wgs_csbd --CSBDTS11    # Revenue Code to HCPCS Xwalk-1B Collection
python main_processor.py --wgs_csbd --CSBDTS12    # Incidentcal Services Facility Collection
python main_processor.py --wgs_csbd --CSBDTS13    # Revenue model CR v3 Collection
python main_processor.py --wgs_csbd --CSBDTS14    # HCPCS to Revenue Code Xwalk Collection
python main_processor.py --wgs_csbd --CSBDTS15    # revenue model Collection
python main_processor.py --wgs_csbd --CSBDTS20    # RadioservicesbilledwithoutRadiopharma Collection
python main_processor.py --wgs_csbd --CSBDTS46    # Multiple E&M Same day Collection
python main_processor.py --wgs_csbd --CSBDTS47    # Multiple Billing of Obstetrical Services Collection
python main_processor.py --wgs_csbd --CSBDTS48    # Revenue code to HCPCS Alignment edit Collection

# Process GBDF MCR models (with --gbdf_mcr flag)
python main_processor.py --gbdf_mcr --GBDTS47    # Covid GBDF MCR Collection
python main_processor.py --gbdf_mcr --GBDTS48    # Multiple E&M Same day GBDF MCR Collection
python main_processor.py --gbdf_mcr --GBDTS60    # Unspecified dx code outpt GBDF MCR Collection
python main_processor.py --gbdf_mcr --GBDTS61    # Unspecified dx code prof GBDF MCR Collection
python main_processor.py --gbdf_mcr --GBDTS138   # Multiple E&M Same day GBDF MCR Collection
python main_processor.py --gbdf_mcr --GBDTS140   # NDC UOM Validation Edit Expansion Iprep-138 GBDF MCR Collection
python main_processor.py --gbdf_mcr --GBDTS144   # Nebulizer A52466 IPERP-132 GBDF MCR Collection
python main_processor.py --gbdf_mcr --GBDTS146   # No match of Procedure code GBDF MCR Collection

# Process GBDF GRS models (with --gbdf_grs flag)
python main_processor.py --gbdf_grs --TS49    # Multiple E&M Same day GBDF GRS Collection
python main_processor.py --gbdf_grs --TS59    # Unspecified dx code outpt GBDF GRS Collection
python main_processor.py --gbdf_grs --TS61    # Unspecified dx code prof GBDF GRS Collection
python main_processor.py --gbdf_grs --TS62    # Unspecified dx code prof GBDF GRS Collection
python main_processor.py --gbdf_grs --TS139   # Multiple E&M Same day GBDF GRS Collection
python main_processor.py --gbdf_grs --TS141   # NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS Collection
python main_processor.py --gbdf_grs --TS145   # Nebulizer A52466 IPERP-132 GBDF GRS Collection
python main_processor.py --gbdf_grs --TS147   # No match of Procedure code GBDF GRS Collection

# Process WGS_NYK models (with --wgs_nyk flag - Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS130   # Observation Services WGS NYK Collection
python main_processor.py --wgs_nyk --NYKTS124   # Observation Services WGS NYK Collection
python main_processor.py --wgs_nyk --NYKTS125   # Observation Services WGS NYK Collection
python main_processor.py --wgs_nyk --NYKTS126   # Observation Services WGS NYK Collection
python main_processor.py --wgs_nyk --NYKTS127   # Observation Services WGS NYK Collection
python main_processor.py --wgs_nyk --NYKTS128   # Observation Services WGS NYK Collection
python main_processor.py --wgs_nyk --NYKTS129   # Observation Services WGS NYK Collection
python main_processor.py --wgs_nyk --NYKTS130   # Observation Services WGS NYK Collection

# Process all models at once
python main_processor.py --wgs_csbd --all     # All WGS_CSBD models
python main_processor.py --gbdf_mcr --all     # All GBDF MCR models
python main_processor.py --gbdf_grs --all     # All GBDF GRS models
python main_processor.py --wgs_nyk --all     # All WGS_NYK models

# Standalone Postman operations
python postman_cli.py generate-all
python postman_cli.py list-directories
```

**Note**: This script modifies file locations and names. Always backup your data before running it on production files.

## 🗂️ Folder Management Commands

### Commands to Empty Folders

#### For Git Bash (Recommended):
```bash
# Empty renaming_jsons folder (removes all contents)
rm -rf renaming_jsons/*

# Empty postman_collections folder (removes all contents)
rm -rf postman_collections/*

# Empty both folders at once
rm -rf renaming_jsons/* postman_collections/*
```

#### For Windows Command Prompt/PowerShell:
```cmd
# Empty renaming_jsons folder (removes and recreates)
rmdir /s /q renaming_jsons
mkdir renaming_jsons

# Empty postman_collections folder (removes and recreates)
rmdir /s /q postman_collections
mkdir postman_collections
```

#### Alternative Git Bash Commands (removes and recreates folders):
```bash
# Empty renaming_jsons folder (removes and recreates)
rm -rf renaming_jsons
mkdir renaming_jsons

# Empty postman_collections folder (removes and recreates)
rm -rf postman_collections
mkdir postman_collections
```

### Current Folder Contents:

**`renaming_jsons` folder contains:**
- 5 WGS_CSBD subdirectories (TS_01, TS_02, TS_03, TS_46, TS_47)
- 13 GBDF subdirectories (TS_47, TS_48, TS_49, TS_59, TS_60, TS_61, TS_62, TS_138, TS_139, TS_140, TS_141, TS_146, TS_147)
- Each with a `regression` subfolder containing JSON test case files
- Diverse model types: Covid, Laterality, Revenue, Lab, Device, Recovery, HCPCS, Incidentcal Services, Multiple E&M Same day, NDC UOM Validation Edit Expansion Iprep-138, No match of Procedure code

**`postman_collections` folder contains:**
- 5 WGS_CSBD subdirectories (TS_01_Covid_Collection, TS_02_Laterality_Collection, TS_03_Revenue_Collection, TS_46_Multiple E&M Same day_Collection, TS_47_Multiple Billing of Obstetrical Services_Collection)
- 13 GBDF subdirectories (TS_47_Covid_gbdf_mcr_Collection, TS_48_Multiple E&M Same day_gbdf_mcr_Collection, TS_49_Multiple E&M Same day_gbdf_grs_Collection, TS_59_Unspecified_dx_code_outpt_gbdf_grs_Collection, TS_60_Unspecified_dx_code_outpt_gbdf_mcr_Collection, TS_61_Unspecified_dx_code_prof_gbdf_grs_Collection, TS_62_Unspecified_dx_code_prof_gbdf_grs_Collection, TS_138_Multiple E&M Same day_gbdf_mcr_Collection, TS_139_Multiple E&M Same day_gbdf_grs_Collection, TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_Collection, TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_Collection, TS_146_No match of Procedure code_gbdf_mcr_Collection, TS_147_No match of Procedure code_gbdf_grs_Collection)
- Each contains properly structured Postman collection files
- Professional naming and organization

**`reports` folder contains:**
- `collection_reports/` - Excel timing reports with timestamps and performance analytics
- `list_reports/` - List-based reports and analytics (currently available for future use)
- Professional formatting with headers and color coding
- Model breakdown and status tracking across all processed models

**`source_folder` folder contains:**
- Original source files before processing
- WGS_CSBD and GBDF source directories
- Maintains original file structure for reference

⚠️ **Warning**: The `rm -rf` command will permanently delete all contents. Make sure you want to remove these files before running the commands.