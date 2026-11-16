"""Metadata-only policy checks for Global Developer Core."""
from __future__ import annotations

SECRET_KEY_PARTS = ("password", "secret", "token", "api_key", "private_key", "credential", "authorization")
ADULT_ONLY_PROVIDER_IDS = frozenset({
    "adult_creator_business", "adult_platform_discovery",
    "age_verification_consent", "sexual_wellness_education",
})
PROHIBITED_USE_CASES = frozenset({
    "sexual_content_involving_minors", "non_consensual_intimate_imagery",
    "coercion_exploitation_or_trafficking", "doxxing_or_private_data_exposure",
    "malware_or_unauthorized_access",
})

def find_secret_fields(value, prefix=""):
    found = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            if any(part in str(key).lower() for part in SECRET_KEY_PARTS):
                found.append(path)
            else:
                found.extend(find_secret_fields(child, path))
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            found.extend(find_secret_fields(child, f"{prefix}[{index}]"))
    return found

def validate_metadata(payload):
    if not isinstance(payload, dict):
        return {"allowed": False, "errors": ["payload_must_be_object"]}
    secret_fields = find_secret_fields(payload)
    return {"allowed": not secret_fields, "errors": ["secret_material_not_allowed"] if secret_fields else [], "secret_fields": secret_fields}

def adult_provider_enabled(provider_id, *, explicit_review=False, age_assurance_verified=False, consent_controls_verified=False, jurisdiction_reviewed=False):
    if provider_id not in ADULT_ONLY_PROVIDER_IDS:
        return True
    return bool(explicit_review and age_assurance_verified and consent_controls_verified and jurisdiction_reviewed)
