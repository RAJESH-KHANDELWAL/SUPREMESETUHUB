"""Validation and safe redaction helpers for configuration data."""

SECRET_MARKERS = ("SECRET", "TOKEN", "PASSWORD", "API_KEY", "PRIVATE_KEY", "CREDENTIAL")


def is_secret_key(key):
    normalized = str(key).upper()
    return any(marker in normalized for marker in SECRET_MARKERS)


def redact_values(values):
    return {key: ("[REDACTED]" if is_secret_key(key) else value) for key, value in values.items()}


def validate_required(values, required_keys=()):
    return tuple(f"Missing required configuration: {key}" for key in required_keys if key not in values or values[key] in (None, ""))
