# POTRAZ Control Evidence Matrix

| Control objective | Evidence | Status |
|---|---|---|
| Define processing purpose and accountability | Governance policy, ROPA, DPIA | Draft; accountable roles require confirmation |
| Preserve source integrity | Immutable raw file, SHA-256, source occurrences | Implemented in evidence build |
| Demonstrate dataset completeness | Record counts, court coverage, validation report | Implemented for supplied corpus |
| Prevent silent changes | Normalization log, record hashes, manifests, changelog | Implemented |
| Control access | Access-control policy, private-repository boundary, access register | Policy present; operational evidence required |
| Protect sensitive content | Sensitive-content scan, privacy review, minimized derivative | Partial; human review required |
| Manage accuracy | Schema validation, critical-field checks, correction procedure | Implemented technically; editorial approval pending |
| Retain human oversight | Manual-review queue and publication approval register | Implemented structurally |
| Manage incidents | Incident procedure and register | Documented; exercise and contacts pending |
| Support data-subject rights | Request procedure and register | Documented; operational channel pending |
| Control retention and deletion | Policy and retention schedule | Draft; periods require approval |
| Manage processors and transfers | Processor register and transfer assessment | Templates present; provider decisions pending |
| Control AI use | AI assessment, deployment boundaries, system card | Documented |
| Enable reproducibility | Python package, scripts, tests, CI workflows | Implemented |
| Maintain release accountability | Release policy, approval register, hashes, manifests | Implemented structurally; sign-off pending |
| Verify submission readiness | Gap assessment, checklist, sign-off template | Present |
