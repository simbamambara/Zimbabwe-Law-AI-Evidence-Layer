.PHONY: install normalise validate test public manifest verify evidence all
install:
	python -m pip install -e ".[dev]"
normalise:
	python scripts/normalise_dataset.py
validate:
	python scripts/validate_dataset.py
public:
	python scripts/build_public_release.py
test:
	pytest -q
manifest:
	python scripts/generate_manifest.py
verify:
	python scripts/verify_hashes.py
evidence:
	python scripts/build_submission_pack.py
all: normalise validate public test manifest verify evidence
