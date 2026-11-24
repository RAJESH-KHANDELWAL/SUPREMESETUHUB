"""Contract tests for the MAIN BASE FOUNDATION infrastructure model."""
from backend.infrastructure.model import (
    InfrastructureCategory,
    InfrastructureOwnershipType,
    InfrastructureRegistry,
    InfrastructureRelationship,
    InfrastructureRelationshipType,
    InfrastructureResource,
    InfrastructureResourceStatus,
    InfrastructureResourceType,
)


def make_resource(resource_id="srv-001"):
    return InfrastructureResource(
        resource_id=resource_id,
        name="Example VPS",
        resource_type=InfrastructureResourceType.VPS,
        category=InfrastructureCategory.SERVER,
        status=InfrastructureResourceStatus.ACTIVE,
        ownership_type=InfrastructureOwnershipType.PLATFORM,
        provider="Hostinger",
    )


def test_resource_contract_serializes_stable_fields():
    payload = make_resource().to_dict()
    assert payload["resource_id"] == "srv-001"
    assert payload["resource_type"] == "vps"
    assert payload["category"] == "server"
    assert payload["status"] == "active"
    assert payload["provider"] == "Hostinger"


def test_resource_registry_registers_reads_and_removes():
    registry = InfrastructureRegistry()
    resource = make_resource()
    registry.register(resource)
    assert registry.get("srv-001") is resource
    assert registry.list_all() == [resource]
    assert registry.remove("srv-001") is True
    assert registry.get("srv-001") is None


def test_relationship_contract_serializes_type():
    relationship = InfrastructureRelationship(
        relationship_id="rel-001",
        source_resource_id="hosting-001",
        target_resource_id="site-001",
        relationship_type=InfrastructureRelationshipType.HOSTS,
    )
    assert relationship.to_dict()["relationship_type"] == "hosts"
