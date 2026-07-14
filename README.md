# Zimbabwe Law AI Evidence Layer

This repository is the technical, governance, validation, and audit evidence layer for **Zimbabwe Law AI**.

It preserves the project structure needed to demonstrate data provenance, integrity controls, reproducible processing, quality assurance, privacy safeguards, human review, and submission readiness. It is not a claim of regulatory approval, not legal advice, and not an official court publication.

## Evidence snapshot

The current 2022 evidence dataset contains 522 canonical records across the Constitutional Court, Supreme Court, and High Court. The repository records validation results, correction provenance, review queues, source hashes, schemas, processing code, governance controls, and POTRAZ submission material.

## Repository structure

```text
data/raw/          Original rebuilt JSONL uploaded manually
data/processed/    Normalized and minimized derivatives uploaded manually
data/public/       Public-minimal derivative and sample
data/index/        Review-friendly CSV index
data/metadata/     Validation reports, manifests, queues, and audit logs
schemas/           JSON Schema and data dictionary
src/               Reusable Python validation and processing package
scripts/           Build, validation, integrity, and release utilities
tests/             Structural and privacy-boundary tests
docs/              Architecture, governance, compliance, and registers
evidence/potraz/   POTRAZ evidence index, control matrix, and sign-off pack
```

## Manual large-file upload

Upload the large files manually to these exact paths:

```text
data/raw/zimbabwe_2022_law_reports_all_courts_rebuilt.jsonl
data/processed/zimbabwe_2022_law_reports_normalized.jsonl
data/processed/zimbabwe_2022_law_reports_normalized.jsonl.gz
data/processed/zimbabwe_2022_law_reports_metadata_only.jsonl
data/public/zimbabwe_2022_law_reports_public_minimal.jsonl
```

Upload these supporting evidence files to their exact paths when they are not already present:

```text
data/index/zimbabwe_2022_law_reports_index.csv
data/metadata/normalization_log.csv
data/public/zimbabwe_2022_public_sample.jsonl
```

## Run the checks

After the manual upload:

```bash
python -m pip install -e ".[dev]"
python scripts/validate_dataset.py
pytest -q
python scripts/verify_hashes.py
```

Windows PowerShell:

```powershell
.\scripts\run_all_checks.ps1
```

Before the large files are uploaded, CI performs repository-structure and code tests and reports dataset validation as pending instead of failing on missing files.

## Evidence controls

The repository includes deterministic hashing, schema validation, normalization logs, duplicate-source evidence, manual-review queues, privacy and governance templates, access and retention controls, incident procedures, correction and takedown processes, processing and risk registers, and POTRAZ evidence indexing.

## Publication boundary

Keep the repository private when it contains full source text, source blocks, personal information, or internal submission evidence. Any public release requires a documented legal, privacy, editorial, and data-owner decision.

## Status

Evidence framework: configured.  
Large dataset upload: manual step.  
POTRAZ filing: requires completion and sign-off by the accountable organisation.
