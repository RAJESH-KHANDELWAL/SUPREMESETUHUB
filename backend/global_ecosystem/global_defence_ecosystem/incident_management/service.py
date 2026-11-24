"""Human-governed incident record state machine."""
from __future__ import annotations

_STATES = ("reported", "triaged", "assigned", "mitigating", "contained", "recovered", "closed")
_ALLOWED = {
    "reported": {"triaged"}, "triaged": {"assigned", "closed"},
    "assigned": {"mitigating", "closed"}, "mitigating": {"contained"},
    "contained": {"recovered"}, "recovered": {"closed"}, "closed": set(),
}

def incident_states() -> tuple[str, ...]:
    return _STATES

def create_incident_record(incident_id: str, category: str, reported_by: str) -> dict[str, str]:
    if not all(str(v).strip() for v in (incident_id, category, reported_by)):
        raise ValueError("incident_id, category and reported_by are required")
    return {"incident_id": incident_id.strip(), "category": category.strip(),
            "reported_by": reported_by.strip(), "state": "reported"}

def transition_incident(record: dict[str, str], next_state: str, approved_by: str) -> dict[str, str]:
    current = record.get("state", "")
    if next_state not in _ALLOWED.get(current, set()):
        raise ValueError(f"Invalid incident transition: {current} -> {next_state}")
    if not approved_by.strip():
        raise ValueError("A named human approver is required")
    updated = dict(record)
    updated["state"] = next_state
    updated["last_approved_by"] = approved_by.strip()
    return updated
