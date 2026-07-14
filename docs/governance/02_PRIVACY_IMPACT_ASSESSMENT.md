# Data Protection Impact Assessment

## Processing assessed
Compilation, normalization, indexing, search, and controlled publication of Zimbabwean 2022 court-judgment and structured editorial records.

## Data subjects
Litigants, witnesses, minors, legal practitioners, judicial officers, public officials, employees, family members, and other persons mentioned in judgments.

## Data categories
Names, legal allegations, case histories, addresses, employment information, family information, health-related information, criminal matters, protected identities, and other potentially sensitive content.

## Purpose
Create structured research and publication-support tooling while preserving provenance and supporting lawful, accurate use.

## Necessity and proportionality
- Full text is retained only in the private evidence layer.
- A public-minimal derivative omits names and narrative fields.
- Manual review is required for protected identities and sensitive matters.
- Source blocks and hashes are retained for accountability.

## Principal risks
1. Exposure of personal or sensitive information.
2. Incorrect or hallucinated legal summaries.
3. Publication of records without authority.
4. Re-identification through metadata.
5. Unauthorised access or copying.
6. Over-retention and uncontrolled backups.
7. Automated use beyond the approved purpose.
8. Inability to correct or suppress inaccurate records.

## Existing controls
Private-repository default, role-based access, source hashing, record hashing, manual-review queue, classification gate, public-minimal release, correction process, incident response, release sign-off, and validation tests.

## Residual risk
Medium to high until official-source verification, DPO review, legal authority for publication, protected-identity review, and deployment security are completed.

## Required decisions before production
- Confirm controller and processor roles and lawful basis.
- Appoint and document the DPO.
- Complete applicable POTRAZ registration or licensing steps.
- Approve retention and deletion periods.
- Approve public-release scope.
- Conduct security testing and backup-restore testing.
- Establish correction, takedown, and data-subject request channels.

Dataset snapshot assessed: 522 records; 393 High Court, 119 Supreme Court, and 10 Constitutional Court.
