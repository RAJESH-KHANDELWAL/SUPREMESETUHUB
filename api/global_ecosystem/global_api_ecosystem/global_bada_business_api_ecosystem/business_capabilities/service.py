"""Service layer for Bada Business API capability contracts."""
from .registry import (
    get_analytics_contract,
    get_compliance_framework,
    list_lifecycle_stages,
    list_trust_safety_controls,
    validate_capability_registry,
)

def get_lifecycle():
    stages = list_lifecycle_stages()
    return {"success": True, "count": len(stages), "stages": stages, "coverage": "idea_to_closure"}

def get_trust_safety():
    controls = list_trust_safety_controls()
    return {
        "success": True,
        "count": len(controls),
        "status": "framework_only",
        "controls": controls,
        "note": "These are control definitions; identity checks, fraud detection and moderation are not represented as operational until connected to verified evidence and review workflows.",
    }

def get_compliance():
    return {"success": True, **get_compliance_framework()}

def get_business_intelligence():
    return {"success": True, **get_analytics_contract()}

def get_capability_integrity():
    result = validate_capability_registry()
    return {"success": result["valid"], **result}
