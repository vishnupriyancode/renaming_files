# File Renaming Project

A Python script for automatically renaming and organizing test case JSON files based on predefined naming conventions and suffix mappings.

## Overview

This project automatically processes test case JSON files from a source directory, renames them according to a specific naming template, and moves them to a destination directory. It's designed for organizing test automation payloads with consistent naming patterns.

## Project Structure

```
renaming_files/
├── rename_files.py                    # Main Python script
├── renaming_jsons/                    # Output directory for renamed files
│   └── TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads/
│       └── smoke/                     # Processed test cases
├── TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads/
│   └── smoke/                         # Source directory (original files)
└── README.md                          # This file
```

## Features

- **Automatic File Renaming**: Converts files from 2-part format to detailed 5-part naming convention
- **Suffix Mapping**: Maps test case types to appropriate suffixes
- **File Organization**: Moves renamed files to organized directory structure
- **Error Handling**: Provides detailed logging and error reporting
- **Batch Processing**: Processes multiple JSON files simultaneously

## Naming Convention

### Input Format
Files must follow this pattern:

```
TC_XX#suffix.json
```

**Examples:**
- `TC_01#Eligiable.json`
- `TC_02#bypass.json`
- `TC_05#market.json`
- `TC_08#bypass.json`

### Output Format
Files are renamed to follow this template:
```
TC_XX#suffix#edit_id#code#mapped_suffix.json
```

**Examples:**
- `TC_01#Eligiable#rvn001#00W5#posi.json`
- `TC_02#bypass#rvn001#00W5#nega.json`
- `TC_05#market#rvn001#00W5#ex.json`

## Parameters

### Hardcoded Parameters
The script uses the following hardcoded parameters:

- **`edit_id`**: `"rvn001"` - Unique identifier for the edit/revision
- **`code`**: `"00W5"` - Code identifier for the test suite
- **`source_dir`**: `"TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads/smoke"` - Source directory path
- **`dest_dir`**: Absolute path to the destination directory

### Suffix Mapping
The script automatically maps test case types to appropriate suffixes:

| Original Suffix | Mapped Suffix | Description |
|----------------|---------------|-------------|
| `Eligiable`   | `posi`        | Positive test cases |
| `bypass`      | `nega`        | Negative test cases |
| `market`      | `ex`          | Exception test cases |
| `dos`         | `ex`          | Exception test cases |

**Note**: The script automatically determines the appropriate suffix based on the test case type. For example, `bypass` files automatically get the `nega` suffix in the new 5-part template.

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
Current (3-part): TC_01#Eligiable#posi.json
New:     TC_01#Eligiable#rvn001#00W5#posi.json
Moving to: C:\Users\Vishnu\Cursor_AI_proj\GIT_HUB\renaming_files\renaming_jsons\TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads\smoke
----------------------------------------
✓ Successfully copied and renamed: TC_01#Eligiable#posi.json → TC_01#Eligiable#rvn001#00W5#posi.json
✓ Removed original file: TC_01#Eligiable#posi.json

Current (2-part): TC_08#bypass.json
Converting to 3-part template...
New:     TC_08#bypass#rvn001#00W5#nega.json
Moving to: C:\Users\Vishnu\Cursor_AI_proj\GIT_HUB\renaming_files\renaming_jsons\TS_01_REVENUE_WGS_CSBD_rvn001_00W5_payloads\smoke
----------------------------------------
✓ Successfully copied and renamed: TC_08#bypass.json → TC_08#bypass#rvn001#00W5#nega.json
✓ Removed original file: TC_08#bypass.json
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
    "Eligiable": "posi",
    "bypass": "nega",
    "market": "ex",
    "dos": "ex",
    "new_type": "new_suffix"  # Add new mappings here
}
```

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
   - Verify that input files follow the expected naming convention
   - Check that files are valid JSON format

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
