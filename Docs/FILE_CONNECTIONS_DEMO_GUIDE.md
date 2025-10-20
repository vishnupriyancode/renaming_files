# 🏗️ **File Architecture & Connections - Complete Demo Guide**

## **📋 Overview**
This project consists of 5 interconnected Python files that work together to create an automated file processing and API testing system. This guide explains how they connect and work together for your demo presentation.

---

## **🔗 File Connection Architecture**

```
┌─────────────────────────────────────────────────────────────────┐
│                    🎯 MAIN ENTRY POINT                          │
│                    main_processor.py                            │
│              (Orchestrates the entire workflow)                 │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   File Renaming │  │ Model Processing│  │   CLI Interface │ │
│  │   & Moving      │  │   (Single/Batch)│  │   (User Input)  │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🔍 MODEL DISCOVERY                           │
│                    dynamic_models.py                            │
│              (Auto-discovers TS folders & models)               │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ Pattern Matching│  │ Model Extraction│  │   Normalization │ │
│  │   (Regex)       │  │ (Edit ID, Code) │  │ (TS Numbers)    │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ⚙️ CONFIGURATION MANAGER                     │
│                    models_config.py                             │
│              (Manages model configurations)                     │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  Static Config  │  │ Dynamic Loading │  │  Fallback System│ │
│  │ (Hardcoded)     │  │ (Auto-Discovery)│  │ (Error Handling)│ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                    📁 FILE PROCESSING                           │
│                    main_processor.py (continued)                │
│              (Renames files & applies transformations)          │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  File Renaming  │  │   Transformations│  │   File Moving   │ │
│  │ (New Format)    │  │ (Headers/Footers)│  │ (Source→Dest)   │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🚀 POSTMAN GENERATION                        │
│                    postman_generator.py                         │
│              (Creates API test collections)                     │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ Collection Gen  │  │  Request Creation│  │   Validation    │ │
│  │ (v2.1.0 Format) │  │ (JSON→API Calls)│  │ (Format Check)  │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🎛️ CLI INTERFACE                             │
│                    postman_cli.py                               │
│              (Command-line interface for Postman)               │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   Generate      │  │   List/Stats    │  │   Validate      │ │
│  │  Collections    │  │  (Directories)  │  │ (Collections)   │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## **🎯 How Each File Works & Connects**

### **1. 🚀 `main_processor.py` - The Master Controller**

**Role**: Main entry point and workflow orchestrator

**Key Functions**:
- **File Renaming**: Converts JSON files from old format to new naming convention
- **Model Processing**: Handles both single and batch processing
- **CLI Interface**: Provides user-friendly command-line interface
- **Integration Hub**: Connects all other modules together

**Connections**:
- **Imports**: `postman_generator.py` for collection creation
- **Uses**: `models_config.py` for model configurations
- **Calls**: `dynamic_models.py` functions for model discovery

**Key Code Sections**:
```python
# Imports from other modules
from postman_generator import PostmanCollectionGenerator
from models_config import get_models_config, get_model_by_ts

# Main processing function
def rename_files(edit_id, code, source_dir, dest_dir, generate_postman=True):
    # File processing logic
    # Calls postman_generator for collection creation
```

---

### **2. 🔍 `dynamic_models.py` - The Smart Discovery Engine**

**Role**: Automatically discovers and analyzes TS (Test Suite) folders

**Key Functions**:
- **Pattern Recognition**: Uses regex to identify TS folder patterns
- **Model Extraction**: Extracts edit IDs, codes, and metadata from folder names
- **Flexible Discovery**: Supports both WGS_CSBD and GBDF model types
- **Normalization**: Handles different TS number formats (01, 1, 001)

**Connections**:
- **Used by**: `models_config.py` for dynamic configuration loading
- **Called by**: `main_processor.py` for model discovery

**Key Code Sections**:
```python
# Main discovery function
def discover_ts_folders(base_dir=".", use_wgs_csbd_destination=False):
    # Pattern matching and model extraction
    # Returns list of model configurations

# Utility functions
def get_model_by_ts_number(ts_number, base_dir="."):
    # Find specific model by TS number
```

---

### **3. ⚙️ `models_config.py` - The Configuration Manager**

**Role**: Manages model configurations with fallback support

**Key Functions**:
- **Static Config**: Maintains hardcoded model configurations
- **Dynamic Loading**: Uses `dynamic_models.py` for auto-discovery
- **Fallback System**: Falls back to static config if dynamic discovery fails
- **Model Lookup**: Provides functions to find specific models by TS number

**Connections**:
- **Imports**: `dynamic_models.py` for discovery functions
- **Used by**: `main_processor.py` for getting model configurations

**Key Code Sections**:
```python
# Import from dynamic_models
from dynamic_models import discover_ts_folders, get_model_by_ts_number

# Configuration loading with fallback
def get_models_config(use_dynamic=True, use_wgs_csbd_destination=False, use_gbdf_mcr=False):
    if use_dynamic:
        # Try dynamic discovery first
        discovered_models = discover_ts_folders("source_folder/WGS_CSBD", use_wgs_csbd_destination)
        if discovered_models:
            return discovered_models
        else:
            # Fallback to static config
            return STATIC_MODELS_CONFIG.get("wgs_csbd", [])
```

---

### **4. 🚀 `postman_generator.py` - The API Collection Creator**

**Role**: Converts JSON files into Postman API test collections

**Key Functions**:
- **Collection Generation**: Creates Postman v2.1.0 format collections
- **Request Creation**: Converts JSON files into API requests
- **Header Management**: Applies appropriate headers for WGS_CSBD vs GBDF models
- **Validation**: Validates generated collections

**Connections**:
- **Used by**: `main_processor.py` for collection generation
- **Used by**: `postman_cli.py` for standalone collection creation

**Key Code Sections**:
```python
class PostmanCollectionGenerator:
    def generate_postman_collection(self, collection_name, custom_filename=None, is_gbdf_model=False):
        # Create Postman collection from JSON files
        # Handle different model types (WGS_CSBD vs GBDF)
        
    def _create_postman_request(self, json_file_path, parsed_info, is_gbdf_model=False):
        # Convert JSON file to Postman request
```

---

### **5. 🎛️ `postman_cli.py` - The Command Line Interface**

**Role**: Provides standalone CLI for Postman collection operations

**Key Functions**:
- **Collection Generation**: Generate collections independently
- **Directory Listing**: List available directories for processing
- **Statistics**: Show detailed statistics about directories
- **Validation**: Validate existing Postman collections

**Connections**:
- **Imports**: `postman_generator.py` for all collection operations
- **Standalone**: Can work independently of the main workflow

**Key Code Sections**:
```python
# Import the generator
from postman_generator import PostmanCollectionGenerator

# CLI command handlers
def handle_generate(args):
    generator = PostmanCollectionGenerator(args.source_dir, args.output_dir)
    collection_path = generator.generate_postman_collection(args.collection_name)
```

---

## **🔄 Data Flow Examples**

### **Example 1: Complete Workflow (Most Common)**
```bash
python main_processor.py --wgs_csbd --TS01
```

**Flow Diagram**:
```
User Command
     │
     ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ main_processor  │───▶│ models_config   │───▶│ dynamic_models  │
│ (CLI Parser)    │    │ (Load Config)   │    │ (Discover TS01) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
     │
     ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ main_processor  │───▶│ postman_generator│───▶│ Postman Collection│
│ (File Process)  │    │ (Create Collection)│  │ (Ready for API) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

**Step-by-Step Process**:
1. **`main_processor.py`** starts and parses CLI arguments
2. **`models_config.py`** loads configuration using dynamic discovery
3. **`dynamic_models.py`** scans `source_folder/WGS_CSBD/` for TS01 folders
4. **`main_processor.py`** processes files (renames, moves, transforms)
5. **`postman_generator.py`** creates Postman collection
6. **Result**: Renamed files + Postman collection ready for API testing

---

### **Example 2: Batch Processing**
```bash
python main_processor.py --wgs_csbd --all
```

**Flow Diagram**:
```
User Command
     │
     ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ main_processor  │───▶│ dynamic_models  │───▶│ Multiple Models │
│ (Batch Mode)    │    │ (Find All TS)   │    │ (TS01, TS02...) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
     │
     ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ main_processor  │───▶│ postman_generator│───▶│ Multiple Collections│
│ (Process Each)  │    │ (Create Each)   │    │ (Individual)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

**Step-by-Step Process**:
1. **`main_processor.py`** discovers all WGS_CSBD models
2. **`dynamic_models.py`** finds all TS folders matching patterns
3. **`models_config.py`** provides configurations for each model
4. **`main_processor.py`** processes each model sequentially
5. **`postman_generator.py`** creates collections for each model
6. **Result**: Multiple model processing with individual collections

---

### **Example 3: Standalone Postman Operations**
```bash
python postman_cli.py generate --collection-name "MyTestCollection"
```

**Flow Diagram**:
```
User Command
     │
     ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ postman_cli     │───▶│ postman_generator│───▶│ Postman Collection│
│ (CLI Parser)    │    │ (Scan JSON Files)│   │ (Standalone)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

**Step-by-Step Process**:
1. **`postman_cli.py`** parses CLI arguments
2. **`postman_generator.py`** scans for JSON files
3. **`postman_generator.py`** creates collection from existing files
4. **Result**: New Postman collection without file processing

---

## **🎯 Key Integration Points**

### **Import Relationships**:
```python
# main_processor.py imports:
from postman_generator import PostmanCollectionGenerator
from models_config import get_models_config, get_model_by_ts

# models_config.py imports:
from dynamic_models import discover_ts_folders, get_model_by_ts_number

# postman_cli.py imports:
from postman_generator import PostmanCollectionGenerator
```

### **Data Flow Diagram**:
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Source      │───▶│ dynamic_    │───▶│ models_     │───▶│ main_       │───▶│ postman_    │
│ Folders     │    │ models.py   │    │ config.py   │    │ processor.py│    │ generator.py│
│ (TS_XX_*)   │    │ (Discovery) │    │ (Config)    │    │ (Process)   │    │ (Collection)│
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                                    │
                                                                                    ▼
                                                                            ┌─────────────┐
                                                                            │ Postman     │
                                                                            │ Collections │
                                                                            │ (Ready)     │
                                                                            └─────────────┘
```

### **Configuration Flow**:
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Static      │◄──►│ Dynamic     │───▶│ Model       │───▶│ Processing  │
│ Config      │    │ Discovery   │    │ Configs     │    │ (main_      │
│ (models_    │    │ (dynamic_   │    │ (Ready)     │    │ processor)  │
│ config.py)  │    │ models.py)  │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

---

## **🎪 Demo Presentation Points**

### **For Your Demo, Emphasize**:

1. **🔄 Automation**: The system automatically discovers models without manual configuration
2. **🎯 Flexibility**: Supports both WGS_CSBD and GBDF model types
3. **📁 File Processing**: Converts files from old naming to new standardized format
4. **🚀 API Testing**: Generates ready-to-use Postman collections
5. **🛠️ CLI Interface**: User-friendly command-line interface for all operations

### **Demo Commands to Show**:
```bash
# Show model discovery
python main_processor.py --list

# Process a specific model
python main_processor.py --wgs_csbd --TS01

# Process all models
python main_processor.py --wgs_csbd --all

# Standalone Postman operations
python postman_cli.py list-directories
python postman_cli.py generate --collection-name "DemoCollection"
```

### **Key Benefits to Highlight**:
- **🔄 End-to-End Automation**: From file discovery to API testing
- **📊 Scalability**: Handles multiple models and batch processing
- **🎯 Accuracy**: Pattern-based discovery reduces manual errors
- **🚀 Efficiency**: Generates production-ready Postman collections
- **🛠️ Maintainability**: Modular design makes it easy to extend

---

## **📊 File Dependencies Summary**

| File | Imports From | Used By | Primary Function |
|------|-------------|---------|------------------|
| `main_processor.py` | `postman_generator.py`, `models_config.py` | User (CLI) | Workflow orchestration |
| `dynamic_models.py` | None | `models_config.py`, `main_processor.py` | Model discovery |
| `models_config.py` | `dynamic_models.py` | `main_processor.py` | Configuration management |
| `postman_generator.py` | None | `main_processor.py`, `postman_cli.py` | Collection generation |
| `postman_cli.py` | `postman_generator.py` | User (CLI) | Standalone Postman operations |

---

## **🎯 Demo Script Suggestions**

### **Opening (2 minutes)**:
"Today I'll show you an automated file processing and API testing system. This system consists of 5 interconnected Python files that work together to discover, process, and create API test collections from JSON files."

### **Architecture Overview (3 minutes)**:
"Let me show you how these files connect. The main_processor.py is our orchestrator, dynamic_models.py discovers models automatically, models_config.py manages configurations, postman_generator.py creates API collections, and postman_cli.py provides standalone operations."

### **Live Demo (5 minutes)**:
1. Show model discovery: `python main_processor.py --list`
2. Process a model: `python main_processor.py --wgs_csbd --TS01`
3. Show generated files and Postman collection
4. Demonstrate standalone Postman operations

### **Closing (2 minutes)**:
"This system provides end-to-end automation, from file discovery to API testing, with scalability and maintainability built-in. The modular design makes it easy to extend and customize for different use cases."

---

This architecture provides a complete solution for automated file processing and API testing workflow, making it perfect for demonstrating a well-integrated system!
