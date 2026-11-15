import pytest
from adobe_experience_manager_assets_storage_ecosystem.models import StorageObjectRecord
from adobe_experience_manager_assets_storage_ecosystem.registry import StorageMetadataRegistry
from adobe_experience_manager_assets_storage_ecosystem.service import StorageEcosystemService
def rec(**kw):
    v={"provider_id":"adobe","ecosystem_id":"experience_manager_assets","object_id":"obj-1","name":"sample","size_bytes":2};v.update(kw);return StorageObjectRecord(**v)
def test_model_validation():
    with pytest.raises(ValueError):rec(object_id="")
    with pytest.raises(ValueError):rec(size_bytes=-1)
def test_registry_guards_duplicate():
    r=StorageMetadataRegistry();x=rec();r.register(x)
    with pytest.raises(ValueError,match="DUPLICATE_OBJECT_ID"):r.register(x)
def test_health_is_catalog_only():
    s=StorageEcosystemService();assert s.health()["status"]=="FOUNDATION_READY";assert not s.health()["external_connections_verified"];assert s.describe()["connection_state"]=="NOT_CONFIGURED"
def test_service_checks_namespace():
    with pytest.raises(ValueError,match="RECORD_PROVIDER_OR_ECOSYSTEM_MISMATCH"):StorageEcosystemService().register_metadata(rec(ecosystem_id="wrong"))
