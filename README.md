# File Renaming Project

A Python script for automatically renaming and organizing test case JSON files based on predefined naming conventions and suffix mappings.

## Overview

This project automatically processes test case JSON files from a source directory, renames them according to a specific naming template, and moves them to a destination directory. It's designed for organizing test automation payloads with consistent naming patterns.

## Project Structure

```
renaming_files/
├── rename_files.py                    # Main Python script
├── renaming_jsons/                    # Output directory for renamed files
│   └── TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis/
│       └── smoke/                     # Processed test cases
├── TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/
│   └── smoke/                         # Source directory (original files)
└── README.md                          # This file
```

## Features

- **Automatic File Renaming**: Converts files from 3-part format to detailed 5-part naming convention
- **Suffix Mapping**: Maps test case types to appropriate suffixes
- **File Organization**: Moves renamed files to organized directory structure
- **Error Handling**: Provides detailed logging and error reporting
- **Batch Processing**: Processes multiple JSON files simultaneously

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
- **`source_dir`**: `"TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_sur/smoke"` - Source directory path
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
- Required Python modules: `os`, `re`, `shutil` (all are standard library modules)

### Running the Script

1. **Navigate to the project directory:**
   ```bash
   cd /path/to/renaming_files
   ```

2. **Execute the Python script:**
   ```bash
   python rename_files.py
   ```

3. **For Windows users:**
   ```bash
   python rename_files.py
   # or
   py rename_files.py
   ```

### What the Script Does

1. **Source Validation**: Checks if the source directory exists
2. **Directory Creation**: Creates the destination directory if it doesn't exist
3. **File Discovery**: Finds all JSON files in the source directory
4. **Parsing**: Extracts components from each filename
5. **Mapping**: Applies suffix mapping rules to determine correct suffix
6. **Renaming**: Generates new filenames according to the 5-part template
7. **File Operations**: Copies files to destination with new names and removes originals
8. **Logging**: Provides detailed output of all operations

## Example Output

```
Files to be renamed and moved:
============================================================
Current: TC#01_12345#deny.json
Converting to new template...
New:     TC#01_12345#rvn001#00W5#LR.json
Moving to: C:\Users\Vishnu\Cursor_AI_proj\GIT_HUB\renaming_files\renaming_jsons\TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis\smoke
----------------------------------------
✓ Successfully copied and renamed: TC#01_12345#deny.json → TC#01_12345#rvn001#00W5#LR.json
✓ Removed original file: TC#01_12345#deny.json

Current: TC#02_67890#bypass.json
Converting to new template...
New:     TC#02_67890#rvn001#00W5#NR.json
Moving to: C:\Users\Vishnu\Cursor_AI_proj\GIT_HUB\renaming_files\renaming_jsons\TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis\smoke
----------------------------------------
✓ Successfully copied and renamed: TC#02_67890#bypass.json → TC#02_67890#rvn001#00W5#NR.json
✓ Removed original file: TC#02_67890#bypass.json

Current: TC#05_11111#market.json
Converting to new template...
New:     TC#05_11111#rvn001#00W5#EX.json
Moving to: C:\Users\Vishnu\Cursor_AI_proj\GIT_HUB\renaming_files\renaming_jsons\TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis\smoke
----------------------------------------
✓ Successfully copied and renamed: TC#05_11111#market.json → TC#05_11111#rvn001#00W5#EX.json
✓ Removed original file: TC#05_11111#market.json

Current: TC#03_99999#date.json
Converting to new template...
New:     TC#03_99999#rvn001#00W5#EX.json
Moving to: C:\Users\Vishnu\Cursor_AI_proj\GIT_HUB\renaming_files\renaming_jsons\TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads_dis\smoke
----------------------------------------
✓ Successfully copied and renamed: TC#03_99999#date.json → TC#03_99999#rvn001#00W5#EX.json
✓ Removed original file: TC#03_99999#date.json
...
============================================================
Renaming and moving completed!
Files moved to: [destination_path]
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
  "testType": "Smoke",
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
To change the hardcoded parameters, edit the following variables in `rename_files.py`:

```python
# Parameters extracted from folder name
edit_id = "rvn001"        # Change this to your edit ID
code = "00W5"             # Change this to your code

# Source directory containing the files
source_dir = "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads/smoke"

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

## Error Handling

The script includes comprehensive error handling:

- **Directory Validation**: Checks if source directory exists
- **File Format Validation**: Warns about files that don't match expected format
- **File Operation Safety**: Uses try-catch blocks for file operations
- **Detailed Logging**: Provides clear feedback for all operations

## Troubleshooting

### Common Issues

1. **Source Directory Not Found**
   - Ensure the source directory path is correct
   - Check if the directory exists in the expected location

2. **Permission Errors**
   - Ensure you have read/write permissions for both source and destination directories
   - Run the script with appropriate privileges

3. **File Format Errors**
   - Verify that input files follow the expected naming convention: `TC#XX_XXXXX#suffix.json`
   - Check that files are valid JSON format
   - Ensure files have exactly 3 parts separated by `#` characters

### Debug Mode
To add more detailed logging, you can modify the script to include debug information:

```python
# Add debug logging
print(f"Processing file: {filename}")
print(f"Parts: {parts}")
print(f"Mapped suffix: {mapped_suffix}")
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

---

**Note**: This script modifies file locations and names. Always backup your data before running it on production files.
