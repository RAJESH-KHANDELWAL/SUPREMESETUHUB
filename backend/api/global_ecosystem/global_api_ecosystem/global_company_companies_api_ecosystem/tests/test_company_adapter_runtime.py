"""Runtime integration tests for Company-specific adapter packages."""
from backend.api.global_ecosystem.global_api_ecosystem.global_company_companies_api_ecosystem.global_companies_ecosystem.service import (
    get_company_adapter_status,
    get_company_ecosystem_status,
    get_company_profile,
    list_companies,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_company_companies_api_ecosystem.global_companies_ecosystem.routes import router


def test_company_adapter_service_lists_all_26_profiles():
    result = list_companies(limit=100)
    assert result["total"] == 26
    assert len(result["items"]) == 26
    assert result["live_connections"] is False
    assert all(item["record_type"] == "company" for item in result["items"])


def test_company_adapter_service_filters_and_paginates():
    result = list_companies(query="open", limit=10, offset=0)
    assert result["total"] >= 1
    assert all("open" in item["company_id"] or "open" in item["canonical_name"].casefold() for item in result["items"])
    page = list_companies(limit=5, offset=5)
    assert len(page["items"]) == 5
    assert page["offset"] == 5


def test_company_adapter_service_returns_source_and_status():
    profile = get_company_profile("openai")
    status = get_company_adapter_status("openai")
    ecosystem = get_company_ecosystem_status()
    assert profile is not None
    assert profile["profile_status"] == "source_registered_unverified"
    assert profile["sources"]
    assert status["live_connection"] is False
    assert ecosystem["adapter_count"] == 26
    assert ecosystem["live_connections"] == 0


def test_company_adapter_service_rejects_unknown_id_and_invalid_pagination():
    assert get_company_profile("not-a-company-adapter") is None
    try:
        list_companies(limit=101)
    except ValueError as error:
        assert "limit" in str(error)
    else:
        raise AssertionError("Invalid limit should be rejected")


def test_company_adapter_aggregate_routes_are_mounted():
    paths = {route.path for route in router.routes}
    assert "/global/company-profile-adapters" in paths
    assert "/global/company-profile-adapters/status" in paths
    assert "/global/company-profile-adapters/{company_id}" in paths
    assert "/global/company-profile-adapters/{company_id}/sources" in paths


def test_company_ecosystem_package_and_parent_api_router_are_connected():
    from backend.api.global_ecosystem.global_api_ecosystem.global_company_companies_api_ecosystem import (
        search_companies,
    )
    from backend.api.global_api_ecosystem_routes import router as parent_router
    from backend.api.global_ecosystem.global_api_ecosystem.global_company_companies_api_ecosystem.global_companies_ecosystem import (
        get_ecosystem_info,
    )

    paths = {route.path for route in parent_router.routes}
    assert callable(search_companies)
    assert "/api/v1/global-api-ecosystem/global/company-profile-adapters" in paths
    assert "/api/v1/global-api-ecosystem/global/companies" in paths
    assert get_ecosystem_info()["adapter_count"] == 26
