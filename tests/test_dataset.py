from pathlib import Path

import pytest

from zimlex_dataset.io import load_jsonl
from zimlex_dataset.validate import validate_records

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data/processed/zimbabwe_2022_law_reports_normalized.jsonl"
pytestmark = pytest.mark.skipif(not DATASET.exists(), reason="manual dataset upload pending")


def test_dataset_validation_passes():
    report = validate_records(load_jsonl(DATASET), expected_rows=522)
    assert report["validation_passed"], report


def test_expected_court_counts():
    records = load_jsonl(DATASET)
    counts = {}
    for record in records:
        counts[record["court_family"]] = counts.get(record["court_family"], 0) + 1
    assert counts == {"Constitutional Court": 10, "High Court": 393, "Supreme Court": 119}


def test_expected_record_type_counts():
    records = load_jsonl(DATASET)
    counts = {}
    for record in records:
        counts[record["record_type"]] = counts.get(record["record_type"], 0) + 1
    assert counts == {"law_report_draft": 465, "excluded": 51, "manual_review": 6}
