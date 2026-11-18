def validate_payload(payload, required=()):
    if not hasattr(payload, "get"):
        return False, ("payload must be a mapping",)
    missing = tuple(key for key in required if key not in payload)
    return not missing, tuple(f"missing required field: {key}" for key in missing)
