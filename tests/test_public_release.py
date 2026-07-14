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
        "facts", "full_formatted_judgment_text", "source_block_text",
        "source_occurrences",
    }
    assert records
    for record in records:
        assert not (forbidden & set(record))
