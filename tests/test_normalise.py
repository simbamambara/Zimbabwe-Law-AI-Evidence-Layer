from zimlex_dataset.normalise import normalise_record, parse_numbered_fields


def test_inline_numbered_fields_are_recovered():
    block = """Document name: Example.docx
1. Case name: Example v Example
2. Court: High Court of Zimbabwe
27. Approval status: Draft
28. Export history:
"""
    fields = parse_numbered_fields(block)
    assert fields["case_name"] == "Example v Example"
    assert fields["court"] == "High Court of Zimbabwe"
    assert fields["approval_status"] == "Draft"


def test_normalise_sets_draft_status():
    record = {
        "record_type": "law_report_draft",
        "court_family": "High Court",
        "division": "Harare",
        "judgment_number": "HH 1-22",
        "source_block_text": "",
        "source_occurrences": [],
        "source_occurrence_count": 0,
        "duplicate_detected": False,
        "approval_status": "",
    }
    normalized, actions = normalise_record(record)
    assert normalized["approval_status"] == "Draft"
    assert any("approval_status" in action for action in actions)
    assert len(normalized["record_sha256"]) == 64


def test_corrupted_court_falls_back_to_court_family():
    record = {
        "record_type": "law_report_draft",
        "court_family": "Constitutional Court",
        "division": "",
        "court": "1. The provisional order is confirmed.\n" * 20,
        "judgment_number": "Judgment No. CCZ 9/22",
        "source_block_text": "",
        "source_occurrences": [],
        "source_occurrence_count": 0,
        "duplicate_detected": False,
        "approval_status": "Draft",
    }
    normalized, actions = normalise_record(record)
    assert normalized["court"] == "CONSTITUTIONAL COURT OF ZIMBABWE"
    assert "replaced:court:from_court_family" in actions
    assert len(normalized["record_sha256"]) == 64
