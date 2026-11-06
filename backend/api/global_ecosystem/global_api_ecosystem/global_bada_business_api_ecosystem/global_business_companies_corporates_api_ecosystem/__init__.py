"""Global Businesses, Companies & Corporates domain adapter."""
from .catalog import get_category, list_categories
from .service import DomainService

__all__ = ["get_category", "list_categories", "DomainService"]
