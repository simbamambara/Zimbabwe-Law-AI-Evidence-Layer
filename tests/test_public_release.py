from pathlib import Path

import pytest

from zimlex_dataset.io import load_jsonl

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "data/public/zimbabwe_2022_law_reports_public_minimal.jsonl"
pytestmark = pytest.mark.skipif(not PUBLIC.exists(), reason="public derivative build pending")


def test_public_minimal_excludes_high_risk_content_fields():
    records = load_jsonl(PUBLIC)
    forbidden = {
        "case_name", "document_name", "parties", "counsel_and_appearances",
        "facts", "procedural_history", "final_order",
        "full_formatted_judgment_text", "source_block_text",
        "source_occurrences",
    }
    assert records
    for record in records:
        assert not (forbidden & set(record))


def test_public_minimal_short_metadata_cannot_contain_source_passages():
    records = load_jsonl(PUBLIC)
    limits = {
        "court": 200,
        "case_number": 200,
        "judgment_number": 120,
        "citation": 250,
        "division": 80,
        "record_type": 80,
        "publication_workflow_status": 160,
        "official_header_classification": 120,
        "approval_status": 80,
    }

    for record in records:
        for field, limit in limits.items():
            value = str(record.get(field, "")).strip()
            assert len(value) <= limit, (record.get("record_id"), field, len(value))
            assert value.count("\n") <= 2, (record.get("record_id"), field)


def test_public_minimal_does_not_expose_local_paths():
    records = load_jsonl(PUBLIC)
    for record in records:
        serialized = str(record)
        assert "\\Users\\" not in serialized
        assert "/home/" not in serialized
        assert "/Users/" not in serialized