"""Declared System Core boundaries to sibling ecosystem layers.

These are dependency references only. This registry does not create live
connections or invoke provider APIs.
"""
INTEGRATION_BOUNDARIES = {
    "api": {"target": "backend/api/global_ecosystem/global_api_ecosystem", "purpose": "Provider control-plane APIs where available", "enabled": False},
    "security": {"target": "backend/core/global_ecosystem/global_core_ecosystem/global_security_core_ecosystem", "purpose": "Security policy and posture references", "enabled": False},
    "server": {"target": "backend/core/global_ecosystem/global_core_ecosystem/global_server_core_ecosystem", "purpose": "Host and server platform references", "enabled": False},
    "software": {"target": "backend/core/global_ecosystem/global_core_ecosystem/global_software_core_ecosystem", "purpose": "Software compatibility and lifecycle references", "enabled": False},
}


def list_integration_boundaries() -> list[dict[str, object]]:
    return [{"layer": key, **value} for key, value in INTEGRATION_BOUNDARIES.items()]
