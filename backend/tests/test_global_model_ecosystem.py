from backend.infrastructure.model.global_ecosystem.global_model_ecosystem import (
    MODEL_CATALOG,
    MODEL_FAMILY,
    STATUS,
    get_model_catalog,
    validate_resource_record,
)
from backend.infrastructure.model.global_ecosystem.global_model_ecosystem.relationships import (
    RELATIONSHIP_TYPES,
)
from backend.infrastructure.model.global_ecosystem.global_model_ecosystem.resources import (
    RESOURCE_CATEGORIES,
)
from backend.infrastructure.model.global_ecosystem.global_model_ecosystem.schemas import (
    GlobalProviderReference,
    GlobalResourceCapacity,
    GlobalResourceIdentity,
    GlobalResourceLifecycle,
    GlobalResourceLocation,
    GlobalResourceRelationship,
)


def test_global_model_ecosystem_package_metadata():
    assert MODEL_FAMILY == "GLOBAL_MODEL_ECOSYSTEM"
    assert STATUS == "CONTRACT_FOUNDATION"
    assert MODEL_CATALOG == get_model_catalog()


def test_resource_catalog_has_expected_infrastructure_domains():
    assert {"compute", "network", "storage", "data", "platform", "security"} <= set(RESOURCE_CATEGORIES)
    assert "server" in RESOURCE_CATEGORIES["compute"]
    assert "database" in RESOURCE_CATEGORIES["data"]


def test_relationship_vocabulary_is_available():
    assert "HOSTS" in RELATIONSHIP_TYPES
    assert "DEPENDS_ON" in RELATIONSHIP_TYPES


def test_identity_and_provider_reference_serialize_to_stable_field_names():
    assert GlobalResourceIdentity("srv-1", "vps", "provider-x", "remote-1").to_dict() == {
        "resource_id": "srv-1",
        "resource_type": "vps",
        "provider_id": "provider-x",
        "external_id": "remote-1",
    }
    assert GlobalProviderReference("provider-x", "remote-1").to_dict() == {
        "provider_id": "provider-x",
        "external_id": "remote-1",
    }


def test_relationship_lifecycle_location_and_capacity_models():
    assert GlobalResourceRelationship("srv-1", "db-1", "USES").to_dict()["relationship_type"] == "USES"
    assert GlobalResourceLifecycle("ACTIVE").to_dict()["state"] == "ACTIVE"
    assert GlobalResourceLocation(region="ap-south-1").to_dict()["region"] == "ap-south-1"
    assert GlobalResourceCapacity(cpu="4 vCPU", memory="16 GB").to_dict()["memory"] == "16 GB"


def test_resource_validation_accepts_valid_record_and_rejects_missing_fields():
    valid = {"resource_id": "srv-1", "resource_type": "vps", "category": "compute"}
    assert validate_resource_record(valid) == []
    errors = validate_resource_record({"resource_id": "", "resource_type": "vps"})
    assert len(errors) == 2
    assert any("resource_id" in error for error in errors)
    assert any("category" in error for error in errors)


def test_resource_validation_rejects_non_mapping_metadata():
    errors = validate_resource_record({
        "resource_id": "srv-1",
        "resource_type": "vps",
        "category": "compute",
        "metadata": "not-a-mapping",
    })
    assert errors == ["metadata must be a mapping when provided"]
