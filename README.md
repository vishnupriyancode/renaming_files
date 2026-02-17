# File Renaming Project with Postman Collection Generation

A Python script for automatically renaming and organizing test case JSON files based on predefined naming conventions and suffix mappings, with integrated Postman collection generation for API testing.

---

## 👤 For Users

**What this does:** Renames test-case JSON files and (optionally) generates Postman collections for API testing. Supports WGS_CSBD, WGS_NYK, GBDF MCR, and GBDF GRS model types.

**Quick start:**
1. **Install:** `pip install -r requirements.txt`
2. **Run:** `python main_processor.py --wgs_csbd --CSBDTS01` or `python main_processor.py --wgs_nyk --NYKTS124`
3. **Help:** `python main_processor.py --help` or `python main_processor.py --list` to see available models

**Where to go next:**
- [Getting Started (New Users)](#-getting-started-new-users) — setup and first run
- [User Commands & Model Commands](#-user-commands--model-commands) — all CLI options and how to combine them
- [Quick Start Commands](#-quick-start-commands-verified--ready-to-use) — copy-paste commands by model type
- [Troubleshooting](#troubleshooting) — common issues and fixes

---

## 🚀 Getting Started (New Users)

1. **Install dependencies:** `pip install -r requirements.txt`
2. **Configure environment (optional):** Copy `.env.example` to `.env` and adjust settings (e.g., `ENABLE_REPORT_GENERATION`)
3. **Run a model:** `python main_processor.py --wgs_csbd --CSBDTS01` or `python main_processor.py --wgs_nyk --NYKTS124`

For full command reference, see [Quick Start Commands](#-quick-start-commands-verified--ready-to-use).

## 📑 Table of Contents

- [For Users](#-for-users)
- [Getting Started (New Users)](#-getting-started-new-users)
- [Recent Updates & Fixes](#-recent-updates--fixes)
- [Quick Start Commands](#-quick-start-commands-verified--ready-to-use)
- [User Commands & Model Commands](#-user-commands--model-commands)
- [Model Summary & Quick Reference](#-model-summary--quick-reference)
- [Overview](#overview)
- [Model Types Supported](#-model-types-supported)
- [System Architecture](#️-system-architecture)
- [Project Structure](#project-structure)
- [Features](#features)
- [Recent Fixes & Improvements](#-recent-fixes--improvements)
- [Naming Convention](#naming-convention)
- [Parameters](#parameters)
- [Usage](#usage)
- [Auto Edit Processor](#-auto-edit-processor)
- [Postman Collection Features](#postman-collection-features)
- [Example Output](#example-output)
- [File Structure](#file-structure)
- [Excel Reporting System](#excel-reporting-system)
- [KEY_CHK_DCN_NBR Generator](#key_chk_dcn_nbr-generator)
- [How the Mapping Works](#how-the-mapping-works)
- [Customization](#customization)
- [Error Handling](#error-handling)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Presentation Tools](#-presentation-tools)
- [Support](#support)
- [Project Status Summary](#-project-status-summary)
- [Folder Management Commands](#️-folder-management-commands)

## 🔧 Recent Updates & Fixes

**✅ CSBDTS59 RefDB Support & Windows Encoding Fix (Latest Update)**

The project has been enhanced with refdb support for CSBDTS59 and Windows encoding improvements:

- **✅ Added CSBDTS59 RefDB Support**: CSBDTS59 (Antepartum Services) is now supported for refdb value replacement
- **✅ Windows Encoding Fix**: Fixed Unicode character encoding issues on Windows systems for refdb processing
- **✅ Enhanced Error Handling**: Improved error messages and handling for refdb processing on Windows
- **✅ UTF-8 Encoding**: Automatic UTF-8 encoding configuration for stdout/stderr on Windows
- **✅ Comprehensive Documentation**: Updated all refdb examples and documentation to include CSBDTS59

**Examples:**
```bash
# Process CSBDTS59 with refdb value replacement
python main_processor.py --wgs_csbd --CSBDTS59 --refdb    # Process TS59 (Antepartum Services) with refdb value replacement - edit ID: RULESUB4000001

# Process all refdb-supported WGS_CSBD models
python main_processor.py --wgs_csbd --CSBDTS46 --refdb    # Process TS46 with refdb value replacement - edit ID: RULEEMSD000002
python main_processor.py --wgs_csbd --CSBDTS47 --refdb    # Process TS47 with refdb value replacement - edit ID: RULEMBOS000001
python main_processor.py --wgs_csbd --CSBDTS59 --refdb    # Process TS59 with refdb value replacement - edit ID: RULESUB4000001
```

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
python main_processor.py --wgs_nyk --NYKTS122   # Process TS122 model (Revenue code to HCPCS Alignment edit WGS NYK) - edit ID: RULERCTH00001
python main_processor.py --wgs_nyk --NYKTS123   # Process TS123 model (Observation Services WGS NYK) - edit ID: RULEOBSER00001
python main_processor.py --wgs_nyk --NYKTS124   # Process TS124 model (Observation Services WGS NYK) - edit ID: RULEOBSER00002
python main_processor.py --wgs_nyk --NYKTS125   # Process TS125 model (Observation Services WGS NYK) - edit ID: RULEOBSER00003
python main_processor.py --wgs_nyk --NYKTS126   # Process TS126 model (Observation Services WGS NYK) - edit ID: RULEOBSER00004
python main_processor.py --wgs_nyk --NYKTS127   # Process TS127 model (Observation Services WGS NYK) - edit ID: RULEOBSER00005
python main_processor.py --wgs_nyk --NYKTS128   # Process TS128 model (Observation Services WGS NYK) - edit ID: RULEOBSER00006
python main_processor.py --wgs_nyk --NYKTS129   # Process TS129 model (Observation Services WGS NYK) - edit ID: RULEOBSER00007
python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation Services WGS NYK) - edit ID: RULEOBSER00008
python main_processor.py --wgs_nyk --NYKTS132   # Process TS132 model (add_on without base WGS NYK) - edit ID: RULERADDON00001
python main_processor.py --wgs_nyk --all     # Process all 14 WGS_NYK models
```

**✅ GBDF Model Command Format Update**

The project now supports the new `--GBDTSXX` format for all GBDF MCR models (similar to `--CSBDTSXX` for WGS_CSBD models):

- **✅ New --GBDTSXX Format**: All GBDF MCR models now support the required `--GBDTSXX` format (e.g., `--GBDTS47`, `--GBDTS138`)
- **✅ Consistent Command Structure**: GBDF models now follow the same pattern as WGS_CSBD models for consistency
- **✅ Legacy Format Removed**: Legacy `--TSXX` format is no longer supported for GBDF MCR models - use `--GBDTSXX` format instead
- **✅ Dynamic Discovery Fix**: Fixed dynamic discovery to correctly handle GBDF models with `payloads/regression` folder structure
- **✅ Static Config Update**: Updated all GBDF model source paths to include `/payloads/` in the path
- **✅ Comprehensive Documentation**: Updated all README examples to use the new `--GBDTSXX` format

**Examples:**
```bash
# Recommended format (new)
python main_processor.py --gbdf_mcr --GBDTS47    # Process TS47 model (Covid GBDF MCR) - edit ID: RULEEM000001
python main_processor.py --gbdf_mcr --GBDTS138   # Process TS138 model (Multiple E&M Same day GBDF MCR) - edit ID: RULEEMSD000002

```

**✅ GBDF Dynamic Discovery & Catch-All Pattern Support (Latest Update)**

The project has been enhanced with flexible folder discovery and pattern matching for GBDF models:

- **✅ Catch-All Pattern Support**: The system now automatically discovers GBDF models using catch-all patterns, supporting any model name without requiring hardcoded patterns
- **✅ GBDTS_* Folder Naming**: Added support for `GBDTS_XX_*` folder naming convention (e.g., `GBDTS_70_InappropriatePrimaryDiagnosis_gbdf_mcr_*_sur`)
- **✅ Flexible Model Discovery**: Dynamic discovery now handles both `TS_XX_*` and `GBDTS_XX_*` folder naming patterns
- **✅ TS70 Model Support**: Added support for TS70 model (InappropriatePrimaryDiagnosis GBDF MCR) with `GBDTS_70_*` folder structure
- **✅ Automatic Pattern Matching**: The system automatically extracts model information from folder names using flexible regex patterns
- **✅ Backward Compatibility**: All existing models continue to work with the enhanced discovery system

**Examples:**
```bash
# TS70 model with GBDTS_* folder naming
python main_processor.py --gbdf_mcr --GBDTS70    # Process TS70 model (InappropriatePrimaryDiagnosis GBDF MCR) - edit ID: RULE00000376

# Any new GBDF model will be automatically discovered if it follows the naming convention:
# TS_XX_ModelName_gbdf_mcr_EDIT_ID_CODE_sur or GBDTS_XX_ModelName_gbdf_mcr_EDIT_ID_CODE_sur
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
    ├── NYKTS_122_Revenue code to HCPCS Alignment edit_Collection/
    ├── NYKTS_123_Observation_Services_Collection/
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
│   ├── TS_01_Covid_WGS_CSBD_RULEEM000001_00W04_dis/
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
│   ├── TS_63_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_Outpt_GRS_v17_dis/
│   ├── TS_62_Unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_outpt_MCR_v17_dis/
│   ├── TS_138_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/
│   ├── TS_139_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/
│   ├── TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_RULENDCUOM000001_v41_dis/
│   ├── TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_RULENDCUOM000001_v41_dis/
│   ├── TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_RULENEBU000001_v18_dis/
│   ├── TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_RULENEBU000001_v18_dis/
│   ├── TS_146_No match of Procedure code_gbdf_mcr_RULENMP000001_v18_dis/
│   └── TS_147_No match of Procedure code_gbdf_grs_RULENMP000001_v18_dis/
└── WGS_KERNAL/                                  # WGS_NYK Processed Files (Note: folder name is WGS_KERNAL)
    ├── NYKTS_122_Revenue code to HCPCS Alignment edit_WGS_NYK_RULERCTH00001_00W26_dis/
    ├── NYKTS_123_Observation_Services_WGS_NYK_RULEOBSER00001_00W28_dis/
    ├── NYKTS_124_Observation_Services_WGS_NYK_RULEOBSER00002_00W28_dis/
    ├── NYKTS_125_Observation_Services_WGS_NYK_RULEOBSER00003_00W28_dis/
    ├── NYKTS_126_Observation_Services_WGS_NYK_RULEOBSER00004_00W28_dis/
    ├── NYKTS_127_Observation_Services_WGS_NYK_RULEOBSER00005_00W28_dis/
    ├── NYKTS_128_Observation_Services_WGS_NYK_RULEOBSER00006_00W28_dis/
    ├── NYKTS_129_Observation_Services_WGS_NYK_RULEOBSER00007_00W28_dis/
    ├── NYKTS_130_Observation_Services_WGS_NYK_RULEOBSER00008_00W28_dis/
    └── NYKTS_132_add_on without base_WGS_NYK_RULERADDON00001_00W60_dis/
```

## 🚀 Quick Start Commands (Verified & Ready to Use)

**✅ All commands have been tested and verified to work correctly:**

### WGS_CSBD Models (Healthcare Claims Processing)
```bash
# Process specific TS models (WGS_CSBD flag required)
python main_processor.py --wgs_csbd --CSBDTS01    # Process TS01 model (Covid) - edit ID: RULEEM000001
python main_processor.py --wgs_csbd --CSBDTS02    # Process TS02 model (Laterality Policy-Disgnosis to Diagnosis) - edit ID: RULELATE000001
python main_processor.py --wgs_csbd --CSBDTS03    # Process TS03 model (Revenue code Services not payable on Facility claim Sub Edit 5) - edit ID: RULEREVE000005
python main_processor.py --wgs_csbd --CSBDTS04    # Process TS04 model (Revenue code Services not payable on Facility claim Sub Edit 4) - edit ID: RULEREVE000004
python main_processor.py --wgs_csbd --CSBDTS05    # Process TS05 model (Revenue code Services not payable on Facility claim Sub Edit 3) - edit ID: RULEREVE000003
python main_processor.py --wgs_csbd --CSBDTS06    # Process TS06 model (Revenue code Services not payable on Facility claim Sub Edit 2) - edit ID: RULEREVE000002
python main_processor.py --wgs_csbd --CSBDTS07    # Process TS07 model (Revenue code Services not payable on Facility claim Sub Edit 1) - edit ID: RULEREVE000001
python main_processor.py --wgs_csbd --CSBDTS08    # Process TS08 model (Lab panel Model) - edit ID: RULELAB0000009
python main_processor.py --wgs_csbd --CSBDTS09    # Process TS09 model (Device Dependent Procedures(R1)-1B) - edit ID: RULEDEVI000003
python main_processor.py --wgs_csbd --CSBDTS10    # Process TS10 model (Recovery Room Reimbursement) - edit ID: RULERECO000001
python main_processor.py --wgs_csbd --CSBDTS11    # Process TS11 model (Revenue Code to HCPCS Xwalk-1B) - edit ID: RULERECO000003
python main_processor.py --wgs_csbd --CSBDTS12    # Process TS12 model (Incidentcal Services Facility) - edit ID: RULEINCI000001
python main_processor.py --wgs_csbd --CSBDTS13    # Process TS13 model (Revenue model CR v3) - edit ID: RULERCE0000006
python main_processor.py --wgs_csbd --CSBDTS14    # Process TS14 model (HCPCS to Revenue Code Xwalk) - edit ID: RULERCE000001
python main_processor.py --wgs_csbd --CSBDTS15    # Process TS15 model (WGS_CSBD) - edit ID: RULERCE000005
python main_processor.py --wgs_csbd --CSBDTS20    # Process TS20 model (RadioservicesbilledwithoutRadiopharma) - edit ID: RULERBWR000001
python main_processor.py --wgs_csbd --CSBDTS46    # Process TS46 model (Multiple E&M Same day) - edit ID: RULEEMSD000002
python main_processor.py --wgs_csbd --CSBDTS47    # Process TS47 model (Multiple Billing of Obstetrical Services) - edit ID: RULEMBOS000001
python main_processor.py --wgs_csbd --CSBDTS48    # Process TS48 model (Revenue code to HCPCS Alignment edit) - edit ID: RULERCTH00001
python main_processor.py --wgs_csbd --CSBDTS49    # Process TS49 model (Observation_Services) - edit ID: RULEOBSER00001
python main_processor.py --wgs_csbd --CSBDTS50    # Process TS50 model (Observation_Services) - edit ID: RULEOBSER00002
python main_processor.py --wgs_csbd --CSBDTS51    # Process TS51 model (Observation_Services) - edit ID: RULEOBSER00003
python main_processor.py --wgs_csbd --CSBDTS52    # Process TS52 model (Observation_Services) - edit ID: RULEOBSER00004
python main_processor.py --wgs_csbd --CSBDTS53    # Process TS53 model (Observation_Services) - edit ID: RULEOBSER00005
python main_processor.py --wgs_csbd --CSBDTS54    # Process TS54 model (Observation_Services) - edit ID: RULEOBSER00006
python main_processor.py --wgs_csbd --CSBDTS55    # Process TS55 model (Observation_Services) - edit ID: RULEOBSER00007
python main_processor.py --wgs_csbd --CSBDTS56    # Process TS56 model (Observation_Services) - edit ID: RULEOBSER00008
python main_processor.py --wgs_csbd --CSBDTS57    # Process TS57 model (add_on without base) - edit ID: RULERADDON00001
python main_processor.py --wgs_csbd --CSBDTS58    # Process TS58 model (Expansion) - edit ID: RULESUB4000001
python main_processor.py --wgs_csbd --CSBDTS59    # Process TS59 model (Wgs) - edit ID: RULESUB4000001
python main_processor.py --wgs_csbd --CSBDTS60    # Process TS60 model (Inpatient) - edit ID: RULEINPCC00001
python main_processor.py --wgs_csbd --CSBDTS61    # Process TS61 model (Op) - edit ID: RULEOPBS000001
python main_processor.py --wgs_csbd --CSBDTS62    # Process TS62 model (Anesthesia) - edit ID: RULEANES000001
python main_processor.py --wgs_csbd --CSBDTS63    # Process TS63 model (Bundled) - edit ID: RULEBDLG000004
python main_processor.py --wgs_csbd --CSBDTS64    # Process TS64 model (Clia) - edit ID: RULECLIA00001
python main_processor.py --wgs_csbd --CSBDTS65    # Process TS65 model (Medical) - edit ID: RULEJWME000001
python main_processor.py --wgs_csbd --CSBDTS66    # Process TS66 model (Missing) - edit ID: RULEMFTM000001
python main_processor.py --wgs_csbd --CSBDTS67    # Process TS67 model (Ncci) - edit ID: RULENCCIPTP001
python main_processor.py --wgs_csbd --CSBDTS68    # Process TS68 model (Ndc) - edit ID: RULENDC000001
python main_processor.py --wgs_csbd --CSBDTS70    # Process TS70 model (Correct) - edit ID: RULERCRO000001
python main_processor.py --wgs_csbd --CSBDTS71    # Process TS71 model (Revenue) - edit ID: RULERCTH000001
python main_processor.py --wgs_csbd --CSBDTS73    # Process TS73 model (Unacceptable) - edit ID: RULEUNAC000001
python main_processor.py --wgs_csbd --CSBDTS74    # Process TS74 model - edit ID: RULEEM0000012 MNP Model
python main_processor.py --wgs_csbd --CSBDTS75    # Process TS75 model (Preventive) - edit ID: RULEPREV000001

# Process all WGS_CSBD models at once
python main_processor.py --wgs_csbd --all     # Process all WGS_CSBD models
```

## 📋 User Commands & Model Commands

This section documents all CLI options for `main_processor.py`: **user commands** (global options and modifiers) and **model commands** (model type + model selector).

### User commands (global options)

These flags control *how* the script runs. They can be combined with any model command.

| Command | Description |
|--------|-------------|
| `--list` | List all available TS models for the given model type; with a specific model (e.g. `--CSBDTS01`) generates JSON renaming timing report for that model |
| `--all` | Process all discovered models for the selected model type (requires `--wgs_csbd`, `--wgs_nyk`, `--gbdf_mcr`, or `--gbdf_grs`) |
| `--no-postman` | Skip Postman collection generation; only rename files |
| `--no-report` | Disable Excel report generation (skip timing reports) |
| `--refdb` | Apply refdb value replacement for refdb-supported models (e.g. CSBDTS46, CSBDTS47, CSBDTS59, NYKTS123) |
| `--edit-id <id>` | Custom edit ID (e.g. `rvn001`) |
| `--code <code>` | Custom code (e.g. `00W5`) |
| `--source-dir <path>` | Custom source directory path |
| `--dest-dir <path>` | Custom destination directory path |
| `--collection-name <name>` | Custom Postman collection name |
| `--help` | Show help and example usage |

**Examples (user commands with a model):**
```bash
python main_processor.py --wgs_csbd --CSBDTS01 --list      # Timing report for TS01
python main_processor.py --wgs_csbd --CSBDTS07 --no-postman
python main_processor.py --gbdf_mcr --GBDTS47 --no-postman
python main_processor.py --wgs_csbd --all --refdb
python main_processor.py --wgs_csbd --all --no-postman
```

### Model commands (model type + model selector)

You must choose **one** model type and **one** model (or `--all`). Model type and selector format must match.

| Model type (flag) | Model selector format | Example |
|-------------------|------------------------|--------|
| `--wgs_csbd` | `--CSBDTS<NN>` or `--all` | `--wgs_csbd --CSBDTS01`, `--wgs_csbd --all` |
| `--wgs_nyk` | `--NYKTS<NN>` or `--all` | `--wgs_nyk --NYKTS124`, `--wgs_nyk --all` |
| `--gbdf_mcr` | `--GBDTS<NN>` or `--all` | `--gbdf_mcr --GBDTS47`, `--gbdf_mcr --all` |
| `--gbdf_grs` | `--GBDTS<NN>` or `--all` | `--gbdf_grs --GBDTS49`, `--gbdf_grs --all` |

**Rules:**

- **WGS_CSBD:** Use `--wgs_csbd` with `--CSBDTS01`, `--CSBDTS02`, … `--CSBDTS75` (no `--TSXX`).
- **WGS_NYK:** Use `--wgs_nyk` with `--NYKTS122`, `--NYKTS123`, … (e.g. `--NYKTS130`, `--NYKTS132`, `--NYKTS149`, `--NYKTS150`).
- **GBDF MCR:** Use `--gbdf_mcr` with `--GBDTS47`, `--GBDTS62`, … (e.g. `--GBDTS138`, `--GBDTS144`).
- **GBDF GRS:** Use `--gbdf_grs` with `--GBDTS49`, `--GBDTS61`, … (e.g. `--GBDTS139`, `--GBDTS141`).

**Examples (model commands only):**
```bash
# Single model
python main_processor.py --wgs_csbd --CSBDTS01
python main_processor.py --wgs_nyk --NYKTS124
python main_processor.py --gbdf_mcr --GBDTS47
python main_processor.py --gbdf_grs --GBDTS49

# All models of a type
python main_processor.py --wgs_csbd --all
python main_processor.py --wgs_nyk --all
python main_processor.py --gbdf_mcr --all
python main_processor.py --gbdf_grs --all
```

### GBDF_MCR Models (Global Burden of Disease Foundation - Medical Claims Research)
```bash
# Process specific GBDF MCR models (GBDF_MCR flag required - Recommended format: --GBDTSXX)
python main_processor.py --gbdf_mcr --GBDTS47    # Process TS47 model (Covid) - edit ID: RULEEM000001
python main_processor.py --gbdf_mcr --GBDTS62    # Process TS62 model (Unspecified_dx_code_outpt_MCR) - edit ID: RULEUSD00100_outpt_MCR
python main_processor.py --gbdf_mcr --GBDTS70    # Process TS70 model (InappropriatePrimaryDiagnosis) - edit ID: RULE00000376
python main_processor.py --gbdf_mcr --GBDTS138    # Process TS138 model (Multiple E&M Same day) - edit ID: RULEEMSD000002
python main_processor.py --gbdf_mcr --GBDTS140    # Process TS140 model (NDC UOM Validation Edit Expansion Iprep-138) - edit ID: RULENDCUOM000001
python main_processor.py --gbdf_mcr --GBDTS144    # Process TS144 model (Nebulizer A52466 IPERP-132) - edit ID: RULENEBU000001
python main_processor.py --gbdf_mcr --GBDTS49    # Process TS49 model (Laterality) - edit ID: RULELATE000001
python main_processor.py --gbdf_mcr --GBDTS50    # Process TS50 model (Psm) - edit ID: PSMEM000001
python main_processor.py --gbdf_mcr --GBDTS52    # Process TS52 model (Psm) - edit ID: PSMEM000002
python main_processor.py --gbdf_mcr --GBDTS54    # Process TS54 model (Psm) - edit ID: PSMEM000003
python main_processor.py --gbdf_mcr --GBDTS56    # Process TS56 model (Psm) - edit ID: PSMEM000004
python main_processor.py --gbdf_mcr --GBDTS58    # Process TS58 model (Manifestation) - edit ID: RULEMAN000004
python main_processor.py --gbdf_mcr --GBDTS63    # Process TS63 model (Shadow) - edit ID: RULEAMBU000001
python main_processor.py --gbdf_mcr --GBDTS64    # Process TS64 model (Unspecified Prof_MCR) - edit ID: RULEUSD00100_Prof_MCR
python main_processor.py --gbdf_mcr --GBDTS65    # Process TS65 model (Gbdf) - edit ID: RULEAMBU000001
python main_processor.py --gbdf_mcr --GBDTS66    # Process TS66 model (Gbdf) - edit ID: RULE00000022
python main_processor.py --gbdf_mcr --GBDTS67    # Process TS67 model (Inaccurate) - edit ID: RULE00000022
python main_processor.py --gbdf_mcr --GBDTS72    # Process TS72 model (Always) - edit ID: RULEALWA000001
python main_processor.py --gbdf_mcr --GBDTS73    # Process TS73 model (Gbdf) - edit ID: RULEEXCL000001
python main_processor.py --gbdf_mcr --GBDTS75    # Process TS75 model (Excludes) - edit ID: RULEEXCL000001
python main_processor.py --gbdf_mcr --GBDTS123    # Process TS123 model (Anesthesia) - edit ID: RULEANES000001
python main_processor.py --gbdf_mcr --GBDTS125    # Process TS125 model (Clia) - edit ID: RULECLIA00001
python main_processor.py --gbdf_mcr --GBDTS126    # Process TS126 model (Clia) - edit ID: RULECLIA00001
python main_processor.py --gbdf_mcr --GBDTS127    # Process TS127 model (Toxoid GBD-Facets-MCR_v38_sur) - edit ID: RULEIPVT000001
python main_processor.py --gbdf_mcr --GBDTS129    # Process TS129 model (Gbdf) - edit ID: RULEIMMU000001
python main_processor.py --gbdf_mcr --GBDTS131    # Process TS131 model (Gbdf) - edit ID: RULEKNEE000001
python main_processor.py --gbdf_mcr --GBDTS134    # Process TS134 model (Gbdf) - edit ID: RULEJWME000001
python main_processor.py --gbdf_mcr --GBDTS136    # Process TS136 model (Gbdf) - edit ID: RULEEM0000012
python main_processor.py --gbdf_mcr --GBDTS142    # Process TS142 model (Gbdf) - edit ID: RULENDC000001
python main_processor.py --gbdf_mcr --GBDTS146    # Process TS146 model (Gbdf) - edit ID: RULENMP000001
python main_processor.py --gbdf_mcr --GBDTS148    # Process TS148 model (Gbdf) - edit ID: RULEOSTO000001
python main_processor.py --gbdf_mcr --GBDTS150    # Process TS150 model (Gbdf) - edit ID: RULETRAC000001
python main_processor.py --gbdf_mcr --GBDTS152    # Process TS152 model (Gbdf) - edit ID: RULERCRO000001
python main_processor.py --gbdf_mcr --GBDTS154    # Process TS154 model (Gbdf) - edit ID: RULEIPDXE00001
python main_processor.py --gbdf_mcr --GBDTS155    # Process TS155 model (Gbdf) - edit ID: RULEIPDXE00001
python main_processor.py --gbdf_mcr --GBDTS156    # Process TS156 model (Geneticstesting) - edit ID: RULEGENE000001
python main_processor.py --gbdf_mcr --GBDTS159    # Process TS159 model (Mcr) - edit ID: RULERCWP000001
python main_processor.py --gbdf_mcr --GBDTS161    # Process TS161 model (Mcr) - edit ID: RULEPMAM000001
python main_processor.py --gbdf_mcr --GBDTS162    # Process TS162 model (Gbdf) - edit ID: PSMEM000003_algo
python main_processor.py --gbdf_mcr --GBDTS164    # Process TS164 model (Psm) - edit ID: PSMEM000004_algo
python main_processor.py --gbdf_mcr --GBDTS166    # Process TS166 model (Sick) - edit ID: RULEEM000002_refdb

# Process all GBDF MCR models at once
python main_processor.py --gbdf_mcr --all     # Process all GBDF MCR models

```

### GBDF_GRS Models (Global Burden of Disease Foundation - Global Research Services)
```bash
# Process specific GBDF GRS models (GBDF_GRS flag required - use --GBDTSXX format)
python main_processor.py --gbdf_grs --GBDTS47    # Process TS47 model (Covid) - edit ID: RULEEM000001
python main_processor.py --gbdf_grs --GBDTS48    # Process TS48 model (Laterality) - edit ID: RULELATE000001
python main_processor.py --gbdf_grs --GBDTS51    # Process TS51 model (Psm) - edit ID: PSMEM000001
python main_processor.py --gbdf_grs --GBDTS53    # Process TS53 model (Psm) - edit ID: PSMEM000002
python main_processor.py --gbdf_grs --GBDTS55    # Process TS55 model (Psm) - edit ID: PSMEM000003
python main_processor.py --gbdf_grs --GBDTS57    # Process TS57 model (Psm) - edit ID: PSMEM000004
python main_processor.py --gbdf_grs --GBDTS61    # Process TS61 model (Unspecified) - edit ID: RULEUSD00100_Prof_GRS
python main_processor.py --gbdf_grs --GBDTS63    # Process TS63 model (Unspecified Outpt_GRS) - edit ID: RULEUSD00100_Outpt_GRS
python main_processor.py --gbdf_grs --GBDTS64    # Process TS64 model (Shadow) - edit ID: RULEAMBU000001
python main_processor.py --gbdf_grs --GBDTS68    # Process TS68 model (Inaccurate) - edit ID: RULE00000022
python main_processor.py --gbdf_grs --GBDTS69    # Process TS69 model (Inappropriate) - edit ID: RULE00000376
python main_processor.py --gbdf_grs --GBDTS71    # Process TS71 model (Always) - edit ID: RULEALWA000001
python main_processor.py --gbdf_grs --GBDTS74    # Process TS74 model (Excludes) - edit ID: RULEEXCL000001
python main_processor.py --gbdf_grs --GBDTS122    # Process TS122 model (Geneticstesting) - edit ID: RULEGENE000001
python main_processor.py --gbdf_grs --GBDTS124    # Process TS124 model (Anesthesia) - edit ID: RULEANES000001
python main_processor.py --gbdf_grs --GBDTS128    # Process TS128 model (Toxoid GBD-Facets-GRS_v38_sur) - edit ID: RULEIPVT000001
python main_processor.py --gbdf_grs --GBDTS130    # Process TS130 model (Gbdf) - edit ID: RULEIMMU000001
python main_processor.py --gbdf_grs --GBDTS132    # Process TS132 model (Gbdf) - edit ID: RULEKNEE000001
python main_processor.py --gbdf_grs --GBDTS133    # Process TS133 model (Manifestation) - edit ID: RULEMAN000004
python main_processor.py --gbdf_grs --GBDTS135    # Process TS135 model (Gbdf) - edit ID: RULEJWME000001
python main_processor.py --gbdf_grs --GBDTS137    # Process TS137 model (Gbdf) - edit ID: RULEEM0000012
python main_processor.py --gbdf_grs --GBDTS139    # Process TS139 model (Multiple E&M Same day) - edit ID: RULEEMSD000002
python main_processor.py --gbdf_grs --GBDTS141    # Process TS141 model (NDC UOM Validation Edit Expansion Iprep-138) - edit ID: RULENDCUOM000001
python main_processor.py --gbdf_grs --GBDTS143    # Process TS143 model (Gbdf) - edit ID: RULENDC000001
python main_processor.py --gbdf_grs --GBDTS145    # Process TS145 model (Nebulizer A52466 IPERP-132) - edit ID: RULENEBU000001
python main_processor.py --gbdf_grs --GBDTS147    # Process TS147 model (Gbdf) - edit ID: RULENMP000001
python main_processor.py --gbdf_grs --GBDTS149    # Process TS149 model (Gbdf) - edit ID: RULEOSTO000001
python main_processor.py --gbdf_grs --GBDTS151    # Process TS151 model (Gbdf) - edit ID: RULETRAC000001
python main_processor.py --gbdf_grs --GBDTS153    # Process TS153 model (Gbdf) - edit ID: RULERCRO000001
python main_processor.py --gbdf_grs --GBDTS157    # Process TS157 model (Gbdf) - edit ID: RULEIPDXH00001
python main_processor.py --gbdf_grs --GBDTS158    # Process TS158 model (Grs) - edit ID: RULERCWP000001
python main_processor.py --gbdf_grs --GBDTS160    # Process TS160 model (Grs) - edit ID: RULEPMAM000001
python main_processor.py --gbdf_grs --GBDTS163    # Process TS163 model (Gbdf) - edit ID: PSMEM000003_algo
python main_processor.py --gbdf_grs --GBDTS165    # Process TS165 model (Psm) - edit ID: PSMEM000004_algo
python main_processor.py --gbdf_grs --GBDTS167    # Process TS167 model (Sick) - edit ID: RULEEM000002_refdb

# Process all GBDF GRS models at once
python main_processor.py --gbdf_grs --all     # Process all GBDF GRS models
```

### WGS_NYK Models (Working Group Standards - New York Kernal)
```bash
# Process specific WGS_NYK models (WGS_NYK flag required - Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS122   # Process TS122 model (Revenue code to HCPCS Alignment edit) - edit ID: RULERCTH00001
python main_processor.py --wgs_nyk --NYKTS123   # Process TS123 model (Observation_Services) - edit ID: RULEOBSER00001
python main_processor.py --wgs_nyk --NYKTS124   # Process TS124 model (Observation_Services) - edit ID: RULEOBSER00002
python main_processor.py --wgs_nyk --NYKTS125   # Process TS125 model (Observation_Services) - edit ID: RULEOBSER00003
python main_processor.py --wgs_nyk --NYKTS126   # Process TS126 model (Observation_Services) - edit ID: RULEOBSER00004
python main_processor.py --wgs_nyk --NYKTS127   # Process TS127 model (Observation_Services) - edit ID: RULEOBSER00005
python main_processor.py --wgs_nyk --NYKTS128   # Process TS128 model (Observation_Services) - edit ID: RULEOBSER00006
python main_processor.py --wgs_nyk --NYKTS129   # Process TS129 model (Observation_Services) - edit ID: RULEOBSER00007
python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation_Services) - edit ID: RULEOBSER00008
python main_processor.py --wgs_nyk --NYKTS132   # Process TS132 model (add_on without base) - edit ID: RULERADDON00001
python main_processor.py --wgs_nyk --NYKTS149   # Process TS149 model (Preventative Medicine and Screening) - edit ID: RULEPREV00001
python main_processor.py --wgs_nyk --NYKTS150   # Process TS150 model (Inpatient) - edit ID: RULEINPCC00001

# Process all WGS_NYK models at once
python main_processor.py --wgs_nyk --all     # Process all WGS_NYK models
```

### Auto Edit Processor (Config from Excel)
```bash
# Process edits from Excel sheet (default: WGS_CSBD)
python auto_edit_processor.py
python auto_edit_processor.py --sheet WGS_CSBD
python auto_edit_processor.py --sheet GBDF
python auto_edit_processor.py --sheet GBDF_MCR
python auto_edit_processor.py --sheet GBDF_GRS
python auto_edit_processor.py --sheet KERNAL

# Sync Test Suite IDs from Excel to models_config.py
python auto_edit_processor.py --sync-from-excel --sheet WGS_CSBD
python auto_edit_processor.py --sync-from-excel --sheet GBDF
python auto_edit_processor.py --sync-from-excel --sheet KERNAL

# Sort STATIC_MODELS_CONFIG by ts_number (ascending)
python auto_edit_processor.py --sort-config

# Dry run (preview without updating)
python auto_edit_processor.py --dry-run
```

## 📊 Model Summary & Quick Reference

### Available Models Overview
| Model Type | Count | TS Numbers | Description |
|------------|-------|------------|-------------|
| **WGS_CSBD** | 46 | TS01-TS15, TS20, TS46-TS75 (see `models_config.py`) | Healthcare Claims Processing |
| **GBDF_MCR** | 62 | Full GBDF MCR static config set (TS47-TS166 range, see `models_config.py`) | Global Burden of Disease Foundation - Medical Claims Research |
| **GBDF_GRS** | 54 | Full GBDF GRS static config set (TS47-TS167 range, see `models_config.py`) | Global Burden of Disease Foundation - Global Research Services |
| **WGS_NYK** | 14 | TS122-TS130, TS132, TS149, TS150 (see `models_config.py`) | Working Group Standards - New York Kernal (Revenue code to HCPCS Alignment edit, Observation Services) |
| **TOTAL** | **174** | | **All Available Models** |

### Quick Command Reference
```bash
# Process ALL models of each type
python main_processor.py --wgs_csbd --all     # All 46 WGS_CSBD models
python main_processor.py --gbdf_mcr --all     # All 62 GBDF MCR models  
python main_processor.py --gbdf_grs --all     # All 54 GBDF GRS models
python main_processor.py --wgs_nyk --all      # All 14 WGS_NYK models

# Process ALL models of each type WITHOUT Postman generation
python main_processor.py --wgs_csbd --all --no-postman
python main_processor.py --gbdf_mcr --all --no-postman
python main_processor.py --gbdf_grs --all --no-postman
python main_processor.py --wgs_nyk --all --no-postman

# Process ALL refdb-supported models with value replacement (WGS_CSBD: CSBDTS46, CSBDTS47, CSBDTS59; WGS_NYK: NYKTS123)
python main_processor.py --wgs_csbd --all --refdb
python main_processor.py --wgs_nyk --all --refdb

# List all available models
python main_processor.py --list

# Get help
python main_processor.py --help
```

### Postman Collection Generation Commands
```bash
# Process models with automatic Postman collection generation (default behavior)
python main_processor.py --wgs_csbd --CSBDTS01    # Generates TS_01_Covid_Collection - edit ID: RULEEM000001
python main_processor.py --wgs_csbd --CSBDTS02    # Generates TS_02_Laterality_Collection - edit ID: RULELATE000001
python main_processor.py --wgs_csbd --CSBDTS03    # Generates TS_03_Revenue_Collection - edit ID: RULEREVE000005
python main_processor.py --wgs_csbd --CSBDTS04    # Generates TS_04_Revenue_Collection - edit ID: RULEREVE000004
python main_processor.py --wgs_csbd --CSBDTS05    # Generates TS_05_Revenue_Collection - edit ID: RULEREVE000003
python main_processor.py --wgs_csbd --CSBDTS06    # Generates TS_06_Revenue_Collection - edit ID: RULEREVE000002
python main_processor.py --wgs_csbd --CSBDTS07    # Generates TS_07_Revenue_Collection - edit ID: RULEREVE000001
python main_processor.py --wgs_csbd --CSBDTS08    # Generates TS_08_Lab_Collection - edit ID: RULELAB0000009
python main_processor.py --wgs_csbd --CSBDTS09    # Generates TS_09_Device_Collection - edit ID: RULEDEVI000003
python main_processor.py --wgs_csbd --CSBDTS10    # Generates TS_10_Recovery_Collection - edit ID: RULERECO000001
python main_processor.py --wgs_csbd --CSBDTS11    # Generates TS_11_Revenue_Collection - edit ID: RULERECO000003
python main_processor.py --wgs_csbd --CSBDTS12    # Generates TS_12_Incidentcal_Collection - edit ID: RULEINCI000001
python main_processor.py --wgs_csbd --CSBDTS13    # Generates TS_13_Revenue_Collection - edit ID: RULERCE0000006
python main_processor.py --wgs_csbd --CSBDTS14    # Generates TS_14_HCPCS_Collection - edit ID: RULERCE000001
python main_processor.py --wgs_csbd --CSBDTS15    # Generates TS_15_Revenue_Collection - edit ID: RULERCE000005
python main_processor.py --wgs_csbd --CSBDTS20    # Generates TS_20_RadioservicesbilledwithoutRadiopharma_Collection - edit ID: RULERBWR000001
python main_processor.py --wgs_csbd --CSBDTS46    # Generates TS_46_Multiple E&M Same day_Collection - edit ID: RULEEMSD000002
python main_processor.py --wgs_csbd --CSBDTS47    # Generates TS_47_Multiple Billing of Obstetrical Services_Collection - edit ID: RULEMBOS000001
python main_processor.py --wgs_csbd --CSBDTS48    # Generates CSBD_TS_48_Revenue code to HCPCS Alignment edit_Collection - edit ID: RULERCTH00001
python main_processor.py --wgs_csbd --CSBDTS49    # Generates CSBDTS_49_Observation_Services_Collection - edit ID: RULEOBSER00001
python main_processor.py --wgs_csbd --CSBDTS50    # Generates CSBDTS_50_Observation_Services_Collection - edit ID: RULEOBSER00002
python main_processor.py --wgs_csbd --CSBDTS51    # Generates CSBDTS_51_Observation_Services_Collection - edit ID: RULEOBSER00003
python main_processor.py --wgs_csbd --CSBDTS52    # Generates CSBDTS_52_Observation_Services_Collection - edit ID: RULEOBSER00004
python main_processor.py --wgs_csbd --CSBDTS53    # Generates CSBDTS_53_Observation_Services_Collection - edit ID: RULEOBSER00005
python main_processor.py --wgs_csbd --CSBDTS54    # Generates CSBDTS_54_Observation_Services_Collection - edit ID: RULEOBSER00006
python main_processor.py --wgs_csbd --CSBDTS55    # Generates CSBDTS_55_Observation_Services_Collection - edit ID: RULEOBSER00007
python main_processor.py --wgs_csbd --CSBDTS56    # Generates CSBDTS_56_Observation_Services_Collection - edit ID: RULEOBSER00008
python main_processor.py --wgs_csbd --CSBDTS57    # Generates CSBDTS_57_add_on without base_Collection - edit ID: RULERADDON00001
python main_processor.py --wgs_csbd --CSBDTS59    # Generates CSBDTS_59_AntepartumServices_Collection - edit ID: RULESUB4000001
python main_processor.py --wgs_csbd --all     # Generates collections for all WGS_CSBD models

# GBDF MCR models with Postman collection generation (Recommended format: --GBDTSXX)
python main_processor.py --gbdf_mcr --GBDTS47    # Generates TS_47_Covid_gbdf_mcr_Collection - edit ID: RULEEM000001
python main_processor.py --gbdf_mcr --GBDTS62    # Generates TS_62_Unspecified_dx_code_outpt_gbdf_mcr_Collection - edit ID: RULEUSD00100_outpt_MCR
python main_processor.py --gbdf_mcr --GBDTS70    # Generates TS_70_InappropriatePrimaryDiagnosis_gbdf_mcr_Collection - edit ID: RULE00000376
python main_processor.py --gbdf_mcr --GBDTS138   # Generates TS_138_Multiple E&M Same day_gbdf_mcr_Collection - edit ID: RULEEMSD000002
python main_processor.py --gbdf_mcr --GBDTS140   # Generates TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_Collection - edit ID: RULENDCUOM000001
python main_processor.py --gbdf_mcr --GBDTS144   # Generates TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_Collection - edit ID: RULENEBU000001
python main_processor.py --gbdf_mcr --GBDTS146   # Generates TS_146_No match of Procedure code_gbdf_mcr_Collection - edit ID: RULENMP000001
python main_processor.py --gbdf_mcr --all     # Generates collections for all GBDF MCR models


# GBDF GRS models with Postman collection generation
python main_processor.py --gbdf_grs --GBDTS63    # Generates TS_63_Unspecified_dx_code_outpt_gbdf_grs_Collection - edit ID: RULEUSD00100_Outpt_GRS
python main_processor.py --gbdf_grs --GBDTS61    # Generates TS_61_Unspecified_dx_code_prof_gbdf_grs_Collection - edit ID: RULEUSD00100_Prof_GRS
python main_processor.py --gbdf_grs --TS139   # Generates TS_139_Multiple E&M Same day_gbdf_grs_Collection - edit ID: RULEEMSD000002
python main_processor.py --gbdf_grs --TS141   # Generates TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_Collection - edit ID: RULENDCUOM000001
python main_processor.py --gbdf_grs --TS145   # Generates TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_Collection - edit ID: RULENEBU000001
python main_processor.py --gbdf_grs --TS147   # Generates TS_147_No match of Procedure code_gbdf_grs_Collection - edit ID: RULENMP000001
python main_processor.py --gbdf_grs --all     # Generates collections for all GBDF GRS models

# WGS_NYK models with Postman collection generation (Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS122   # Generates NYKTS_122_Revenue code to HCPCS Alignment edit_Collection - edit ID: RULERCTH00001
python main_processor.py --wgs_nyk --NYKTS123   # Generates NYKTS_123_Observation_Services_Collection - edit ID: RULEOBSER00001
python main_processor.py --wgs_nyk --NYKTS124   # Generates NYKTS_124_Observation_Services_Collection - edit ID: RULEOBSER00002
python main_processor.py --wgs_nyk --NYKTS125   # Generates NYKTS_125_Observation_Services_Collection - edit ID: RULEOBSER00003
python main_processor.py --wgs_nyk --NYKTS126   # Generates NYKTS_126_Observation_Services_Collection - edit ID: RULEOBSER00004
python main_processor.py --wgs_nyk --NYKTS127   # Generates NYKTS_127_Observation_Services_Collection - edit ID: RULEOBSER00005
python main_processor.py --wgs_nyk --NYKTS128   # Generates NYKTS_128_Observation_Services_Collection - edit ID: RULEOBSER00006
python main_processor.py --wgs_nyk --NYKTS129   # Generates NYKTS_129_Observation_Services_Collection - edit ID: RULEOBSER00007
python main_processor.py --wgs_nyk --NYKTS130   # Generates NYKTS_130_Observation_Services_Collection - edit ID: RULEOBSER00008
python main_processor.py --wgs_nyk --NYKTS132   # Generates NYKTS_132_add_on without base_Collection - edit ID: RULERADDON00001
python main_processor.py --wgs_nyk --all     # Generates collections for all WGS_NYK models

# Process models without generating Postman collections
python main_processor.py --wgs_csbd --CSBDTS01 --no-postman    # edit ID: RULEEM000001
python main_processor.py --wgs_csbd --CSBDTS02 --no-postman    # edit ID: RULELATE000001
python main_processor.py --wgs_csbd --CSBDTS03 --no-postman    # edit ID: RULEREVE000005
python main_processor.py --wgs_csbd --CSBDTS04 --no-postman    # edit ID: RULEREVE000004
python main_processor.py --wgs_csbd --CSBDTS05 --no-postman    # edit ID: RULEREVE000003
python main_processor.py --wgs_csbd --CSBDTS06 --no-postman    # edit ID: RULEREVE000002
python main_processor.py --wgs_csbd --CSBDTS07 --no-postman    # edit ID: RULEREVE000001
python main_processor.py --wgs_csbd --CSBDTS08 --no-postman    # edit ID: RULELAB0000009
python main_processor.py --wgs_csbd --CSBDTS09 --no-postman    # edit ID: RULEDEVI000003
python main_processor.py --wgs_csbd --CSBDTS10 --no-postman    # edit ID: RULERECO000001
python main_processor.py --wgs_csbd --CSBDTS11 --no-postman    # edit ID: RULERECO000003
python main_processor.py --wgs_csbd --CSBDTS12 --no-postman    # edit ID: RULEINCI000001
python main_processor.py --wgs_csbd --CSBDTS13 --no-postman    # edit ID: RULERCE0000006
python main_processor.py --wgs_csbd --CSBDTS14 --no-postman    # edit ID: RULERCE000001
python main_processor.py --wgs_csbd --CSBDTS15 --no-postman    # edit ID: RULERCE000005
python main_processor.py --wgs_csbd --CSBDTS20 --no-postman    # edit ID: RULERBWR000001
python main_processor.py --wgs_csbd --CSBDTS46 --no-postman    # edit ID: RULEEMSD000002
python main_processor.py --wgs_csbd --CSBDTS47 --no-postman    # edit ID: RULEMBOS000001
python main_processor.py --wgs_csbd --CSBDTS48 --no-postman    # edit ID: RULERCTH00001
python main_processor.py --wgs_csbd --CSBDTS59 --no-postman    # edit ID: RULESUB4000001
python main_processor.py --wgs_csbd --all --no-postman

# GBDF MCR models without Postman collection generation
python main_processor.py --gbdf_mcr --GBDTS47 --no-postman    # edit ID: RULEEM000001
python main_processor.py --gbdf_mcr --GBDTS62 --no-postman    # edit ID: RULEUSD00100_outpt_MCR
python main_processor.py --gbdf_mcr --GBDTS70 --no-postman    # edit ID: RULE00000376
python main_processor.py --gbdf_mcr --GBDTS138 --no-postman    # edit ID: RULEEMSD000002
python main_processor.py --gbdf_mcr --GBDTS140 --no-postman    # edit ID: RULENDCUOM000001
python main_processor.py --gbdf_mcr --GBDTS144 --no-postman    # edit ID: RULENEBU000001
python main_processor.py --gbdf_mcr --GBDTS146 --no-postman    # edit ID: RULENMP000001
python main_processor.py --gbdf_mcr --all --no-postman

# GBDF GRS models without Postman collection generation
python main_processor.py --gbdf_grs --GBDTS63 --no-postman    # edit ID: RULEUSD00100_Outpt_GRS
python main_processor.py --gbdf_grs --GBDTS61 --no-postman    # edit ID: RULEUSD00100_Prof_GRS
python main_processor.py --gbdf_grs --TS139 --no-postman    # edit ID: RULEEMSD000002
python main_processor.py --gbdf_grs --TS141 --no-postman    # edit ID: RULENDCUOM000001
python main_processor.py --gbdf_grs --TS145 --no-postman    # edit ID: RULENEBU000001
python main_processor.py --gbdf_grs --TS147 --no-postman    # edit ID: RULENMP000001
python main_processor.py --gbdf_grs --all --no-postman

# WGS_NYK models without Postman collection generation (Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS122 --no-postman    # edit ID: RULERCTH00001
python main_processor.py --wgs_nyk --NYKTS123 --no-postman    # edit ID: RULEOBSER00001
python main_processor.py --wgs_nyk --NYKTS124 --no-postman    # edit ID: RULEOBSER00002
python main_processor.py --wgs_nyk --NYKTS125 --no-postman    # edit ID: RULEOBSER00003
python main_processor.py --wgs_nyk --NYKTS126 --no-postman    # edit ID: RULEOBSER00004
python main_processor.py --wgs_nyk --NYKTS127 --no-postman    # edit ID: RULEOBSER00005
python main_processor.py --wgs_nyk --NYKTS128 --no-postman    # edit ID: RULEOBSER00006
python main_processor.py --wgs_nyk --NYKTS129 --no-postman    # edit ID: RULEOBSER00007
python main_processor.py --wgs_nyk --NYKTS130 --no-postman    # edit ID: RULEOBSER00008
python main_processor.py --wgs_nyk --NYKTS132 --no-postman    # edit ID: RULERADDON00001
python main_processor.py --wgs_nyk --all --no-postman
```

**Additional Options:**
```bash
# List all available models with detailed information
python main_processor.py --list

# Generate timing report for specific model (without processing files)
python main_processor.py --wgs_csbd --CSBDTS47 --list    # Generate timing report for TS47 WGS_CSBD - edit ID: RULEMBOS000001
python main_processor.py --gbdf_mcr --GBDTS47 --list    # Generate timing report for TS47 GBDF MCR - edit ID: RULEEM000001
python main_processor.py --gbdf_grs --TS139 --list   # Generate timing report for TS139 GBDF GRS - edit ID: RULEEMSD000002
python main_processor.py --wgs_nyk --NYKTS130 --list   # Generate timing report for TS130 WGS_NYK - edit ID: RULEOBSER00008

# Show help and all available options
python main_processor.py --help
```

### RefDB Value Replacement Commands

**RefDB** (Reference Database) functionality allows you to replace specific values in JSON files with predefined values from `refdb_values.json`. This is useful for standardizing test data across refdb-specific models.

**Currently Supported RefDB Models:**
- **WGS_CSBD**: CSBDTS_46 (Multiple E&M Same day), CSBDTS_47 (Multiple Billing of Obstetrical Services), CSBDTS_59 (Antepartum Services)
- **WGS_KERNAL**: NYKTS_123 (Observation Services)

**RefDB Value Replacement:**
The `--refdb` flag automatically replaces the following variables in JSON files:
- `HCID` - Healthcare ID
- `PAT_BRTH_DT` - Patient Birth Date
- `PAT_FRST_NME` - Patient First Name
- `PAT_LAST_NM` - Patient Last Name
- `PROV_TAX_ID` - Provider Tax ID
- `BILLG_NPI` - Billing NPI
- `NAT_EA2_RNDR_NPI` - National EA2 Renderer NPI

**RefDB Commands:**
```bash
# Process WGS_CSBD refdb models with value replacement
python main_processor.py --wgs_csbd --CSBDTS46 --refdb    # Process TS46 with refdb value replacement - edit ID: RULEEMSD000002
python main_processor.py --wgs_csbd --CSBDTS47 --refdb    # Process TS47 with refdb value replacement - edit ID: RULEMBOS000001
python main_processor.py --wgs_csbd --CSBDTS59 --refdb    # Process TS59 (Antepartum Services) with refdb value replacement - edit ID: RULESUB4000001

# Process WGS_NYK refdb models with value replacement
python main_processor.py --wgs_nyk --NYKTS123 --refdb    # Process NYKTS123 with refdb value replacement - edit ID: RULEOBSER00001

# Process ALL refdb-supported models with value replacement
python main_processor.py --wgs_csbd --all --refdb        # Process all WGS_CSBD refdb models (CSBDTS46, CSBDTS47, CSBDTS59)
python main_processor.py --wgs_nyk --all --refdb       # Process all WGS_NYK refdb models (NYKTS123)

# Process refdb models without Postman collection generation
python main_processor.py --wgs_csbd --CSBDTS46 --refdb --no-postman    # edit ID: RULEEMSD000002
python main_processor.py --wgs_csbd --CSBDTS47 --refdb --no-postman    # edit ID: RULEMBOS000001
python main_processor.py --wgs_csbd --CSBDTS59 --refdb --no-postman    # edit ID: RULESUB4000001
python main_processor.py --wgs_nyk --NYKTS123 --refdb --no-postman    # edit ID: RULEOBSER00001
```

**RefDB Configuration:**
- Values are loaded from `refdb_values.json` based on the specified model type
- The configuration file contains model-specific default values
- Only refdb-specific models (CSBDTS_46, CSBDTS_47, CSBDTS_59, NYKTS_123) will be processed when using `--refdb` flag
- Files from non-refdb models will be skipped with a warning message
- Windows encoding issues have been resolved with automatic UTF-8 encoding configuration

**Note:** The `--refdb` flag must be used with a refdb-supported model. Attempting to use `--refdb` with non-refdb models will result in the refdb processing being skipped.

**What these commands do:**
- ✅ Rename files from 3-part format (`TC#XX_XXXXX#suffix.json`) to 5-part format (`TC#XX_XXXXX#edit_id#code#mapped_suffix.json`)
- ✅ Move files to organized directory structure
- ✅ Generate Postman collections for API testing (unless `--no-postman` is used)
- ✅ Provide detailed processing output and summary
- ✅ Generate timing reports for performance analysis (when using `--list` with model flags)

**✅ Verification Status:**

### WGS_CSBD Models (29 total):
- `python main_processor.py --wgs_csbd --CSBDTS01` - **TESTED & WORKING** ✓ (edit ID: RULEEM000001)
- `python main_processor.py --wgs_csbd --CSBDTS02` - **TESTED & WORKING** ✓ (edit ID: RULELATE000001)  
- `python main_processor.py --wgs_csbd --CSBDTS03` - **TESTED & WORKING** ✓ (edit ID: RULEREVE000005)
- `python main_processor.py --wgs_csbd --CSBDTS04` - **TESTED & WORKING** ✓ (edit ID: RULEREVE000004)
- `python main_processor.py --wgs_csbd --CSBDTS05` - **TESTED & WORKING** ✓ (edit ID: RULEREVE000003)
- `python main_processor.py --wgs_csbd --CSBDTS06` - **TESTED & WORKING** ✓ (edit ID: RULEREVE000002)
- `python main_processor.py --wgs_csbd --CSBDTS07` - **TESTED & WORKING** ✓ (edit ID: RULEREVE000001)
- `python main_processor.py --wgs_csbd --CSBDTS08` - **TESTED & WORKING** ✓ (edit ID: RULELAB0000009)
- `python main_processor.py --wgs_csbd --CSBDTS09` - **TESTED & WORKING** ✓ (edit ID: RULEDEVI000003)
- `python main_processor.py --wgs_csbd --CSBDTS10` - **TESTED & WORKING** ✓ (edit ID: RULERECO000001)
- `python main_processor.py --wgs_csbd --CSBDTS11` - **TESTED & WORKING** ✓ (edit ID: RULERECO000003)
- `python main_processor.py --wgs_csbd --CSBDTS12` - **TESTED & WORKING** ✓ (edit ID: RULEINCI000001)
- `python main_processor.py --wgs_csbd --CSBDTS13` - **TESTED & WORKING** ✓ (edit ID: RULERCE0000006)
- `python main_processor.py --wgs_csbd --CSBDTS14` - **TESTED & WORKING** ✓ (edit ID: RULERCE000001)
- `python main_processor.py --wgs_csbd --CSBDTS15` - **TESTED & WORKING** ✓ (edit ID: RULERCE000005)
- `python main_processor.py --wgs_csbd --CSBDTS20` - **TESTED & WORKING** ✓ (edit ID: RULERBWR000001)
- `python main_processor.py --wgs_csbd --CSBDTS46` - **TESTED & WORKING** ✓ (edit ID: RULEEMSD000002)
- `python main_processor.py --wgs_csbd --CSBDTS47` - **TESTED & WORKING** ✓ (edit ID: RULEMBOS000001)
- `python main_processor.py --wgs_csbd --CSBDTS48` - **TESTED & WORKING** ✓ (edit ID: RULERCTH00001)
- `python main_processor.py --wgs_csbd --CSBDTS49` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00001)
- `python main_processor.py --wgs_csbd --CSBDTS50` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00002)
- `python main_processor.py --wgs_csbd --CSBDTS51` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00003)
- `python main_processor.py --wgs_csbd --CSBDTS52` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00004)
- `python main_processor.py --wgs_csbd --CSBDTS53` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00005)
- `python main_processor.py --wgs_csbd --CSBDTS54` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00006)
- `python main_processor.py --wgs_csbd --CSBDTS55` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00007)
- `python main_processor.py --wgs_csbd --CSBDTS56` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00008)
- `python main_processor.py --wgs_csbd --CSBDTS57` - **TESTED & WORKING** ✓ (edit ID: RULERADDON00001)
- `python main_processor.py --wgs_csbd --CSBDTS59` - **TESTED & WORKING** ✓ (edit ID: RULESUB4000001)
- `python main_processor.py --wgs_csbd --all` - **TESTED & WORKING** ✓

### GBDF_MCR Models:
- `python main_processor.py --gbdf_mcr --GBDTS47` - **TESTED & WORKING** ✓ (edit ID: RULEEM000001, recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS62` - **TESTED & WORKING** ✓ (edit ID: RULEUSD00100_outpt_MCR, recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS70` - **TESTED & WORKING** ✓ (edit ID: RULE00000376, recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS138` - **TESTED & WORKING** ✓ (edit ID: RULEEMSD000002, recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS140` - **TESTED & WORKING** ✓ (edit ID: RULENDCUOM000001, recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS144` - **TESTED & WORKING** ✓ (edit ID: RULENEBU000001, recommended format)
- `python main_processor.py --gbdf_mcr --GBDTS146` - **TESTED & WORKING** ✓ (edit ID: RULENMP000001, recommended format)
- `python main_processor.py --gbdf_mcr --all` - **TESTED & WORKING** ✓

### GBDF_GRS Models:
- `python main_processor.py --gbdf_grs --GBDTS63` - **TESTED & WORKING** ✓ (edit ID: RULEUSD00100_Outpt_GRS)
- `python main_processor.py --gbdf_grs --GBDTS61` - **TESTED & WORKING** ✓ (edit ID: RULEUSD00100_Prof_GRS)
- `python main_processor.py --gbdf_grs --TS139` - **TESTED & WORKING** ✓ (edit ID: RULEEMSD000002)
- `python main_processor.py --gbdf_grs --TS141` - **TESTED & WORKING** ✓ (edit ID: RULENDCUOM000001)
- `python main_processor.py --gbdf_grs --TS145` - **TESTED & WORKING** ✓ (edit ID: RULENEBU000001)
- `python main_processor.py --gbdf_grs --TS147` - **TESTED & WORKING** ✓ (edit ID: RULENMP000001)
- `python main_processor.py --gbdf_grs --all` - **TESTED & WORKING** ✓

### WGS_NYK Models:
- `python main_processor.py --wgs_nyk --NYKTS122` - **TESTED & WORKING** ✓ (edit ID: RULERCTH00001)
- `python main_processor.py --wgs_nyk --NYKTS123` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00001)
- `python main_processor.py --wgs_nyk --NYKTS124` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00002)
- `python main_processor.py --wgs_nyk --NYKTS125` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00003)
- `python main_processor.py --wgs_nyk --NYKTS126` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00004)
- `python main_processor.py --wgs_nyk --NYKTS127` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00005)
- `python main_processor.py --wgs_nyk --NYKTS128` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00006)
- `python main_processor.py --wgs_nyk --NYKTS129` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00007)
- `python main_processor.py --wgs_nyk --NYKTS130` - **TESTED & WORKING** ✓ (edit ID: RULEOBSER00008)
- `python main_processor.py --wgs_nyk --NYKTS132` - **TESTED & WORKING** ✓ (edit ID: RULERADDON00001)
- `python main_processor.py --wgs_nyk --all` - **TESTED & WORKING** ✓

### General Commands:
- `python main_processor.py --list` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --CSBDTS47 --list` - **TESTED & WORKING** ✓ (Generates timing report, edit ID: RULEMBOS000001)
- `python main_processor.py --gbdf_mcr --GBDTS47 --list` - **TESTED & WORKING** ✓ (Generates timing report, edit ID: RULEEM000001)
- `python main_processor.py --gbdf_grs --TS139 --list` - **TESTED & WORKING** ✓ (Generates timing report, edit ID: RULEEMSD000002)
- `python main_processor.py --wgs_nyk --NYKTS130 --list` - **TESTED & WORKING** ✓ (Generates timing report, edit ID: RULEOBSER00008)

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
- Observation Services (CSBDTS49, CSBDTS50-CSBDTS56)

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
2. **`rename_files.py`** - File renaming module that handles JSON file renaming, header/footer transformations, and model information extraction
3. **`postman_generator.py`** - Core engine for creating Postman collections from JSON files
4. **`postman_cli.py`** - Standalone CLI interface for Postman operations
5. **`models_config.py`** - Configuration manager supporting both static and dynamic configurations
6. **`dynamic_models.py`** - Auto-discovery engine that detects TS folders and extracts parameters
7. **`report_generate.py`** - Master report generation module (consolidated from excel_report_generator.py) - Excel report generation with timing data, performance analytics, and comprehensive reporting functionality

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

For detailed architecture information, see `Docs/project_architecture_diagram.md`.

For comprehensive file connections and demo guide, see `Docs/FILE_CONNECTIONS_DEMO_GUIDE.md`.

For Excel reporting functionality, see `Docs/EXCEL_REPORTING_GUIDE.md`.

## Project Structure

```
renaming_files/
├── main_processor.py                  # Main consolidated processor (combines file renaming + Postman generation)
├── rename_files.py                    # File renaming module (handles JSON renaming, header/footer transformations)
├── postman_generator.py               # Postman collection generator
├── postman_cli.py                     # CLI for Postman operations
├── models_config.py                   # Configuration for different test models
├── dynamic_models.py                  # Dynamic model discovery and management
├── report_generate.py                 # Master report generation module (Excel reports, timing data, performance analytics)
├── refdb_change.py                    # RefDB value replacement for refdb-specific models
├── auto_edit_processor.py             # Auto-generates model config from edits_list.xlsx
├── requirements.txt                   # Python dependencies
├── .env.example                       # Example environment configuration (copy to .env)
├── Docs/                              # Documentation directory
│   ├── project_architecture_diagram.md    # Visual architecture documentation
│   ├── EXCEL_REPORTING_GUIDE.md          # Excel reporting functionality guide
│   └── FILE_CONNECTIONS_DEMO_GUIDE.md    # File architecture and connections demo guide
├── renaming_jsons/                    # Output directory for renamed files
│   ├── WGS_CSBD/                      # WGS_CSBD processed files
│   │   ├── TS_01_Covid_WGS_CSBD_RULEEM000001_00W04_dis/
│   │   │   └── regression/
│   │   │       └── TC#01_sample#RULEEM000001#00W04#LR.json
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
│   │   ├── TS_63_Unspecified_dx_code_outpt_gbdf_grs_RULEUSD00100_Outpt_GRS_v17_dis/
│   │   ├── TS_62_Unspecified_dx_code_outpt_gbdf_mcr_RULEUSD00100_outpt_MCR_v17_dis/
│   │   ├── TS_138_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/
│   │   ├── TS_139_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/
│   │   ├── TS_140_NDC UOM Validation Edit Expansion Iprep-138_gbdf_mcr_RULENDCUOM000001_v41_dis/
│   │   ├── TS_141_NDC UOM Validation Edit Expansion Iprep-138_gbdf_grs_RULENDCUOM000001_v41_dis/
│   │   ├── TS_144_Nebulizer A52466 IPERP-132_gbdf_mcr_RULENEBU000001_v18_dis/
│   │   ├── TS_145_Nebulizer A52466 IPERP-132_gbdf_grs_RULENEBU000001_v18_dis/
│   │   ├── TS_146_No match of Procedure code_gbdf_mcr_RULENMP000001_v18_dis/
│   │   └── TS_147_No match of Procedure code_gbdf_grs_RULENMP000001_v18_dis/
│   └── WGS_KERNAL/                    # WGS_NYK processed files (Note: folder name is WGS_KERNAL)
│       ├── NYKTS_122_Revenue code to HCPCS Alignment edit_WGS_NYK_RULERCTH00001_00W26_dis/
│       ├── NYKTS_123_Observation_Services_WGS_NYK_RULEOBSER00001_00W28_dis/
│       ├── NYKTS_124_Observation_Services_WGS_NYK_RULEOBSER00002_00W28_dis/
│       ├── NYKTS_125_Observation_Services_WGS_NYK_RULEOBSER00003_00W28_dis/
│       ├── NYKTS_126_Observation_Services_WGS_NYK_RULEOBSER00004_00W28_dis/
│       ├── NYKTS_127_Observation_Services_WGS_NYK_RULEOBSER00005_00W28_dis/
│       ├── NYKTS_128_Observation_Services_WGS_NYK_RULEOBSER00006_00W28_dis/
│       ├── NYKTS_129_Observation_Services_WGS_NYK_RULEOBSER00007_00W28_dis/
│       ├── NYKTS_130_Observation_Services_WGS_NYK_RULEOBSER00008_00W28_dis/
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
│       ├── NYKTS_122_Revenue code to HCPCS Alignment edit_Collection/
│       ├── NYKTS_123_Observation_Services_Collection/
│       ├── NYKTS_124_Observation_Services_Collection/
│       ├── NYKTS_125_Observation_Services_Collection/
│       ├── NYKTS_126_Observation_Services_Collection/
│       ├── NYKTS_127_Observation_Services_Collection/
│       ├── NYKTS_128_Observation_Services_Collection/
│       ├── NYKTS_129_Observation_Services_Collection/
│       ├── NYKTS_130_Observation_Services_Collection/
│       └── NYKTS_132_add_on without base_Collection/
├── reports/                           # Excel timing reports
│   ├── collection_reports/            # Excel timing reports with timestamps
│   │   ├── JSON_Renaming_Timing_Report_WGS_CSBD_20251016_192351.xlsx
│   │   ├── JSON_Renaming_Timing_Report_GBDF_MCR_YYYYMMDD_HHMMSS.xlsx
│   │   └── JSON_Renaming_Timing_Report_GBDF_GRS_YYYYMMDD_HHMMSS.xlsx
│   └── list_reports/                  # List-based reports and analytics
├── source_folder/                     # Source directory (original files)
│   ├── WGS_CSBD/                      # WGS_CSBD source files
│   │   ├── TS_01_Covid_WGS_CSBD_RULEEM000001_00W04_sur/
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
- **RefDB Value Replacement**: Automatically replaces specific values (HCID, PAT_BRTH_DT, PAT_FRST_NME, PAT_LAST_NM, PROV_TAX_ID, BILLG_NPI, NAT_EA2_RNDR_NPI) in refdb-specific models using values from `refdb_values.json`
- **Dynamic Model Discovery**: Automatically detects TS folders and extracts model parameters
- **Modular Architecture**: Clean separation of concerns with dedicated modules (`rename_files.py`, `postman_generator.py`, `report_generate.py`, etc.)
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
- Python 3.8 or higher
- Required Python modules: `os`, `re`, `shutil`, `json`, `uuid`, `pathlib` (all are standard library modules)
- Additional dependencies: `pandas`, `openpyxl`, `python-dotenv` (installed via `requirements.txt`)

### Installation
```bash
# Install required dependencies
pip install -r requirements.txt
```

**Environment configuration (optional):**
```bash
# Copy the example env file and edit as needed
# Git Bash / Linux / macOS:
cp .env.example .env
# Windows CMD:
copy .env.example .env

# In .env you can configure:
# ENABLE_REPORT_GENERATION=true   # Set to false to disable Excel report generation
```

**Note**: The `requirements.txt` file contains all necessary dependencies for the project including Excel reporting functionality.

### Running the Scripts

> **💡 Quick Start:** For immediate usage, see the [Quick Start Commands](#-quick-start-commands-verified--ready-to-use) section above.

#### 1. Enhanced Script with Postman Integration (Recommended)

The enhanced script supports direct command-line arguments for processing specific models with the required `--wgs_csbd` flag:

```bash
# Process specific WGS_CSBD TS models (WGS_CSBD flag required)
python main_processor.py --wgs_csbd --CSBDTS01    # Process TS01 model (Covid) - edit ID: RULEEM000001
python main_processor.py --wgs_csbd --CSBDTS02    # Process TS02 model (Laterality Policy) - edit ID: RULELATE000001
python main_processor.py --wgs_csbd --CSBDTS03    # Process TS03 model (Revenue Sub Edit 5) - edit ID: RULEREVE000005
python main_processor.py --wgs_csbd --CSBDTS04    # Process TS04 model (Revenue Sub Edit 4) - edit ID: RULEREVE000004
python main_processor.py --wgs_csbd --CSBDTS05    # Process TS05 model (Revenue Sub Edit 3) - edit ID: RULEREVE000003
python main_processor.py --wgs_csbd --CSBDTS06    # Process TS06 model (Revenue Sub Edit 2) - edit ID: RULEREVE000002
python main_processor.py --wgs_csbd --CSBDTS07    # Process TS07 model (Revenue Sub Edit 1) - edit ID: RULEREVE000001
python main_processor.py --wgs_csbd --CSBDTS08    # Process TS08 model (Lab panel Model) - edit ID: RULELAB0000009
python main_processor.py --wgs_csbd --CSBDTS09    # Process TS09 model (Device Dependent Procedures) - edit ID: RULEDEVI000003
python main_processor.py --wgs_csbd --CSBDTS10    # Process TS10 model (Recovery Room Reimbursement) - edit ID: RULERECO000001
python main_processor.py --wgs_csbd --CSBDTS11    # Process TS11 model (Revenue Code to HCPCS Xwalk-1B) - edit ID: RULERECO000003
python main_processor.py --wgs_csbd --CSBDTS12    # Process TS12 model (Incidentcal Services Facility) - edit ID: RULEINCI000001
python main_processor.py --wgs_csbd --CSBDTS13    # Process TS13 model (Revenue model CR v3) - edit ID: RULERCE0000006
python main_processor.py --wgs_csbd --CSBDTS14    # Process TS14 model (HCPCS to Revenue Code Xwalk) - edit ID: RULERCE000001
python main_processor.py --wgs_csbd --CSBDTS15    # Process TS15 model (revenue model) - edit ID: RULERCE000005

# Process specific GBDF MCR models (GBDF_MCR flag required - Recommended format: --GBDTSXX)
python main_processor.py --gbdf_mcr --GBDTS47    # Process TS47 model (Covid GBDF MCR) - edit ID: RULEEM000001
python main_processor.py --gbdf_mcr --GBDTS62    # Process TS62 model (Unspecified dx code outpt GBDF MCR) - edit ID: RULEUSD00100_outpt_MCR
python main_processor.py --gbdf_mcr --GBDTS70    # Process TS70 model (InappropriatePrimaryDiagnosis GBDF MCR) - edit ID: RULE00000376
python main_processor.py --gbdf_mcr --GBDTS138   # Process TS138 model (Multiple E&M Same day GBDF MCR) - edit ID: RULEEMSD000002
python main_processor.py --gbdf_mcr --GBDTS140   # Process TS140 model (NDC UOM Validation Edit Expansion Iprep-138 GBDF MCR) - edit ID: RULENDCUOM000001
python main_processor.py --gbdf_mcr --GBDTS144   # Process TS144 model (Nebulizer A52466 IPERP-132 GBDF MCR) - edit ID: RULENEBU000001
python main_processor.py --gbdf_mcr --GBDTS146   # Process TS146 model (No match of Procedure code GBDF MCR) - edit ID: RULENMP000001


# Process specific GBDF GRS models (GBDF_GRS flag required)
python main_processor.py --gbdf_grs --GBDTS63    # Process TS63 model (Unspecified dx code outpt GBDF GRS) - edit ID: RULEUSD00100_Outpt_GRS
python main_processor.py --gbdf_grs --GBDTS61    # Process TS61 model (Unspecified dx code prof GBDF GRS) - edit ID: RULEUSD00100_Prof_GRS
python main_processor.py --gbdf_grs --TS139   # Process TS139 model (Multiple E&M Same day GBDF GRS) - edit ID: RULEEMSD000002
python main_processor.py --gbdf_grs --TS141   # Process TS141 model (NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS) - edit ID: RULENDCUOM000001
python main_processor.py --gbdf_grs --TS145   # Process TS145 model (Nebulizer A52466 IPERP-132 GBDF GRS) - edit ID: RULENEBU000001
python main_processor.py --gbdf_grs --TS147   # Process TS147 model (No match of Procedure code GBDF GRS) - edit ID: RULENMP000001

# Process specific WGS_NYK models (WGS_NYK flag required - Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS122   # Process TS122 model (Revenue code to HCPCS Alignment edit WGS NYK) - edit ID: RULERCTH00001
python main_processor.py --wgs_nyk --NYKTS123   # Process TS123 model (Observation Services WGS NYK) - edit ID: RULEOBSER00001
python main_processor.py --wgs_nyk --NYKTS124   # Process TS124 model (Observation Services WGS NYK) - edit ID: RULEOBSER00002
python main_processor.py --wgs_nyk --NYKTS125   # Process TS125 model (Observation Services WGS NYK) - edit ID: RULEOBSER00003
python main_processor.py --wgs_nyk --NYKTS126   # Process TS126 model (Observation Services WGS NYK) - edit ID: RULEOBSER00004
python main_processor.py --wgs_nyk --NYKTS127   # Process TS127 model (Observation Services WGS NYK) - edit ID: RULEOBSER00005
python main_processor.py --wgs_nyk --NYKTS128   # Process TS128 model (Observation Services WGS NYK) - edit ID: RULEOBSER00006
python main_processor.py --wgs_nyk --NYKTS129   # Process TS129 model (Observation Services WGS NYK) - edit ID: RULEOBSER00007
python main_processor.py --wgs_nyk --NYKTS130   # Process TS130 model (Observation Services WGS NYK) - edit ID: RULEOBSER00008
python main_processor.py --wgs_nyk --NYKTS132   # Process TS132 model (add_on without base WGS NYK) - edit ID: RULERADDON00001

# Process all configured models
python main_processor.py --wgs_csbd --all     # Process all WGS_CSBD models
python main_processor.py --gbdf_mcr --all     # Process all GBDF MCR models
python main_processor.py --gbdf_grs --all     # Process all GBDF GRS models
python main_processor.py --wgs_nyk --all     # Process all WGS_NYK models

# Process refdb models with value replacement (refdb-specific models only)
python main_processor.py --wgs_csbd --CSBDTS46 --refdb    # Process TS46 with refdb value replacement - edit ID: RULEEMSD000002
python main_processor.py --wgs_csbd --CSBDTS47 --refdb    # Process TS47 with refdb value replacement - edit ID: RULEMBOS000001
python main_processor.py --wgs_csbd --CSBDTS59 --refdb    # Process TS59 (Antepartum Services) with refdb value replacement - edit ID: RULESUB4000001
python main_processor.py --wgs_nyk --NYKTS123 --refdb    # Process NYKTS123 with refdb value replacement - edit ID: RULEOBSER00001

# Process models without generating Postman collection
python main_processor.py --wgs_csbd --CSBDTS07 --no-postman    # edit ID: RULEREVE000001
python main_processor.py --gbdf_mcr --GBDTS47 --no-postman    # edit ID: RULEEM000001
python main_processor.py --gbdf_mcr --GBDTS138 --no-postman    # edit ID: RULEEMSD000002
python main_processor.py --gbdf_mcr --GBDTS140 --no-postman    # edit ID: RULENDCUOM000001
python main_processor.py --gbdf_mcr --GBDTS146 --no-postman    # edit ID: RULENMP000001
python main_processor.py --gbdf_grs --TS139 --no-postman    # edit ID: RULEEMSD000002
python main_processor.py --gbdf_grs --TS141 --no-postman    # edit ID: RULENDCUOM000001
python main_processor.py --gbdf_grs --TS147 --no-postman    # edit ID: RULENMP000001

# Show help and available options
python main_processor.py --help
```

**Command Options:**
- `--wgs_csbd`: **REQUIRED** flag for WGS_CSBD TS model processing
- `--gbdf_mcr`: **REQUIRED** flag for GBDF MCR model processing
- `--gbdf_grs`: **REQUIRED** flag for GBDF GRS model processing
- `--wgs_nyk`: **REQUIRED** flag for WGS_NYK TS model processing
- `--CSBDTS01` through `--CSBDTS15`: Process specific WGS_CSBD TS models
- `--CSBDTS20`, `--CSBDTS46`, `--CSBDTS47`, `--CSBDTS48`, `--CSBDTS57`, `--CSBDTS59`: Process additional WGS_CSBD TS models (RadioservicesbilledwithoutRadiopharma, Multiple E&M Same day, Multiple Billing of Obstetrical Services, Revenue code to HCPCS Alignment edit, add_on without base, Antepartum Services)
- `--CSBDTS49` through `--CSBDTS56`: Process Observation Services WGS_CSBD models
- `--GBDTS47`, `--GBDTS48`, `--GBDTS62`, `--GBDTS64`, `--GBDTS70`, `--GBDTS138`, `--GBDTS140`, `--GBDTS144`, `--GBDTS146`: Process GBDF MCR models (Covid GBDF MCR, Multiple E&M Same day GBDF MCR, Unspecified dx code outpt_MCR GBDF MCR, Unspecified Prof_MCR GBDF MCR, InappropriatePrimaryDiagnosis GBDF MCR, NDC UOM Validation Edit Expansion Iprep-138 GBDF MCR, Nebulizer A52466 IPERP-132 GBDF MCR, No match of Procedure code GBDF MCR) - requires `--gbdf_mcr` flag
- `--GBDTS49`, `--GBDTS61`, `--GBDTS63`, `--GBDTS139`, `--GBDTS141`, `--GBDTS145`, `--GBDTS147`: Process GBDF GRS models (Multiple E&M Same day GBDF GRS, Unspecified dx code prof GBDF GRS, Unspecified Outpt_GRS GBDF GRS, NDC UOM Validation Edit Expansion Iprep-138 GBDF GRS, Nebulizer A52466 IPERP-132 GBDF GRS, No match of Procedure code GBDF GRS) - requires `--gbdf_grs` flag
- `--NYKTS122`, `--NYKTS123`, `--NYKTS124`, `--NYKTS125`, `--NYKTS126`, `--NYKTS127`, `--NYKTS128`, `--NYKTS129`, `--NYKTS130`, `--NYKTS132`: Process WGS_NYK models (Revenue code to HCPCS Alignment edit WGS NYK, Observation Services WGS NYK, add_on without base WGS NYK) - requires `--wgs_nyk` flag (Must use --NYKTSXX format)
- `--all`: Process all configured models (requires either --wgs_csbd, --gbdf_mcr, --gbdf_grs, or --wgs_nyk flag)
- `--refdb`: Apply refdb value replacement for refdb-specific models (CSBDTS_46, CSBDTS_47, CSBDTS_59, NYKTS_123) - replaces HCID, PAT_BRTH_DT, PAT_FRST_NME, PAT_LAST_NM, PROV_TAX_ID, BILLG_NPI, NAT_EA2_RNDR_NPI with values from `refdb_values.json`
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

The file renaming functionality is handled by the `rename_files.py` module, which is called by `main_processor.py`. This modular design allows for better code organization and maintainability.

#### File Renaming Process (via `rename_files.py`)
1. **Source Validation**: Checks if the source directory exists
2. **Directory Creation**: Creates the destination directory if it doesn't exist
3. **File Discovery**: Finds all JSON files in the source directory
4. **Parsing**: Extracts components from each filename
5. **Mapping**: Applies suffix mapping rules to determine correct suffix
6. **Header/Footer Transformation**: For WGS_CSBD files, applies header/footer structure with KEY_CHK_CDN_NBR generation
7. **Renaming**: Generates new filenames according to the 5-part template
8. **File Operations**: Copies files to destination with new names and removes originals
9. **Model Information Extraction**: Extracts model details from directory structure
10. **Logging**: Provides detailed output of all operations

#### Postman Collection Generation
1. **File Analysis**: Scans renamed JSON files for test case information
2. **Request Creation**: Creates Postman requests with proper headers and body
3. **Collection Structure**: Builds Postman collection with metadata
4. **File Generation**: Saves collection in Postman-compatible JSON format
5. **Validation**: Ensures collection structure is correct

## 🤖 Auto Edit Processor

The `auto_edit_processor.py` script automates the process of adding new model configurations to the project. It reads edit information from `edits_list.xlsx` and automatically generates entries in `models_config.py`, eliminating the need for manual configuration.

### Overview

The Auto Edit Processor:
1. Reads edits from `edits_list.xlsx` Excel file
2. Parses edit information from the "List of Edits that need to be Automated" column
3. Extracts EDIT ID, model name with LOB, and EOB code
4. Generates config entries in `STATIC_MODELS_CONFIG` format
5. Checks if command already exists to avoid duplicates
6. Updates `models_config.py` with new entries
7. Updates Excel file with command status

### Prerequisites

- Python 3.6 or higher
- `pandas` library (for Excel file processing)
- `openpyxl` library (for Excel file writing)
- `edits_list.xlsx` file with proper structure

### Excel File Structure

The `edits_list.xlsx` file should contain sheets for different model types:
- **WGS_CSBD**: For WGS_CSBD models
- **GBDF**: For GBDF MCR models
- **KERNAL**: For WGS_NYK (Kernal) models

Each sheet should have the following columns:
- **List of Edits that need to be Automated**: Contains edit strings in format like `RULEEM000001~covid~wgs~csbd~00W17--live`
- **Test Sutie ID**: (Optional) Will be populated with generated TS number
- **Cmd status**: (Optional) Will be set to "Created" after processing

### Edit String Format

The script supports flexible edit string formats:
- **Standard format**: `RULEEM000001~covid~wgs~csbd~00W17--live` (5 parts)
- **Short format**: `RULESUB4000001~Expansion on sub-edit4--live` (2 parts)
- **Any format**: `RULEXXX~part1~part2~...~partN--live` (any N parts)

The parser automatically:
- Extracts EDIT ID (first part before `~`)
- Finds EOB code (patterns like `00W04`, `v04`, `00W17`, etc.)
- Builds model name from remaining parts
- Handles `--live` suffix

### Usage

#### Basic Usage

```bash
# Process WGS_CSBD sheet (default)
python auto_edit_processor.py

# Process specific sheet
python auto_edit_processor.py --sheet WGS_CSBD
python auto_edit_processor.py --sheet GBDF
python auto_edit_processor.py --sheet GBDF_MCR
python auto_edit_processor.py --sheet GBDF_GRS
python auto_edit_processor.py --sheet KERNAL

# Sync Test Suite IDs from Excel to models_config.py (sync-only mode)
python auto_edit_processor.py --sync-from-excel --sheet WGS_CSBD
python auto_edit_processor.py --sync-from-excel --sheet GBDF
python auto_edit_processor.py --sync-from-excel --sheet KERNAL

# Sort STATIC_MODELS_CONFIG by ts_number (ascending) for all models
python auto_edit_processor.py --sort-config

# Use custom Excel file
python auto_edit_processor.py --excel my_edits.xlsx

# Dry run (preview changes without updating files)
python auto_edit_processor.py --dry-run
```

#### Command Options

- `--sheet SHEET_NAME`: Excel sheet name to process (default: `WGS_CSBD`)
  - Options: `WGS_CSBD`, `GBDF`, `GBDF_MCR`, `GBDF_GRS`, `KERNAL`
- `--excel EXCEL_PATH`: Path to Excel file (default: `edits_list.xlsx`)
- `--dry-run`: Preview changes without updating files
- `--sync-from-excel`: Sync STATIC_MODELS_CONFIG from Excel Test Suite IDs (updates models_config.py only)
- `--sort-config`: Sort STATIC_MODELS_CONFIG by ts_number in ascending order for all models

### How It Works

1. **Read Excel File**: Loads the specified sheet from `edits_list.xlsx`
2. **Parse Edit Strings**: Extracts EDIT ID, model name, and EOB code from each row
3. **Check Existing Configs**: Verifies if edit already exists in `models_config.py`
4. **Generate TS Number**: Automatically assigns next available TS number
5. **Generate Config Entry**: Creates complete configuration dictionary
6. **Update Files**: 
   - Adds new entries to `models_config.py`
   - Updates Excel file with Test Suite ID and command status

### Example Output

```
============================================================
Processing edits from WGS_CSBD sheet
============================================================

[INFO] Processing edit: RULEEM000001
  Model: covid_wgs_csbd
  EOB Code: 00W04
  [SUCCESS] Generated config for TS58
  Command: python main_processor.py --wgs_csbd --CSBDTS58    # edit ID: RULEEM000001

============================================================
SUMMARY: Generated 1 new config entries
============================================================

TS58: RULEEM000001 - python main_processor.py --wgs_csbd --CSBDTS58    # edit ID: RULEEM000001

============================================================
Updating files...
============================================================

[SUCCESS] Updated models_config.py with 1 new entries
[SUCCESS] Updated edits_list.xlsx with command information

============================================================
Processing complete!
============================================================
```

### Features

- **Automatic TS Number Assignment**: Finds next available TS number automatically
- **Duplicate Detection**: Checks for existing edit IDs and EOB codes
- **Flexible Parsing**: Handles various edit string formats
- **EOB Code Detection**: Automatically finds EOB codes in multiple formats
- **Excel Integration**: Updates Excel file with generated commands
- **Dry Run Mode**: Preview changes before applying
- **Error Handling**: Skips invalid entries with clear error messages
- **Sync from Excel**: `--sync-from-excel` syncs Test Suite IDs from Excel to models_config.py
- **Ascending Order**: Config is kept sorted by ts_number (ascending) for all models; use `--sort-config` to sort manually

### Generated Configuration

The script generates configuration entries in this format:

```python
{
    "ts_number": "58",
    "edit_id": "RULEEM000001",
    "code": "00W04",
    "source_dir": "source_folder/WGS_CSBD/CSBDTS_58_Covid_WGS_CSBD_RULEEM000001_00W04_sur/payloads/regression",
    "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_58_Covid_WGS_CSBD_RULEEM000001_00W04_dis/payloads/regression",
    "postman_collection_name": "CSBDTS_58_Covid_Collection",
    "postman_file_name": "covid_wgs_csbd_RULEEM000001_00W04.json"
}
```

### Warnings and Notes

- **EOB Code Placeholder**: If EOB code is not found, uses `00W00` as placeholder - verify and update manually if needed
- **Existing Commands**: Script warns if command already exists in Excel but continues processing
- **Duplicate Edit IDs**: Script skips entries that already exist with same EDIT ID and EOB code
- **Test Suite ID**: If Test Suite ID is already set in Excel, script uses that TS number instead of generating new one

### Troubleshooting

**Issue**: "Column 'List of Edits that need to be Automated' not found"
- **Solution**: Ensure the Excel sheet has the correct column name

**Issue**: "EOB code not found - using placeholder"
- **Solution**: Verify edit string contains EOB code (e.g., `00W04`, `v17`) or manually update in `models_config.py` after processing

**Issue**: "Command already exists"
- **Solution**: Script will skip duplicate entries. Check Excel file for existing commands

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
$ python main_processor.py --wgs_csbd --CSBDTS01    # edit ID: RULEEM000001
✅ Configuration loaded with dynamic discovery

🚀 Processing 1 model(s)...
============================================================

📋 Processing Model 1/1: TS_01 (RULEEM000001_00W04)
----------------------------------------
Files to be renamed and moved:
============================================================
Current: TC#01_od#deny.json
Converting to new template...
New:     TC#01_od#RULEEM000001#00W04#LR.json
Moving to: renaming_jsons\TS_01_Covid_WGS_CSBD_RULEEM000001_00W04_dis\regression
----------------------------------------
[INFO] Generated random 11-digit number for KEY_CHK_CDN_NBR (payload level): 62620451899
✓ Successfully copied and renamed: TC#01_od#deny.json → TC#01_od#RULEEM000001#00W04#LR.json
✓ Removed original file: TC#01_od#deny.json

============================================================
Renaming and moving completed!
Files moved to: renaming_jsons\TS_01_Covid_WGS_CSBD_RULEEM000001_00W04_dis\regression

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

✅ Model TS_01 (RULEEM000001_00W04): Successfully processed 1 files

============================================================
📊 PROCESSING SUMMARY
============================================================
Models processed: 1
Successful models: 1
Total files processed: 1

✅ SUCCESSFUL MODELS:
   • TS_01 (RULEEM000001_00W04): 1 files

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
$ python main_processor.py --CSBDTS01    # edit ID: RULEEM000001
✅ Configuration loaded with dynamic discovery
❌ Error: --wgs_csbd flag is required for TS model processing!

Please use the --wgs_csbd flag with TS model commands:
  python main_processor.py --wgs_csbd --CSBDTS01    # Process TS01 model (Covid) - edit ID: RULEEM000001
  python main_processor.py --wgs_csbd --CSBDTS02    # Process TS02 model (Laterality Policy) - edit ID: RULELATE000001
  python main_processor.py --wgs_csbd --CSBDTS03    # Process TS03 model - edit ID: RULEREVE000005
  python main_processor.py --wgs_csbd --CSBDTS04    # Process TS04 model - edit ID: RULEREVE000004
  python main_processor.py --wgs_csbd --CSBDTS05    # Process TS05 model - edit ID: RULEREVE000003
  python main_processor.py --wgs_csbd --CSBDTS06    # Process TS06 model - edit ID: RULEREVE000002
  python main_processor.py --wgs_csbd --CSBDTS07    # Process TS07 model - edit ID: RULEREVE000001
  python main_processor.py --wgs_csbd --CSBDTS08    # Process TS08 model - edit ID: RULELAB0000009
  python main_processor.py --wgs_csbd --CSBDTS09    # Process TS09 model - edit ID: RULEDEVI000003
  python main_processor.py --wgs_csbd --CSBDTS10    # Process TS10 model - edit ID: RULERECO000001
  python main_processor.py --wgs_csbd --CSBDTS11    # Process TS11 model - edit ID: RULERECO000003
  python main_processor.py --wgs_csbd --CSBDTS12    # Process TS12 model - edit ID: RULEINCI000001
  python main_processor.py --wgs_csbd --CSBDTS13    # Process TS13 model - edit ID: RULERCE0000006
  python main_processor.py --wgs_csbd --CSBDTS14    # Process TS14 model - edit ID: RULERCE000001
  python main_processor.py --wgs_csbd --CSBDTS15    # Process TS15 model - edit ID: RULERCE000005
  python main_processor.py --wgs_csbd --all     # Process all discovered models

Use --help for more information.
```

#### Alternative Command Format Examples
```bash
# Using the main processor with different models (WGS_CSBD flag required)
$ python main_processor.py --wgs_csbd --CSBDTS01    # edit ID: RULEEM000001
✅ Configuration loaded with dynamic discovery
🚀 Processing 1 model(s)...
...

$ python main_processor.py --wgs_csbd --CSBDTS15    # edit ID: RULERCE000005
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
python main_processor.py --wgs_csbd --CSBDTS47 --list    # Generate timing report for TS47 WGS_CSBD - edit ID: RULEMBOS000001
python main_processor.py --gbdf_mcr --GBDTS47 --list    # Generate timing report for TS47 GBDF MCR - edit ID: RULEEM000001
python main_processor.py --gbdf_grs --TS139 --list   # Generate timing report for TS139 GBDF GRS - edit ID: RULEEMSD000002
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
    - `python main_processor.py --wgs_csbd --CSBDTS01` (edit ID: RULEEM000001)
     - `python main_processor.py --wgs_csbd --all`

2. **Missing WGS_CSBD Flag Error**
   ```
   ❌ Error: --wgs_csbd flag is required for TS model processing!
   ```
   - **Solution**: Always include the `--wgs_csbd` flag when processing WGS_CSBD TS models
   - **Examples**: 
    - `python main_processor.py --wgs_csbd --CSBDTS01` (edit ID: RULEEM000001)
    - `python main_processor.py --wgs_csbd --CSBDTS15` (edit ID: RULERCE000005)

3. **Missing GBDF_MCR Flag Error**
   ```
   ❌ Error: --gbdf_mcr flag is required for GBDF MCR TS model processing!
   ```
   - **Solution**: Always include the `--gbdf_mcr` flag when processing GBDF MCR models
   - **Examples**: 
    - `python main_processor.py --gbdf_mcr --GBDTS47` (Covid GBDF MCR model, edit ID: RULEEM000001) - Recommended format
    - `python main_processor.py --gbdf_mcr --GBDTS138` (Multiple E&M Same day GBDF MCR model, edit ID: RULEEMSD000002) - Recommended format
     - `python main_processor.py --gbdf_mcr --all`
   - **Note**: There are two different TS47 models:
    - `python main_processor.py --wgs_csbd --CSBDTS47` (Multiple Billing of Obstetrical Services - WGS_CSBD, edit ID: RULEMBOS000001)
    - `python main_processor.py --gbdf_mcr --GBDTS47` (Covid GBDF MCR - GBDF MCR, edit ID: RULEEM000001) - Recommended format

4. **Missing GBDF_GRS Flag Error**
   ```
   ❌ Error: --gbdf_grs flag is required for GBDF GRS TS model processing!
   ```
   - **Solution**: Always include the `--gbdf_grs` flag when processing GBDF GRS models
   - **Examples**: 
    - `python main_processor.py --gbdf_grs --TS139` (Multiple E&M Same day GBDF GRS model, edit ID: RULEEMSD000002)
     - `python main_processor.py --gbdf_grs --all`

5. **Missing WGS_NYK Flag Error**
   ```
   ❌ Error: --wgs_nyk flag is required for NYKTS model processing!
   ```
  - **Solution**: Always include the `--wgs_nyk` flag when processing WGS_NYK models
  - **Examples**: 
    - `python main_processor.py --wgs_nyk --NYKTS122` (Revenue code to HCPCS Alignment edit WGS NYK model, edit ID: RULERCTH00001) - Must use --NYKTSXX format
    - `python main_processor.py --wgs_nyk --NYKTS123` (Observation Services WGS NYK model, edit ID: RULEOBSER00001) - Must use --NYKTSXX format
    - `python main_processor.py --wgs_nyk --NYKTS124` (Observation Services WGS NYK model, edit ID: RULEOBSER00002) - Must use --NYKTSXX format
    - `python main_processor.py --wgs_nyk --NYKTS130` (Observation Services WGS NYK model, edit ID: RULEOBSER00008) - Must use --NYKTSXX format
    - `python main_processor.py --wgs_nyk --NYKTS132` (add_on without base WGS NYK model, edit ID: RULERADDON00001) - Must use --NYKTSXX format
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

12. **Windows Encoding Errors (RefDB Processing)**
   ```
   WARNING Refdb processing failed: 'charmap' codec can't encode character '\u26a0' in position 2
   ```
   - **Status**: ✅ **FIXED** - This issue has been resolved in the latest version
   - **Solution**: The script now automatically configures UTF-8 encoding for stdout/stderr on Windows
   - **Note**: If you still encounter encoding issues, ensure you're using the latest version of `refdb_change.py`
   - **Workaround**: The refdb processing will continue even if there are encoding warnings, but Unicode characters in output may not display correctly on older Windows systems

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
# Process WGS_CSBD models (TS01-TS15, TS20, TS46-TS49, CSBDTS50-CSBDTS57, TS59 supported with --wgs_csbd flag)
python main_processor.py --wgs_csbd --CSBDTS01    # Covid Collection - edit ID: RULEEM000001
python main_processor.py --wgs_csbd --CSBDTS02    # Laterality Collection - edit ID: RULELATE000001
python main_processor.py --wgs_csbd --CSBDTS03    # Revenue Sub Edit 5 Collection - edit ID: RULEREVE000005
python main_processor.py --wgs_csbd --CSBDTS04    # Revenue Sub Edit 4 Collection - edit ID: RULEREVE000004
python main_processor.py --wgs_csbd --CSBDTS05    # Revenue Sub Edit 3 Collection - edit ID: RULEREVE000003
python main_processor.py --wgs_csbd --CSBDTS06    # Revenue Sub Edit 2 Collection - edit ID: RULEREVE000002
python main_processor.py --wgs_csbd --CSBDTS07    # Revenue Sub Edit 1 Collection - edit ID: RULEREVE000001
python main_processor.py --wgs_csbd --CSBDTS08    # Lab panel Model Collection - edit ID: RULELAB0000009
python main_processor.py --wgs_csbd --CSBDTS09    # Device Dependent Procedures Collection - edit ID: RULEDEVI000003
python main_processor.py --wgs_csbd --CSBDTS10    # Recovery Room Reimbursement Collection - edit ID: RULERECO000001
python main_processor.py --wgs_csbd --CSBDTS11    # Revenue Code to HCPCS Xwalk-1B Collection - edit ID: RULERECO000003
python main_processor.py --wgs_csbd --CSBDTS12    # Incidentcal Services Facility Collection - edit ID: RULEINCI000001
python main_processor.py --wgs_csbd --CSBDTS13    # Revenue model CR v3 Collection - edit ID: RULERCE0000006
python main_processor.py --wgs_csbd --CSBDTS14    # HCPCS to Revenue Code Xwalk Collection - edit ID: RULERCE000001
python main_processor.py --wgs_csbd --CSBDTS15    # revenue model Collection - edit ID: RULERCE000005
python main_processor.py --wgs_csbd --CSBDTS20    # RadioservicesbilledwithoutRadiopharma Collection - edit ID: RULERBWR000001
python main_processor.py --wgs_csbd --CSBDTS46    # Multiple E&M Same day Collection - edit ID: RULEEMSD000002
python main_processor.py --wgs_csbd --CSBDTS47    # Multiple Billing of Obstetrical Services Collection - edit ID: RULEMBOS000001
python main_processor.py --wgs_csbd --CSBDTS48    # Revenue code to HCPCS Alignment edit Collection - edit ID: RULERCTH00001
python main_processor.py --wgs_csbd --CSBDTS59    # Antepartum Services Collection - edit ID: RULESUB4000001

# Process GBDF MCR models (with --gbdf_mcr flag) - use --GBDTS{number} format
python main_processor.py --gbdf_mcr --GBDTS47    # Covid - RULEEM000001
python main_processor.py --gbdf_mcr --GBDTS50    # Laterality - RULELATE000001
python main_processor.py --gbdf_mcr --GBDTS51    # Psm - PSMEM000001
python main_processor.py --gbdf_mcr --GBDTS53    # Psm - PSMEM000002
python main_processor.py --gbdf_mcr --GBDTS55    # Psm - PSMEM000003
python main_processor.py --gbdf_mcr --GBDTS57    # Psm - PSMEM000004
python main_processor.py --gbdf_mcr --GBDTS59    # Manifestation - RULEMAN000004
python main_processor.py --gbdf_mcr --GBDTS62    # Unspecified dx code outpt - RULEUSD00100_outpt_MCR
python main_processor.py --gbdf_mcr --GBDTS63    # Unspecified/Shadow - RULEUSD00100_Prof_MCR, RULEAMBU000001
python main_processor.py --gbdf_mcr --GBDTS65    # Gbdf/Inaccurate - RULEAMBU000001, RULE00000022
python main_processor.py --gbdf_mcr --GBDTS67    # Inaccurate - RULE00000022
python main_processor.py --gbdf_mcr --GBDTS68    # Inappropriate - RULE00000376
python main_processor.py --gbdf_mcr --GBDTS70    # Always - RULEALWA000001
python main_processor.py --gbdf_mcr --GBDTS71    # Gbdf - RULEEXCL000001
python main_processor.py --gbdf_mcr --GBDTS75    # Excludes/Anesthesia - RULEEXCL000001, RULEANES000001
python main_processor.py --gbdf_mcr --GBDTS78    # Clia - RULECLIA00001
python main_processor.py --gbdf_mcr --GBDTS81    # Gbdf - Ambulance Mileage
python main_processor.py --gbdf_mcr --GBDTS82    # Immunization - RULEIPVT000001
python main_processor.py --gbdf_mcr --GBDTS84    # Immuno Drugs - RULEIMMU000001
python main_processor.py --gbdf_mcr --GBDTS86    # Knee Orthosis - RULEKNEE000001
python main_processor.py --gbdf_mcr --GBDTS89    # JW Modifier - RULEJWME000001
python main_processor.py --gbdf_mcr --GBDTS91    # MNP Model - RULEEM0000012
python main_processor.py --gbdf_mcr --GBDTS93    # Multiple E&M Same Day - RULEEMSD000002
python main_processor.py --gbdf_mcr --GBDTS95    # NDC UOM - RULENDCUOM000001
python main_processor.py --gbdf_mcr --GBDTS97    # NDC Validation - RULENDC000001
python main_processor.py --gbdf_mcr --GBDTS99    # Nebulizer - RULENEBU000001
python main_processor.py --gbdf_mcr --GBDTS101   # No match Procedure - RULENMP000001
python main_processor.py --gbdf_mcr --GBDTS103   # Ostomy Supplies - RULEOSTO000001
python main_processor.py --gbdf_mcr --GBDTS105   # Trach Supply - RULETRAC000001
python main_processor.py --gbdf_mcr --GBDTS107   # Recovery room - RULERCRO000001
python main_processor.py --gbdf_mcr --GBDTS109   # Inappropriate Primary Dxs - RULEIPDXE00001
python main_processor.py --gbdf_mcr --GBDTS110   # Inappropriate Primary Dxs GRS - RULEIPDXE00001
python main_processor.py --gbdf_mcr --GBDTS111   # Geneticstesting - RULEGENE000001
python main_processor.py --gbdf_mcr --GBDTS114   # Revenue Code - RULERCWP000001
python main_processor.py --gbdf_mcr --GBDTS116   # Anatomical Modifier - RULEPMAM000001
python main_processor.py --gbdf_mcr --GBDTS117   # PSM algo - PSMEM000003_algo
python main_processor.py --gbdf_mcr --GBDTS119   # PSM algo - PSMEM000004_algo
python main_processor.py --gbdf_mcr --GBDTS121   # Sick - RULEEM000002_refdb
python main_processor.py --gbdf_mcr --GBDTS126   # Clia - RULECLIA00001
python main_processor.py --gbdf_mcr --GBDTS127   # Immunization - RULEIPVT000001
python main_processor.py --gbdf_mcr --GBDTS129   # Immuno Drugs - RULEIMMU000001
python main_processor.py --gbdf_mcr --GBDTS131   # Knee Orthosis - RULEKNEE000001
python main_processor.py --gbdf_mcr --GBDTS134   # JW Modifier - RULEJWME000001
python main_processor.py --gbdf_mcr --GBDTS136   # MNP Model - RULEEM0000012
python main_processor.py --gbdf_mcr --GBDTS138   # Multiple E&M Same day - RULEEMSD000002
python main_processor.py --gbdf_mcr --GBDTS140   # NDC UOM Iprep-138 - RULENDCUOM000001
python main_processor.py --gbdf_mcr --GBDTS142   # NDC Validation - RULENDC000001
python main_processor.py --gbdf_mcr --GBDTS144   # Nebulizer IPERP-132 - RULENEBU000001
python main_processor.py --gbdf_mcr --GBDTS146   # No match Procedure - RULENMP000001
python main_processor.py --gbdf_mcr --GBDTS148   # Ostomy Supplies - RULEOSTO000001
python main_processor.py --gbdf_mcr --GBDTS150   # Trach Supply - RULETRAC000001
python main_processor.py --gbdf_mcr --GBDTS152   # Recovery room - RULERCRO000001
python main_processor.py --gbdf_mcr --GBDTS154   # Inappropriate Primary Dxs - RULEIPDXE00001
python main_processor.py --gbdf_mcr --GBDTS155   # Inappropriate Primary Dxs GRS - RULEIPDXE00001
python main_processor.py --gbdf_mcr --GBDTS159   # Revenue Code - RULERCWP000001
python main_processor.py --gbdf_mcr --GBDTS161   # Anatomical Modifier - RULEPMAM000001
python main_processor.py --gbdf_mcr --GBDTS170   # Ambulance Mileage - RULEAMBU000001

# Process GBDF GRS models (with --gbdf_grs flag) - use --GBDTS{number} format
python main_processor.py --gbdf_grs --GBDTS48    # Covid - RULEEM000001
python main_processor.py --gbdf_grs --GBDTS49    # Laterality - RULELATE000001
python main_processor.py --gbdf_grs --GBDTS52    # Psm - PSMEM000001
python main_processor.py --gbdf_grs --GBDTS54    # Psm - PSMEM000002
python main_processor.py --gbdf_grs --GBDTS56    # Psm - PSMEM000003
python main_processor.py --gbdf_grs --GBDTS58    # Psm - PSMEM000004
python main_processor.py --gbdf_grs --GBDTS60    # Unspecified Outpt - RULEUSD00100_Outpt_GRS
python main_processor.py --gbdf_grs --GBDTS62    # Unspecified Prof - RULEUSD00100_Prof_GRS
python main_processor.py --gbdf_grs --GBDTS64    # Shadow - RULEAMBU000001
python main_processor.py --gbdf_grs --GBDTS66    # Inaccurate - RULE00000022
python main_processor.py --gbdf_grs --GBDTS67    # Inappropriate - RULE00000376
python main_processor.py --gbdf_grs --GBDTS69    # Always - RULEALWA000001
python main_processor.py --gbdf_grs --GBDTS72    # Excludes - RULEEXCL000001
python main_processor.py --gbdf_grs --GBDTS74    # Geneticstesting - RULEGENE000001
python main_processor.py --gbdf_grs --GBDTS76    # Anesthesia - RULEANES000001
python main_processor.py --gbdf_grs --GBDTS80    # Shadow Ambulance - RULEAMBU000001
python main_processor.py --gbdf_grs --GBDTS83    # Immunization - RULEIPVT000001
python main_processor.py --gbdf_grs --GBDTS85    # Immuno Drugs - RULEIMMU000001
python main_processor.py --gbdf_grs --GBDTS87    # Knee Orthosis - RULEKNEE000001
python main_processor.py --gbdf_grs --GBDTS88    # Manifestation - RULEMAN000004
python main_processor.py --gbdf_grs --GBDTS90    # JW Modifier - RULEJWME000001
python main_processor.py --gbdf_grs --GBDTS92    # MNP Model - RULEEM0000012
python main_processor.py --gbdf_grs --GBDTS94    # Multiple E&M Same Day - RULEEMSD000002
python main_processor.py --gbdf_grs --GBDTS96    # NDC UOM - RULENDCUOM000001
python main_processor.py --gbdf_grs --GBDTS98    # NDC Validation - RULENDC000001
python main_processor.py --gbdf_grs --GBDTS100   # Nebulizer - RULENEBU000001
python main_processor.py --gbdf_grs --GBDTS102   # No match Procedure - RULENMP000001
python main_processor.py --gbdf_grs --GBDTS104   # Ostomy Supplies - RULEOSTO000001
python main_processor.py --gbdf_grs --GBDTS106   # Trach Supply - RULETRAC000001
python main_processor.py --gbdf_grs --GBDTS108   # Recovery room - RULERCRO000001
python main_processor.py --gbdf_grs --GBDTS112   # Inappropriate Primary DX - RULEIPDXH00001
python main_processor.py --gbdf_grs --GBDTS113   # Revenue Code - RULERCWP000001
python main_processor.py --gbdf_grs --GBDTS115   # Anatomical Modifier - RULEPMAM000001
python main_processor.py --gbdf_grs --GBDTS118   # PSM algo - PSMEM000003_algo
python main_processor.py --gbdf_grs --GBDTS120   # PSM algo - PSMEM000004_algo
python main_processor.py --gbdf_grs --GBDTS122   # Sick - RULEEM000002_refdb
python main_processor.py --gbdf_grs --GBDTS128   # Immunization - RULEIPVT000001
python main_processor.py --gbdf_grs --GBDTS130   # Immuno Drugs - RULEIMMU000001
python main_processor.py --gbdf_grs --GBDTS132   # Knee Orthosis - RULEKNEE000001
python main_processor.py --gbdf_grs --GBDTS135   # JW Modifier - RULEJWME000001
python main_processor.py --gbdf_grs --GBDTS137   # MNP Model - RULEEM0000012
python main_processor.py --gbdf_grs --GBDTS139   # Multiple E&M Same day - RULEEMSD000002
python main_processor.py --gbdf_grs --GBDTS141   # NDC UOM Iprep-138 - RULENDCUOM000001
python main_processor.py --gbdf_grs --GBDTS143   # NDC Validation - RULENDC000001
python main_processor.py --gbdf_grs --GBDTS145   # Nebulizer IPERP-132 - RULENEBU000001
python main_processor.py --gbdf_grs --GBDTS147   # No match Procedure - RULENMP000001
python main_processor.py --gbdf_grs --GBDTS149   # Ostomy Supplies - RULEOSTO000001
python main_processor.py --gbdf_grs --GBDTS151   # Trach Supply - RULETRAC000001
python main_processor.py --gbdf_grs --GBDTS153   # Recovery room - RULERCRO000001
python main_processor.py --gbdf_grs --GBDTS157   # Inappropriate Primary DX - RULEIPDXH00001
python main_processor.py --gbdf_grs --GBDTS158   # Revenue Code - RULERCWP000001
python main_processor.py --gbdf_grs --GBDTS160   # Anatomical Modifier - RULEPMAM000001

# Process WGS_NYK models (with --wgs_nyk flag - Must use --NYKTSXX format)
python main_processor.py --wgs_nyk --NYKTS122   # Revenue code to HCPCS Alignment edit WGS NYK Collection - edit ID: RULERCTH00001
python main_processor.py --wgs_nyk --NYKTS123   # Observation Services WGS NYK Collection - edit ID: RULEOBSER00001
python main_processor.py --wgs_nyk --NYKTS124   # Observation Services WGS NYK Collection - edit ID: RULEOBSER00002
python main_processor.py --wgs_nyk --NYKTS125   # Observation Services WGS NYK Collection - edit ID: RULEOBSER00003
python main_processor.py --wgs_nyk --NYKTS126   # Observation Services WGS NYK Collection - edit ID: RULEOBSER00004
python main_processor.py --wgs_nyk --NYKTS127   # Observation Services WGS NYK Collection - edit ID: RULEOBSER00005
python main_processor.py --wgs_nyk --NYKTS128   # Observation Services WGS NYK Collection - edit ID: RULEOBSER00006
python main_processor.py --wgs_nyk --NYKTS129   # Observation Services WGS NYK Collection - edit ID: RULEOBSER00007
python main_processor.py --wgs_nyk --NYKTS130   # Observation Services WGS NYK Collection - edit ID: RULEOBSER00008
python main_processor.py --wgs_nyk --NYKTS132   # add_on without base WGS NYK Collection - edit ID: RULERADDON00001

# Process all models at once (46 WGS_CSBD, 62 GBDF MCR, 54 GBDF GRS, 14 WGS_NYK)
python main_processor.py --wgs_csbd --all     # All WGS_CSBD models
python main_processor.py --gbdf_mcr --all     # All GBDF MCR models
python main_processor.py --gbdf_grs --all     # All GBDF GRS models
python main_processor.py --wgs_nyk --all     # All WGS_NYK models

# Process all models without Postman generation
python main_processor.py --wgs_csbd --all --no-postman
python main_processor.py --gbdf_mcr --all --no-postman
python main_processor.py --gbdf_grs --all --no-postman
python main_processor.py --wgs_nyk --all --no-postman

# Process all refdb-supported models (WGS_CSBD: CSBDTS46, CSBDTS47, CSBDTS59; WGS_NYK: NYKTS123)
python main_processor.py --wgs_csbd --all --refdb
python main_processor.py --wgs_nyk --all --refdb

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
- **CSBDTS/** – WGS_CSBD processed files (e.g., CSBDTS_01_Covid, CSBDTS_46, CSBDTS_51–56)
- **NYKTS/** – WGS_NYK processed files (e.g., NYKTS_122–130)
- Each model folder has `payloads/regression/` and `payloads/smoke/` subfolders with JSON test case files
- Diverse model types: Covid, Multiple E&M Same day, Observation Services, Revenue code to HCPCS Alignment

**`postman_collections` folder contains:**
- **WGS_CSBD/** – Collections for CSBDTS models (e.g., TS_01_Covid_Collection, CSBDTS_51–56_Observation_Services_Collection)
- **WGS_KERNAL/** – Collections for NYKTS models (e.g., NYKTS_124–130_Observation_Services_Collection)
- Each collection folder contains regression and smoke JSON files for Postman import
- Professional naming and organization

**`reports` folder contains:**
- `collection_reports/` – Excel timing reports with timestamps and performance analytics
- `list_reports/` – List-based reports and analytics (currently available for future use)
- Professional formatting with headers and color coding
- Model breakdown and status tracking across all processed models

**`source_folder` folder contains:**
- Original source files before processing
- Maintains original file structure for reference

⚠️ **Warning**: The `rm -rf` command will permanently delete all contents. Make sure you want to remove these files before running the commands.