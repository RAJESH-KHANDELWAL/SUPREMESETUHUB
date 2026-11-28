"""Manager utilities for the Global Legal Service Work Business Core Ecosystem."""

from __future__ import annotations

from typing import Any

SERVICE_DOMAINS = (
    "legal_consultation_and_advisory",
    "advocacy_and_litigation",
    "corporate_and_commercial_law",
    "contracts_and_documentation",
    "dispute_resolution_mediation_arbitration",
    "intellectual_property_services",
    "tax_labour_property_and_family_law",
    "legal_research_and_paralegal_support",
    "legal_technology_and_online_platforms",
    "compliance_and_case_management",
)


def ecosystem_manifest() -> dict[str, Any]:
    """Return the service-business ecosystem manifest."""
    return {
        "name": "global_legal_service_work_business_core_ecosystem",
        "layer": "global_bada_business_core_ecosystem",
        "service_domains": list(SERVICE_DOMAINS),
        "regulated_activity_notice": (
            "Regulated legal work must be performed by appropriately "
            "authorized professionals in the relevant jurisdiction."
        ),
    }


def validate_service_record(record: dict[str, Any]) -> list[str]:
    """Return missing or invalid fields for a legal-service provider record."""
    errors: list[str] = []
    for field in ("provider_name", "service_domain", "jurisdiction"):
        if not isinstance(record.get(field), str) or not record[field].strip():
            errors.append(f"{field} is required")
    if record.get("service_domain") and record["service_domain"] not in SERVICE_DOMAINS:
        errors.append("service_domain is not a recognized legal service domain")
    return errors
