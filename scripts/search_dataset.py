from pathlib import Path
import argparse

from zimlex_dataset.io import load_jsonl
from zimlex_dataset.search import search

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data/processed/zimbabwe_2022_law_reports_normalized.jsonl"

parser = argparse.ArgumentParser()
parser.add_argument("query")
parser.add_argument("--limit", type=int, default=20)
args = parser.parse_args()

if not DATASET.exists():
    raise SystemExit(f"Dataset not found: {DATASET}")

records = load_jsonl(DATASET)
for record in search(records, args.query, args.limit):
    print(f"{record['judgment_number']} | {record['case_name']} | {record['subject_area']}")
