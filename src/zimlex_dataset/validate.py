from __future__ import annotations

from collections import Counter
import re

from .normalise import canonical_record_hash

CRITICAL_DRAFT_FIELDS = [
    "case_name", "court", "case_number", "judgment_number", "judges",
    "subject_area", "catchwords_flynote", "headnote", "facts",
    "issues_for_determination", "legal_principles", "held_decision_points",
    "ratio_decidendi", "final_order", "full_formatted_judgment_text",
    "approval_status",
]


def validate_records(records: list[dict], expected_rows: int | None = None) -> dict:
    ids = [record.get("record_id") for record in records]
    identities = [record.get("canonical_identity") for record in records]
    rows = [record.get("dataset_row_number") for record in records]
    critical_missing = []

    for record in records:
        if record.get("record_type") == "law_report_draft":
            missing = [field for field in CRITICAL_DRAFT_FIELDS if not str(record.get(field, "")).strip()]
            if missing:
                critical_missing.append({"record_id": record.get("record_id"), "missing_fields": missing})

    report = {
        "parsed_rows": len(records),
        "row_numbers_are_contiguous_1_to_n": rows == list(range(1, len(records) + 1)),
        "duplicate_record_id_count": len(ids) - len(set(ids)),
        "duplicate_canonical_identity_count": len(identities) - len(set(identities)),
        "missing_record_id_count": sum(not value for value in ids),
        "record_type_counts": dict(Counter(record.get("record_type", "") for record in records)),
        "court_family_counts": dict(Counter(record.get("court_family", "") for record in records)),
        "source_occurrence_count_mismatches": sum(record.get("source_occurrence_count") != len(record.get("source_occurrences", [])) for record in records),
        "record_hash_mismatch_count": sum(record.get("record_sha256") != canonical_record_hash(record) for record in records),
        "draft_critical_missing_count": len(critical_missing),
        "draft_critical_missing": critical_missing,
        "non_high_court_records_with_division_count": sum(record.get("court_family") != "High Court" and bool(str(record.get("division", "")).strip()) for record in records),
        "high_court_records_without_division_count": sum(record.get("court_family") == "High Court" and not str(record.get("division", "")).strip() for record in records),
        "absolute_source_path_hit_count": sum(bool(re.search(r"(?i)(?:[A-Z]:\\Users\\|/home/|/Users/)", str(occ.get("source_file_relative", "")))) for record in records for occ in record.get("source_occurrences", [])),
    }

    if expected_rows is not None:
        report["expected_rows"] = expected_rows
        report["row_count_matches"] = len(records) == expected_rows

    report["validation_passed"] = all([
        report.get("row_count_matches", True),
        report["row_numbers_are_contiguous_1_to_n"],
        report["duplicate_record_id_count"] == 0,
        report["duplicate_canonical_identity_count"] == 0,
        report["missing_record_id_count"] == 0,
        report["source_occurrence_count_mismatches"] == 0,
        report["record_hash_mismatch_count"] == 0,
        report["draft_critical_missing_count"] == 0,
        report["non_high_court_records_with_division_count"] == 0,
        report["high_court_records_without_division_count"] == 0,
        report["absolute_source_path_hit_count"] == 0,
    ])
    return report
