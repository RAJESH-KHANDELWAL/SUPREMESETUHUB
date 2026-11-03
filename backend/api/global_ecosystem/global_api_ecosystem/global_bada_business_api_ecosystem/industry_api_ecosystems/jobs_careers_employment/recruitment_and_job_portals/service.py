"""Service boundary for Recruitment & Job Portals."""
from __future__ import annotations
from .catalog import get_category

class CategoryService:
    """Read-only service for this independently maintained category."""
    def get_category(self) -> dict[str, object]:
        return get_category()

    def get_status(self) -> dict[str, object]:
        category = get_category()
        return {
            "success": True,
            "category_id": category["id"],
            "category_name": category["name"],
            "subcategory_count": len(category["subcategories"]),
            "status": "taxonomy_scaffold",
        }
