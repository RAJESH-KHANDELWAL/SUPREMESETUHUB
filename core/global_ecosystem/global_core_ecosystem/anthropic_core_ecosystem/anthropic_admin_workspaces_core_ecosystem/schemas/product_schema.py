"""Minimal product manifest validation."""
REQUIRED=("provider","product_id","product_name","category","availability")

def validate(manifest: dict) -> bool:
    missing=[key for key in REQUIRED if not manifest.get(key)]
    if missing:
        raise ValueError("missing: "+", ".join(missing))
    if manifest["provider"]!="anthropic":
        raise ValueError("provider mismatch")
    if manifest.get("live_connection") is True:
        raise ValueError("Core catalog cannot assert a live provider connection")
    return True
