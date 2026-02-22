---
description: Postman and JSON file naming conventions for renaming_files
globs: "**/postman_collections/**/*.json,**/renaming_jsons/**/*.json,**/source_folder/**/*.json"
alwaysApply: false
trigger: glob
---

# Postman and JSON Naming Conventions

## Renamed JSON File Format
- **Pattern:** `TC#<ID>#<EditID>#<Code>#<Suffix>.json`
- **Example:** `TC#01_sample#RULEOBSER00001#00W28#LR.json`
- **Suffix mapping (do not change):** deny→LR, bypass→NR, exclusion→EX (and any exception variants→EX).
- Source files use old format: `TC#<ID>#deny.json`, `TC#<ID>#bypass.json`, etc. Renaming must produce the new format exactly.

## Directory Conventions
- **Source:** `source_folder/[Category]/.../payloads/regression` or `.../payloads/smoke`. Folder suffix `_sur`.
- **Destination:** `renaming_jsons/[Category]/.../payloads/` (smoke/regression). Folder suffix `_dis`.
- Paths must include `/payloads/`; subfolder is either `smoke` or `regression`.

## Postman Collections
- **Location:** `postman_collections/[Category]/[ModelName]_Collection/`.
- **Naming:** Collection and file names follow model: e.g. `observation_services_wgs_csbd_RULEOBSER00005_00W28_smoke.json`.
- **Format:** Postman v2.1.0; request names/IDs derived from renamed JSON filenames (TC#ID#EditID#Code#Suffix).
- Do not manually change EditID or Code segments in filenames; they come from `models_config` / discovery.

## WGS_CSBD-Only Behavior
- Header/footer transformation and random 11-digit `KEY_CHK_DCN_NBR` (root and payload) apply only to WGS_CSBD. Do not add to GBDF or WGS_NYK payloads.

## Editing JSON Payloads
- Preserve structure expected by postman_generator (e.g. request body from renamed JSON).
- When adding or renaming test case files in source, ensure the corresponding EditID and Code exist in config and that the new name matches the `TC#ID#EditID#Code#Suffix` pattern after processing.
