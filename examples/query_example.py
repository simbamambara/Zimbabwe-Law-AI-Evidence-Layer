from pathlib import Path

from zimlex_dataset.io import load_jsonl
from zimlex_dataset.search import search

root = Path(__file__).resolve().parents[1]
dataset = root / "data/processed/zimbabwe_2022_law_reports_normalized.jsonl"
if not dataset.exists():
    raise SystemExit(f"Dataset not found: {dataset}")

records = load_jsonl(dataset)
for result in search(records, "administrative justice", limit=5):
    print(result["judgment_number"], result["case_name"])
