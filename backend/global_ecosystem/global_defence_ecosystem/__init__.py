"""Bharat-to-global defence, civil-protection and resilience domain package."""
from .catalog import DefenceCapability, list_capability_groups, is_prohibited_automation
from .models import DefenceUseCase
from .registry import DefenceUseCaseRegistry
from .risk import evaluate_use_case, validate_safeguards
from .civil_protection import emergency_capabilities, build_response_checklist
from .cyber_defence import defensive_controls, assess_control_coverage
from .readiness import assess_readiness
from .disaster_response import response_phases, build_resource_plan
from .emergency_communications import communication_channels, build_message_record
from .infrastructure_resilience import infrastructure_sectors, assess_dependencies
from .governance import governance_controls, check_governance
from .regional import regional_profiles, resolve_region
from .incident_management import incident_states, create_incident_record, transition_incident
from .training import exercise_types, build_exercise_plan
from .logistics import resource_categories, build_supply_request
from ..domain_registry import get_domain_profile

_DOMAIN_ID = __name__.rsplit(".", 1)[-1]
DOMAIN_PROFILE = get_domain_profile(_DOMAIN_ID)

def get_profile() -> dict:
    """Return this package's detached shared domain profile."""
    if DOMAIN_PROFILE is None:
        raise RuntimeError(f"No registered domain profile for {_DOMAIN_ID}")
    return get_domain_profile(_DOMAIN_ID)

__all__ = [
    "DOMAIN_PROFILE", "get_profile", "DefenceCapability", "DefenceUseCase",
    "DefenceUseCaseRegistry", "list_capability_groups", "is_prohibited_automation",
    "evaluate_use_case", "validate_safeguards", "emergency_capabilities",
    "build_response_checklist", "defensive_controls", "assess_control_coverage",
    "assess_readiness", "response_phases", "build_resource_plan",
    "communication_channels", "build_message_record", "infrastructure_sectors",
    "assess_dependencies", "governance_controls", "check_governance",
    "regional_profiles", "resolve_region", "incident_states",
    "create_incident_record", "transition_incident", "exercise_types",
    "build_exercise_plan", "resource_categories", "build_supply_request",
]
