import pytest
from adobe_creative_cloud_assets_storage_ecosystem.models import StorageObjectRecord
from adobe_creative_cloud_assets_storage_ecosystem.registry import StorageMetadataRegistry
from adobe_creative_cloud_assets_storage_ecosystem.service import StorageEcosystemService

def record(**kw):
    data={"provider_id":"adobe","ecosystem_id":"creative_cloud_assets","object_id":"obj-1","name":"sample","size_bytes":10}; data.update(kw); return StorageObjectRecord(**data)
def test_validation():
    with pytest.raises(ValueError): record(object_id="")
    with pytest.raises(ValueError): record(size_bytes=-1)
def test_registry_and_duplicate_guard():
    r=StorageMetadataRegistry(); item=record(); assert r.register(item)["object_id"]=="obj-1"; assert r.get("obj-1")["name"]=="sample"
    with pytest.raises(ValueError,match="DUPLICATE_OBJECT_ID"): r.register(item)
def test_health_is_not_live_connection():
    s=StorageEcosystemService(); assert s.health()["status"]=="FOUNDATION_READY"; assert s.health()["external_connections_verified"] is False; assert s.describe()["connection_state"]=="NOT_CONFIGURED"
def test_wrong_ecosystem_rejected():
    with pytest.raises(ValueError,match="RECORD_PROVIDER_OR_ECOSYSTEM_MISMATCH"): StorageEcosystemService().register_metadata(record(ecosystem_id="other"))
