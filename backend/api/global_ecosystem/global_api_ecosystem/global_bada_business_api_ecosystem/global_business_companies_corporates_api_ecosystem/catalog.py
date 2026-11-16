"""Category adapter over the canonical Global Company business-enterprise taxonomy."""
from __future__ import annotations
from .models import CategoryRecord
from ...global_company_companies_api_ecosystem.business_catalog import SUBCATEGORIES

DOMAIN_ID = "business_companies_corporates"

def list_categories() -> list[CategoryRecord]:
    return [CategoryRecord(id=value, name=value.replace("_", " ").title()) for value in SUBCATEGORIES]

def get_category(category_id: str) -> CategoryRecord | None:
    return next((item for item in list_categories() if item.id == category_id), None)
