"""Business logic for Education, Learning & Training."""
from __future__ import annotations

from .catalog import get_education_category, list_education_categories

class EducationLearningService:
    DOMAIN_ID = "education_learning_training"

    def list_categories(self, *, query: str | None = None) -> list[dict[str, object]]:
        items = list_education_categories()
        if query:
            term = query.strip().casefold()
            items = [
                item for item in items
                if term in str(item["id"]).casefold()
                or term in str(item["name"]).casefold()
                or any(term in value.replace("_", " ").casefold() for value in item["subcategories"])
            ]
        return items

    def get_category(self, category_id: str) -> dict[str, object] | None:
        return get_education_category(category_id)

    def get_status(self) -> dict[str, object]:
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "status": "taxonomy_scaffold",
            "category_count": len(list_education_categories()),
            "coverage": ["india", "global"],
            "channels": ["online", "offline", "hybrid"],
            "note": "Education taxonomy only; no accreditation, admission, placement or provider verification is implied.",
        }
