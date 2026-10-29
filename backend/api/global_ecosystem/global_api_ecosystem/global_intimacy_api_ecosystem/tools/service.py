"""Catalog of safety and diagnostic tools for the relationship/intimacy ecosystem."""
from copy import deepcopy
from typing import Any

_ENTRIES: tuple[dict[str, Any], ...] = (
    {"tool_id":"provider_policy_readiness","name":"Provider Policy Readiness Checklist","description":"Manual checklist to verify official API availability, adult-content terms, jurisdiction, and provider restrictions.","safety_critical":True,"implementation_status":"CATALOG_ONLY"},
    {"tool_id":"age_consent_safety_checklist","name":"Age, Consent, and Rights Checklist","description":"Workflow checklist for documenting age assurance, participant consent, content rights, and reporting pathways.","safety_critical":True,"implementation_status":"CATALOG_ONLY"},
    {"tool_id":"privacy_security_review","name":"Privacy and Security Review","description":"Checklist for data minimization, access control, retention, deletion, and security review.","safety_critical":True,"implementation_status":"CATALOG_ONLY"},
    {"tool_id":"provider_adapter_test_harness","name":"Provider Adapter Test Harness","description":"Planned non-production test harness for authorized provider API adapters and sanitized test data.","safety_critical":False,"implementation_status":"CATALOG_ONLY"},
    {"tool_id":"moderation_reporting_workflow","name":"Moderation and Reporting Workflow","description":"Catalog definition for user reporting, abuse escalation, rights complaints, and content removal workflows.","safety_critical":True,"implementation_status":"CATALOG_ONLY"},
)

def list_entries() -> list[dict[str, Any]]:
    """Return tool metadata; this is not an execution interface."""
    return deepcopy(list(_ENTRIES))
