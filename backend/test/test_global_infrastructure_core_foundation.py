from backend.core.global_ecosystem.global_core_ecosystem.global_infrastructure_core_ecosystem import (
    GlobalInfrastructureCoreOrchestrator,
    GlobalInfrastructureCoreService,
    get_domain_catalog,
    get_provider_catalog,
)


def test_catalog_is_provider_neutral_and_read_only():
    catalog = GlobalInfrastructureCoreOrchestrator().catalog()
    assert catalog["ecosystem_id"] == "GLOBAL-INFRASTRUCTURE-CORE-ECOSYSTEM"
    assert len(catalog["domains"]) == 21
    assert all(provider["live_connection_verified"] is False for provider in catalog["providers"])


def test_catalog_returns_independent_data():
    domains = get_domain_catalog()
    domains[0]["name"] = "MUTATED"
    assert get_domain_catalog()[0]["name"] != "MUTATED"


def test_existing_resource_validation_is_preserved():
    service = GlobalInfrastructureCoreService()
    assert service.validate_resource(
        {"resource_id": "srv-001", "resource_type": "vps", "category": "compute"}
    )["success"] is True
    assert service.validate_resource(
        {"resource_id": "", "resource_type": "vps"}
    )["success"] is False


def test_core_health_reports_metadata_only_status():
    health = GlobalInfrastructureCoreOrchestrator().health()
    assert health["status"] == "CATALOG_ONLY"
    assert health["health_check_performed"] is False
    assert health["provider_operations_enabled"] is False
    assert health["live_connections_verified"] is False


def test_provider_catalog_is_metadata_only():
    assert all(provider["status"] == "CATALOG_ONLY" for provider in get_provider_catalog())


def test_validation_output_redacts_secret_metadata():
    service = GlobalInfrastructureCoreService()
    result = service.validate_resource(
        {
            "resource_id": "srv-003",
            "resource_type": "vm",
            "category": "compute",
            "metadata": {
                "region": "ap-south-1",
                "api_key": "must-not-leak",
                "clientSecret": "must-not-leak",
                "private-key": "must-not-leak",
                "nested": {"password": "hidden", "tier": "standard"},
            },
        }
    )
    assert result["success"] is True
    assert result["resource"]["metadata"] == {
        "region": "ap-south-1",
        "nested": {"tier": "standard"},
    }


def test_non_mapping_resource_is_rejected_safely():
    assert GlobalInfrastructureCoreService().validate_resource(None)["success"] is False
