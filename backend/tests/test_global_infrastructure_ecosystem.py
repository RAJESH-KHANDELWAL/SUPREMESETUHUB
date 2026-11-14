from fastapi import FastAPI
from backend.api.global_ecosystem.global_api_ecosystem.global_infrastructure_api_ecosystem import router
from backend.core.global_ecosystem.global_core_ecosystem.global_infrastructure_core_ecosystem import (
    GlobalInfrastructureCoreService,
)
from backend.engine.global_ecosystem.global_engine_ecosystem.global_infrastructure_engine_ecosystem import (
    get_infrastructure_engine,
)
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem import (
    GlobalInfrastructureEcosystemService,
)
from backend.infrastructure.global_models.global_infrastructure_models import (
    get_model_catalog,
    validate_resource_record,
)


def test_global_infrastructure_catalog_has_all_twenty_domains():
    service = GlobalInfrastructureEcosystemService()
    assert len(service.get_modules()) == 20
    assert service.get_overview()["provider_operations_enabled"] is False


def test_global_infrastructure_catalog_marks_provider_connections_unconfigured():
    catalog = GlobalInfrastructureEcosystemService().get_catalog()
    assert catalog["providers"]
    assert all(
        item["status"] in {"NOT_CONFIGURED", "CATALOG_ONLY"}
        for item in catalog["providers"]
    )


def test_global_infrastructure_models_validate_minimum_resource_contract():
    valid = {"resource_id": "srv-001", "resource_type": "vps", "category": "compute"}
    assert validate_resource_record(valid) == []
    assert validate_resource_record({"resource_id": "", "resource_type": "vps"}) 


def test_core_owns_resource_contract_validation():
    result = GlobalInfrastructureCoreService().validate_resource(
        {"resource_id": "srv-001", "resource_type": "vps", "category": "compute"}
    )
    assert result["success"] is True
    assert result["validated_by"] == "GLOBAL_INFRASTRUCTURE_CORE"


def test_engine_delegates_validation_to_core_only_when_running():
    engine = get_infrastructure_engine()
    engine.start()
    try:
        result = engine.validate_resource(
            {"resource_id": "srv-002", "resource_type": "server", "category": "compute"}
        )
        assert result["success"] is True
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
