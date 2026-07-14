from __future__ import annotations

PUBLIC_MINIMAL_FIELDS = [
    "dataset_row_number", "record_id", "dataset_year", "court_family",
    "court_instance", "division", "record_type", "publication_workflow_status",
    "workflow_reason", "official_header_classification", "court", "case_number",
    "judgment_number", "citation", "judges", "hearing_date", "judgment_date",
    "subject_area", "catchwords_flynote", "approval_status",
    "judgment_number_prefix", "judgment_number_int", "subject_area_terms",
    "source_occurrence_count", "duplicate_detected", "record_sha256",
]

METADATA_EXCLUDE_FIELDS = {
    "full_formatted_judgment_text", "source_block_text", "parties",
    "counsel_and_appearances", "facts", "procedural_history", "final_order",
    "source_occurrences",
}


def build_public_minimal(records: list[dict]) -> list[dict]:
    return [{key: record.get(key) for key in PUBLIC_MINIMAL_FIELDS} for record in records]


def build_metadata_only(records: list[dict]) -> list[dict]:
    return [{key: value for key, value in record.items() if key not in METADATA_EXCLUDE_FIELDS} for record in records]
