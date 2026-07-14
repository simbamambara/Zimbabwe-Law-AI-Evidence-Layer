from pathlib import Path
import json

from zimlex_dataset.io import load_jsonl
from zimlex_dataset.validate import validate_records

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data/processed/zimbabwe_2022_law_reports_normalized.jsonl"
REPORT = ROOT / "data/metadata/validation_report.rebuilt.json"


def main() -> int:
    if not DATASET.exists():
        print(f"Dataset not found: {DATASET}")
        print("Upload the normalized JSONL file to the exact path documented in README.md.")
        return 2

    report = validate_records(load_jsonl(DATASET), expected_rows=522)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["validation_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
