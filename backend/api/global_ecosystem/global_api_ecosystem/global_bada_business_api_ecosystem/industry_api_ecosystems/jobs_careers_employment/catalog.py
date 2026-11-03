"""Aggregate view over independently owned Jobs, Careers & Employment categories."""
from __future__ import annotations
from copy import deepcopy
from .recruitment_and_job_portals.catalog import CATEGORY as RECRUITMENT_AND_JOB_PORTALS_CATEGORY
from .freelancing_and_gig_work.catalog import CATEGORY as FREELANCING_AND_GIG_WORK_CATEGORY
from .remote_and_hybrid_work.catalog import CATEGORY as REMOTE_AND_HYBRID_WORK_CATEGORY
from .staffing_and_placement.catalog import CATEGORY as STAFFING_AND_PLACEMENT_CATEGORY
from .human_resources_and_payroll.catalog import CATEGORY as HUMAN_RESOURCES_AND_PAYROLL_CATEGORY
from .career_guidance_and_counselling.catalog import CATEGORY as CAREER_GUIDANCE_AND_COUNSELLING_CATEGORY
from .internships_and_apprenticeships.catalog import CATEGORY as INTERNSHIPS_AND_APPRENTICESHIPS_CATEGORY
from .executive_search.catalog import CATEGORY as EXECUTIVE_SEARCH_CATEGORY
from .workforce_management.catalog import CATEGORY as WORKFORCE_MANAGEMENT_CATEGORY
from .resume_and_interview_services.catalog import CATEGORY as RESUME_AND_INTERVIEW_SERVICES_CATEGORY
from .employer_branding.catalog import CATEGORY as EMPLOYER_BRANDING_CATEGORY
from .employment_compliance.catalog import CATEGORY as EMPLOYMENT_COMPLIANCE_CATEGORY
from .outsourcing_and_bpo.catalog import CATEGORY as OUTSOURCING_AND_BPO_CATEGORY
from .reskilling_and_outplacement.catalog import CATEGORY as RESKILLING_AND_OUTPLACEMENT_CATEGORY
from .professional_networking.catalog import CATEGORY as PROFESSIONAL_NETWORKING_CATEGORY

JOBS_CAREERS_EMPLOYMENT_CATEGORIES = [
    RECRUITMENT_AND_JOB_PORTALS_CATEGORY,
    FREELANCING_AND_GIG_WORK_CATEGORY,
    REMOTE_AND_HYBRID_WORK_CATEGORY,
    STAFFING_AND_PLACEMENT_CATEGORY,
    HUMAN_RESOURCES_AND_PAYROLL_CATEGORY,
    CAREER_GUIDANCE_AND_COUNSELLING_CATEGORY,
    INTERNSHIPS_AND_APPRENTICESHIPS_CATEGORY,
    EXECUTIVE_SEARCH_CATEGORY,
    WORKFORCE_MANAGEMENT_CATEGORY,
    RESUME_AND_INTERVIEW_SERVICES_CATEGORY,
    EMPLOYER_BRANDING_CATEGORY,
    EMPLOYMENT_COMPLIANCE_CATEGORY,
    OUTSOURCING_AND_BPO_CATEGORY,
    RESKILLING_AND_OUTPLACEMENT_CATEGORY,
    PROFESSIONAL_NETWORKING_CATEGORY,
]

def list_categories() -> list[dict[str, object]]:
    """Return defensive copies of all independently maintained categories."""
    return deepcopy(JOBS_CAREERS_EMPLOYMENT_CATEGORIES)

def get_category(category_id: str) -> dict[str, object] | None:
    """Return one category by stable identifier."""
    for item in JOBS_CAREERS_EMPLOYMENT_CATEGORIES:
        if item["id"] == category_id:
            return deepcopy(item)
    return None
