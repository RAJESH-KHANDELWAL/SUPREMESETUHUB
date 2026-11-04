"""Tests for Healthcare & Life Sciences taxonomy and service."""
from .service import HealthcareService

def test_catalog_has_unique_ids_and_categories():
    service = HealthcareService()
    items = service.list_categories()
    ids = [item["id"] for item in items]
    assert len(items) >= 10
    assert len(ids) == len(set(ids))
    assert all(item["name"] and item["subcategories"] for item in items)

def test_search_and_detail():
    service = HealthcareService()
    first = service.list_categories()[0]
    assert service.get_category(first["id"])["id"] == first["id"]
    assert service.list_categories(query=first["id"])
    assert service.get_category("not_a_real_category") is None

def test_status_is_explicit_about_scaffold():
    status = HealthcareService().get_status()
    assert status["status"] == "taxonomy_scaffold"
    assert status["category_count"] == len(HealthcareService().list_categories())
