import pytest
from adobe_document_cloud_storage_ecosystem.models import StorageObjectRecord
from adobe_document_cloud_storage_ecosystem.registry import StorageMetadataRegistry
from adobe_document_cloud_storage_ecosystem.service import StorageEcosystemService
def record(**kw):
    v={"provider_id":"adobe","ecosystem_id":"document_cloud","object_id":"obj-1","name":"sample","size_bytes":10}; v.update(kw); return StorageObjectRecord(**v)
def test_validation():
    with pytest.raises(ValueError): record(object_id="")
    with pytest.raises(ValueError): record(size_bytes=-1)
def test_registry_duplicate_guard():
    r=StorageMetadataRegistry(); x=record(); assert r.register(x)["object_id"]=="obj-1"
    with pytest.raises(ValueError,match="DUPLICATE_OBJECT_ID"): r.register(x)
def test_readiness_not_live_connection():
    s=StorageEcosystemService(); assert s.health()["status"]=="FOUNDATION_READY"; assert not s.health()["external_connections_verified"]; assert s.describe()["connection_state"]=="NOT_CONFIGURED"
def test_mismatch_rejected():
    with pytest.raises(ValueError,match="RECORD_PROVIDER_OR_ECOSYSTEM_MISMATCH"): StorageEcosystemService().register_metadata(record(ecosystem_id="other"))
