import pytest
from adobe_workfront_storage_ecosystem.models import StorageObjectRecord
from adobe_workfront_storage_ecosystem.registry import StorageMetadataRegistry
from adobe_workfront_storage_ecosystem.service import StorageEcosystemService
def rec(**kw):
    v={"provider_id":"adobe","ecosystem_id":"workfront","object_id":"obj-1","name":"sample","size_bytes":1};v.update(kw);return StorageObjectRecord(**v)
def test_model_validation():
    with pytest.raises(ValueError):rec(object_id="")
    with pytest.raises(ValueError):rec(size_bytes=-1)
def test_registry_duplicate_guard():
    r=StorageMetadataRegistry();x=rec();r.register(x)
    with pytest.raises(ValueError,match="DUPLICATE_OBJECT_ID"):r.register(x)
def test_readiness_not_live_connection():
    s=StorageEcosystemService();assert s.health()["status"]=="FOUNDATION_READY";assert not s.health()["external_connections_verified"];assert s.describe()["connection_state"]=="NOT_CONFIGURED"
def test_wrong_ecosystem_rejected():
    with pytest.raises(ValueError,match="RECORD_PROVIDER_OR_ECOSYSTEM_MISMATCH"):StorageEcosystemService().register_metadata(rec(ecosystem_id="wrong"))
