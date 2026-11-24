from backend.core.global_ecosystem.global_core_ecosystem.global_server_core_ecosystem.catalog import get_catalog
from backend.core.global_ecosystem.global_core_ecosystem.global_server_core_ecosystem.provider_catalog import get_provider
def test_catalog_has_seven_provider_domains():
    data=get_catalog()
    assert data["provider_count"] == 7
    assert data["remote_operations_enabled"] is False
def test_all_registered_providers_have_metadata():
    data=get_catalog()
    assert all(item["folder"] and item["capabilities"] for item in data["providers"])
    assert get_provider("AWS")["provider_id"] == "AWS"

def test_service_rejects_unknown_provider_and_environment():
    from backend.core.global_ecosystem.global_core_ecosystem.global_server_core_ecosystem.service import ServerCoreService
    service=ServerCoreService()
    payload={"server_id":"test-node","provider_id":"UNKNOWN","server_type":"vps","server_role":"app","country":"IN","region":"test-region","environment":"test","metadata":{}}
    assert service.validate_identity(payload)["success"] is False
    payload["provider_id"]="aws"
    payload["environment"]="sandbox"
    assert service.validate_identity(payload)["success"] is False
