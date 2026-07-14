from __future__ import annotations

import json
from pathlib import Path

from zimlawai_evidence.validation import validate_dataset

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data/curated/zimbabwe_2022_evidence_dataset_v1.jsonl"
REPORT = ROOT / "data/quality/validation_report.json"


def main() -> int:
    if not DATASET.exists():
        print(f"Dataset not found: {DATASET}")
        print("Upload the curated JSONL file to the documented path and rerun.")
        return 2

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    result = validate_dataset(DATASET, expected_rows=522)
    REPORT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["validation_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
