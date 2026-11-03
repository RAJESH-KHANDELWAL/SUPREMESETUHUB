"""Tests for canonical Work & Careers taxonomy ownership in the industry adapter."""
from .service import JobsCareersService
from .catalog import CANONICAL_OWNER


def test_adapter_uses_canonical_owner_and_category_count():
    service = JobsCareersService()
    status = service.get_status()
    assert CANONICAL_OWNER == "work_careers_employment_business_api_ecosystem"
    assert status["canonical_domain_id"] == "work_careers_employment"
    assert status["category_count"] == 24


def test_adapter_list_search_and_detail_share_canonical_ids():
    service = JobsCareersService()
    all_items = service.list_categories()
    ids = {item["id"] for item in all_items}
    assert len(ids) == 24
    assert {"government_jobs", "private_sector_jobs", "corporate_jobs", "remote_jobs"} <= ids
    assert any(item["id"] == "government_jobs" for item in service.list_categories(query="government"))
    assert service.get_category("private_sector_jobs")["id"] == "private_sector_jobs"
    assert service.get_category("not_a_real_category") is None


def test_employment_compatibility_alias_does_not_add_records():
    service = JobsCareersService()
    assert service.list_employment_categories() == service.list_categories()
    assert len(service.list_employment_categories()) == 24
