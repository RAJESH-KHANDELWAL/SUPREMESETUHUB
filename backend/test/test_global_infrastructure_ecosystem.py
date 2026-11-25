from fastapi import FastAPI
from backend.api.global_ecosystem.global_api_ecosystem.global_infrastructure_api_ecosystem import router
from backend.engine.global_ecosystem.global_engine_ecosystem.global_infrastructure_engine_ecosystem import get_infrastructure_engine
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem import GlobalInfrastructureEcosystemService
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.model.global_ecosystem.global_model_ecosystem import get_model_catalog, validate_resource_record
from backend.infrastructure.model import InfrastructureResource, InfrastructureCategory, InfrastructureResourceType

def test_infrastructure_model_package_exports_existing_resource_contract():
    assert InfrastructureResource
    assert InfrastructureCategory.SERVER.value == "server"
    assert InfrastructureResourceType.VPS.value == "vps"

def test_global_infrastructure_catalog_has_all_twenty_domains():
    service = GlobalInfrastructureEcosystemService()
    assert len(service.get_modules()) == 21
    assert service.get_overview()["provider_operations_enabled"] is False

def test_global_infrastructure_catalog_marks_provider_connections_unconfigured():
    catalog = GlobalInfrastructureEcosystemService().get_catalog()
    assert catalog["providers"]
    assert all(item["status"] in {"NOT_CONFIGURED", "CATALOG_ONLY"} for item in catalog["providers"])

def test_global_infrastructure_models_validate_minimum_resource_contract():
    valid = {"resource_id": "srv-001", "resource_type": "vps", "category": "compute"}
    assert validate_resource_record(valid) == []
    assert validate_resource_record({"resource_id": "", "resource_type": "vps"})

def test_model_contract_owns_resource_validation():
    assert validate_resource_record({"resource_id": "srv-001", "resource_type": "vps", "category": "compute"}) == []

def test_engine_exposes_lifecycle_status_without_provider_execution():
    engine = get_infrastructure_engine()
    engine.start()
    try:
        assert engine.status()["layer"] == "ENGINE"
        assert engine.status()["provider_operations_enabled"] is False
    finally:
        engine.stop()

def test_global_infrastructure_api_routes_are_mounted():
    app = FastAPI()
    app.include_router(router)
    paths = {route.path for route in app.routes}
    assert "/infrastructure/status" in paths
    assert "/infrastructure/catalog" in paths
    assert "/infrastructure/models" in paths
    assert "/infrastructure/validate-resource" in paths

def test_model_catalog_is_exposed():
    assert "resource_identity" in get_model_catalog()

def test_global_infrastructure_engine_is_registered_by_bootstrap():
    from backend.core.bootstrap import Bootstrap
    bootstrap = Bootstrap()
    bootstrap.register_engines()
    engine = bootstrap.engine_manager.get_engine("global_infrastructure")
    assert engine is get_infrastructure_engine()
    assert engine.status()["layer"] == "ENGINE"

def test_global_infrastructure_api_is_registered_in_global_api_parent():
    from backend.api.global_api_ecosystem_routes import router as global_api_router
    app = FastAPI()
    app.include_router(global_api_router)
    paths = {route.path for route in app.routes}
    assert "/api/v1/global-api-ecosystem/infrastructure/status" in paths
    assert "/api/v1/global-api-ecosystem/infrastructure/catalog" in paths


def test_global_infrastructure_manager_checks_required_structure_and_external_provider_ownership():
    from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.manager import get_manager
    health = get_manager().health()
    assert health["expected_domain_count"] == 21
    assert health["present_domain_count"] == 21
    assert health["healthy"] is True
    assert health["provider_operations_enabled"] is False


def test_provider_adapters_are_registered_from_backend_global_ecosystem():
    from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules import ROOT_MODULES
    assert ROOT_MODULES["hostinger_api"] == "backend.global_ecosystem.global_hosting_ecosystem.hostinger_api"
    assert ROOT_MODULES["nsfwinfra"] == "backend.global_ecosystem.nsfwinfra_ecosystem.nsfwinfra"


def test_all_global_infrastructure_domain_packages_have_structural_managers():
    from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.manager import get_manager
    health = get_manager().health()
    assert health["expected_global_package_count"] == 21
    assert health["present_global_package_count"] == 21
    assert all(health["checks"][f"global_package_{name}"] for name in (
        "backup", "billing", "cdn", "containers", "database", "dns", "domains",
        "email", "firewall", "ftp", "hosting", "ipam", "load_balancer", "model",
        "monitoring", "network", "object_storage", "security", "server", "ssl", "storage",
    ))
    assert health["healthy"] is True
