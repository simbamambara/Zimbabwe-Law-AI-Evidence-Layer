# Reproducibility Report

Input: `data/raw/zimbabwe_2022_law_reports_all_courts_rebuilt.jsonl`  
Input rows: 522  
Input SHA-256: `60c2f8f21330a41e336a4210809681f58da03c1ec42755df424aacd5484e9f65`

Commands:

```bash
python -m pip install -e ".[dev]"
python scripts/normalise_dataset.py
python scripts/validate_dataset.py
pytest -q
```

Expected normalized rows: 522. Expected validation: passed. The normalization log documents field recovery and derived-value refreshes. Record hashes are calculated from canonical JSON excluding `record_sha256`.
