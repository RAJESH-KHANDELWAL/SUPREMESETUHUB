"""People Life CORE policy guardrails; not legal, clinical or provider authorization."""
from __future__ import annotations
from collections.abc import Mapping
from copy import deepcopy
from typing import Any

SENSITIVE_KEYS = frozenset({
    "api_key","access_token","refresh_token","client_secret","token","secret","password",
    "private_key","authorization","email","phone","mobile","address","date_of_birth",
    "government_id","passport_number","aadhaar_number","pan_number","precise_location",
    "sexual_history","health_record","medical_record","intimate_image","biometric",
})
SENSITIVE_MARKERS = (
    "ADMIN","DELETE","WRITE","PUBLISH","BILLING","CREDENTIAL","PROFILE_EXPORT",
    "CONSENT","AGE","SEXUAL","MEDICAL","FINANCIAL","LEGAL","LOCATION","IDENTITY",
)

class PeopleLifePolicyError(PermissionError):
    """Raised when a People Life Core metadata request violates policy."""

def redact_sensitive_metadata(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(k):redact_sensitive_metadata(v) for k,v in value.items() if str(k).casefold() not in SENSITIVE_KEYS}
    if isinstance(value, list):
        return [redact_sensitive_metadata(v) for v in value]
    if isinstance(value, tuple):
        return tuple(redact_sensitive_metadata(v) for v in value)
    return deepcopy(value)

def require_tenant_context(context: Any) -> None:
    if context is None or not callable(getattr(context, "validate", None)):
        raise PeopleLifePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
    try:
        context.validate()
    except (TypeError, ValueError) as exc:
        raise PeopleLifePolicyError(str(exc)) from exc

def validate_capability(domain: dict[str, Any], capability: str, context: Any) -> None:
    if not domain.get("enabled", True):
        raise PeopleLifePolicyError("DOMAIN_DISABLED")
    if capability not in set(domain.get("capabilities", [])):
        raise PeopleLifePolicyError("CAPABILITY_NOT_REGISTERED")
    if domain.get("age_restricted"):
        if not bool(getattr(context, "verified_adult", False)):
            raise PeopleLifePolicyError("VERIFIED_ADULT_CONTEXT_REQUIRED")
        if not bool(getattr(context, "informed_consent", False)):
            raise PeopleLifePolicyError("INFORMED_CONSENT_REQUIRED")
        if not getattr(context, "jurisdiction", None):
            raise PeopleLifePolicyError("JURISDICTION_CONTEXT_REQUIRED")

def classify_capability(capability: str) -> str:
    return (
        "SENSITIVE_REQUIRES_EXPLICIT_APPLICATION_AUTHORIZATION"
        if any(marker in capability.upper() for marker in SENSITIVE_MARKERS)
        else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
    )

def safe_domain_summary(domain: dict[str, Any]) -> dict[str, Any]:
    return redact_sensitive_metadata(domain)

def adult_content_policy() -> dict[str, Any]:
    return {
        "age_restricted": True, "verified_adults_only": True,
        "informed_consent_required": True, "rights_and_licensing_required": True,
        "jurisdictional_legal_review_required": True, "privacy_by_design_required": True,
        "moderation_and_takedown_required": True,
        "prohibited": [
            "sexual content involving minors", "non-consensual intimate imagery",
            "coercion", "trafficking", "exploitation", "illegal sexual content",
            "non-consensual recording or distribution", "identity or age-document fraud",
        ],
        "warning": "Core metadata does not establish legal age, identity, consent, rights, clinical suitability or entitlement; independent lawful application controls are mandatory.",
    }
