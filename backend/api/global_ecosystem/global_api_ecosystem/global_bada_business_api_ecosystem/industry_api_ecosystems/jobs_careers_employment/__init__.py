"""Jobs, Careers & Employment industry adapter package."""
INDUSTRY_ID = "jobs_careers_employment"
INDUSTRY_NAME = "Jobs, Careers & Employment"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_adapter"

from .service import JobsCareersService

__all__ = [
    "INDUSTRY_ID",
    "INDUSTRY_NAME",
    "COVERAGE",
    "CHANNELS",
    "STATUS",
    "JobsCareersService",
]
