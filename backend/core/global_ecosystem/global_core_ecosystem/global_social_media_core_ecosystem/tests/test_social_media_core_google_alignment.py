from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.global_social_media_core_ecosystem import (
    GlobalSocialMediaCoreService, TenantContext, get_platform, list_platforms,
)
ROOT = Path(__file__).resolve().parents[1]

def test_platform_inventory_matches_preserved_direct_child_packages():
    packages = {p.name for p in ROOT.iterdir() if p.is_dir() and p.name.endswith("_social_media_core_ecosystem")}
    records = {item["core_folder"] for item in list_platforms()}
    assert len(list_platforms()) == 113
    assert packages == records

def test_google_core_package_layout_is_present_for_every_platform():
    required = {"README.md", "__init__.py", "contracts.py", "ecosystem_config.py", "ecosystem_manifest.json", "service.py",
                "authentication", "capabilities", "docs", "events", "lifecycle", "models", "schemas", "security", "services", "tests"}
    for record in list_platforms():
        package = ROOT / record["core_folder"]
        assert required <= {item.name for item in package.iterdir()}

def test_catalog_service_is_metadata_only():
    result = GlobalSocialMediaCoreService().status()
    assert result["ecosystem_id"] == "GLOBAL-SOCIAL-MEDIA-CORE-ECOSYSTEM"
    assert result["platforms"]["platform_count"] == 113
    assert result["live_connections_verified"] == 0
    assert result["api_transport_in_core"] is False

def test_platform_lookup_is_stable_and_disconnected():
    assert get_platform("instagram")["name"] == "Instagram"
    status = GlobalSocialMediaCoreService().platform_service("instagram").status()
    assert status["connected"] is False
    assert status["api_call_performed"] is False

def test_tenant_context_is_required_and_capability_is_allowlisted():
    service = GlobalSocialMediaCoreService().platform_service("facebook")
    denied = service.authorize_capability("PROFILE_METADATA_BOUNDARY", None)
    assert denied["success"] is False
    unknown = service.authorize_capability("UNRECOGNIZED_ACTION", TenantContext("tenant-1", "actor-1"))
    assert unknown["success"] is False
    passed = service.authorize_capability("PROFILE_METADATA_BOUNDARY", TenantContext("tenant-1", "actor-1"))
    assert passed["success"] is True
