# AI Coding Agent Instructions for renaming_files

## Project Overview
Healthcare test case automation system that renames JSON files (mapping `TC#ID#deny.json` → `TC#ID#EditID#Code#LR.json`) and generates Postman API collections for testing across 54 healthcare models (WGS_CSBD, GBDF_MCR, GBDF_GRS, WGS_NYK).

## Architecture: 5-Module Processing Pipeline

**Data Flow**: `source_folder/[Category]/` → **main_processor.py** (CLI orchestrator) → **dynamic_models.py** (discovery) → **models_config.py** (config) → file renaming + **postman_generator.py** (collections) → **excel_report_generator.py** (timing reports)

### Core Modules

1. **`main_processor.py`** - Orchestrator
   - CLI: `python main_processor.py --[category] --[TSXX]` (e.g., `--wgs_csbd --CSBDTS49`)
   - 4 model categories: `--wgs_csbd`, `--gbdf_mcr`, `--gbdf_grs`, `--wgs_nyk`
   - Coordinates rename → Postman generation → Excel reporting pipeline
   - Key function: `extract_model_info_from_directory()` parses destination paths with regex patterns to extract TS number, model name, edit_id, eob_code

2. **`dynamic_models.py`** - Discovery Engine
   - Auto-scans `source_folder/` for TS pattern folders via regex
   - `discover_ts_folders(model_type)` returns list of matching models
   - `normalize_ts_number()` handles variations (1, 01, 001 → consistent format)
   - Fallback: If discovery fails, uses `STATIC_MODELS_CONFIG` from `models_config.py`

3. **`models_config.py`** - Configuration Manager
   - `STATIC_MODELS_CONFIG` dict with all 54 models as fallback
   - Each model specifies: ts_number, edit_id, code, source_dir, dest_dir, postman_collection_name
   - Source paths: `source_folder/[Category]/TS_XX_*_sur/regression` (or `smoke`)
   - Dest paths: `renaming_jsons/[Category]/[MODELNAME]_dis/payloads/`
   - **Unique pattern:** WGS_CSBD files get header/footer transformation with random 11-digit `KEY_CHK_DCN_NBR` added

4. **`postman_generator.py`** - Collection Creator
   - Parses renamed filename format: `TC#ID#EditID#Code#Suffix.json`
   - Suffix mapping: deny→LR (Likely Reject), bypass→NR, exception→EX
   - Creates v2.1.0 Postman collections with request items, UUIDs, default endpoint
   - Output: `postman_collections/[Category]/[ModelName]_Collection/`

5. **`excel_report_generator.py`** - Reporting System
   - `TimingTracker` class measures all operations in milliseconds
   - Excel reports: `[Type]_YYYYMMDD_HHMMSS.xlsx` with columns: TC#ID, Model LOB, Model Name, Edit ID, EOB Code, timing
   - Saved to: `reports/Collection_Reports/`

## Critical Patterns & Conventions

### Model Command Formats (Strict)
- **WGS_CSBD**: `--wgs_csbd --CSBDTS[XX]` (e.g., `--CSBDTS49`, `--CSBDTS01`). Supports TS01-15, TS20, TS46-56 (27 total)
- **WGS_NYK**: `--wgs_nyk --NYKTS[XXX]` (requires NYKTS prefix, NOT TSXX). Supports TS122-130, TS132 (10 total)
- **GBDF_MCR**: `--gbdf_mcr --GBDTS[XX]` (e.g., `--GBDTS47`, `--GBDTS138`). Supports TS47-48, TS60-61, TS70, TS138, TS140, TS144, TS146 (9 total)
- **GBDF_GRS**: `--gbdf_grs --TS[XX]` (uses TS prefix). Supports TS49, TS59, TS61-62, TS139, TS141, TS145, TS147 (8 total)
- All support `--all` flag for batch processing, `--no-postman` to skip collections, `--list` to list models

### File Transformation Logic
```python
# Input file: source_folder/WGS_CSBD/TS_49_*/payloads/regression/TC#01_sample#deny.json
# Rename: TC#01_sample#deny.json → TC#01_sample#RULEOBSER00001#00W28#LR.json
# Output: renaming_jsons/CSBDTS/CSBDTS_49_*/payloads/regression/TC#01_sample#RULEOBSER00001#00W28#LR.json
# Special for WGS_CSBD: Apply header/footer, add KEY_CHK_DCN_NBR random 11-digit number
```

### Directory Pattern Recognition
- **WGS_CSBD**: `CSBDTS_XX_ModelName_WGS_CSBD_EditID_Code_[sur|dis]`
- **GBDF**: `GBDTS_XX_ModelName_gbdf_[mcr|grs]_EditID_Code_[sur|dis]` OR `TS_XX_ModelName_gbdf_[mcr|grs]_EditID_Code_[sur|dis]`
- **WGS_NYK**: `NYKTS_XX_ModelName_WGS_NYK_EditID_Code_[sur|dis]`
- Regex patterns in `main_processor.py` `extract_model_info_from_directory()` match these to extract metadata

### Key Data Structures
**Model Config Entry (from `models_config.py`)**:
```python
{
    "ts_number": "49",
    "edit_id": "RULEOBSER00001",
    "code": "00W28",
    "source_dir": "source_folder/WGS_CSBD/CSBDTS_49_Observation_Services_WGS_CSBD_RULEOBSER00001_00W28_sur/payloads/regression",
    "dest_dir": "renaming_jsons/CSBDTS/CSBDTS_49_Observation_Services_WGS_CSBD_RULEOBSER00001_00W28_dis/payloads/regression",
    "postman_collection_name": "CSBDTS_49_Observation_Services_Collection"
}
```

## Developer Workflows

### Adding a New Model
1. Add folder in `source_folder/[Category]/TS_XX_ModelName_[MODEL_TYPE]_EditID_Code_sur/payloads/[regression|smoke]/`
2. Add entry to `STATIC_MODELS_CONFIG` in `models_config.py` (static fallback)
3. Or rely on dynamic discovery via `dynamic_models.py` (preferred)
4. Run: `python main_processor.py --[category] --[TSXX]`

### Testing
```bash
python main_processor.py --wgs_csbd --CSBDTS49          # Single model test
python main_processor.py --wgs_csbd --all               # Batch test
python main_processor.py --list                          # List discoverable models
python main_processor.py --wgs_csbd --CSBDTS49 --no-postman  # Skip Postman gen
```

### Debugging Model Discovery Issues
1. Check folder naming matches regex patterns in `extract_model_info_from_directory()`
2. Verify dynamic discovery in `dynamic_models.py` with: `discover_ts_folders("wgs_csbd")`
3. Falls back to `STATIC_MODELS_CONFIG` if discovery fails - check that dict for missing entries
4. TS number normalization edge cases (1, 01, 001) handled by `normalize_ts_number()` in `dynamic_models.py`

## Integration Points & Dependencies

### External Dependencies
- `pandas`, `openpyxl` - Excel report generation
- `python-docx` - Optional, not actively used
- Standard library: `os`, `sys`, `json`, `re`, `shutil`, `argparse`, `glob`, `uuid`, `pathlib`, `datetime`

### Cross-Module Communication
- **main_processor → dynamic_models**: Calls `discover_ts_folders(model_type)` to find models
- **main_processor → models_config**: Loads `STATIC_MODELS_CONFIG` as fallback or for validation
- **main_processor → postman_generator**: Instantiates `PostmanCollectionGenerator()` after renaming
- **main_processor → excel_report_generator**: Uses `TimingTracker()` and `ExcelReportGenerator()` for reports
- All modules use shared path conventions: `source_folder/`, `renaming_jsons/`, `postman_collections/`, `reports/Collection_Reports/`

### Output Validation
- Renamed files: Check `renaming_jsons/[Category]/*/payloads/` for correct filename format (`TC#ID#EditID#Code#Suffix.json`)
- Postman collections: Check `postman_collections/[Category]/*/` for valid v2.1.0 JSON with request items
- Excel reports: Check `reports/Collection_Reports/` for XLSX with correct timestamps and timing metrics (in milliseconds)

## Project-Specific Conventions

1. **Naming Clarity**: Model categories use full flags (`--wgs_csbd`) and full argument prefixes (`--CSBDTS49`, `--NYKTS122`, `--GBDTS47`)
2. **Folder Suffixes**: Source folders end with `_sur` (source), destination with `_dis` (destination)
3. **Dual Processing**: `regression` and `smoke` test types processed separately for each model
4. **Timing in MS**: All Excel reports track timing in milliseconds, not seconds
5. **WGS_CSBD Special Case**: Only WGS_CSBD files get dual-level transformation (root + payload) with KEY_CHK_DCN_NBR; GBDF/WGS_NYK do not

## Common Gotchas

- **NYKTS vs TSXX**: WGS_NYK requires `--NYKTS` prefix, NOT `--TS`. Will fail with `--TSXX` format.
- **Static Config Fallback**: If dynamic discovery fails (e.g., folder not found), system silently falls back to `STATIC_MODELS_CONFIG`. Verify model exists in both discovery and config.
- **Directory Structure**: Source paths must include `/payloads/` subdirectory for all models. Destination also creates `/payloads/` structure.
- **TS Number Normalization**: Single digits (1, 2, 9) pad to 2 digits (01, 02, 09); three-digit TS (122, 138) keep 3 digits.

## Reference Implementation Examples

- **Model discovery fallback pattern**: `dynamic_models.py` → `discover_ts_folders()` returns empty → `models_config.py` `STATIC_MODELS_CONFIG` used
- **File extraction pattern**: `main_processor.py` `extract_model_info_from_directory()` traverses up 5 directory levels matching regex patterns
- **Timing tracking pattern**: `excel_report_generator.py` `TimingTracker.start()` / `.end()` wraps each operation
- **CLI pattern**: `main_processor.py` uses `argparse` with subcommand-style flags for model categories and TS arguments
