"""Verified user-approved scope decisions for the Global Bada Business API Ecosystem.

Only questions with a retrieved, explicit user answer are recorded here.
This file is a decision record, not proof that a capability is live or legally certified.
"""
from __future__ import annotations

APPROVED_REQUIREMENTS = (
    {
        "id": "Q10",
        "title": "One connected ecosystem with separate API modules",
        "decision": "YES",
        "requirement": "Maintain one connected Bada Business API ecosystem with distinct, consistently integrated modules and endpoints.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q11",
        "title": "India and global legal compliance",
        "decision": "YES",
        "requirement": "Support applicable country-specific laws, rules, licences, taxes, registrations, and compliance requirements.",
        "implementation_status": "framework_scaffolded_official_datasets_not_ingested",
    },
    {
        "id": "Q12",
        "title": "Verification, trust, safety, and anti-fraud",
        "decision": "YES",
        "requirement": "Provide verification, trust, safety, and anti-fraud controls for business/work listings and related information.",
        "implementation_status": "control_framework_scaffolded_not_operational_verification",
    },
    {
        "id": "Q14",
        "title": "Business lifecycle from idea to closure",
        "decision": "YES",
        "requirement": "Cover the business lifecycle from idea and validation through setup, launch, operations, growth, transition, and closure.",
        "implementation_status": "lifecycle_taxonomy_scaffolded",
    },
    {
        "id": "Q21",
        "title": "Business Intelligence and API analytics",
        "decision": "YES",
        "requirement": "Provide Business Intelligence and API analytics within the Bada Business ecosystem; other ecosystems retain analytics in their own folders.",
        "implementation_status": "analytics_contract_scaffolded_no_live_metrics_store",
    },
    {
        "id": "Q22",
        "title": "Standards and interoperability",
        "decision": "YES",
        "requirement": "Use recognised standards and interoperable contracts where applicable.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q23",
        "title": "Common architecture and response conventions",
        "decision": "YES",
        "requirement": "Use a consistent modular architecture and common API response conventions.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q24",
        "title": "Extensibility",
        "decision": "YES",
        "requirement": "Allow new business domains, modules, and integrations to be added without duplicating existing ownership or logic.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q25",
        "title": "Central integration and connectivity",
        "decision": "YES",
        "requirement": "Provide central integration within Bada Business while connecting external and sibling ecosystems through their owning APIs, without taking over their folders or duplicating their implementation.",
        "implementation_status": "provider_catalog_only_live_connections_unverified",
    },
    {
        "id": "Q26",
        "title": "Authorised and lawful APIs",
        "decision": "YES",
        "requirement": "Use external APIs only where access is authorised and permitted by provider terms and applicable law.",
        "implementation_status": "policy_recorded_provider_access_not_verified",
    },
    {
        "id": "Q27",
        "title": "Webhooks, events, and real-time integration",
        "decision": "YES",
        "requirement": "Support governed webhook, event-driven, and real-time integration patterns where supported by the authorised provider.",
        "implementation_status": "contract_scaffold_not_live",
    },
    {
        "id": "Q28",
        "title": "Standardised schemas",
        "decision": "YES",
        "requirement": "Use documented, versionable schemas and consistent data contracts across modules.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q29",
        "title": "Security, privacy, audit, and consent",
        "decision": "YES",
        "requirement": "Design for security, privacy, access control, auditability, and consent management.",
        "implementation_status": "requirements_recorded_controls_require_implementation_review",
    },
    {
        "id": "Q30",
        "title": "Jurisdictional controls",
        "decision": "YES",
        "requirement": "Apply country and jurisdiction-specific eligibility, legal, and compliance controls.",
        "implementation_status": "framework_scaffolded_official_datasets_not_ingested",
    },
    {
        "id": "Q31",
        "title": "Restricted adult-industry access",
        "decision": "YES",
        "requirement": "Keep lawful adult-industry areas separately classified and subject to age, jurisdiction, provider, and access restrictions; a catalogue flag alone is not age verification.",
        "implementation_status": "taxonomy_scaffolded_age_verification_not_implemented",
    },
    {
        "id": "Q32",
        "title": "API protocols",
        "decision": "YES",
        "requirement": "Use REST and other appropriate documented protocols according to the owning integration and technical requirements.",
        "implementation_status": "rest_routes_present_other_protocols_not_verified",
    },
    {
        "id": "Q33",
        "title": "Separate environments",
        "decision": "YES",
        "requirement": "Account for separate development, testing, staging, and production environments.",
        "implementation_status": "environment_configuration_not_verified",
    },
    {
        "id": "Q34",
        "title": "Mandatory tests, documentation, and CI",
        "decision": "YES",
        "requirement": "Require automated tests, implementation documentation, and CI checks for changes.",
        "implementation_status": "tests_present_ci_result_requires_verification",
    },
    {
        "id": "Q35",
        "title": "Versioning and backward compatibility",
        "decision": "YES",
        "requirement": "Version public API contracts and manage backward compatibility deliberately.",
        "implementation_status": "versioning_policy_scaffolded",
    },
)

APPROVED_SCOPE_CONSTRAINTS = (
    {
        "id": "SCOPE-API-ONLY",
        "decision": "Bada Business API work only; do not create a separate Bada Business platform or move this work into another ecosystem.",
    },
    {
        "id": "SCOPE-NO-AI-HERE",
        "decision": "AI and automation implementation is excluded from this folder; it belongs in its separately owned folder and may be reviewed later.",
    },
    {
        "id": "SCOPE-EDUCATION-IN-BADA",
        "decision": "Education and learning business APIs belong within this Bada Business API ecosystem.",
    },
    {
        "id": "SCOPE-FINANCE-EXTERNAL",
        "decision": "Banking and payment APIs remain in their separately owned API folders and are connected only through authorised external API contracts.",
    },
    {
        "id": "SCOPE-FOUR-ECOSYSTEM-BOUNDARIES",
        "decision": "Bada Business, Company/Companies, Platforms, and Organizations remain distinct ecosystems; this change modifies only Bada Business and must not duplicate or take over the other three.",
    },
    {
        "id": "SCOPE-BUSINESS-ANALYTICS",
        "decision": "Business Intelligence and Bada Business API analytics belong here; other ecosystems retain their own analytics in their own folders.",
    },
)

def list_approved_requirements() -> list[dict[str, str]]:
    """Return defensive copies of explicit approved decisions only."""
    return [dict(item) for item in APPROVED_REQUIREMENTS]

def list_scope_constraints() -> list[dict[str, str]]:
    """Return defensive copies of the user's explicit scope boundaries."""
    return [dict(item) for item in APPROVED_SCOPE_CONSTRAINTS]

def validate_approved_requirements() -> dict[str, object]:
    ids = [item["id"] for item in APPROVED_REQUIREMENTS]
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    invalid_decisions = sorted({item["id"] for item in APPROVED_REQUIREMENTS if item["decision"] != "YES"})
    missing_fields = sorted({
        item["id"] for item in APPROVED_REQUIREMENTS
        if not all(item.get(field) for field in ("id", "title", "decision", "requirement", "implementation_status"))
    })
    constraint_ids = [item["id"] for item in APPROVED_SCOPE_CONSTRAINTS]
    duplicate_constraint_ids = sorted({value for value in constraint_ids if constraint_ids.count(value) > 1})
    return {
        "valid": not duplicate_ids and not invalid_decisions and not missing_fields and not duplicate_constraint_ids,
        "count": len(APPROVED_REQUIREMENTS),
        "duplicate_ids": duplicate_ids,
        "invalid_decisions": invalid_decisions,
        "missing_fields": missing_fields,
        "scope_constraint_count": len(APPROVED_SCOPE_CONSTRAINTS),
        "duplicate_scope_constraint_ids": duplicate_constraint_ids,
        "unanswered_or_cancelled_questions_recorded_as_approved": [],
        "note": "Only explicitly retrieved user decisions are included. Q08, Q09, Q13, and unanswered Q15 are intentionally not represented as approved decisions. Registry integrity does not certify implementation or legal compliance.",
    }
