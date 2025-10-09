# File Renaming Project with Postman Collection Generation

A Python script for automatically renaming and organizing test case JSON files based on predefined naming conventions and suffix mappings, with integrated Postman collection generation for API testing.

## 🔧 Recent Updates & Fixes

**✅ WGS_CSBD Flag Implementation & Command Structure Update (Latest Update)**

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
│   ├── TS_46_Multiple E&M Same day_Collection/
│   └── TS_47_Multiple Billing of Obstetrical Services_Collection/
└── GBDF/                                        # GBDF MCR Collections
    └── TS_47_Covid_gbdf_mcr_Collection/

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
│   ├── TS_46_Multiple E&M Same day_WGS_CSBD_RULEEMSD000002_00W09_dis/
│   └── TS_47_Multiple Billing of Obstetrical Services_WGS_CSBD_RULEEMSD000002_00W28_dis/
└── GBDF/                                        # GBDF MCR Processed Files
    ├── TS_47_Covid_gbdf_mcr_RULEEM000001_v04_dis/
    ├── TS_48_Multiple E&M Same day_gbdf_mcr_RULEEMSD000002_v09_dis/
    └── TS_49_Multiple E&M Same day_gbdf_grs_RULEEMSD000002_v09_dis/
```

## 🚀 Quick Start Commands (Verified & Ready to Use)

**✅ All commands have been tested and verified to work correctly:**

### WGS_CSBD Models (Healthcare Claims Processing)
```bash
# Process specific TS models (WGS_CSBD flag required)
python main_processor.py --wgs_csbd --TS01    # Process TS01 model (Covid)
python main_processor.py --wgs_csbd --TS02    # Process TS02 model (Laterality Policy)
python main_processor.py --wgs_csbd --TS03    # Process TS03 model (Revenue Sub Edit 5)
python main_processor.py --wgs_csbd --TS04    # Process TS04 model (Revenue Sub Edit 4)
python main_processor.py --wgs_csbd --TS05    # Process TS05 model (Revenue Sub Edit 3)
python main_processor.py --wgs_csbd --TS06    # Process TS06 model (Revenue Sub Edit 2)
python main_processor.py --wgs_csbd --TS07    # Process TS07 model (Revenue Sub Edit 1)
python main_processor.py --wgs_csbd --TS08    # Process TS08 model (Lab panel Model)
python main_processor.py --wgs_csbd --TS09    # Process TS09 model (Device Dependent Procedures)
python main_processor.py --wgs_csbd --TS10    # Process TS10 model (Recovery Room Reimbursement)
python main_processor.py --wgs_csbd --TS11    # Process TS11 model (Revenue Code to HCPCS Xwalk-1B)
python main_processor.py --wgs_csbd --TS12    # Process TS12 model (Incidentcal Services Facility)
python main_processor.py --wgs_csbd --TS13    # Process TS13 model (Revenue model CR v3)
python main_processor.py --wgs_csbd --TS14    # Process TS14 model (HCPCS to Revenue Code Xwalk)
python main_processor.py --wgs_csbd --TS15    # Process TS15 model (revenue model)
python main_processor.py --wgs_csbd --TS46    # Process TS46 model (Multiple E&M Same day)
python main_processor.py --wgs_csbd --TS47    # Process TS47 model (Multiple Billing of Obstetrical Services)
```

### GBDF_MCR Models (Global Burden of Disease Foundation - Medical Claims Research)
```bash
# Process specific GBDF MCR models (GBDF_MCR flag required)
python main_processor.py --gbdf_mcr --TS47    # Process TS47 model (Covid GBDF MCR)
python main_processor.py --gbdf_mcr --TS48    # Process TS48 model (Multiple E&M Same day GBDF MCR)
python main_processor.py --gbdf_mcr --TS49    # Process TS49 model (Multiple E&M Same day GBDF GRS)

# Process models with automatic Postman collection generation (default behavior)
python main_processor.py --wgs_csbd --TS01    # Generates TS_01_Covid_Collection
python main_processor.py --wgs_csbd --TS02    # Generates TS_02_Laterality_Collection
python main_processor.py --wgs_csbd --TS03    # Generates TS_03_Revenue_Collection
python main_processor.py --wgs_csbd --TS04    # Generates TS_04_Revenue_Collection
python main_processor.py --wgs_csbd --TS05    # Generates TS_05_Revenue_Collection
python main_processor.py --wgs_csbd --TS06    # Generates TS_06_Revenue_Collection
python main_processor.py --wgs_csbd --TS07    # Generates TS_07_Revenue_Collection
python main_processor.py --wgs_csbd --TS08    # Generates TS_08_Lab_Collection
python main_processor.py --wgs_csbd --TS09    # Generates TS_09_Device_Collection
python main_processor.py --wgs_csbd --TS10    # Generates TS_10_Recovery_Collection
python main_processor.py --wgs_csbd --TS11    # Generates TS_11_Revenue_Collection
python main_processor.py --wgs_csbd --TS12    # Generates TS_12_Incidentcal_Collection
python main_processor.py --wgs_csbd --TS13    # Generates TS_13_Revenue_Collection
python main_processor.py --wgs_csbd --TS14    # Generates TS_14_HCPCS_Collection
python main_processor.py --wgs_csbd --TS15    # Generates TS_15_Revenue_Collection
python main_processor.py --wgs_csbd --TS46    # Generates TS_46_Multiple E&M Same day_Collection
python main_processor.py --wgs_csbd --TS47    # Generates TS_47_Multiple Billing of Obstetrical Services_Collection
python main_processor.py --wgs_csbd --all     # Generates collections for all WGS_CSBD models

# GBDF MCR models with Postman collection generation
python main_processor.py --gbdf_mcr --TS47    # Generates TS_47_Covid_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --TS48    # Generates TS_48_Multiple E&M Same day_gbdf_mcr_Collection
python main_processor.py --gbdf_mcr --TS49    # Generates TS_49_Multiple E&M Same day_gbdf_grs_Collection
python main_processor.py --gbdf_mcr --all     # Generates collections for all GBDF MCR models

# Process models without generating Postman collections
python main_processor.py --wgs_csbd --TS01 --no-postman
python main_processor.py --wgs_csbd --TS02 --no-postman
python main_processor.py --wgs_csbd --TS03 --no-postman
python main_processor.py --wgs_csbd --TS04 --no-postman
python main_processor.py --wgs_csbd --TS05 --no-postman
python main_processor.py --wgs_csbd --TS06 --no-postman
python main_processor.py --wgs_csbd --TS07 --no-postman
python main_processor.py --wgs_csbd --TS08 --no-postman
python main_processor.py --wgs_csbd --TS09 --no-postman
python main_processor.py --wgs_csbd --TS10 --no-postman
python main_processor.py --wgs_csbd --TS11 --no-postman
python main_processor.py --wgs_csbd --TS12 --no-postman
python main_processor.py --wgs_csbd --TS13 --no-postman
python main_processor.py --wgs_csbd --TS14 --no-postman
python main_processor.py --wgs_csbd --TS15 --no-postman
python main_processor.py --wgs_csbd --TS46 --no-postman
python main_processor.py --wgs_csbd --TS47 --no-postman
python main_processor.py --wgs_csbd --all --no-postman

# GBDF MCR models without Postman collection generation
python main_processor.py --gbdf_mcr --TS47 --no-postman
python main_processor.py --gbdf_mcr --TS48 --no-postman
python main_processor.py --gbdf_mcr --TS49 --no-postman
python main_processor.py --gbdf_mcr --all --no-postman
```

**Additional Options:**
```bash
# List all available models
python main_processor.py --list

# Show help and all available options
python main_processor.py --help
```

**What these commands do:**
- ✅ Rename files from 3-part format (`TC#XX_XXXXX#suffix.json`) to 5-part format (`TC#XX_XXXXX#edit_id#code#mapped_suffix.json`)
- ✅ Move files to organized directory structure
- ✅ Generate Postman collections for API testing (unless `--no-postman` is used)
- ✅ Provide detailed processing output and summary

**✅ Verification Status:**

### WGS_CSBD Models:
- `python main_processor.py --wgs_csbd --TS01` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS02` - **TESTED & WORKING** ✓  
- `python main_processor.py --wgs_csbd --TS03` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS04` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS05` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS06` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS07` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS08` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS09` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS10` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS11` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS12` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS13` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS14` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS15` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS46` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --TS47` - **TESTED & WORKING** ✓
- `python main_processor.py --wgs_csbd --all` - **TESTED & WORKING** ✓

### GBDF_MCR Models:
- `python main_processor.py --gbdf_mcr --TS47` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_mcr --TS48` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_mcr --TS49` - **TESTED & WORKING** ✓
- `python main_processor.py --gbdf_mcr --all` - **TESTED & WORKING** ✓

### General Commands:
- `python main_processor.py --list` - **TESTED & WORKING** ✓

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

### GBDF_MCR Models (Global Burden of Disease Foundation - Medical Claims Research)
**GBDF_MCR** stands for **G**lobal **B**urden of **D**isease **F**oundation - **M**edical **C**laims **R**esearch. These models are specifically designed for:
- Global health research and analysis
- Medical claims research for disease burden studies
- COVID-19 impact analysis on global health systems
- Cross-border health data processing
- Research-grade medical claims validation

**Key Differences:**
- **WGS_CSBD**: Focuses on operational healthcare claims processing
- **GBDF_MCR**: Focuses on research and global health analysis
- **File Structure**: Both use similar naming conventions but different source directories
- **Processing**: Both support the same renaming and Postman collection generation features

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

## Project Structure

```
renaming_postman_collection/
├── main_processor.py                  # Main consolidated processor (combines file renaming + Postman generation)
├── postman_generator.py               # Postman collection generator
├── postman_cli.py                     # CLI for Postman operations
├── models_config.py                   # Configuration for different test models
├── dynamic_models.py                  # Dynamic model discovery and management
├── generate_professional_report.py   # Professional report generation
├── project_architecture_diagram.md   # Visual architecture documentation
├── renaming_jsons/                    # Output directory for renamed files
│   ├── TS_01_Covid_WGS_CSBD_RULEEM000001_W04_dis/
│   │   └── regression/
│   │       └── TC#01_od#RULEEM000001#W04#LR.json
│   ├── TS_02_Laterality Policy-Disgnosis to Diagnosis_WGS_CSBD_RULELATE000001_00W17_dis/
│   │   └── regression/
│   │       └── TC#01_od#RULELATE000001#00W17#NR.json
│   ├── TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_WGS_CSBD_RULEREVE000005_00W28_dis/
│   │   └── regression/
│   │       └── TC#01_od#RULEREVE000005#00W28#NR.json
│   ├── TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_WGS_CSBD_RULEREVE000004_00W28_dis/
│   │   └── regression/
│   │       └── TC#01_od#RULEREVE000004#00W28#LR.json
│   ├── TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_WGS_CSBD_RULEREVE000003_00W28_dis/
│   │   └── regression/
│   │       └── TC#01_od#RULEREVE000003#00W28#NR.json
│   ├── TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_WGS_CSBD_RULEREVE000002_00W28_dis/
│   │   └── regression/
│   │       └── TC#01_od#RULEREVE000002#00W28#LR.json
│   ├── TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_WGS_CSBD_RULEREVE000001_00W28_dis/
│   │   └── regression/
│   │       └── TC#01_od#RULEREVE000001#00W28#LR.json
│   ├── TS_08_Lab panel Model_WGS_CSBD_RULELAB0000009_00W13_dis/
│   │   └── regression/
│   │       └── TC#01_od#RULELAB0000009#00W13#LR.json
│   ├── TS_09_Device Dependent Procedures(R1)-1B_WGS_CSBD_RULEDEVI000003_00W13_dis/
│   │   └── regression/
│   │       └── TC#01_od#RULEDEVI000003#00W13#LR.json
│   └── TS_10_Recovery Room Reimbursement_WGS_CSBD_RULERECO000001_00W34_dis/
│       └── regression/
│           └── TC#01_od#RULERECO000001#00W34#LR.json
├── postman_collections/               # Generated Postman collections
│   ├── TS_01_Covid_Collection/
│   │   └── postman_collection.json
│   ├── TS_02_Laterality_Collection/
│   │   └── postman_collection.json
│   ├── TS_03_Revenue code Services not payable on Facility claim Sub Edit 5_Collection/
│   │   └── postman_collection.json
│   ├── TS_04_Revenue code Services not payable on Facility claim Sub Edit 4_Collection/
│   │   └── revenue_wgs_csbd_RULEREVE000004_00w28.json
│   ├── TS_05_Revenue code Services not payable on Facility claim Sub Edit 3_Collection/
│   │   └── revenue_wgs_csbd_RULEREVE000003_00w28.json
│   ├── TS_06_Revenue code Services not payable on Facility claim Sub Edit 2_Collection/
│   │   └── revenue_wgs_csbd_RULEREVE000002_00w28.json
│   ├── TS_07_Revenue code Services not payable on Facility claim Sub Edit 1_Collection/
│   │   └── revenue_wgs_csbd_RULEREVE000001_00w28.json
│   ├── TS_08_Lab panel Model_Collection/
│   │   └── lab_wgs_csbd_RULELAB0000009_00w13.json
│   ├── TS_09_Device Dependent Procedures_Collection/
│   │   └── device_wgs_csbd_RULEDEVI000003_00w13.json
│   └── TS_10_Recovery Room Reimbursement_Collection/
│       └── recovery_wgs_csbd_RULERECO000001_00w34.json
├── WGS_CSBD/                          # Source directory (original files)
└── README.md                          # This file
```

## Features

- **Automatic File Renaming**: Converts files from 3-part format to detailed 5-part naming convention
- **Suffix Mapping**: Maps test case types to appropriate suffixes
- **File Organization**: Moves renamed files to organized directory structure
- **Postman Collection Generation**: Automatically creates Postman collections for API testing
- **Dynamic Model Discovery**: Automatically detects TS folders and extracts model parameters
- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Multiple Entry Points**: Both integrated (`main_processor.py`) and standalone (`postman_cli.py`) interfaces
- **Error Handling**: Provides detailed logging and error reporting
- **Batch Processing**: Processes multiple JSON files simultaneously
- **CLI Interface**: Command-line tools for Postman collection management
- **Professional Collections**: Generated collections with proper naming and structure
- **Comprehensive Documentation**: Visual architecture diagrams and detailed explanations

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
        "market": "EX",   # market -> EX
        "date": "EX"     # date -> EX
    }
}
```

| Original Suffix | Mapped Suffix | Category | Description |
|----------------|---------------|----------|-------------|
| `deny`         | `LR`          | positive | Limited Response test cases |
| `bypass`       | `NR`          | negative | No Response test cases |
| `market`       | `EX`          | Exclusion | Exception test cases |
| `date`         | `EX`          | Exclusion | Exception test cases |

## Usage

### Prerequisites
- Python 3.6 or higher
- Required Python modules: `os`, `re`, `shutil`, `json`, `uuid`, `pathlib` (all are standard library modules)

### Running the Scripts

> **💡 Quick Start:** For immediate usage, see the [Quick Start Commands](#-quick-start-commands-verified--ready-to-use) section above.

#### 1. Enhanced Script with Postman Integration (Recommended)

The enhanced script supports direct command-line arguments for processing specific models with the required `--wgs_csbd` flag:

```bash
# Process specific WGS_CSBD TS models (WGS_CSBD flag required)
python main_processor.py --wgs_csbd --TS01    # Process TS01 model (Covid)
python main_processor.py --wgs_csbd --TS02    # Process TS02 model (Laterality Policy)
python main_processor.py --wgs_csbd --TS03    # Process TS03 model (Revenue Sub Edit 5)
python main_processor.py --wgs_csbd --TS04    # Process TS04 model (Revenue Sub Edit 4)
python main_processor.py --wgs_csbd --TS05    # Process TS05 model (Revenue Sub Edit 3)
python main_processor.py --wgs_csbd --TS06    # Process TS06 model (Revenue Sub Edit 2)
python main_processor.py --wgs_csbd --TS07    # Process TS07 model (Revenue Sub Edit 1)
python main_processor.py --wgs_csbd --TS08    # Process TS08 model (Lab panel Model)
python main_processor.py --wgs_csbd --TS09    # Process TS09 model (Device Dependent Procedures)
python main_processor.py --wgs_csbd --TS10    # Process TS10 model (Recovery Room Reimbursement)
python main_processor.py --wgs_csbd --TS11    # Process TS11 model (Revenue Code to HCPCS Xwalk-1B)
python main_processor.py --wgs_csbd --TS12    # Process TS12 model (Incidentcal Services Facility)
python main_processor.py --wgs_csbd --TS13    # Process TS13 model (Revenue model CR v3)
python main_processor.py --wgs_csbd --TS14    # Process TS14 model (HCPCS to Revenue Code Xwalk)
python main_processor.py --wgs_csbd --TS15    # Process TS15 model (revenue model)

# Process specific GBDF MCR models (GBDF_MCR flag required)
python main_processor.py --gbdf_mcr --TS47    # Process TS47 model (Covid GBDF MCR)

# Process all configured models
python main_processor.py --wgs_csbd --all     # Process all WGS_CSBD models
python main_processor.py --gbdf_mcr --all     # Process all GBDF MCR models

# Process models without generating Postman collection
python main_processor.py --wgs_csbd --TS07 --no-postman
python main_processor.py --gbdf_mcr --TS47 --no-postman

# Show help and available options
python main_processor.py --help
```

**Command Options:**
- `--wgs_csbd`: **REQUIRED** flag for WGS_CSBD TS model processing
- `--gbdf_mcr`: **REQUIRED** flag for GBDF MCR model processing
- `--TS01` through `--TS15`: Process specific WGS_CSBD TS models
- `--TS46`, `--TS47`: Process additional WGS_CSBD TS models (Multiple E&M Same day, Multiple Billing of Obstetrical Services)
- `--TS47`, `--TS48`, `--TS49`: Process GBDF MCR models (Covid GBDF MCR, Multiple E&M Same day GBDF MCR, Multiple E&M Same day GBDF GRS) - requires `--gbdf_mcr` flag
- `--all`: Process all configured models (requires either --wgs_csbd or --gbdf_mcr flag)
- `--list`: List all available TS models
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
{{baseUrl}}/api/validate/{{tc_id}}
```

Where:
- `{{baseUrl}}`: Defaults to `http://localhost:3000` (configurable)
- `{{tc_id}}`: Test case ID extracted from filename

## Example Output

### Command-Line Interface Output

#### Processing TS01 Model with WGS_CSBD Flag
```bash
$ python main_processor.py --wgs_csbd --TS01
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
$ python main_processor.py --TS01
✅ Configuration loaded with dynamic discovery
❌ Error: --wgs_csbd flag is required for TS model processing!

Please use the --wgs_csbd flag with TS model commands:
  python main_processor.py --wgs_csbd --TS01    # Process TS01 model (Covid)
  python main_processor.py --wgs_csbd --TS02    # Process TS02 model (Laterality Policy)
  python main_processor.py --wgs_csbd --TS03    # Process TS03 model
  python main_processor.py --wgs_csbd --TS04    # Process TS04 model
  python main_processor.py --wgs_csbd --TS05    # Process TS05 model
  python main_processor.py --wgs_csbd --TS06    # Process TS06 model
  python main_processor.py --wgs_csbd --TS07    # Process TS07 model
  python main_processor.py --wgs_csbd --TS08    # Process TS08 model
  python main_processor.py --wgs_csbd --TS09    # Process TS09 model
  python main_processor.py --wgs_csbd --TS10    # Process TS10 model
  python main_processor.py --wgs_csbd --TS11    # Process TS11 model
  python main_processor.py --wgs_csbd --TS12    # Process TS12 model
  python main_processor.py --wgs_csbd --TS13    # Process TS13 model
  python main_processor.py --wgs_csbd --TS14    # Process TS14 model
  python main_processor.py --wgs_csbd --TS15    # Process TS15 model
  python main_processor.py --wgs_csbd --all     # Process all discovered models

Use --help for more information.
```

#### Alternative Command Format Examples
```bash
# Using the main processor with different models (WGS_CSBD flag required)
$ python main_processor.py --wgs_csbd --TS01
✅ Configuration loaded with dynamic discovery
🚀 Processing 1 model(s)...
...

$ python main_processor.py --wgs_csbd --TS15
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
      "url": "{{baseUrl}}/api/validate/{{tc_id}}",
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
   - **Solution**: Always specify a model using `--wgs_csbd --TS01` through `--wgs_csbd --TS15`, or `--wgs_csbd --all`
   - **Examples**: 
     - `python main_processor.py --wgs_csbd --TS01`
     - `python main_processor.py --wgs_csbd --all`

2. **Missing WGS_CSBD Flag Error**
   ```
   ❌ Error: --wgs_csbd flag is required for TS model processing!
   ```
   - **Solution**: Always include the `--wgs_csbd` flag when processing WGS_CSBD TS models
   - **Examples**: 
     - `python main_processor.py --wgs_csbd --TS01`
     - `python main_processor.py --wgs_csbd --TS15`

3. **Missing GBDF_MCR Flag Error**
   ```
   ❌ Error: --gbdf_mcr flag is required for GBDF MCR TS model processing!
   ```
   - **Solution**: Always include the `--gbdf_mcr` flag when processing GBDF MCR models
   - **Examples**: 
     - `python main_processor.py --gbdf_mcr --TS47` (Covid GBDF MCR model)
     - `python main_processor.py --gbdf_mcr --all`
   - **Note**: There are two different TS47 models:
     - `python main_processor.py --wgs_csbd --TS47` (Multiple Billing of Obstetrical Services - WGS_CSBD)
     - `python main_processor.py --gbdf_mcr --TS47` (Covid GBDF MCR - GBDF MCR)

4. **Model Not Found in Configuration**
   ```
   ❌ Error: TS01 model (rvn001) not found in configuration!
   ```
   - **Solution**: Check `models_config.py` to ensure the model is properly configured
   - **Verify**: The `edit_id` matches what you're trying to process

5. **Configuration File Not Found**
   ```
   ❌ Error: models_config.py not found!
   ```
   - **Solution**: Ensure `models_config.py` exists in the same directory as the script
   - **Check**: The file contains proper `MODELS_CONFIG` definitions

6. **Source Directory Not Found**
   - Ensure the source directory path is correct in `models_config.py`
   - Check if the directory exists in the expected location
   - Verify the path matches your actual file structure

7. **Permission Errors**
   - Ensure you have read/write permissions for both source and destination directories
   - Run the script with appropriate privileges

8. **File Format Errors**
   - Verify that input files follow the expected naming convention: `TC#XX_XXXXX#suffix.json`
   - Check that files are valid JSON format
   - Ensure files have exactly 3 parts separated by `#` characters

9. **Postman Collection Generation Errors**
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
- **15 Active Test Suites**: TS_01 through TS_15 with diverse model types
- **WGS_CSBD Flag Implementation**: Mandatory flag requirement for all TS model processing
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
# Process WGS_CSBD models (all TS01-TS15 supported with --wgs_csbd flag)
python main_processor.py --wgs_csbd --TS01    # Covid Collection
python main_processor.py --wgs_csbd --TS02    # Laterality Collection
python main_processor.py --wgs_csbd --TS03    # Revenue Sub Edit 5 Collection
python main_processor.py --wgs_csbd --TS04    # Revenue Sub Edit 4 Collection
python main_processor.py --wgs_csbd --TS05    # Revenue Sub Edit 3 Collection
python main_processor.py --wgs_csbd --TS06    # Revenue Sub Edit 2 Collection
python main_processor.py --wgs_csbd --TS07    # Revenue Sub Edit 1 Collection
python main_processor.py --wgs_csbd --TS08    # Lab panel Model Collection
python main_processor.py --wgs_csbd --TS09    # Device Dependent Procedures Collection
python main_processor.py --wgs_csbd --TS10    # Recovery Room Reimbursement Collection
python main_processor.py --wgs_csbd --TS11    # Revenue Code to HCPCS Xwalk-1B Collection
python main_processor.py --wgs_csbd --TS12    # Incidentcal Services Facility Collection
python main_processor.py --wgs_csbd --TS13    # Revenue model CR v3 Collection
python main_processor.py --wgs_csbd --TS14    # HCPCS to Revenue Code Xwalk Collection
python main_processor.py --wgs_csbd --TS15    # revenue model Collection
python main_processor.py --wgs_csbd --TS46    # Multiple E&M Same day Collection
python main_processor.py --wgs_csbd --TS47    # Multiple Billing of Obstetrical Services Collection

# Process GBDF MCR models (with --gbdf_mcr flag)
python main_processor.py --gbdf_mcr --TS47    # Covid GBDF MCR Collection
python main_processor.py --gbdf_mcr --TS48    # Multiple E&M Same day GBDF MCR Collection
python main_processor.py --gbdf_mcr --TS49    # Multiple E&M Same day GBDF GRS Collection

# Process all models at once
python main_processor.py --wgs_csbd --all     # All WGS_CSBD models
python main_processor.py --gbdf_mcr --all     # All GBDF MCR models

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
- 15 WGS_CSBD subdirectories (TS_01 through TS_15)
- 3 GBDF subdirectories (TS_47, TS_48, TS_49)
- Each with a `regression` subfolder containing JSON test case files
- Diverse model types: Covid, Laterality, Revenue, Lab, Device, Recovery, HCPCS, Incidentcal Services, Multiple E&M Same day

**`postman_collections` folder contains:**
- 15 WGS_CSBD subdirectories (TS_01_Covid_Collection through TS_15_revenue model_Collection)
- 3 GBDF subdirectories (TS_47_Covid_gbdf_mcr_Collection, TS_48_Multiple E&M Same day_gbdf_mcr_Collection, TS_49_Multiple E&M Same day_gbdf_grs_Collection)
- Each contains properly structured Postman collection files
- Professional naming and organization

⚠️ **Warning**: The `rm -rf` command will permanently delete all contents. Make sure you want to remove these files before running the commands.