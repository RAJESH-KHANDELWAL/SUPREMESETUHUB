import pytest
from ..models import StorageObjectRecord
from ..registry import StorageMetadataRegistry
from ..service import StorageEcosystemService

def record(**kw):
    v={"provider_id":"adobe","ecosystem_id":"express","object_id":"obj-1","name":"sample","size_bytes":10};v.update(kw);return StorageObjectRecord(**v)
def test_validation():
    with pytest.raises(ValueError):record(object_id="")
    with pytest.raises(ValueError):record(size_bytes=-1)
def test_registry_duplicate():
    r=StorageMetadataRegistry();x=record();r.register(x)
    with pytest.raises(ValueError,match="DUPLICATE_OBJECT_ID"):r.register(x)
def test_health_boundary():
    s=StorageEcosystemService();assert s.health()["status"]=="FOUNDATION_READY";assert not s.health()["external_connections_verified"];assert s.describe()["connection_state"]=="NOT_CONFIGURED"
def test_namespace_guard():
    with pytest.raises(ValueError,match="RECORD_PROVIDER_OR_ECOSYSTEM_MISMATCH"):StorageEcosystemService().register_metadata(record(ecosystem_id="wrong"))
