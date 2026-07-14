# Reproducibility Report

I use the following source dataset as the input to the reproducible build:

- **Input:** `data/raw/zimbabwe_2022_law_reports_all_courts_rebuilt.jsonl`
- **Input rows:** 522
- **Input SHA-256:** `60c2f8f21330a41e336a4210809681f58da03c1ec42755df424aacd5484e9f65`

I rebuild and test the derived dataset with:

```bash
python -m pip install -e ".[dev]"
python scripts/normalise_dataset.py
python scripts/validate_dataset.py
pytest -q
```

I expect the normalised output to contain 522 records. The validation report must pass before I treat the build as complete. I use the normalisation log to record field recovery and derived-value changes, and I calculate each record hash from canonical JSON after excluding the `record_sha256` field itself.