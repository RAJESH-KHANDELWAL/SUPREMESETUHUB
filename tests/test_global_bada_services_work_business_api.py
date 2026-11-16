"""Contract tests for Global Bada Business Services and Work/Business API facades."""
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.routes import router
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_services_api_ecosystem.service import GlobalServicesAPIService
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_work_business_api_ecosystem.service import GlobalWorkBusinessAPIService


def test_services_api_uses_canonical_services_catalogue():
    service = GlobalServicesAPIService()
    status = service.status()
    categories = service.categories()
    assert status["ecosystem_id"] == "GLOBAL-BADA-BUSINESS-SERVICES-API"
    assert categories["count"] > 0
    assert all(item["domain_id"] == "services_platforms_integrations" for item in categories["categories"])


def test_work_business_api_aggregates_canonical_work_sources():
    service = GlobalWorkBusinessAPIService()
    status = service.status()
    sectors = service.list_sectors()
    assert status["ecosystem_id"] == "GLOBAL-BADA-BUSINESS-WORK-BUSINESS-API"
    assert sectors["count"] == 25
    assert status["freelance_specialization_count"] == 25
    assert status["live_jobs_or_gigs"] is False


def test_bada_business_router_mounts_both_facades():
    paths = {route.path for route in router.routes}
    assert "/api/v1/global-ecosystem/business/services/status" in paths
    assert "/api/v1/global-ecosystem/business/work-business-directory/status" in paths
