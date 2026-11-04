"""Explicit Bada Business API capability contracts.

These are API contracts and workflow taxonomies. They do not claim that
verification, legal review, analytics storage, or external integrations are live.
"""
from __future__ import annotations
from copy import deepcopy

BUSINESS_LIFECYCLE_STAGES = (
    {"id": "idea", "name": "Idea", "sequence": 1, "description": "Capture the business idea, problem, audience and proposed value."},
    {"id": "validation", "name": "Validation", "sequence": 2, "description": "Assess demand, feasibility, competition, risks and business model."},
    {"id": "planning", "name": "Planning", "sequence": 3, "description": "Prepare business plan, resources, funding, operating model and milestones."},
    {"id": "registration_compliance", "name": "Registration and Compliance", "sequence": 4, "description": "Identify required entity registrations, licences, tax registrations and jurisdictional obligations."},
    {"id": "setup", "name": "Setup", "sequence": 5, "description": "Set up people, premises, systems, suppliers, services and operating processes."},
    {"id": "launch", "name": "Launch", "sequence": 6, "description": "Start lawful business operations and publish approved business information."},
    {"id": "operations", "name": "Operations", "sequence": 7, "description": "Manage customers, products, services, employees, suppliers and ongoing obligations."},
    {"id": "growth", "name": "Growth", "sequence": 8, "description": "Support expansion, market entry, partnerships, investment and performance improvement."},
    {"id": "transition", "name": "Transition", "sequence": 9, "description": "Manage ownership, succession, restructuring, sale or other lawful transition."},
    {"id": "closure", "name": "Closure", "sequence": 10, "description": "Track closure, deregistration, tax and filing obligations, contracts and record retention."},
)

TRUST_SAFETY_CONTROLS = (
    {"id": "business_identity", "name": "Business identity verification", "scope": "Identity and ownership evidence for business profiles", "status": "framework_only"},
    {"id": "registration_licence", "name": "Registration and licence checks", "scope": "Jurisdiction-specific registration and licence evidence", "status": "framework_only"},
    {"id": "employer_job", "name": "Employer and job verification", "scope": "Employer identity, vacancy authenticity and suspicious recruitment patterns", "status": "framework_only"},
    {"id": "product_service", "name": "Product and service checks", "scope": "Provider identity, listing consistency, prohibited claims and safety flags", "status": "framework_only"},
    {"id": "fraud_scam_reporting", "name": "Fraud and scam reporting", "scope": "User reports, evidence references, review status and audit trail", "status": "framework_only"},
    {"id": "misinformation_review", "name": "Misleading information review", "scope": "Evidence-backed review and correction workflow", "status": "framework_only"},
)

COMPLIANCE_RECORD_REQUIRED_FIELDS = (
    "jurisdiction_code",
    "jurisdiction_name",
    "business_activity_code",
    "obligation_type",
    "obligation_name",
    "issuing_authority",
    "official_source_url",
    "effective_from",
    "effective_to",
    "last_verified_at",
    "verification_method",
    "record_status",
)

ANALYTICS_EVENT_FIELDS = (
    "event_id",
    "event_type",
    "occurred_at",
    "ecosystem_id",
    "module_id",
    "api_route",
    "api_version",
    "environment",
    "request_correlation_id",
    "actor_type",
    "jurisdiction_code",
    "outcome",
    "duration_ms",
)

ANALYTICS_CAPABILITIES = (
    {"id": "api_usage", "name": "API usage and endpoint analytics", "status": "contract_only"},
    {"id": "catalog_discovery", "name": "Business and industry catalogue discovery", "status": "contract_only"},
    {"id": "lifecycle_progress", "name": "Business lifecycle progress analytics", "status": "contract_only"},
    {"id": "trust_safety_operations", "name": "Trust and safety operations analytics", "status": "contract_only"},
    {"id": "compliance_coverage", "name": "Jurisdictional compliance coverage analytics", "status": "contract_only"},
)

def _copies(items):
    return deepcopy(list(items))

def list_lifecycle_stages():
    return _copies(BUSINESS_LIFECYCLE_STAGES)

def list_trust_safety_controls():
    return _copies(TRUST_SAFETY_CONTROLS)

def get_compliance_framework():
    return {
        "framework_status": "schema_scaffold_official_jurisdiction_datasets_not_ingested",
        "coverage_claim": "none",
        "jurisdiction_records": [],
        "required_record_fields": list(COMPLIANCE_RECORD_REQUIRED_FIELDS),
        "validation_rules": [
            "Use an official government or regulator source for each legal obligation.",
            "Record jurisdiction, business activity, issuing authority, effective dates and last verification time.",
            "Do not mark a legal obligation verified without a traceable official source and review evidence.",
            "Do not treat one country's rules as applicable to every country.",
            "Escalate ambiguous or conflicting requirements for qualified local legal review.",
        ],
        "note": "This endpoint defines the data contract only. It does not provide legal advice or claim that India or worldwide legal datasets have been ingested or verified.",
    }

def get_analytics_contract():
    return {
        "analytics_status": "event_contract_only_no_live_metrics_store",
        "capabilities": _copies(ANALYTICS_CAPABILITIES),
        "event_fields": list(ANALYTICS_EVENT_FIELDS),
        "privacy_controls": [
            "Do not place passwords, API keys, payment credentials or unnecessary personal data in analytics events.",
            "Use pseudonymous actor references and request correlation IDs where appropriate.",
            "Apply role-based access, retention limits and jurisdictional privacy requirements before storing analytics.",
        ],
        "ownership": "Bada Business API analytics only; other ecosystems own their analytics in their respective folders.",
    }

def validate_capability_registry():
    stage_ids = [item["id"] for item in BUSINESS_LIFECYCLE_STAGES]
    trust_ids = [item["id"] for item in TRUST_SAFETY_CONTROLS]
    analytics_ids = [item["id"] for item in ANALYTICS_CAPABILITIES]
    return {
        "valid": (
            len(stage_ids) == len(set(stage_ids))
            and len(trust_ids) == len(set(trust_ids))
            and len(analytics_ids) == len(set(analytics_ids))
            and [item["sequence"] for item in BUSINESS_LIFECYCLE_STAGES] == list(range(1, len(BUSINESS_LIFECYCLE_STAGES) + 1))
        ),
        "lifecycle_stage_count": len(stage_ids),
        "trust_control_count": len(trust_ids),
        "analytics_capability_count": len(analytics_ids),
        "compliance_required_field_count": len(COMPLIANCE_RECORD_REQUIRED_FIELDS),
        "live_verification_enabled": False,
        "legal_datasets_verified": False,
        "analytics_store_enabled": False,
    }
