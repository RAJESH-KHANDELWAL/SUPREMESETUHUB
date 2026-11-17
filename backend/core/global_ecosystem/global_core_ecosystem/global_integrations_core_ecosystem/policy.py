"""Metadata safety helpers for integration catalogs."""
from collections.abc import Mapping
from copy import deepcopy

SENSITIVE_KEYS = frozenset({
    "token", "access_token", "refresh_token", "client_secret", "api_key",
    "secret", "authorization", "password", "credential", "credential_value",
    "private_key", "webhook_secret", "signing_secret", "cookie", "session",
    "email", "phone", "mobile", "address", "date_of_birth", "dob",
    "government_id", "passport_number", "aadhaar_number", "pan_number",
    "bank_account", "card_number",
})

def redact_sensitive_metadata(value):
    if isinstance(value, Mapping):
        return {str(key): redact_sensitive_metadata(item) for key, item in value.items()
                if str(key).lower() not in SENSITIVE_KEYS}
    if isinstance(value, list):
        return [redact_sensitive_metadata(item) for item in value]
    if isinstance(value, tuple):
        return tuple(redact_sensitive_metadata(item) for item in value)
    return deepcopy(value)

def validate_provider_reference(provider_id: str) -> bool:
    return isinstance(provider_id, str) and bool(provider_id.strip())
