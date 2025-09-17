# Python Files Explanation

This document provides a comprehensive explanation of the main Python files in the Postman Collection Renaming project.

## Table of Contents

1. [main_processor.py](#main_processorpy)
2. [models_config.py](#models_configpy)
3. [dynamic_models.py](#dynamic_modelspy)
4. [postman_generator.py](#postman_generatorpy)

---

## main_processor.py

### Overview
The main processor is the central orchestrator that combines file renaming functionality with Postman collection generation. It serves as the primary entry point for the entire workflow.

### Key Features

#### 1. File Renaming System
- **Multi-format Support**: Handles 3-part, 4-part, and 5-part filename templates
- **Template Conversion**: Converts between different naming conventions:
  - `TC#XX_XXXXX#suffix.json` → `TC#XX_XXXXX#edit_id#code#suffix.json`
  - `TC#XX_XXXXX#edit_id#suffix.json` → `TC#XX_XXXXX#edit_id#code#suffix.json`
  - `TC#XX_XXXXX#edit_id#code#suffix.json` (already converted, just moves)

#### 2. Suffix Mapping
```python
suffix_mapping = {
    "positive": {
        "deny": "LR",    # deny → LR (Limited Response)
    },
    "negative": {
        "bypass": "NR",  # bypass → NR (No Response)
    },
    "Exclusion": {
        "market": "EX",   # market → EX (Exception)
        "date": "EX"      # date → EX (Exception)
    }
}
```

#### 3. Command Line Interface
Supports multiple execution modes:
- **Specific Models**: `--TS07`, `--TS100`, `--TS120`, `--TS13`, `--TS50`, `--TS130`
- **Batch Processing**: `--all` (process all discovered models)
- **Custom Parameters**: `--edit-id`, `--code`, `--source-dir`, `--dest-dir`
- **Utility Functions**: `--list` (show available models), `--no-postman` (skip collection generation)

#### 4. Integration with Postman Generator
- Automatically generates Postman collections after file processing
- Configurable collection names and file names
- Error handling and validation

### Core Functions

#### `rename_files()`
```python
def rename_files(edit_id="rvn001", code="00W5", source_dir=None, dest_dir=None, 
                generate_postman=True, postman_collection_name=None, postman_file_name=None)
```
- **Purpose**: Rename and move files for a specific model
- **Parameters**: Model identifiers, directory paths, Postman generation options
- **Returns**: List of successfully renamed files

#### `process_multiple_models()`
```python
def process_multiple_models(models_config, generate_postman=True)
```
- **Purpose**: Batch process multiple models with their configurations
- **Parameters**: List of model configurations, Postman generation flag
- **Returns**: Tuple of (successful_models, failed_models)

#### `main()`
- **Purpose**: Command-line interface and orchestration
- **Features**: Argument parsing, model discovery, error handling, progress reporting

### Usage Examples

```bash
# Process specific TS model
python main_processor.py --TS07

# Process all discovered models
python main_processor.py --all

# List available models
python main_processor.py --list

# Custom model processing
python main_processor.py --edit-id rvn001 --code 00W5 --source-dir custom/path
```

---

## models_config.py

### Overview
Configuration management system that supports both static model definitions and dynamic model discovery. Provides a unified interface for accessing model configurations.

### Key Features

#### 1. Static Configuration
- **Predefined Models**: Contains static configurations for backward compatibility
- **Model Structure**: Each model includes:
  - `edit_id`: Model identifier (e.g., "rvn001")
  - `code`: EOB code (e.g., "00W5")
  - `source_dir`: Source directory path
  - `dest_dir`: Destination directory path
  - `postman_collection_name`: Collection name
  - `postman_file_name`: Custom filename for Postman collection

#### 2. Dynamic Discovery Integration
```python
def get_models_config(use_dynamic=True):
    if use_dynamic:
        discovered_models = discover_ts_folders()
        if discovered_models:
            return discovered_models
        else:
            return STATIC_MODELS_CONFIG  # Fallback
    else:
        return STATIC_MODELS_CONFIG
```

#### 3. Model Lookup Functions
- **`get_model_by_ts(ts_number)`**: Get specific model by TS number
- **`get_models_config(use_dynamic=True)`**: Get all models with dynamic/static option

### Configuration Structure
```python
{
    "edit_id": "rvn001",
    "code": "00W5", 
    "source_dir": "TS_01_REVENUE_WGS_CSBD_rvn001_00W5_sur/regression",
    "dest_dir": "renaming_jsons/TS_01_REVENUE_WGS_CSBD_rvn001_00W5_dis/regression",
    "postman_collection_name": "TS_1_collection",
    "postman_file_name": "revenue_wgs_csbd_rvn001_00w5.json"
}
```

### Global Settings
- `GENERATE_POSTMAN_COLLECTIONS = True`: Enable/disable Postman generation
- `VERBOSE_OUTPUT = True`: Enable/disable verbose logging

---

## dynamic_models.py

### Overview
Advanced model discovery system that automatically detects TS folders and extracts model parameters. Provides intelligent parsing and normalization of folder names.

### Key Features

#### 1. Flexible TS Number Handling
```python
def normalize_ts_number(ts_number_raw: str) -> str:
    # Handles different digit patterns:
    # "1" → "01"     (single digit)
    # "01" → "01"    (already 2 digits)  
    # "001" → "001"  (already 3 digits)
    # "10" → "10"    (2 digits)
    # "100" → "100"  (3 digits)
```

#### 2. Folder Pattern Recognition
- **Pattern Matching**: Uses regex to extract parameters from folder names
- **Multiple Patterns**: Supports various folder naming conventions:
  - `TS_*_REVENUE_WGS_CSBD_*_payloads_sur`
  - `TS_*_REVENUE_WGS_CSBD_*_ayloads_sur` (typo handling)
  - `TS_*_REVENUE_WGS_CSBD_*_sur`

#### 3. Intelligent Parsing
```python
# Regex pattern for folder name parsing
match = re.match(r'TS_(\d{1,3})_REVENUE_WGS_CSBD_(rvn\d+)_(00W\d+)_sur$', folder_name)
```

### Core Functions

#### `discover_ts_folders(base_dir: str = ".")`
- **Purpose**: Scan directory for TS folders and extract model configurations
- **Returns**: List of discovered model configurations
- **Features**: 
  - Automatic folder detection
  - Parameter extraction
  - Validation and error handling

#### `get_model_by_ts_number(ts_number: str)`
- **Purpose**: Get specific model configuration by TS number
- **Features**: Flexible TS number matching (e.g., "1", "01", "10", "100")

#### `validate_model_config(model: Dict)`
- **Purpose**: Validate model configuration completeness
- **Checks**: Required fields, directory existence, path validity

#### `print_discovered_models(models: List[Dict])`
- **Purpose**: Display formatted list of discovered models
- **Features**: Organized output with statistics

### Model Configuration Generation
```python
model_config = {
    "ts_number": ts_number,           # Normalized TS number
    "ts_number_raw": ts_number_raw,   # Original TS number
    "edit_id": edit_id,               # Extracted edit ID
    "code": code,                     # Extracted EOB code
    "source_dir": regression_path,    # Source directory path
    "dest_dir": dest_dir,             # Generated destination path
    "postman_collection_name": postman_collection_name,
    "postman_file_name": postman_file_name,
    "folder_name": folder_name        # Original folder name
}
```

### Error Handling
- **Missing Directories**: Warns about non-existent regression folders
- **Parse Failures**: Handles unparseable folder names gracefully
- **Validation Errors**: Comprehensive validation with detailed error messages

---

## postman_generator.py

### Overview
Comprehensive Postman collection generator that converts organized JSON files into Postman-compatible API collections. Supports multiple collection formats and provides extensive validation.

### Key Features

#### 1. Multi-Format Support
- **Postman v2.1.0**: Standard Postman collection format
- **Minimal Format**: Simplified collection structure for compatibility
- **Flexible Parsing**: Handles various filename patterns

#### 2. Filename Parsing
```python
def _parse_filename(self, filename: str) -> Optional[Dict[str, str]]:
    # Parses: TC#ID#edit_id#eob_code#suffix.json
    # Returns: {
    #     'tc_prefix': 'TC',
    #     'tc_id': '000001_53626', 
    #     'edit_id': 'rvn002',
    #     'eob_code': '00W06',
    #     'suffix': 'LR/NR/EX'
    # }
```

#### 3. HTTP Method Mapping
```python
method_map = {
    'LR': 'POST',  # Limited Response - POST for validation
    'NR': 'POST',  # No Response - POST for validation  
    'EX': 'POST'   # Exception - POST for validation
}
```

### Core Classes

#### `PostmanCollectionGenerator`
Main class for generating Postman collections.

**Constructor:**
```python
def __init__(self, source_dir: str = "renaming_jsons", output_dir: str = "postman_collections")
```

### Key Methods

#### `generate_postman_collection(collection_name: str, custom_filename: str = None)`
- **Purpose**: Generate Postman collection for all JSON files in source directory
- **Features**:
  - Recursive file discovery
  - Automatic request creation
  - Custom filename support
  - Comprehensive error handling

#### `generate_collection_for_directory(dir_name: str)`
- **Purpose**: Generate collection for specific directory
- **Features**:
  - Directory-specific processing
  - Flexible naming conventions
  - TS number extraction

#### `generate_all_collections()`
- **Purpose**: Generate single collection for all files
- **Features**:
  - Automatic collection name detection
  - Unified processing

### Request Structure
```python
postman_request = {
    "name": request_name,
    "request": {
        "method": "POST",
        "header": [
            {"key": "Content-Type", "value": "application/json"},
            {"key": "X-Edit-ID", "value": edit_id},
            {"key": "X-EOB-Code", "value": eob_code},
            {"key": "X-Test-Type", "value": suffix}
        ],
        "url": {
            "raw": "{{baseUrl}}/api/validate/{{tc_id}}",
            "host": ["{{baseUrl}}"],
            "path": ["api", "validate", "{{tc_id}}"]
        },
        "body": {
            "mode": "raw",
            "raw": json_content,
            "options": {"raw": {"language": "json"}}
        }
    }
}
```

### Utility Functions

#### `list_available_directories()`
- **Purpose**: List all directories in source folder
- **Returns**: Sorted list of directory names

#### `get_directory_stats(dir_name: str)`
- **Purpose**: Get detailed statistics for directory
- **Returns**: Dictionary with file counts, types, edit IDs, etc.

#### `validate_collection(collection_path: Path)`
- **Purpose**: Validate Postman collection file
- **Returns**: Validation results with errors, warnings, and statistics

### Collection Variables
```python
"variable": [
    {
        "key": "baseUrl",
        "value": "http://localhost:3000",
        "type": "string"
    }
]
```

### Error Handling
- **File Reading**: Graceful handling of unreadable JSON files
- **Parse Failures**: Warning messages for unparseable filenames
- **Validation**: Comprehensive collection validation
- **Directory Issues**: Clear error messages for missing directories

### Usage Examples

```bash
# Generate collection for all files
python postman_generator.py --collection-name "MyCollection"

# Generate collection for specific directory
python postman_generator.py --directory "TS_07_REVENUE_WGS_CSBD_rvn011_00W11_dis"

# List available directories
python postman_generator.py --list-directories

# Show directory statistics
python postman_generator.py --stats "TS_07_REVENUE_WGS_CSBD_rvn011_00W11_dis"
```

---

## Integration and Workflow

### Complete Workflow
1. **Discovery**: `dynamic_models.py` discovers TS folders
2. **Configuration**: `models_config.py` provides unified model access
3. **Processing**: `main_processor.py` orchestrates file renaming
4. **Generation**: `postman_generator.py` creates Postman collections

### Data Flow
```
TS Folders → Dynamic Discovery → Model Config → File Processing → Postman Collections
     ↓              ↓                ↓              ↓                    ↓
Folder Names → Parameter Extraction → Configuration → Renamed Files → API Collections
```

### Error Handling Strategy
- **Graceful Degradation**: Fallback to static config if dynamic discovery fails
- **Comprehensive Validation**: Multiple validation layers
- **Detailed Logging**: Verbose output for debugging
- **User-Friendly Messages**: Clear error descriptions and suggestions

### Extensibility
- **Plugin Architecture**: Easy to add new model types
- **Configurable Mappings**: Customizable suffix mappings
- **Flexible Naming**: Support for various naming conventions
- **Modular Design**: Independent components for easy maintenance

This system provides a robust, scalable solution for managing test case files and generating Postman collections for API testing workflows.
