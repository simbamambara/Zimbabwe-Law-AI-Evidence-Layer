from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist/ZIMLEX-POTRAZ-Submission-Pack.zip"
INCLUDE_PREFIXES = [
    "evidence/potraz/",
    "docs/governance/",
    "docs/registers/",
    "docs/compliance/",
    "data/metadata/",
    "schemas/",
]
INCLUDE_FILES = ["README.md", "SECURITY.md", "LICENSE_DATA.md", "CHANGELOG.md"]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
        relative = path.relative_to(ROOT).as_posix()
        if relative == OUTPUT.relative_to(ROOT).as_posix():
            continue
        if relative in INCLUDE_FILES or any(relative.startswith(prefix) for prefix in INCLUDE_PREFIXES):
            archive.write(path, relative)

print(OUTPUT)
