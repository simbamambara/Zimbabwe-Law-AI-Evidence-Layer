from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


def iter_jsonl(path: str | Path) -> Iterable[dict[str, Any]]:
    source = Path(path)
    with source.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}: {exc}") from exc


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_dataset(path: str | Path, expected_rows: int | None = 522) -> dict[str, Any]:
    records = list(iter_jsonl(path))
    record_ids = [str(record.get("record_id", "")).strip() for record in records]
    identities = [str(record.get("canonical_identity", "")).strip() for record in records]

    duplicate_record_ids = [key for key, count in Counter(record_ids).items() if key and count > 1]
    duplicate_identities = [key for key, count in Counter(identities).items() if key and count > 1]

    report = {
        "dataset_path": str(path),
        "sha256": sha256_file(path),
        "record_count": len(records),
        "expected_rows": expected_rows,
        "row_count_matches": expected_rows is None or len(records) == expected_rows,
        "empty_record_id_count": sum(not value for value in record_ids),
        "duplicate_record_ids": duplicate_record_ids,
        "duplicate_canonical_identities": duplicate_identities,
    }
    report["validation_passed"] = (
        report["row_count_matches"]
        and report["empty_record_id_count"] == 0
        and not duplicate_record_ids
        and not duplicate_identities
    )
    return report
