"""Incident classification and response checklist generation."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Incident:
    incident_id: str
    category: str
    impact: str
    confirmed: bool = False
def assess_incident(incident):
    if not incident.incident_id.strip(): raise ValueError("incident_id is required")
    if incident.category not in {"account_compromise", "malware", "data_exposure", "service_disruption", "phishing", "policy_violation", "unknown"}: raise ValueError("unsupported incident category")
    if incident.impact not in {"critical", "high", "medium", "low"}: raise ValueError("invalid impact")
    steps=["preserve relevant logs and evidence", "assign incident owner", "record timeline and affected assets"]
    if incident.confirmed: steps += ["follow approved containment plan", "notify required stakeholders", "validate recovery and monitor recurrence"]
    else: steps += ["triage and verify indicators before disruptive action"]
    return tuple(steps)
