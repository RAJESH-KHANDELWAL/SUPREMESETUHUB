"""Bharat-to-global defence, civil-protection and resilience domain package.

This package provides catalogue and planning metadata. Operational command,
weapons control, surveillance, and live infrastructure integrations are out
of scope; runtime ownership remains with the repository's canonical layers.
"""
from .catalog import DefenceCapability, list_capability_groups, is_prohibited_automation
from .models import DefenceUseCase
from .registry import DefenceUseCaseRegistry
from .risk import evaluate_use_case, validate_safeguards
from .civil_protection import emergency_capabilities, build_response_checklist
from .cyber_defence import defensive_controls, assess_control_coverage
from .readiness import assess_readiness
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
    "assess_readiness",
]
