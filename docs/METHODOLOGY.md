# Methodology

1. Preserve the rebuilt JSONL exactly as supplied.
2. Parse one JSON object per line and reject malformed JSON.
3. Recover missing top-level structured values only from each record's preserved `source_block_text`.
4. Set blank `approval_status` to `Draft` only for structured draft records.
5. Clear `division` for Constitutional Court and Supreme Court records because the field is reserved for High Court stations.
6. Recompute judgment-number derivatives, term arrays, source-occurrence metrics, and record hashes.
7. Preserve source spellings and classification anomalies; route uncertain records to human review.
8. Produce full, metadata-only, and public-minimal derivatives.
9. Validate row count, identifiers, hashes, critical fields, court divisions, source paths, and release boundaries.
10. Retain all audit logs and release manifests.
