"""Defence capability catalogue; metadata only, no weapons-control runtime."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Final

MATURITY_LEVELS: Final[tuple[str, ...]] = (
    "normal", "standard", "professional", "enterprise", "advanced", "supreme"
)
GEOGRAPHIC_SCOPES: Final[tuple[str, ...]] = (
    "india", "india_state", "india_district", "south_asia", "apac",
    "middle_east", "europe", "africa", "north_america", "latin_america", "global"
)
CAPABILITY_GROUPS: Final[dict[str, tuple[str, ...]]] = {
    "cyber_defence": ("asset_inventory", "vulnerability_management", "threat_intelligence",
                      "security_monitoring", "incident_response", "resilience_testing"),
    "physical_protection": ("perimeter_safety", "facility_access", "emergency_readiness",
                            "critical_infrastructure_resilience"),
    "disaster_response": ("early_warning", "search_and_rescue_coordination",
                          "shelter_logistics", "relief_supply_chain"),
    "maritime_and_aerospace_safety": ("situational_awareness", "navigation_safety",
                                      "search_and_rescue", "maintenance_readiness"),
    "public_sector": ("civil_defence", "continuity_of_government", "interagency_coordination"),
    "research_and_training": ("simulation", "readiness_assessment", "training_records"),
}
PROHIBITED_AUTOMATION: Final[tuple[str, ...]] = (
    "autonomous_target_selection", "autonomous_lethal_action",
    "weapon_release_control", "unlawful_surveillance", "civilian_harm_optimization"
)

@dataclass(frozen=True)
class DefenceCapability:
    capability_id: str
    group: str
    purpose: str
    maturity: str = "standard"
    geographic_scope: str = "india"
    requires_human_approval: bool = True

    def __post_init__(self) -> None:
        if self.group not in CAPABILITY_GROUPS:
            raise ValueError(f"Unknown capability group: {self.group}")
        if self.maturity not in MATURITY_LEVELS:
            raise ValueError(f"Unknown maturity level: {self.maturity}")
        if self.geographic_scope not in GEOGRAPHIC_SCOPES:
            raise ValueError(f"Unknown geographic scope: {self.geographic_scope}")
        if not self.capability_id.strip() or not self.purpose.strip():
            raise ValueError("capability_id and purpose are required")

def list_capability_groups() -> dict[str, tuple[str, ...]]:
    """Return a detached mapping of supported non-weapon capability groups."""
    return {key: tuple(value) for key, value in CAPABILITY_GROUPS.items()}

def is_prohibited_automation(capability_id: str) -> bool:
    """Identify explicitly excluded weapon/abuse automation categories."""
    return capability_id.strip().lower() in PROHIBITED_AUTOMATION
