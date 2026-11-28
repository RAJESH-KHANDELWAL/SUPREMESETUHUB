"""Manager helpers for the government and private employment service-work business ecosystem."""

from __future__ import annotations

from typing import Any


ECOSYSTEM_ID = (
    "global_government_private_jobs_careers_employment_"
    "service_work_business_core_ecosystem"
)

SERVICE_DOMAINS = (
    "government_employment_services",
    "private_sector_recruitment",
    "staffing_and_placement",
    "executive_search",
    "recruitment_and_job_portals",
    "career_guidance_and_counselling",
    "resume_and_interview_services",
    "human_resources_and_payroll",
    "workforce_management",
    "employer_branding",
    "internships_and_apprenticeships",
    "freelancing_and_gig_work",
    "remote_and_hybrid_work",
    "outsourcing_and_bpo",
    "reskilling_and_outplacement",
    "employment_compliance",
    "professional_networking",
)


def ecosystem_manifest() -> dict[str, Any]:
    """Return the stable identity and scope of this business ecosystem."""
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "layer": "global_bada_business_core_ecosystem",
        "audience": ["government", "private_sector", "service_providers", "employers", "workers"],
        "service_domains": list(SERVICE_DOMAINS),
    }


def validate_service_record(record: dict[str, Any]) -> list[str]:
    """Return validation errors for a service or employment-business record."""
    errors: list[str] = []
    for field in ("service_id", "service_name", "service_domain", "provider_type"):
        if not record.get(field):
            errors.append(f"missing_required_field:{field}")

    if record.get("provider_type") not in (None, "government", "private", "public_private_partnership", "nonprofit"):
        errors.append("invalid_provider_type")

    if record.get("service_domain") and record["service_domain"] not in SERVICE_DOMAINS:
        errors.append("unknown_service_domain")

    return errors
