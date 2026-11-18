"""Business logic for Jobs, Careers & Employment."""
from __future__ import annotations
from dataclasses import asdict
from .catalog import get_category, list_categories
from ..global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem.catalog import (
    get_category as get_employment_category,
    list_categories as list_employment_categories,
)

class JobsCareersService:
    DOMAIN_ID = "jobs_careers_employment"

    def list_categories(self, *, query: str | None = None) -> list[dict[str, object]]:
        items = list_categories()
        if query:
            term = query.strip().casefold()
            items = [item for item in items if term in str(item["id"]).casefold() or term in str(item["name"]).casefold() or any(term in value.replace("_", " ").casefold() for value in item["subcategories"])]
        return items

    def get_category(self, category_id: str) -> dict[str, object] | None:
        return get_category(category_id)


    def list_employment_categories(self, *, query: str | None = None) -> list[dict[str, object]]:
        """Expose the detailed employment taxonomy without duplicating its source."""
        items = [asdict(item) for item in list_employment_categories()]
        if query:
            term = query.strip().casefold()
            items = [
                item for item in items
                if term in str(item["id"]).casefold()
                or term in str(item["name"]).casefold()
                or term in str(item["description"]).casefold()
                or any(term in value.casefold() for field in ("search_terms", "scope_notes", "employment_types", "work_arrangements") for value in item[field])
            ]
        return items

    def get_employment_category(self, category_id: str) -> dict[str, object] | None:
        """Return one detailed employment category by its stable identifier."""
        item = get_employment_category(category_id)
        return asdict(item) if item is not None else None

    def get_status(self) -> dict[str, object]:
        return {"success": True, "domain_id": self.DOMAIN_ID, "status": "taxonomy_scaffold", "category_count": len(list_categories()), "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "note": "Taxonomy scaffold only; no live provider verification, transaction processing or regulatory approval is implied."}
