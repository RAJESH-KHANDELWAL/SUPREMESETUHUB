"""Runtime integration tests for the Global Platforms registry and providers."""
from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem.provider_directory import (
    get_platform_provider,
    get_provider_directory_status,
    list_platform_providers,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem.global_platforms_ecosystem.service import (
    get_platform_profile,
    list_platforms,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem.global_platforms_ecosystem.routes import router as directory_router
from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem.routes import router as platforms_router


def test_nested_platform_service_uses_canonical_registry(monkeypatch):
    from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem.global_platforms_ecosystem import service

    records = [{"platform_id": "sample-platform", "name": "Sample Platform"}]
    monkeypatch.setattr(service, "search_platforms", lambda **kwargs: {
        "total": 1, "limit": kwargs["limit"], "offset": kwargs["offset"],
        "include_adult": kwargs["include_adult"], "items": records,
    })
    result = list_platforms(query="sample")
    assert result["items"] == records
    assert get_platform_profile("sample-platform") is None


def test_platform_provider_directory_has_real_package_metadata():
    providers = list_platform_providers()
    assert len(providers) == 4
    assert {item["provider_id"] for item in providers} == {"apple", "aws", "google", "microsoft"}
    assert all(item["implementation_status"] == "CATALOG_ONLY" for item in providers)
    assert all(item["live_connection_verified"] is False for item in providers)


def test_adult_platform_providers_are_separate_and_age_gated():
    default = list_platform_providers()
    expanded = list_platform_providers(include_adult=True)
    assert len(expanded) == 18
    adult = [item for item in expanded if item["adult_only"]]
    assert len(adult) == 14
    assert all(item["minimum_age"] == 18 for item in adult)
    assert get_platform_provider("onlyfans") is None
    assert get_platform_provider("onlyfans", include_adult=True)["minimum_age"] == 18


def test_provider_directory_status_is_explicit_about_non_live_state():
    status = get_provider_directory_status()
    assert status["provider_count"] == 18
    assert status["adult_provider_count"] == 14
    assert status["live_connections"] == 0


def test_platform_directory_routes_are_included_under_platform_api():
    paths = {route.path for route in platforms_router.routes}
    assert "/global/platforms/directory" in paths
    assert "/global/platforms/directory/status" in paths
    assert "/global/platforms/directory/{platform_id}" in paths
    assert "/global/platforms/providers" in paths
    assert "/global/platforms/providers/{provider_id}" in paths
    assert {route.path for route in directory_router.routes}


def test_platform_directory_validates_query_and_preserves_registry_contract():
    result = list_platforms(limit=25, offset=0)
    assert result["total"] == len(result["items"])
    assert result["include_adult"] is False


def test_global_api_compatibility_facade_and_parent_router_mount():
    from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem import (
        get_ecosystem_info,
        router as compatibility_router,
    )
    from backend.api.global_api_ecosystem_routes import router as parent_router
    from backend.api.global_ecosystem.global_api_ecosystem import CATEGORY_ECOSYSTEMS

    facade_paths = {route.path for route in compatibility_router.routes}
    parent_paths = {route.path for route in parent_router.routes}
    category_ids = {item["id"] for item in CATEGORY_ECOSYSTEMS}

    assert "/global/platforms/status" in facade_paths
    assert "/global/platforms/directory" in facade_paths
    assert "/api/v1/global-api-ecosystem/global/platforms/directory" in parent_paths
    assert "companies" in category_ids
    assert "platforms" in category_ids
    assert get_ecosystem_info()["status"] == "ready_with_records"


def test_platform_provider_static_routes_precede_dynamic_detail_route():
    paths = [route.path for route in platforms_router.routes]
    assert paths.index("/global/platforms/providers") < paths.index("/global/platforms/{platform_id}")
