# Repository Structure

## Data layer

- `data/source/`: immutable controlled-source files.
- `data/curated/`: normalised evidence datasets with correction provenance.
- `data/public/`: derivatives explicitly approved for public use.
- `data/index/`: review and retrieval indexes.
- `data/quality/`: validation, anomaly, duplicate, correction, and review reports.
- `data/manifests/`: source, release, and integrity manifests.
- `data/schema/`: JSON Schema and data dictionary.

## Technical layer

- `src/zimlawai_evidence/`: reusable validation and governance utilities.
- `scripts/`: controlled build, validation, hashing, and release commands.
- `tests/`: regression and integrity tests.
- `.github/workflows/`: continuous validation.

## Governance layer

- `docs/architecture/`: system boundaries and data flows.
- `docs/methodology/`: collection, transformation, and quality methods.
- `docs/governance/`: ownership, access, retention, review, and release controls.
- `docs/compliance/`: privacy, security, risk, and regulatory preparation.
- `docs/registers/`: accountable-person, incident, access, correction, and approval registers.
- `docs/potraz/`: submission-preparation documents.
- `evidence/potraz/`: machine-verifiable evidence index and control mapping.
