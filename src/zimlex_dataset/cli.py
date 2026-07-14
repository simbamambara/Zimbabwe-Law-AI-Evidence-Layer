from __future__ import annotations

import argparse
import json
from pathlib import Path

from .io import load_jsonl, write_jsonl
from .normalise import normalise_record
from .release import build_public_minimal
from .search import search
from .validate import validate_records


def main() -> int:
    parser = argparse.ArgumentParser(prog="zimlex-dataset")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate")
    p_validate.add_argument("dataset", type=Path)
    p_validate.add_argument("--expected-rows", type=int, default=522)

    p_normalise = sub.add_parser("normalise")
    p_normalise.add_argument("source", type=Path)
    p_normalise.add_argument("output", type=Path)

    p_public = sub.add_parser("public-release")
    p_public.add_argument("source", type=Path)
    p_public.add_argument("output", type=Path)

    p_search = sub.add_parser("search")
    p_search.add_argument("source", type=Path)
    p_search.add_argument("query")
    p_search.add_argument("--limit", type=int, default=20)

    args = parser.parse_args()

    if args.command == "validate":
        report = validate_records(load_jsonl(args.dataset), args.expected_rows)
        print(json.dumps(report, indent=2))
        return 0 if report["validation_passed"] else 1

    if args.command == "normalise":
        normalized = [normalise_record(record)[0] for record in load_jsonl(args.source)]
        write_jsonl(args.output, normalized)
        return 0

    if args.command == "public-release":
        write_jsonl(args.output, build_public_minimal(load_jsonl(args.source)))
        return 0

    if args.command == "search":
        results = search(load_jsonl(args.source), args.query, args.limit)
        for record in results:
            print(json.dumps({
                key: record.get(key)
                for key in ["record_id", "case_name", "court", "judgment_number", "citation", "subject_area"]
            }, ensure_ascii=False))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
