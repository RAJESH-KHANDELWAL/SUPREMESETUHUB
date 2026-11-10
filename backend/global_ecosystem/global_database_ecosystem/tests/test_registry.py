"""Offline tests for metadata registry."""
import pytest
from global_database_ecosystem.models import DatabasePlatform, DataWorkload
from global_database_ecosystem.registry import DatabaseEcosystemRegistry

def test_registry_registers_and_filters():
    registry = DatabaseEcosystemRegistry()
    registry.register_platform(DatabasePlatform("pg", "PostgreSQL", "relational_sql"))
    registry.register_platform(DatabasePlatform("mongo", "MongoDB", "document_nosql"))
    assert len(registry.list_platforms(database_model="relational_sql")) == 1

def test_registry_batch_is_atomic_on_duplicate():
    registry = DatabaseEcosystemRegistry()
    registry.register_workload(DataWorkload("orders", "commerce", "Order processing"))
    with pytest.raises(ValueError):
        registry.load_workloads([
            DataWorkload("new", "commerce", "New workload"),
            DataWorkload("orders", "commerce", "Duplicate"),
        ])
    assert [item.workload_id for item in registry.list_workloads()] == ["orders"]

def test_invalid_platform_status_rejected():
    with pytest.raises(ValueError):
        DatabasePlatform("bad", "Bad", "unknown", integration_status="magic")
