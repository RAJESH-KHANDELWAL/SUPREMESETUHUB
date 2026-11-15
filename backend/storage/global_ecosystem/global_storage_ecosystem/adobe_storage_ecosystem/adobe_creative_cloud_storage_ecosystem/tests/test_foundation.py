import pytest
from ..models import StorageObjectRecord
from ..registry import StorageMetadataRegistry
from ..service import StorageEcosystemService

def record(**kw):
    values={"provider_id":"adobe","ecosystem_id":"creative_cloud","object_id":"obj-1","name":"sample","size_bytes":10}; values.update(kw); return StorageObjectRecord(**values)

def test_model_validation():
    with pytest.raises(ValueError): record(object_id="")
    with pytest.raises(ValueError): record(size_bytes=-1)

def test_registry_duplicate_guard():
    registry=StorageMetadataRegistry(); item=record(); assert registry.register(item)["object_id"]=="obj-1"
    with pytest.raises(ValueError,match="DUPLICATE_OBJECT_ID"): registry.register(item)

def test_health_does_not_claim_live_connection():
    service=StorageEcosystemService(); assert service.health()["status"]=="FOUNDATION_READY"
    assert service.health()["external_connections_verified"] is False
    assert service.describe()["connection_state"]=="NOT_CONFIGURED"

def test_service_rejects_wrong_ecosystem():
    with pytest.raises(ValueError,match="RECORD_PROVIDER_OR_ECOSYSTEM_MISMATCH"):
        StorageEcosystemService().register_metadata(record(ecosystem_id="wrong"))
