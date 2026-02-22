---
description: Workspace persistent context — project purpose, code location, entry points, conventions, and development guidelines
alwaysApply: true
trigger: always_on
---

# Renaming Files Project — Workspace Context

## Project Purpose
Healthcare test-case automation: renames JSON files (e.g. `TC#ID#deny.json` → `TC#ID#EditID#Code#LR.json`) and generates Postman API collections. Supports WGS_CSBD, GBDF MCR/GRS, WGS_NYK (54 models).

## Code Location
**Python modules live in the parent directory** of this workspace (`../`), not inside `renaming_files/`. Key files: `main_processor.py`, `rename_files.py`, `postman_generator.py`, `models_config.py`, `dynamic_models.py`, `report_generate.py`, `refdb_change.py`, `auto_edit_processor.py`, `postman_cli.py`.

## Entry Points
- **Orchestrator:** `python main_processor.py --[category] --[TS]` (e.g. `--wgs_csbd --CSBDTS49`, `--wgs_nyk --NYKTS124`, `--gbdf_mcr --GBDTS47`).
- **List models:** `python main_processor.py --list`
- **Batch:** `--all`; skip Postman: `--no-postman`
- **RefDB:** `--refdb` for refdb-supported models (e.g. CSBDTS46/47/59).

## Model Command Formats (Strict)
- **WGS_CSBD:** `--wgs_csbd --CSBDTS[XX]` (e.g. CSBDTS01, CSBDTS49).
- **WGS_NYK:** `--wgs_nyk --NYKTS[XXX]` — must use NYKTS prefix, not TS.
- **GBDF MCR:** `--gbdf_mcr --GBDTS[XX]` (e.g. GBDTS47, GBDTS138).
- **GBDF GRS:** `--gbdf_grs --TS[XX]`.

## Key Paths
- Source: `source_folder/[Category]/.../payloads/regression` (or smoke). Folders end with `_sur`.
- Output: `renaming_jsons/[Category]/.../payloads/`, `postman_collections/[Category]/`, `reports/Collection_Reports/`. Dest folders end with `_dis`.

## Conventions
- WGS_CSBD only: header/footer transformation + random 11-digit KEY_CHK_DCN_NBR (root and payload). GBDF/WGS_NYK do not.
- Suffix mapping: deny→LR, bypass→NR; exclusion→EX. Timing in reports is milliseconds.
- Discovery: `dynamic_models.py` discovers TS folders; fallback is `STATIC_MODELS_CONFIG` in `models_config.py`.

## Development Guidelines
- **Environment:** Configure via `.env` file (copy from `.env.example`). Key setting: `ENABLE_REPORT_GENERATION=true/false`.
- **Dependencies:** Install with `pip install -r requirements.txt`.
- **Testing:** Always test with specific TS models before batch operations. Use `--list` to verify model availability.
- **Debugging:** Check logs in console output; reports generated in `reports/Collection_Reports/` with detailed timing and file counts.
- **File Naming:** Follow strict naming conventions - any deviation causes processing failures.

## Architecture Flow
1. `main_processor.py` → argument parsing and orchestration
2. `dynamic_models.py` → TS folder discovery
3. `rename_files.py` → core file renaming logic
4. `postman_generator.py` → API collection creation
5. `report_generate.py` → execution reports
6. `refdb_change.py` → RefDB integration (when enabled)

## Gotchas
- WGS_NYK fails with `--TSXX`; use `--NYKTS122` etc.
- Source/dest paths must include `/payloads/`. TS numbers normalized (1→01, 122 stays 122).
- Excel file `edits_list.xlsx` contains mapping data for auto-edit processor.
- Temporary files in `__pycache__/` can be safely ignored/deleted.

## Current Status
- Active development with regular model additions
- Postman integration fully functional
- Report generation configurable via environment
- Support for multiple healthcare model categories
