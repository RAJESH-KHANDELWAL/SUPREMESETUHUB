"""Non-operational civil-protection planning primitives."""
from __future__ import annotations

_CAPABILITIES = (
    "early_warning", "evacuation_accessibility_planning", "shelter_capacity",
    "medical_supply_logistics", "search_and_rescue_coordination",
    "public_information", "critical_service_recovery"
)

def emergency_capabilities() -> tuple[str, ...]:
    return _CAPABILITIES

def build_response_checklist(event_type: str) -> dict[str, object]:
    if not event_type.strip():
        raise ValueError("event_type is required")
    return {
        "event_type": event_type.strip(),
        "phases": ("prepare", "alert", "respond", "recover", "review"),
        "coordination": ("local_authority", "emergency_services", "health_services",
                         "utilities", "community_organizations"),
        "accessibility_required": True,
        "human_command_required": True,
    }
