"""Pure identifier normalization helpers."""
def normalize_capability_id(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("capability identifier must be a string")
    normalized = value.strip().casefold()
    if not normalized:
        raise ValueError("capability identifier must not be empty")
    return normalized
