$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

python -m pip install -e ".[dev]"

$Source = "data/raw/zimbabwe_2022_law_reports_all_courts_rebuilt.jsonl"
$Processed = "data/processed/zimbabwe_2022_law_reports_normalized.jsonl"

if (Test-Path $Source) {
    python scripts/normalise_dataset.py
} else {
    Write-Host "Source dataset upload pending: $Source"
}

if (Test-Path $Processed) {
    python scripts/validate_dataset.py
    python scripts/build_public_release.py
} else {
    Write-Host "Processed dataset upload/build pending: $Processed"
}

pytest -q
python scripts/generate_manifest.py
python scripts/verify_hashes.py
python scripts/build_submission_pack.py
