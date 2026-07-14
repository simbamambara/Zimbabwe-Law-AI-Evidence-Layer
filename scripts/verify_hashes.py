from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/metadata/repository_manifest.json"

if not MANIFEST.exists():
    raise SystemExit(f"Manifest not found: {MANIFEST}. Run scripts/generate_manifest.py first.")

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
failures = []
for entry in manifest["files"]:
    path = ROOT / entry["path"]
    if not path.exists():
        failures.append(f"missing:{entry['path']}")
        continue
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != entry["sha256"]:
        failures.append(f"hash:{entry['path']}")

if failures:
    print("Verification failures:")
    print("\n".join(failures))
    raise SystemExit(1)

print(f"Verified {len(manifest['files'])} files")
