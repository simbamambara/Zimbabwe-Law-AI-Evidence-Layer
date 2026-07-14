# Technical Architecture

```mermaid
flowchart LR
  A[Processed court TXT outputs] --> B[Rebuilt all-courts JSONL]
  B --> C[Immutable raw evidence]
  B --> D[Deterministic normalizer]
  D --> E[Normalized 522-record JSONL]
  E --> F[Schema and validation]
  E --> G[CSV review index]
  E --> H[Metadata-only derivative]
  E --> I[Public-minimal derivative]
  F --> J[POTRAZ evidence pack]
  G --> K[Human legal and privacy review]
  K --> L[Approved controlled release]
```

The normalizer fills only blank values recoverable from preserved source blocks, derives machine fields, corrects division scope, and refreshes hashes. It does not rewrite substantive source text.
