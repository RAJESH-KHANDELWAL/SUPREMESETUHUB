"""Minimal provider manifest validation for MICROSOFT LANGUAGE."""
REQUIRED = ("provider_id", "provider_key", "provider_name", "ecosystem_id", "category", "status")


def validate(manifest):
    missing = [field for field in REQUIRED if not manifest.get(field)]
    if missing:
        raise ValueError("PROVIDER_MANIFEST_FIELDS_REQUIRED: " + ", ".join(missing))
    if manifest["category"] != "HUMAN_LANGUAGE_PROVIDER":
        raise ValueError("PROVIDER_CATEGORY_MISMATCH")
    if manifest.get("live_connection") is not False:
        raise ValueError("LIVE_CONNECTION_REQUIRES_VERIFIED_IMPLEMENTATION")
    return True
