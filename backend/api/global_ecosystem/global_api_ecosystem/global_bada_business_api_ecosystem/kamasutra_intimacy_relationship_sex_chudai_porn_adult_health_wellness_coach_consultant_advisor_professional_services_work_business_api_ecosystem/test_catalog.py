"""Integrity tests for the standalone adult wellness taxonomy."""
from importlib import import_module
from .service import AdultWellnessEcosystemService
from .subcategories import SUBCATEGORIES

def test_all_categories_are_registered():
    assert len(SUBCATEGORIES) == 34
    assert len({item["id"] for item in SUBCATEGORIES}) == 34

def test_service_status_and_search():
    service = AdultWellnessEcosystemService()
    assert service.get_status()["category_count"] == 34
    assert service.list_categories(query="kamasutra")[0]["id"] == "kamasutra_ancient_knowledge"

def test_every_category_has_a_separate_catalog():
    for item in SUBCATEGORIES:
        module = import_module(f".{item['folder']}.catalog", package=__package__)
        assert module.CATEGORY_ID == item["id"]
        assert module.SUBDOMAINS
