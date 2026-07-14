# Zimbabwe Law AI Evidence Layer

I built this repository as the technical, governance, validation, and audit evidence layer for **Zimbabwe Law AI**.

My aim is to show, clearly and reproducibly, how I collected, structured, normalised, checked, and governed the 2022 Zimbabwean judicial dataset that supports this project. I use the repository to preserve provenance, document corrections, test data quality, record review decisions, and prepare evidence for organisational and regulatory assessment.

This repository is not a claim of regulatory approval. It is also not legal advice or an official court publication.

## Why I built it

Zimbabwean judgments are available in many formats, but they are not consistently structured for reproducible legal research or responsible AI development. I created this evidence layer so that every important transformation can be traced, reviewed, and repeated rather than hidden inside an informal workflow.

The current evidence dataset contains **522 canonical records** across the Constitutional Court, Supreme Court, and High Court. I preserve the source lineage, validation results, correction history, schemas, review queues, code, governance controls, and POTRAZ submission material alongside the data.

## Repository structure

```text
data/raw/          Original rebuilt JSONL
data/processed/    Normalised and minimised derivatives
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

## Main dataset files

```text
data/raw/zimbabwe_2022_law_reports_all_courts_rebuilt.jsonl
data/processed/zimbabwe_2022_law_reports_normalized.jsonl
data/processed/zimbabwe_2022_law_reports_normalized.jsonl.gz
data/processed/zimbabwe_2022_law_reports_metadata_only.jsonl
data/public/zimbabwe_2022_law_reports_public_minimal.jsonl
data/index/zimbabwe_2022_law_reports_index.csv
```

## How I run the checks

```bash
python -m pip install -e ".[dev]"
python scripts/validate_dataset.py
pytest -q
python scripts/verify_hashes.py
```

On Windows PowerShell I use:

```powershell
.\scripts\run_all_checks.ps1
```

## Evidence controls

I use deterministic hashing, schema validation, normalisation logs, duplicate-source evidence, manual-review queues, privacy checks, access and retention controls, incident procedures, correction and takedown processes, processing registers, risk registers, and POTRAZ evidence indexing.

I do not treat automated validation as a substitute for legal, editorial, privacy, security, or institutional review. Any external release or production deployment still requires documented approval by the relevant accountable persons.

## Publication boundary

The full repository should remain private while it contains complete source text, personal information, internal review decisions, security material, or submission evidence. I only place material under `data/public/` after it has passed technical checks and separate legal, privacy, and institutional review.