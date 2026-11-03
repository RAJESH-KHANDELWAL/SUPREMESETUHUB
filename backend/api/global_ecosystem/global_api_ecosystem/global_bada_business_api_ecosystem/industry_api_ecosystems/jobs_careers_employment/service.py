"""Industry-facing service adapter over the canonical Work & Careers taxonomy."""
from __future__ import annotations

from .catalog import CANONICAL_OWNER, list_categories, get_category, search_categories
from ...work_careers_employment_business_api_ecosystem.catalog import get_catalogue_metadata


class JobsCareersService:
    """Read-only discovery adapter; canonical taxonomy remains in Work & Careers."""

    DOMAIN_ID = "jobs_careers_employment"

    def list_categories(self, *, query: str | None = None) -> list[dict[str, object]]:
        return search_categories(query) if query else list_categories()

    def get_category(self, category_id: str) -> dict[str, object] | None:
        return get_category(category_id)

    def list_employment_categories(self, *, query: str | None = None) -> list[dict[str, object]]:
        """Compatibility name for the same canonical employment taxonomy."""
        return search_categories(query) if query else list_categories()

    def get_employment_category(self, category_id: str) -> dict[str, object] | None:
        """Compatibility name for canonical category lookup."""
        return get_category(category_id)

    def get_status(self) -> dict[str, object]:
        metadata = get_catalogue_metadata()
        return {
            "success": True,
            "industry_id": self.DOMAIN_ID,
            "canonical_domain_id": metadata["domain_id"],
            "canonical_owner": CANONICAL_OWNER,
            "status": metadata["catalogue_status"],
            "category_count": metadata["category_count"],
            "coverage": ["india", "global"],
            "taxonomy_source_structurally_valid": metadata["structurally_valid"],
            "live_vacancies_verified": False,
            "employers_verified": False,
            "legal_eligibility_verified": False,
        }
