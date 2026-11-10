"""Defensive cyber hygiene and incident-readiness metadata."""
from __future__ import annotations

_CONTROLS = frozenset({
    "asset_inventory", "secure_configuration", "identity_mfa", "patch_management",
    "backup_recovery", "centralized_logging", "endpoint_protection",
    "vulnerability_management", "incident_response_plan", "security_training"
})

def defensive_controls() -> tuple[str, ...]:
    return tuple(sorted(_CONTROLS))

def assess_control_coverage(implemented: list[str] | tuple[str, ...]) -> dict[str, object]:
    present = set(implemented) & _CONTROLS
    missing = _CONTROLS - present
    return {
        "implemented": tuple(sorted(present)),
        "missing": tuple(sorted(missing)),
        "coverage_ratio": len(present) / len(_CONTROLS),
        "assessment_only": True,
    }
