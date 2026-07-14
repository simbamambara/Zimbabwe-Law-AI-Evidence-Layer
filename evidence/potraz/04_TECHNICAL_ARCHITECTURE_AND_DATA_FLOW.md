# Technical Architecture and Data Flow

## Components

1. Local processed-source directory.
2. Rebuild notebook or script that recursively scans structured TXT outputs.
3. Immutable raw all-courts JSONL.
4. Deterministic Python normalization package.
5. Normalized JSONL, compressed JSONL, metadata-only derivative, public-minimal derivative, and CSV index.
6. JSON Schema, validation controls, manifests, and review queues.
7. Private GitHub repository with branch, review, and workflow controls.
8. Controlled downstream search or AI services, subject to separate approval.

## Data flow

```text
Processed structured TXT files
        ↓
Rebuild and canonical deduplication
        ↓
Immutable raw JSONL + source hashes
        ↓
Deterministic normalization + audit log
        ↓
Schema and integrity validation
        ↓
Human legal/privacy review
        ↓
Controlled release or restricted downstream use
```

## Trust boundaries

- Local source-processing environment.
- GitHub or other code-hosting environment.
- Cloud storage and backup environment.
- Any AI, embedding, analytics, or search provider.
- Public-release environment.

Each new hosting or processor boundary requires access, transfer, contract, security, retention, and incident-response assessment.
