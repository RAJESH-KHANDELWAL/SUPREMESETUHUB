"""Domain governance: validation, evidence grading and publication safeguards."""
from __future__ import annotations
from typing import Any

ALLOWED_CONFIDENCE = {"HIGH", "MEDIUM", "LOW", "UNASSESSED"}
ALLOWED_PUBLICATION = {"DRAFT", "REVIEW", "APPROVED", "RESTRICTED", "REJECTED"}

def validate_cultural_record(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in ("record_id", "domain_id", "title", "content", "source_kind", "confidence"):
        if not str(record.get(field, "")).strip():
            errors.append(f"MISSING:{field}")
    confidence = str(record.get("confidence", "UNASSESSED")).upper()
    if confidence not in ALLOWED_CONFIDENCE:
        errors.append("INVALID:confidence")
    status = str(record.get("publication_status", "DRAFT")).upper()
    if status not in ALLOWED_PUBLICATION:
        errors.append("INVALID:publication_status")
    if status == "APPROVED" and not record.get("source_url") and not record.get("metadata", {}).get("source_references"):
        errors.append("APPROVED_REQUIRES_SOURCE_REFERENCE")
    return errors

def assess_evidence(items: list[dict[str, Any]]) -> dict[str, Any]:
    usable = [item for item in items if item.get("reference") and item.get("source_kind")]
    return {"evidence_count": len(items), "usable_reference_count": len(usable),
            "assessment": "SUPPORTED_FOR_REVIEW" if usable else "INSUFFICIENT_EVIDENCE",
            "limitations": ["Evidence count alone does not establish historical truth.",
                            "Conflicting sources require explicit comparison."]}
