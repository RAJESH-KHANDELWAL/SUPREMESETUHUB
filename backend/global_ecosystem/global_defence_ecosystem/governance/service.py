"""Governance checks for lawful, accountable defence-adjacent projects."""
from __future__ import annotations

CONTROLS = frozenset({
    "documented_purpose", "legal_authority", "human_accountability",
    "privacy_impact_review", "independent_audit", "incident_reporting",
    "data_retention_policy", "civilian_safeguards"
})

def governance_controls() -> tuple[str, ...]:
    return tuple(sorted(CONTROLS))

def check_governance(controls: list[str] | tuple[str, ...]) -> dict[str, object]:
    supplied = set(controls)
    unknown = supplied - CONTROLS
    missing = CONTROLS - supplied
    return {"complete": not missing and not unknown,
            "present": tuple(sorted(supplied & CONTROLS)),
            "missing": tuple(sorted(missing)),
            "unknown": tuple(sorted(unknown)),
            "human_approval_required": True}
