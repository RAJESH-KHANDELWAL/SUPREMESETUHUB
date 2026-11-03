"""Tests for the independent Internships & Apprenticeships package."""
from .service import CategoryService


def test_category_identity_and_subcategories_are_stable():
    category = CategoryService().get_category()
    assert category["id"] == "internships_and_apprenticeships"
    assert category["name"] == "Internships & Apprenticeships"
    assert len(category["subcategories"]) == 4
    assert len(category["subcategories"]) == len(set(category["subcategories"]))


def test_category_service_returns_defensive_data():
    service = CategoryService()
    first = service.get_category()
    first["subcategories"].append("mutation_probe")
    assert "mutation_probe" not in service.get_category()["subcategories"]


def test_category_status_is_explicit_about_scaffold():
    status = CategoryService().get_status()
    assert status["category_id"] == "internships_and_apprenticeships"
    assert status["status"] == "taxonomy_scaffold"
