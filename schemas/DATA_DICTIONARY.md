# Evidence Dataset Data Dictionary

The normalized JSONL contains one canonical record per dataset row. The raw source remains unchanged in `data/raw`.

| Field | Type | Description |
|---|---|---|
| `dataset_year` | integer | Dataset year; 2022. |
| `court_family` | string | Constitutional Court, Supreme Court, or High Court. |
| `court_instance` | string | Court instance recorded by the build process. |
| `division` | string | High Court station/division; blank for non-High Court records. |
| `record_type` | string | `law_report_draft`, `excluded`, or `manual_review`. |
| `publication_workflow_status` | string | Editorial workflow status. |
| `workflow_reason` | string | Reason for exclusion or manual review where applicable. |
| `official_header_classification` | string | Official classification captured from source. |
| `document_name` | string | Original source-document name. |
| `case_name` | string | Structured editorial field. |
| `court` | string | Structured editorial field. |
| `case_number` | string | Structured editorial field. |
| `judgment_number` | string | Structured editorial field. |
| `citation` | string | Structured editorial field. |
| `parties` | string | Structured editorial field. |
| `judges` | string | Structured editorial field. |
| `hearing_date` | string | Structured editorial field. |
| `judgment_date` | string | Structured editorial field. |
| `counsel_and_appearances` | string | Structured editorial field. |
| `subject_area` | string | Structured editorial field. |
| `catchwords_flynote` | string | Structured editorial field. |
| `headnote` | string | Structured editorial field. |
| `facts` | string | Structured editorial field. |
| `issues_for_determination` | string | Structured editorial field. |
| `legal_principles` | string | Structured editorial field. |
| `held_decision_points` | string | Structured editorial field. |
| `ratio_decidendi` | string | Structured editorial field. |
| `obiter_dicta_where_relevant` | string | Structured editorial field. |
| `cases_referred_to` | string | Structured editorial field. |
| `legislation_considered` | string | Structured editorial field. |
| `constitutional_provisions_considered` | string | Structured editorial field. |
| `procedural_history` | string | Structured editorial field. |
| `final_order` | string | Structured editorial field. |
| `full_formatted_judgment_text` | string | Full source text where available. |
| `reviewer_comments` | string | Editorial-review notes. |
| `approval_status` | string | Human approval status. |
| `export_history` | string | Export-history evidence. |
| `source_block_sha256` | string | SHA-256 of the canonical source block. |
| `source_block_text` | string | Preserved structured source block. |
| `canonical_identity` | string | Deterministic court/judgment identity used for deduplication. |
| `record_id` | string | Stable record identifier. |
| `source_occurrences` | array<object> | Source blocks merged into the canonical record. |
| `source_occurrence_count` | integer | Number of source occurrences. |
| `duplicate_detected` | boolean | True when multiple source occurrences were retained. |
| `record_sha256` | string | SHA-256 of the canonical normalized record excluding this field. |
| `dataset_row_number` | integer | Contiguous dataset row number. |
| `judgment_number_prefix` | string | Derived judgment-number component. |
| `judgment_number_int` | integer or null | Derived judgment-number component. |
| `subject_area_terms` | array<string> | Derived discovery terms. |
| `cases_referred_to_terms` | array<string> | Derived discovery terms. |
| `legislation_considered_terms` | array<string> | Derived discovery terms. |
| `constitutional_provisions_considered_terms` | array<string> | Derived discovery terms. |
