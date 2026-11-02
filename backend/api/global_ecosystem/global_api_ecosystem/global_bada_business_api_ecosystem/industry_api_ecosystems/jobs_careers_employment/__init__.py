"""Jobs, Careers & Employment industry API domain package."""
INDUSTRY_ID = "jobs_careers_employment"
INDUSTRY_NAME = "Jobs, Careers & Employment"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import JobsCareersService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "JobsCareersService"]
