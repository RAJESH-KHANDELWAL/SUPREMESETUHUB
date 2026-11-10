"""Bharat-to-global developer ecosystem namespace."""
from .catalog import DEVELOPER_DOMAINS, GEOGRAPHIC_SCOPES, MATURITY_LEVELS, get_catalog
from .models import DeveloperProject
from .registry import DeveloperProjectRegistry
from .governance import validate_project
from .adult_platforms import validate_adult_platform
from .adult_content_technology import get_adult_content_technology_blueprint
from .web_development import get_web_stack_blueprint
from .ai_development import get_ai_product_blueprint

__all__ = [
    "DEVELOPER_DOMAINS", "GEOGRAPHIC_SCOPES", "MATURITY_LEVELS", "get_catalog",
    "DeveloperProject", "DeveloperProjectRegistry", "validate_project",
    "validate_adult_platform", "get_adult_content_technology_blueprint",
    "get_web_stack_blueprint", "get_ai_product_blueprint",
]
