# File Renaming Project with Postman Collection Generation

A Python script for automatically renaming and organizing test case JSON files based on predefined naming conventions and suffix mappings, with integrated Postman collection generation for API testing.

## 🚀 Quick Start Commands (Verified & Ready to Use)

**✅ All commands have been tested and verified to work correctly:**

```bash
# Process TS01 model (rvn001, 00W5)
python rename_files.py --TS01

# Process TS02 model (rvn002, 00W6)  
python rename_files.py --TS02

# Process all configured models
python rename_files.py --all
```

**Additional Options:**
```bash
# Skip Postman collection generation
python rename_files.py --TS01 --no-postman

# Show help and all available options
python rename_files.py --help
```

**What these commands do:**
- ✅ Rename files from 3-part format (`TC#XX_XXXXX#suffix.json`) to 5-part format (`TC#XX_XXXXX#edit_id#code#mapped_suffix.json`)
- ✅ Move files to organized directory structure
- ✅ Generate Postman collections for API testing (unless `--no-postman` is used)
- ✅ Provide detailed processing output and summary

**✅ Verification Status:**
- `python rename_files.py --TS01` - **TESTED & WORKING** ✓
- `python rename_files.py --TS02` - **TESTED & WORKING** ✓  
- `python rename_files.py --all` - **TESTED & WORKING** ✓

All commands successfully process files and generate expected output with proper error handling.

## Overview

This project automatically processes test case JSON files from a source directory, renames them according to a specific naming template, moves them to a destination directory, and generates Postman collections for API testing. It's designed for organizing test automation payloads with consistent naming patterns and ready-to-use API test collections.

## Project Structure

```
renaming_postman_collection/
├── rename_files.py                    # Original Python script
├── rename_files_with_postman.py       # Enhanced script with Postman integration
├── postman_generator.py               # Postman collection generator
├── postman_cli.py                     # CLI for Postman operations
├── renaming_jsons/                    # Output directory for renamed files
│   └── TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis/
│       └── regression/                     # Processed test cases
├── postman_collections/               # Generated Postman collections
│   └── revenue_test_collection/
│       └── postman_collection.json    # Ready-to-import Postman collection
├── TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/
│   └── regression/                         # Source directory (original files)
└── README.md                          # This file
```

## Features

- **Automatic File Renaming**: Converts files from 3-part format to detailed 5-part naming convention
- **Suffix Mapping**: Maps test case types to appropriate suffixes
- **File Organization**: Moves renamed files to organized directory structure
- **Postman Collection Generation**: Automatically creates Postman collections for API testing
- **Error Handling**: Provides detailed logging and error reporting
- **Batch Processing**: Processes multiple JSON files simultaneously
- **CLI Interface**: Command-line tools for Postman collection management

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
- **`source_dir`**: `"TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/regression"` - Source directory path
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

The enhanced script now supports command-line arguments for processing specific models:

```bash
# Process TS01 model (rvn001, 00W5)
python rename_files_with_postman.py --TS01

# Process TS02 model (rvn002, 00W6)
python rename_files_with_postman.py --TS02

# Process all configured models
python rename_files_with_postman.py --all

# Process TS01 without generating Postman collection
python rename_files_with_postman.py --TS01 --no-postman

# Show help and available options
python rename_files_with_postman.py --help
```

**Alternative Command Format:**
You can also use the shorter command format:

```bash
# Process TS01 model (rvn001, 00W5)
python rename_files.py --TS01

# Process TS02 model (rvn002, 00W6)
python rename_files.py --TS02

# Process all configured models
python rename_files.py --all
```

**Note:** Both command formats work identically. Choose the one that's more convenient for your workflow.

**Command Options:**
- `--TS01`: Process TS01 model (rvn001, 00W5)
- `--TS02`: Process TS02 model (rvn002, 00W6)
- `--all`: Process all configured models
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
        "source_dir": "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/regression",
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
# Run the original script for file renaming only
python rename_files.py
```

#### 3. Postman Collection Management

```bash
# Generate Postman collection for all files
python postman_cli.py generate --collection-name "MyTestCollection"

# Generate collection for specific directory
python postman_cli.py generate --directory "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"

# List available directories
python postman_cli.py list-directories

# Show statistics for a directory
python postman_cli.py stats --directory "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"

# Generate collections for all directories
python postman_cli.py generate-all

# Validate a collection
python postman_cli.py validate --collection-path "postman_collections/test_collection/postman_collection.json"
```

#### 4. Standalone Postman Generator

```bash
# Generate collection with custom parameters
python postman_generator.py --source-dir "renaming_jsons" --output-dir "postman_collections" --collection-name "CustomCollection"

# Generate collection for specific directory
python postman_generator.py --directory "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"

# List available directories
python postman_generator.py --list-directories

# Show statistics
python postman_generator.py --stats "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis"
```

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

#### Processing TS02 Model
```bash
$ python rename_files_with_postman.py --TS02
✅ Configuration loaded from models_config.py

🚀 Processing 1 model(s)...
============================================================

📋 Processing Model 1/1: rvn002_00W6
----------------------------------------
Files to be renamed and moved:
============================================================
Current: TC#01_5#deny.json
Converting to new template...
New:     TC#01_5#rvn002#00W6#LR.json
Moving to: renaming_jsons/TS_02_REVENUE_WGS_CSBD_rvn002_00W6_payloads_dis/regression
----------------------------------------
✓ Successfully copied and renamed: TC#01_5#deny.json → TC#01_5#rvn002#00W6#LR.json
✓ Removed original file: TC#01_5#deny.json

============================================================
Renaming and moving completed!
Files moved to: renaming_jsons/TS_02_REVENUE_WGS_CSBD_rvn002_00W6_payloads_dis/regression

============================================================
Generating Postman collection...
----------------------------------------
Found 2 JSON files for collection 'TS_02_REVENUE_WGS_CSBD_rvn002_00W6'
✅ Generated Postman collection: postman_collections\ts_02_revenue_wgs_csbd_rvn002_00w6_collection\postman_collection.json
   - Collection: TS_02_REVENUE_WGS_CSBD_rvn002_00W6
   - Requests: 2
   - Files processed: 2

🎯 Ready for API testing!
============================================================
To use this collection:
1. Open Postman
2. Click 'Import'
3. Select the file: postman_collections\ts_02_revenue_wgs_csbd_rvn002_00w6_collection\postman_collection.json
4. Start testing your APIs!

✅ Model rvn002_00W6: Successfully processed 1 files

============================================================
📊 PROCESSING SUMMARY
============================================================
Models processed: 1
Successful models: 1
Total files processed: 1

✅ SUCCESSFUL MODELS:
   • rvn002_00W6: 1 files

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
$ python rename_files_with_postman.py
✅ Configuration loaded from models_config.py
❌ Error: No model specified!

Please specify which model to process:
  --TS01    Process TS01 model (rvn001, 00W5)
  --TS02    Process TS02 model (rvn002, 00W6)
  --all     Process all configured models

Use --help for more information.
```

#### Alternative Command Format Examples
```bash
# Using the shorter command format
$ python rename_files.py --TS01
✅ Configuration loaded from models_config.py
🚀 Processing 1 model(s)...
...

$ python rename_files.py --TS02
✅ Configuration loaded from models_config.py
🚀 Processing 1 model(s)...
...

$ python rename_files.py --all
✅ Configuration loaded from models_config.py
🚀 Processing 2 model(s)...
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

### Generated Postman Collection Format
```json
{
  "info": {
    "name": "RevenueTestCollection API Collection",
    "description": "API collection for RevenueTestCollection test cases",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "TC#01_12345#rvn001#00W5#LR",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json",
            "type": "text"
          },
          {
            "key": "X-Edit-ID",
            "value": "rvn001",
            "type": "text"
          },
          {
            "key": "X-EOB-Code",
            "value": "00W5",
            "type": "text"
          },
          {
            "key": "X-Test-Type",
            "value": "LR",
            "type": "text"
          }
        ],
        "url": {
          "raw": "{{baseUrl}}/api/validate/{{tc_id}}",
          "host": ["{{baseUrl}}"],
          "path": ["api", "validate", "{{tc_id}}"]
        },
        "body": {
          "mode": "raw",
          "raw": "{\n  \"testCaseId\": \"TC_001\",\n  ...\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        }
      }
    }
  ],
  "variable": [
    {
      "key": "baseUrl",
      "value": "http://localhost:3000",
      "type": "string"
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
source_dir = "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads/regression"

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
   - **Solution**: Always specify a model using `--TS01`, `--TS02`, or `--all`
   - **Examples**: 
     - `python rename_files_with_postman.py --TS01`
     - `python rename_files.py --TS01`

2. **Model Not Found in Configuration**
   ```
   ❌ Error: TS01 model (rvn001) not found in configuration!
   ```
   - **Solution**: Check `models_config.py` to ensure the model is properly configured
   - **Verify**: The `edit_id` matches what you're trying to process

3. **Configuration File Not Found**
   ```
   ❌ Error: models_config.py not found!
   ```
   - **Solution**: Ensure `models_config.py` exists in the same directory as the script
   - **Check**: The file contains proper `MODELS_CONFIG` definitions

4. **Source Directory Not Found**
   - Ensure the source directory path is correct in `models_config.py`
   - Check if the directory exists in the expected location
   - Verify the path matches your actual file structure

5. **Permission Errors**
   - Ensure you have read/write permissions for both source and destination directories
   - Run the script with appropriate privileges

6. **File Format Errors**
   - Verify that input files follow the expected naming convention: `TC#XX_XXXXX#suffix.json`
   - Check that files are valid JSON format
   - Ensure files have exactly 3 parts separated by `#` characters

7. **Postman Collection Generation Errors**
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

**Note**: This script modifies file locations and names. Always backup your data before running it on production files.