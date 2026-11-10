"""Fail-closed policy checks for sensitive AI use contexts.

These checks are guardrail inputs, not a substitute for legal review, provider
moderation, age assurance, consent verification, or a complete safety system.
"""
from __future__ import annotations

from typing import Any


_POLICY_CATALOG: tuple[dict[str, Any], ...] = (
    {"id": "privacy_by_design", "requirements": ["data_minimization", "purpose_limitation", "secret_redaction", "retention_controls"]},
    {"id": "human_oversight", "requirements": ["human_review_for_high_impact_decisions", "appeal_path", "auditability"]},
    {"id": "adult_only_content", "requirements": ["adults_only", "age_assurance", "informed_consent", "verified_rights", "no_minors", "no_nonconsensual_intimate_content", "no_exploitation"]},
    {"id": "safety_critical_systems", "requirements": ["qualified_oversight", "simulation_and_testing", "bounded_authority", "human_override"]},
    {"id": "regulated_domains", "requirements": ["jurisdiction_review", "professional_scope_limits", "applicable_regulatory_compliance"]},
)


def get_policy_catalog() -> tuple[dict[str, Any], ...]:
    return tuple({**item, "requirements": list(item["requirements"])} for item in _POLICY_CATALOG)


def evaluate_use_context(
    *, domain: str, age_verified: bool = False, consent_confirmed: bool = False,
    rights_confirmed: bool = False, human_review_available: bool = False,
    purpose: str | None = None,
) -> dict[str, Any]:
    """Return missing safeguards; sensitive contexts fail closed by default."""
    normalized = domain.strip().lower()
    required: list[str] = []
    if normalized in {"adult", "adult_content", "adult_platform", "intimacy"}:
        required.extend(["age_verified", "consent_confirmed", "rights_confirmed"])
    if normalized in {"healthcare", "medical", "finance", "legal", "government", "safety_critical"}:
        required.append("human_review_available")
    values = {
        "age_verified": age_verified,
        "consent_confirmed": consent_confirmed,
        "rights_confirmed": rights_confirmed,
        "human_review_available": human_review_available,
    }
    missing = [key for key in required if not values[key]]
    if normalized in {"adult", "adult_content", "adult_platform", "intimacy"} and purpose not in {"education", "wellness", "lawful_adult_platform_safety"}:
        missing.append("permitted_purpose")
    return {
        "domain": normalized,
        "allowed_by_precheck": not missing,
        "missing_safeguards": missing,
        "requires_independent_policy_and_legal_review": normalized in {
            "adult", "adult_content", "adult_platform", "intimacy", "healthcare",
            "medical", "finance", "legal", "government", "safety_critical",
        },
    }
