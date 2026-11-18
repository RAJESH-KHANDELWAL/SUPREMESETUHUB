"""Catalogue access for the Work, Jobs & Careers domain."""
from __future__ import annotations

from . import ADULT_RESTRICTED, DOMAIN_ID, DOMAIN_NAME
from .categories import (
    CATEGORY_DEFINITIONS,
    TAXONOMY_STATUS,
    get_category_definition,
    validate_category_definitions,
)
from .models import CategoryRecord

CATEGORIES = tuple(
    CategoryRecord(
        id=item["id"],
        name=item["name"],
        domain_id=DOMAIN_ID,
        adult_restricted=ADULT_RESTRICTED,
        description=item["description"],
        category_type=item["category_type"],
        ownership_sectors=tuple(item.get("ownership_sectors", ())),
        employer_organization_types=tuple(item.get("employer_organization_types", ())),
        employment_types=tuple(item["employment_types"]),
        work_arrangements=tuple(item["work_arrangements"]),
        seniority_levels=tuple(item["seniority_levels"]),
        audience_groups=tuple(item["audience_groups"]),
        search_terms=tuple(item["search_terms"]),
        scope_notes=tuple(item["scope_notes"]),
        verification_requirements=tuple(item["verification_requirements"]),
        related_category_ids=tuple(item["related_category_ids"]),
        taxonomy_status=item.get("taxonomy_status", TAXONOMY_STATUS),
    )
    for item in CATEGORY_DEFINITIONS
)

def list_categories() -> list[CategoryRecord]:
    return list(CATEGORIES)

def get_category(category_id: str) -> CategoryRecord | None:
    return next((record for record in CATEGORIES if record.id == category_id), None)

def search_categories(query: str) -> list[CategoryRecord]:
    needle = query.strip().casefold()
    if not needle:
        return []
    return [
        record for record in CATEGORIES
        if needle in record.id.casefold()
        or needle in record.name.casefold()
        or needle in record.description.casefold()
        or any(needle in term.casefold() for term in record.search_terms)
    ]

def get_catalogue_metadata() -> dict:
    integrity = validate_category_definitions()
    return {
        "domain_id": DOMAIN_ID,
        "domain_name": DOMAIN_NAME,
        "category_count": len(CATEGORIES),
        "adult_restricted": ADULT_RESTRICTED,
        "catalogue_status": TAXONOMY_STATUS,
        "structurally_valid": integrity["structurally_valid"],
    }

def get_category_definition_by_id(category_id: str) -> dict | None:
    return get_category_definition(category_id)
