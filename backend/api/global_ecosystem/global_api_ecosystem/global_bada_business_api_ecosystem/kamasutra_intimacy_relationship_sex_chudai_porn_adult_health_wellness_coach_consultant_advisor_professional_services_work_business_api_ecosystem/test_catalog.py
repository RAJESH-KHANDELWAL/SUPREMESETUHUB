"""Integrity tests for the adult wellness taxonomy."""
from .service import AdultWellnessEcosystemService
from .subcategories import SUBCATEGORIES

def test_all_categories_are_adult_wellness_taxonomy():
    assert len(SUBCATEGORIES) == 34
    assert len({item["id"] for item in SUBCATEGORIES}) == 34

def test_service_status_and_search():
    service = AdultWellnessEcosystemService()
    assert service.get_status()["category_count"] == 34
    assert service.list_categories(query="kamasutra")[0]["id"] == "kamasutra_ancient_knowledge"

def test_every_category_has_subdomains():
    service = AdultWellnessEcosystemService()
    assert all(item["subdomains"] for item in service.list_categories())
