from __future__ import annotations

import hashlib
import json
import re

FIELD_NAMES = {
    1: "case_name", 2: "court", 3: "case_number", 4: "judgment_number",
    5: "citation", 6: "parties", 7: "judges", 8: "hearing_date",
    9: "judgment_date", 10: "counsel_and_appearances", 11: "subject_area",
    12: "catchwords_flynote", 13: "headnote", 14: "facts",
    15: "issues_for_determination", 16: "legal_principles",
    17: "held_decision_points", 18: "ratio_decidendi",
    19: "obiter_dicta_where_relevant", 20: "cases_referred_to",
    21: "legislation_considered", 22: "constitutional_provisions_considered",
    23: "procedural_history", 24: "final_order",
    25: "full_formatted_judgment_text", 26: "reviewer_comments",
    27: "approval_status", 28: "export_history",
}

TERM_FIELDS = {
    "subject_area": "subject_area_terms",
    "cases_referred_to": "cases_referred_to_terms",
    "legislation_considered": "legislation_considered_terms",
    "constitutional_provisions_considered": "constitutional_provisions_considered_terms",
}

SHORT_FIELD_LIMITS = {
    "court": 200,
    "case_number": 200,
    "judgment_number": 120,
    "citation": 250,
    "division": 80,
    "approval_status": 80,
}

COURT_BY_FAMILY = {
    "Constitutional Court": "CONSTITUTIONAL COURT OF ZIMBABWE",
    "Supreme Court": "SUPREME COURT OF ZIMBABWE",
    "High Court": "HIGH COURT OF ZIMBABWE",
}


def parse_numbered_fields(text: str) -> dict[str, str]:
    pattern = re.compile(r"(?m)^\s*(\d{1,2})\.\s+([^:\n]+):[ \t]*(.*)$")
    matches = list(pattern.finditer(text or ""))
    output: dict[str, str] = {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        if number not in FIELD_NAMES:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        first_line = match.group(3).rstrip()
        continuation = text[match.end():end]
        output[FIELD_NAMES[number]] = (first_line + ("\n" + continuation if continuation else "")).strip()
    return output


def split_terms(value: str) -> list[str]:
    value = (value or "").strip()
    if not value:
        return []
    return [part.strip(" \t\r\n;-") for part in re.split(r"\n+|;\s*(?=[A-Z0-9])", value) if part.strip(" \t\r\n;-")]


def derive_judgment_number_parts(value: str) -> tuple[str, int | None]:
    match = re.search(r"\b(CCZ|SC|HH|HB|HMT|HMA|HCC)\s*[-/]?\s*(\d+)", (value or "").upper())
    return (match.group(1), int(match.group(2))) if match else ("", None)


def canonical_record_hash(record: dict) -> str:
    payload = dict(record)
    payload.pop("record_sha256", None)
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _looks_corrupted_short_field(field: str, value: object) -> bool:
    text = str(value or "").strip()
    if not text:
        return True
    limit = SHORT_FIELD_LIMITS.get(field)
    if limit is not None and len(text) > limit:
        return True
    if text.count("\n") > 2:
        return True
    if field == "court" and "COURT" not in text.upper():
        return True
    return False


def normalise_record(source_record: dict) -> tuple[dict, list[str]]:
    record = json.loads(json.dumps(source_record, ensure_ascii=False))
    actions: list[str] = []
    recovered = parse_numbered_fields(record.get("source_block_text", ""))

    for field in FIELD_NAMES.values():
        recovered_value = recovered.get(field, "").strip()
        current_value = record.get(field, "")

        should_recover = not str(current_value).strip()
        if field in SHORT_FIELD_LIMITS and _looks_corrupted_short_field(field, current_value):
            should_recover = True

        if should_recover and recovered_value:
            record[field] = recovered_value
            action = "replaced" if str(current_value).strip() else "filled"
            actions.append(f"{action}:{field}:from_source_block")

    # A malformed source block may not expose a recoverable numbered court field.
    # In that case the court family is still authoritative enough to restore the
    # short metadata value without copying judgment prose into the court field.
    if _looks_corrupted_short_field("court", record.get("court", "")):
        fallback_court = COURT_BY_FAMILY.get(str(record.get("court_family", "")).strip())
        if fallback_court:
            record["court"] = fallback_court
            actions.append("replaced:court:from_court_family")

    if record.get("record_type") == "law_report_draft" and not str(record.get("approval_status", "")).strip():
        record["approval_status"] = "Draft"
        actions.append("filled:approval_status:derived_from_draft_record")

    if record.get("court_family") != "High Court" and str(record.get("division", "")).strip():
        record["division"] = ""
        actions.append("cleared:division:non_high_court_record")

    prefix, number = derive_judgment_number_parts(str(record.get("judgment_number", "")))
    if record.get("judgment_number_prefix") != prefix:
        record["judgment_number_prefix"] = prefix
        actions.append("recomputed:judgment_number_prefix")
    if record.get("judgment_number_int") != number:
        record["judgment_number_int"] = number
        actions.append("recomputed:judgment_number_int")

    for source_field, term_field in TERM_FIELDS.items():
        derived = split_terms(str(record.get(source_field, "")))
        if not isinstance(record.get(term_field), list) or record.get(term_field) != derived:
            record[term_field] = derived
            actions.append(f"recomputed:{term_field}")

    occurrences = record.get("source_occurrences")
    if not isinstance(occurrences, list):
        occurrences = []
        record["source_occurrences"] = []
        actions.append("repaired:source_occurrences:not_list")
    if record.get("source_occurrence_count") != len(occurrences):
        record["source_occurrence_count"] = len(occurrences)
        actions.append("recomputed:source_occurrence_count")

    duplicate = len(occurrences) > 1
    if bool(record.get("duplicate_detected")) != duplicate:
        record["duplicate_detected"] = duplicate
        actions.append("recomputed:duplicate_detected")

    record["record_sha256"] = canonical_record_hash(record)
    return record, actions
