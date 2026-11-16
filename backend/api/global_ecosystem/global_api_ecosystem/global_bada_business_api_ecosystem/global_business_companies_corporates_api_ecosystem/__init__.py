"""Global Businesses, Companies & Corporates domain adapter."""

INDUSTRY_ID = "business_companies_corporates"
INDUSTRY_NAME = "Businesses, Companies & Corporates"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .catalog import get_category, list_categories
from .service import DomainService

__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "get_category", "list_categories", "DomainService"]
