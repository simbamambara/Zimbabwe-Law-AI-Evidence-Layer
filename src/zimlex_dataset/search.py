from __future__ import annotations

import re

SEARCH_FIELDS = [
    "case_name",
    "judgment_number",
    "citation",
    "subject_area",
    "catchwords_flynote",
    "headnote",
    "ratio_decidendi",
]


def search(records: list[dict], query: str, limit: int = 20) -> list[dict]:
    terms = [term.lower() for term in re.findall(r"[A-Za-z0-9]+", query)]
    scored = []
    for record in records:
        text = "\n".join(str(record.get(field, "")) for field in SEARCH_FIELDS).lower()
        score = sum(text.count(term) for term in terms)
        if score:
            scored.append((score, record))
    scored.sort(key=lambda item: (-item[0], item[1].get("judgment_number", "")))
    return [record for _, record in scored[:limit]]
