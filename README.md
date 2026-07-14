# Zimbabwe Law AI — Evidence Layer

This repository is the technical, governance, and audit evidence layer for Zimbabwe Law AI.

It documents how legal-source data is collected, normalised, validated, governed, reviewed, and prepared for controlled AI use. It is designed to support reproducibility, accountability, regulatory review, security assessment, and institutional sign-off.

> **Status:** development and submission-preparation evidence. This repository is not a declaration of regulatory compliance, not an official legal publication, and not legal advice.

## Evidence snapshot

The current 2022 evidence dataset contains 522 canonical records:

- 465 structured draft records;
- 51 excluded records;
- 6 manual-review records;
- 10 Constitutional Court records;
- 119 Supreme Court records;
- 393 High Court records.

High Court coverage includes Harare, Bulawayo, Masvingo, Chinhoyi, and Mutare.

## Repository purpose

The evidence layer provides:

- dataset lineage and source-integrity controls;
- schema and data-dictionary documentation;
- validation and quality-assurance tooling;
- reproducible dataset build scripts;
- security, privacy, retention, and access-control documentation;
- human-review and approval controls;
- risk, incident, correction, and takedown procedures;
- evidence registers and submission templates;
- automated integrity checks through GitHub Actions.

## Repository structure

```text
data/
├── source/       Controlled source datasets uploaded manually
├── curated/      Normalised and quality-reviewed datasets
├── public/       Approved public-safe derivatives only
├── index/        Search and review indexes
├── quality/      Validation, duplicate, anomaly, and review reports
├── manifests/    Release and integrity manifests
└── schema/       Machine-readable schemas and dictionaries

src/
└── zimlawai_evidence/   Reusable validation and evidence tooling

scripts/          Dataset validation, hashing, release, and audit scripts
tests/            Automated regression and integrity tests
docs/             Architecture, methodology, governance, compliance, and registers
evidence/potraz/  Submission-preparation evidence index and control matrix
.github/          CI workflows, issue templates, and ownership controls
```

## Large dataset files

Large and controlled files are intentionally not created through the repository API. Upload them manually into these exact paths:

```text
data/source/zimbabwe_2022_all_courts_rebuilt.jsonl
data/curated/zimbabwe_2022_evidence_dataset_v1.jsonl
data/index/zimbabwe_2022_evidence_index.csv
```

After uploading, run:

```bash
python -m pip install -e ".[dev]"
python scripts/validate_dataset.py
python scripts/generate_manifest.py
pytest -q
```

## Publication boundary

This repository must remain private while it contains full legal-source text, personal information, unpublished derived records, internal review decisions, regulatory evidence, security documentation, or operational logs.

Only files specifically approved for public release should be placed under `data/public/`.

## Human accountability

Automated processing does not replace legal, editorial, privacy, security, or institutional review. Dataset releases and AI-system use require documented approval by authorised accountable persons.
