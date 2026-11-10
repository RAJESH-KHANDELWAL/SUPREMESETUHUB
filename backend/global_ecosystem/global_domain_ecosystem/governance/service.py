"""Validate domain taxonomy metadata; this is not legal certification."""
from __future__ import annotations
from ..catalog import GEOGRAPHIC_SCOPES, MATURITY_LEVELS, DOMAIN_GROUPS

def validate_domain_profile(profile: dict) -> dict:
    errors = []
    if profile.get("geography", "bharat_india") not in GEOGRAPHIC_SCOPES:
        errors.append("unsupported_geographic_scope")
    if profile.get("maturity", "basic_normal") not in MATURITY_LEVELS:
        errors.append("unsupported_maturity_level")
    group = profile.get("group")
    domain_id = profile.get("domain_id")
    if group not in DOMAIN_GROUPS:
        errors.append("unknown_domain_group")
    elif domain_id not in DOMAIN_GROUPS[group]:
        errors.append("domain_not_registered_in_group")
    if profile.get("adult_only"):
        required = {"age_assurance", "informed_consent", "privacy_controls", "moderation", "takedown_process"}
        missing = sorted(required - set(profile.get("controls", ())))
        if missing:
            errors.append("adult_safety_controls_missing:" + ",".join(missing))
    return {"valid": not errors, "errors": errors, "status": "METADATA_VALIDATION_ONLY"}

__all__ = ["validate_domain_profile"]
