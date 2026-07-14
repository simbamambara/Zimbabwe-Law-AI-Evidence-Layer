from pathlib import Path

from zimlex_dataset.io import load_jsonl, write_jsonl
from zimlex_dataset.release import build_metadata_only, build_public_minimal

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data/processed/zimbabwe_2022_law_reports_normalized.jsonl"

if not DATASET.exists():
    raise SystemExit(f"Normalized dataset not found: {DATASET}")

records = load_jsonl(DATASET)
write_jsonl(
    ROOT / "data/public/zimbabwe_2022_law_reports_public_minimal.jsonl",
    build_public_minimal(records),
)
write_jsonl(
    ROOT / "data/processed/zimbabwe_2022_law_reports_metadata_only.jsonl",
    build_metadata_only(records),
)
print("Public-minimal and metadata-only derivatives generated.")
