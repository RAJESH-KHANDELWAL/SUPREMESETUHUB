"""User-approved requirements for the Global Bada Business API Ecosystem.

This registry records approved scope and acceptance decisions. It is not evidence
that every capability is already implemented, legally cleared, or live in production.
"""
from __future__ import annotations

APPROVED_REQUIREMENTS = (
    {
        "id": "Q08",
        "title": "Complete work and business facilities",
        "decision": "YES",
        "requirement": "Cover the full A-to-Z range of work and business facilities across the ecosystem.",
        "implementation_status": "requirements_recorded",
    },
    {
        "id": "Q09",
        "title": "Business knowledge and resources",
        "decision": "YES",
        "requirement": "Include business-related data, information, knowledge, research, and resources.",
        "implementation_status": "requirements_recorded",
    },
    {
        "id": "Q10",
        "title": "One connected ecosystem with separate API modules",
        "decision": "YES",
        "requirement": "Keep one connected Bada Business ecosystem with distinct, consistently integrated API modules and endpoints.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q11",
        "title": "India and global legal compliance",
        "decision": "YES",
        "requirement": "Account for applicable country-specific laws, licences, taxes, registrations, and compliance requirements.",
        "implementation_status": "requirements_recorded",
    },
    {
        "id": "Q12",
        "title": "Verification, trust, and anti-fraud",
        "decision": "YES",
        "requirement": "Support trust and verification controls addressing fake businesses, jobs, products, and services; scams, fraud, and misinformation.",
        "implementation_status": "requirements_recorded",
    },
    {
        "id": "Q13",
        "title": "AI and automation",
        "decision": "YES",
        "requirement": "Include AI-assisted and automation capabilities within lawful, authorized, and governed boundaries.",
        "implementation_status": "requirements_recorded",
    },
    {
        "id": "Q22",
        "title": "Standards and interoperability",
        "decision": "YES",
        "requirement": "Use recognised standards and interoperable contracts where applicable.",
        "implementation_status": "requirements_recorded",
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
        "requirement": "Provide a central integration approach for this ecosystem while connecting other ecosystems through their owning APIs rather than duplicating their work.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q26",
        "title": "Authorised and lawful APIs",
        "decision": "YES",
        "requirement": "Use APIs only where access is authorised and permitted by provider terms and applicable law.",
        "implementation_status": "requirements_recorded",
    },
    {
        "id": "Q27",
        "title": "Webhooks, events, and real-time integration",
        "decision": "YES",
        "requirement": "Support governed webhook, event-driven, and real-time integration patterns where supported.",
        "implementation_status": "requirements_recorded",
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
        "implementation_status": "requirements_recorded",
    },
    {
        "id": "Q30",
        "title": "Jurisdictional controls",
        "decision": "YES",
        "requirement": "Apply country and jurisdiction-specific eligibility, legal, and compliance controls.",
        "implementation_status": "requirements_recorded",
    },
    {
        "id": "Q31",
        "title": "Restricted adult-industry access",
        "decision": "YES",
        "requirement": "Keep lawful adult-industry areas separately classified and subject to age, jurisdiction, provider, and access restrictions; a catalogue flag alone is not age verification.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q32",
        "title": "API protocols",
        "decision": "YES",
        "requirement": "Use REST and other appropriate documented protocols according to the owning integration and technical requirements.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q33",
        "title": "Separate environments",
        "decision": "YES",
        "requirement": "Account for separate development, testing, staging, and production environments.",
        "implementation_status": "requirements_recorded",
    },
    {
        "id": "Q34",
        "title": "Mandatory tests, documentation, and CI",
        "decision": "YES",
        "requirement": "Require automated tests, implementation documentation, and CI checks for changes.",
        "implementation_status": "partially_scaffolded",
    },
    {
        "id": "Q35",
        "title": "Versioning and backward compatibility",
        "decision": "YES",
        "requirement": "Version public API contracts and manage backward compatibility deliberately.",
        "implementation_status": "partially_scaffolded",
    },
)

def list_approved_requirements() -> list[dict[str, str]]:
    """Return defensive copies of approved requirement records."""
    return [dict(item) for item in APPROVED_REQUIREMENTS]

def validate_approved_requirements() -> dict[str, object]:
    ids = [item["id"] for item in APPROVED_REQUIREMENTS]
    duplicate_ids = sorted({item for item in ids if ids.count(item) > 1})
    invalid_decisions = sorted({item["id"] for item in APPROVED_REQUIREMENTS if item["decision"] != "YES"})
    missing_fields = sorted({
        item["id"]
        for item in APPROVED_REQUIREMENTS
        if not all(item.get(field) for field in ("id", "title", "decision", "requirement", "implementation_status"))
    })
    return {
        "valid": not duplicate_ids and not invalid_decisions and not missing_fields,
        "count": len(APPROVED_REQUIREMENTS),
        "duplicate_ids": duplicate_ids,
        "invalid_decisions": invalid_decisions,
        "missing_fields": missing_fields,
        "note": "This validates the requirements registry only; it does not certify implementation, production readiness, provider connectivity, or legal compliance.",
    }
