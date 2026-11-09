"""Tools taxonomy for relationship, intimacy, and lawful adult-industry systems."""
from copy import deepcopy
from typing import Any

_ROWS: tuple[tuple[str, str, str, bool], ...] = (
    ("provider_policy_readiness","Provider API and Acceptable-Use Policy Review","Checklist for confirming official API docs, account access, allowed use, and provider restrictions.",True),
    ("age_assurance_review","Age Assurance and Age-Gating Review","Checklist to evaluate legal obligations, proportionality, privacy, and age-gating controls.",True),
    ("adult_status_records","Adult Status and Identity Record Workflow","Secure workflow design for verifying authorized adult participants without exposing unnecessary identity data.",True),
    ("consent_release_register","Consent and Release Register","Catalog definition for collecting, versioning, protecting, and revoking appropriate consent/release documentation.",True),
    ("content_rights_register","Content Rights and Copyright Register","Track ownership, licenses, creator permissions, takedown requests, and evidence retention.",True),
    ("nonconsensual_content_reporting","Non-Consensual Intimate Imagery Reporting","Workflow definition for reporting, urgent escalation, removal, preservation of necessary evidence, and appeal review.",True),
    ("minor_safety_enforcement","Minor-Safety and Exploitation Escalation","Safety control definition to prohibit sexual content involving minors and escalate suspected exploitation to appropriate processes.",True),
    ("content_moderation_review","Adult Content Moderation Review","Human-reviewed moderation and policy checks before publishing or distribution.",True),
    ("privacy_impact_assessment","Sensitive Data Privacy Impact Assessment","Assess collection, purpose, access, encryption, retention, deletion, and breach response for intimate data.",True),
    ("security_access_review","Access Control and Security Review","Review least privilege, admin access, secret storage, audit trails, and incident response.",True),
    ("payment_provider_eligibility","Adult-Merchant Payment Eligibility Checklist","Check processor underwriting and written acceptance before implementing a payment workflow.",True),
    ("hosting_policy_review","Hosting and CDN Policy Verification","Verify provider policy for lawful adult use and each product's terms before deployment.",True),
    ("publisher_terms_review","Adult Publisher and Distribution Terms Review","Compare age ratings, content policies, geographic restrictions, rights requirements, and API documentation.",True),
    ("relationship_provider_credentials","Relationship-Service Credential Checklist","Verify professional qualifications and local rules when listing therapeutic or clinical services.",True),
    ("sexual_health_content_review","Sexual-Health Information Review","Plan source quality, editorial review, disclaimers, and escalation to qualified care.",True),
    ("consumer_product_compliance","Adult Wellness Product Compliance Review","Check product safety, consumer information, shipping restrictions, and relevant market requirements.",True),
    ("moderation_reporting_workflow","Moderation, Reporting, and Appeal Workflow","Define user reports, escalation, transparent action logs, appeals, and complaint resolution.",True),
    ("provider_adapter_test_harness","Authorized Provider Adapter Test Harness","Planned test harness for permitted APIs, sandbox accounts, mocked responses, and sanitized data.",False),
    ("catalog_consistency_validator","Catalog Referential Integrity Validator","Validate unique IDs, category references, URL formats, and provider-to-category mapping consistency.",False),
    ("provider_status_audit","Provider Status and Freshness Audit","Review last-verification date, official documentation changes, and whether a connection is actually live.",False),
)

_ENTRIES: tuple[dict[str, Any], ...] = tuple(
    {
        "tool_id": tool_id,
        "name": name,
        "description": description,
        "safety_critical": safety_critical,
        "implementation_status": "CATALOG_ONLY",
    }
    for tool_id, name, description, safety_critical in _ROWS
)

def list_entries() -> list[dict[str, Any]]:
    """Return a copy of tool definitions; entries do not execute checks."""
    return deepcopy(list(_ENTRIES))
