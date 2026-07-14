from pathlib import Path

from zimlawai_evidence.validation import sha256_file, validate_dataset


def test_validation_accepts_unique_records(tmp_path: Path) -> None:
    dataset = tmp_path / "sample.jsonl"
    dataset.write_text(
        '{"record_id":"one","canonical_identity":"court|one"}\n'
        '{"record_id":"two","canonical_identity":"court|two"}\n',
        encoding="utf-8",
    )
    result = validate_dataset(dataset, expected_rows=2)
    assert result["validation_passed"] is True
    assert len(result["sha256"]) == 64


def test_validation_rejects_duplicate_ids(tmp_path: Path) -> None:
    dataset = tmp_path / "sample.jsonl"
    dataset.write_text(
        '{"record_id":"one","canonical_identity":"court|one"}\n'
        '{"record_id":"one","canonical_identity":"court|two"}\n',
        encoding="utf-8",
    )
    result = validate_dataset(dataset, expected_rows=2)
    assert result["validation_passed"] is False
    assert result["duplicate_record_ids"] == ["one"]
