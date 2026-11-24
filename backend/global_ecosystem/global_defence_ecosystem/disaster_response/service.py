"""High-level disaster response planning; no tactical or dispatch control."""
from __future__ import annotations

PHASES = ("mitigation", "preparedness", "response", "recovery")
RESOURCE_TYPES = ("shelter", "food_water", "medical_supplies", "transport",
                  "communications", "accessible_support", "clean_up")

def response_phases() -> tuple[str, ...]:
    return PHASES

def build_resource_plan(event_type: str, population_estimate: int) -> dict[str, object]:
    if not event_type.strip():
        raise ValueError("event_type is required")
    if not isinstance(population_estimate, int) or population_estimate < 0:
        raise ValueError("population_estimate must be a non-negative integer")
    return {
        "event_type": event_type.strip(),
        "population_estimate": population_estimate,
        "resource_categories": RESOURCE_TYPES,
        "needs_local_authority_validation": True,
        "needs_human_approval": True,
    }
