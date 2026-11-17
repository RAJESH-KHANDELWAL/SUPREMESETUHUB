"""Rule-based safety checks for civil and defensive technology use cases."""
from __future__ import annotations

REQUIRED_SAFEGUARDS = frozenset({
    "human_oversight", "audit_logging", "legal_review", "data_minimization"
})
DISALLOWED_PURPOSE_TERMS = frozenset({
    "autonomous lethal", "target prioritization for attack", "weapon release",
    "mass civilian surveillance", "population coercion"
})

def validate_safeguards(safeguards: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    present = set(safeguards)
    return tuple(sorted(REQUIRED_SAFEGUARDS - present))

def evaluate_use_case(purpose: str, safeguards: tuple[str, ...] | list[str]) -> dict[str, object]:
    normalized = purpose.casefold()
    prohibited = next((term for term in DISALLOWED_PURPOSE_TERMS if term in normalized), None)
    missing = validate_safeguards(safeguards)
    return {
        "allowed_for_catalogue": prohibited is None and not missing,
        "prohibited_match": prohibited,
        "missing_safeguards": missing,
        "requires_human_review": True,
    }
