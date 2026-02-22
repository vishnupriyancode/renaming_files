---
name: file-renaming-debug
description: Debug and troubleshoot file renaming issues in the healthcare test-case automation project
---

# File Renaming Debug Skill

## Purpose
Help debug and troubleshoot issues with the file renaming automation system, including file path problems, naming convention violations, and processing failures.

## When to Use
- Files are not being renamed correctly
- Processing fails with path-related errors
- Naming conventions are not being applied properly
- Output files are missing or in wrong locations

## Debugging Steps

### 1. Check Model Command Format
Verify the correct command format is being used:
- WGS_CSBD: `--wgs_csbd --CSBDTS[XX]`
- WGS_NYK: `--wgs_nyk --NYKTS[XXX]` (must use NYKTS prefix)
- GBDF MCR: `--gbdf_mcr --GBDTS[XX]`
- GBDF GRS: `--gbdf_grs --TS[XX]`

### 2. Verify Source Paths
Check that source paths follow the pattern:
```
source_folder/[Category]/.../payloads/regression
source_folder/[Category]/.../payloads/smoke
```
Folders must end with `_sur`.

### 3. Check File Naming Convention
Ensure source files follow the pattern:
```
TC#ID#deny.json → TC#ID#EditID#Code#LR.json
TC#ID#bypass.json → TC#ID#EditID#Code#NR.json
TC#ID#exclusion.json → TC#ID#EditID#Code#EX.json
```

### 4. Verify Environment Configuration
Check `.env` file settings:
- `ENABLE_REPORT_GENERATION=true/false`
- Ensure `.env` exists and is properly configured

### 5. Check Dependencies
Verify all required packages are installed:
```bash
pip install -r requirements.txt
```

### 6. Review Console Output
Look for specific error messages in the console output, especially:
- Path not found errors
- Permission issues
- File naming violations
- Model discovery failures

### 7. Check Reports
Review generated reports in `reports/Collection_Reports/` for:
- Processing timing
- File counts
- Error details
- Success/failure statistics

## Common Issues and Solutions

### Issue: WGS_NYK models fail with `--TSXX`
**Solution:** Use `--NYKTS122` format instead of `--TS122`

### Issue: Files not found in source directory
**Solution:** Verify source paths include `/payloads/` and folders end with `_sur`

### Issue: Output files missing
**Solution:** Check destination paths end with `_dis` and verify write permissions

### Issue: Model not found
**Solution:** Run `python main_processor.py --list` to verify model availability

## Commands to Run for Debugging

```bash
# List available models
python main_processor.py --list

# Test with specific model (example)
python main_processor.py --wgs_csbd --CSBDTS01

# Check environment settings
cat .env

# Verify source structure
ls -la source_folder/
```

## Files to Check
- `main_processor.py` - main orchestration logic
- `rename_files.py` - core renaming functionality
- `dynamic_models.py` - model discovery
- `models_config.py` - static model configurations
- `.env` - environment settings
