---
description: Python coding standards for renaming_files project
globs: "**/*.py"
alwaysApply: false
trigger: model_decision
---

# Python Standards

## Style and Structure
- Use Python 3 with shebang `#!/usr/bin/env python3`.
- Module docstrings at top: purpose, main responsibilities, and key behaviors.
- Prefer `pathlib.Path` for path handling; use `os.path` only when needed for compatibility.
- Load environment via `python-dotenv` from project root: `load_dotenv(dotenv_path=Path(__file__).parent / '.env')`.

## CLI and Configuration
- Use `argparse` for CLI; category and TS model as primary args (e.g. `--wgs_csbd --CSBDTS49`).
- Feature flags and options from `.env`: e.g. `ENABLE_REPORT_GENERATION`, `ENABLE_POSTMAN_*`. Default to `'true'` and check with `.lower() in ('true', '1', 'yes', 'on')`.
- Optional modules (e.g. report_generate): import in try/except and guard usage with env or availability checks.

## Imports and Entry Points
- Core modules live in project root: `main_processor.py`, `rename_files.py`, `postman_generator.py`, `dynamic_models.py`, `models_config.py`, `report_generate.py`.
- Cross-module imports are from the same package (no `../` in imports); run scripts from project root.

## Error Handling and Logging
- Prefer explicit error handling: log context (e.g. path, model id) and re-raise or exit with clear messages.
- Avoid bare `except:`; use `except Exception` and log or re-raise.
- Use existing `TimingTracker` and report generators for timing; keep console output actionable for debugging.

## Naming and Conventions
- Model identifiers: WGS_CSBD (CSBDTS), WGS_NYK (NYKTS), GBDF MCR/GRS (GBDTS/TS). Use exact prefixes (NYKTS not TS for NYK).
- Normalize TS numbers via `dynamic_models.normalize_ts_number()`; paths must include `/payloads/` (smoke or regression).
- Do not change suffix mapping: deny→LR, bypass→NR, exclusion→EX without updating postman_generator and docs.
