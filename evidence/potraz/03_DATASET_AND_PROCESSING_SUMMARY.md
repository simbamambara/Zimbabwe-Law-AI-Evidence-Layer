# Dataset and Processing Summary

## Dataset scope

- Total canonical records: 522
- Structured draft records: 465
- Excluded records: 51
- Manual-review records: 6
- Constitutional Court: 10
- Supreme Court: 119
- High Court: 393

High Court coverage:

- Harare: 272
- Bulawayo: 95
- Masvingo: 19
- Chinhoyi: 6
- Mutare: 1

## Processing sequence

1. Court-specific structured TXT outputs were scanned recursively.
2. Reportable, excluded, and manual-review blocks were parsed.
3. Canonical identities were generated and duplicate source occurrences retained.
4. One rebuilt all-courts JSONL was created.
5. The raw JSONL was preserved without modification.
6. A deterministic normalizer repaired blank values only where recoverable from preserved source blocks and regenerated derived fields and hashes.
7. Schema, integrity, completeness, division, and privacy-boundary checks were applied.
8. Review indexes, anomaly queues, manifests, and minimized derivatives were produced.

## Integrity values

Raw source SHA-256:

`60c2f8f21330a41e336a4210809681f58da03c1ec42755df424aacd5484e9f65`

Normalized dataset SHA-256:

`366e3540a9266313bdc16349d3407c7f256cce33fb5600572ec0d4f42f9174c8`

## Outstanding human work

Six manual-review records and six classification anomalies require official-source verification. All structured drafts require authorised legal and editorial approval before controlled publication or operational use.
