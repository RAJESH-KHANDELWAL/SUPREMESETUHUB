"""Tests for Jobs, Careers & Employment taxonomy and service."""
from .service import JobsCareersService

def test_catalog_has_unique_ids_and_categories():
    service = JobsCareersService()
    items = service.list_categories()
    ids = [item["id"] for item in items]
    assert len(items) >= 10
    assert len(ids) == len(set(ids))
    assert all(item["name"] and item["subcategories"] for item in items)

def test_search_and_detail():
    service = JobsCareersService()
    first = service.list_categories()[0]
    assert service.get_category(first["id"])["id"] == first["id"]
    assert service.list_categories(query=first["id"])
    assert service.get_category("not_a_real_category") is None

def test_status_is_explicit_about_scaffold():
    status = JobsCareersService().get_status()
    assert status["status"] == "taxonomy_scaffold"
    assert status["category_count"] == len(JobsCareersService().list_categories())

def test_employment_taxonomy_bridge_exposes_job_categories():
    service = JobsCareersService()
    items = service.list_employment_categories()
    ids = {item["id"] for item in items}
    assert len(items) == 24
    assert {"government_jobs", "private_sector_jobs", "corporate_jobs", "public_sector_jobs"} <= ids
    assert all(item["taxonomy_status"] == "taxonomy_only" for item in items)

def test_employment_taxonomy_search_and_detail():
    service = JobsCareersService()
    results = service.list_employment_categories(query="government")
    assert any(item["id"] == "government_jobs" for item in results)
    assert service.get_employment_category("private_sector_jobs")["id"] == "private_sector_jobs"
    assert service.get_employment_category("not_a_real_category") is None
