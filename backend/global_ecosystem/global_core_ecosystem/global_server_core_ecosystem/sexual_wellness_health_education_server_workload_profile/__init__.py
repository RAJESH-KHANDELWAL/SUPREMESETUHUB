"""Read-only metadata access for Sexual Wellness and Health Education."""
import json
from pathlib import Path
_PROFILE = Path(__file__).with_name("workload_manifest.json")
def get_workload_manifest() -> dict:
    """Load this profile without network or provider operations."""
    with _PROFILE.open(encoding="utf-8") as stream:
        return json.load(stream)
def get_required_control_areas() -> tuple[str, ...]:
    return tuple(get_workload_manifest().get("required_control_areas", ()))
