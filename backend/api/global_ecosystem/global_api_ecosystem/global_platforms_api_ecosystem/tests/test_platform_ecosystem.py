"""Tests for platform taxonomy and adult-directory filtering."""
from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem.catalog import PLATFORM_DOMAINS
from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem.service import list_domains, search_platforms

def test_domains_have_unique_ids_and_subdomains():
    ids = [item["domain_id"] for item in PLATFORM_DOMAINS]
    assert len(ids) == len(set(ids))
    assert all(item["name"] and item["subdomains"] for item in PLATFORM_DOMAINS)

def test_adult_domain_is_excluded_by_default():
    assert all(not item.get("adult_only") for item in list_domains())
    assert any(item.get("adult_only") for item in list_domains(include_adult=True))

def test_adult_profiles_are_excluded_by_default(monkeypatch):
    from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem import service
    monkeypatch.setattr(service, "load_platform_registry", lambda: [{"platform_id":"ordinary-1","name":"Ordinary Platform"},{"platform_id":"adult-1","name":"Adult Platform","adult_only":True,"minimum_age":18}])
    assert [x["platform_id"] for x in search_platforms()["items"]] == ["ordinary-1"]
    assert {x["platform_id"] for x in search_platforms(include_adult=True)["items"]} == {"ordinary-1","adult-1"}
