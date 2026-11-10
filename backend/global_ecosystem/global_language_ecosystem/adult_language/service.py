"""Safety-first metadata helpers for lawful adult language contexts.

This module does not generate or host sexual content, verify age, or moderate
real content. Those require dedicated audited services and jurisdiction review.
"""
from dataclasses import dataclass

_ALLOWED_CATEGORIES = {
    "sexual_health_education", "adult_relationship_education",
    "adult_content_translation", "adult_entertainment_metadata",
    "consent_and_safety_information",
}

@dataclass(frozen=True)
class AdultLanguageContext:
    category: str
    adults_only: bool
    age_assurance_required: bool = True
    consent_confirmed: bool = False
    privacy_reviewed: bool = False
    jurisdiction_reviewed: bool = False


def classify_adult_language_request(category: str) -> str:
    key = category.strip().lower().replace("-", "_").replace(" ", "_")
    if key not in _ALLOWED_CATEGORIES:
        raise ValueError(f"unsupported adult-language category: {category}")
    return key


def validate_adult_content_context(context: AdultLanguageContext) -> tuple[str, ...]:
    findings: list[str] = []
    if context.category not in _ALLOWED_CATEGORIES:
        findings.append("category_not_allowed")
    if not context.adults_only:
        findings.append("adults_only_scope_required")
    if not context.age_assurance_required:
        findings.append("age_assurance_policy_required")
    if not context.consent_confirmed:
        findings.append("consent_confirmation_required")
    if not context.privacy_reviewed:
        findings.append("privacy_review_required")
    if not context.jurisdiction_reviewed:
        findings.append("jurisdiction_review_required")
    return tuple(findings)
