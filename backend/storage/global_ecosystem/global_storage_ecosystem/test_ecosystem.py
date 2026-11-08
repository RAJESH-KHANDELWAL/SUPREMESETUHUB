"""Offline behavior tests for GLOBAL STORAGE ECOSYSTEM."""
import pytest
from .manager import GlobalStorageEcosystemManager
from .ecosystem_registry import StorageEcosystemRegistry
from .models import StorageEcosystemIdentity, StorageObject
from .registry import list_providers, get_provider

def test_manager_initializes_root_and_six_providers():
    manager = GlobalStorageEcosystemManager()
    assert manager.status()["status"] == "FOUNDATION_READY"
    assert manager.registry.count() == len(list_providers()) + 1
    assert manager.health()["provider_connections_verified"] is False

def test_provider_catalog_has_six_providers():
    assert {p["provider_id"] for p in list_providers()} == {
        "aws_storage", "google_storage", "hostinger_storage",
        "mega_storage", "microsoft_storage", "proton_storage"}

def test_provider_lookup_is_case_insensitive_and_defensive():
    pid = list_providers()[0]["provider_id"]
    item = get_provider(pid.upper())
    item["capabilities"].append("tampered")
    assert "tampered" not in get_provider(pid)["capabilities"]

def test_unknown_provider_raises_key_error():
    with pytest.raises(KeyError):
        get_provider("not-a-provider")

def test_registry_enforces_parent_and_duplicate_ids():
    registry = StorageEcosystemRegistry()
    with pytest.raises(ValueError):
        registry.register(StorageEcosystemIdentity("child", "Child", parent_id="missing"))
    registry.register(StorageEcosystemIdentity("root", "Root"))
    registry.register(StorageEcosystemIdentity("child", "Child", parent_id="root"))
    with pytest.raises(ValueError):
        registry.register(StorageEcosystemIdentity("child", "Duplicate", parent_id="root"))

def test_registry_returns_defensive_records():
    registry = StorageEcosystemRegistry()
    registry.register(StorageEcosystemIdentity("root", "Root", capabilities=["read"]))
    record = registry.get("root")
    record["capabilities"].append("write")
    assert registry.get("root")["capabilities"] == ["read"]

def test_tree_and_connection_map_are_consistent():
    manager = GlobalStorageEcosystemManager()
    assert len(manager.tree()["tree"]["children"]) == len(list_providers())
    graph = manager.connection_map()
    assert graph["node_count"] == graph["edge_count"] + 1

def test_storage_object_validates_fields_and_size():
    with pytest.raises(ValueError):
        StorageObject("id", "aws", "bucket", "key", size_bytes=-1)
    with pytest.raises(ValueError):
        StorageObject("id", "aws", "", "key")

def test_registration_rejects_invalid_parent():
    manager = GlobalStorageEcosystemManager()
    result = manager.register({"ecosystem_id": "orphan", "name": "Orphan", "parent_id": "missing"})
    assert result["success"] is False

def test_manager_lookup_by_id_and_name():
    manager = GlobalStorageEcosystemManager()
    root = manager.get(manager.ROOT_ID)
    assert root is not None
    assert manager.get(root["name"])["ecosystem_id"] == manager.ROOT_ID
