from pathlib import Path
import csv

from zimlex_dataset.io import load_jsonl, write_jsonl
from zimlex_dataset.normalise import normalise_record

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/raw/zimbabwe_2022_law_reports_all_courts_rebuilt.jsonl"
OUTPUT = ROOT / "data/processed/zimbabwe_2022_law_reports_normalized.jsonl"
LOG = ROOT / "data/metadata/normalization_log.rebuilt.csv"

if not SOURCE.exists():
    raise SystemExit(f"Source dataset not found: {SOURCE}")

records = load_jsonl(SOURCE)
normalized = []
rows = []
for record in records:
    result, actions = normalise_record(record)
    normalized.append(result)
    rows.append({"record_id": result.get("record_id", ""), "actions": "; ".join(actions)})

write_jsonl(OUTPUT, normalized)
LOG.parent.mkdir(parents=True, exist_ok=True)
with LOG.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["record_id", "actions"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Normalized {len(normalized)} records -> {OUTPUT}")
