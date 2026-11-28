"""Human Language CORE policy guardrails; not provider authorization."""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any

SENSITIVE_KEYS = frozenset({
    "api_key", "access_token", "refresh_token", "client_secret", "token",
    "secret", "password", "private_key", "authorization", "email", "phone",
    "mobile", "address", "date_of_birth", "government_id", "passport_number",
    "aadhaar_number", "pan_number",
})
SENSITIVE_CAPABILITY_MARKERS = ("ADMIN", "DELETE", "WRITE", "PUBLISH", "BILLING", "CREDENTIAL")


class HumanLanguagePolicyError(PermissionError):
    """Raised when a Core metadata policy boundary is not satisfied."""


def redact_sensitive_metadata(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {
            str(key): redact_sensitive_metadata(item)
            for key, item in value.items()
            if str(key).casefold() not in SENSITIVE_KEYS
        }
    if isinstance(value, list):
        return [redact_sensitive_metadata(item) for item in value]
    if isinstance(value, tuple):
        return tuple(redact_sensitive_metadata(item) for item in value)
    return deepcopy(value)


def require_tenant_context(context: Any) -> None:
    if context is None or not callable(getattr(context, "validate", None)):
        raise HumanLanguagePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
    try:
        context.validate()
    except (TypeError, ValueError) as exc:
        raise HumanLanguagePolicyError(str(exc)) from exc


def validate_capability(provider: dict[str, Any], capability: str) -> None:
    if not provider.get("enabled", True):
        raise HumanLanguagePolicyError("PROVIDER_MODULE_DISABLED")
    if capability not in set(provider.get("capabilities", [])):
        raise HumanLanguagePolicyError("CAPABILITY_NOT_REGISTERED")
    # Passing this check does not prove provider credentials, consent, API access or entitlement.


def classify_capability(capability: str) -> str:
    upper = capability.upper()
    if any(marker in upper for marker in SENSITIVE_CAPABILITY_MARKERS):
        return "SENSITIVE_REQUIRES_EXPLICIT_APPLICATION_AUTHORIZATION"
    return "STANDARD_REQUIRES_TENANT_AUTHORIZATION"


def safe_provider_summary(provider: dict[str, Any]) -> dict[str, Any]:
    return redact_sensitive_metadata(provider)


def adult_content_policy() -> dict[str, Any]:
    return {
        "age_restricted": True,
        "verified_adults_only": True,
        "informed_consent_required": True,
        "content_rights_required": True,
        "regional_legal_review_required": True,
        "moderation_and_takedown_required": True,
        "prohibited": [
            "sexual content involving minors",
            "non-consensual intimate imagery",
            "coercion",
            "trafficking",
            "exploitation",
            "illegal sexual content",
        ],
    }
