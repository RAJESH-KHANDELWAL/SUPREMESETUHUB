"""Canonical source registry; classification data stays in its owning package."""
from .models import WorkBusinessSource

SOURCES = (
    WorkBusinessSource("universal_work_business", "Universal Work & Business A-Z Taxonomy",
        "global_universal_work_business_taxonomy_api_ecosystem", "SECTOR_AND_ACTIVITY"),
    WorkBusinessSource("freelance_gig_independent_work", "Freelancing, Gig & Independent Work",
        "global_freelancer_gig_independent_work_business_api_ecosystem", "INDEPENDENT_WORK_SPECIALIZATION"),
    WorkBusinessSource("jobs_careers_employment", "Jobs, Careers & Employment",
        "global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem",
        "EMPLOYMENT_CONTEXT"),
)

def list_sources():
    return [source.as_dict() for source in SOURCES]
