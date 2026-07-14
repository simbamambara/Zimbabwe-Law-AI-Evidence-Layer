from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {"repository_manifest.json", "SHA256SUMS"}
files = []
for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
    relative = path.relative_to(ROOT).as_posix()
    if path.name in EXCLUDE or relative.startswith(".git/") or relative.startswith("dist/"):
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    files.append({"path": relative, "size_bytes": path.stat().st_size, "sha256": digest})
manifest = {
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "file_count": len(files),
    "files": files,
}
output = ROOT / "data/metadata/repository_manifest.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(f"Manifest contains {len(files)} files")
