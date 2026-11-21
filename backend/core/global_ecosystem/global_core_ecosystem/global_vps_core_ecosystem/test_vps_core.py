"""Structural and behavior tests for Global VPS Core."""
import importlib
from pathlib import Path
import pytest
from .catalog import PROVIDERS, get_catalog
from .contracts import validate_request
from .domain_catalog import DOMAIN_DEFINITIONS, domain_summary
from .domain_runtime import VPSCoreDomainManager
from .master_catalog import get_master_catalog_mapping
from .manager import get_manager
ROOT = Path(__file__).resolve().parent
EXPECTED_PROVIDER_FILES = {"README.md", "__init__.py", "provider.py", "contracts.py"}
def test_provider_inventory_and_packages():
    assert len(PROVIDERS) == 20
    assert len({p["provider_id"] for p in PROVIDERS}) == 20
    for provider in PROVIDERS:
        folder = ROOT / provider["directory"]
        assert folder.is_dir()
        assert {item.name for item in folder.iterdir() if item.is_file()} == EXPECTED_PROVIDER_FILES
        module = importlib.import_module(f"{__package__}.{provider['directory']}.provider")
        contract = importlib.import_module(f"{__package__}.{provider['directory']}.contracts")
        assert module.get_provider()["provider_id"] == provider["provider_id"]
        assert module.health()["live_connection_verified"] is False
        assert contract.validate_request({"operation": "describe"})["validated_only"] is True
def test_domains_and_runtime():
    assert len(DOMAIN_DEFINITIONS) == 16
    assert domain_summary()["domain_count"] == 16
    for key in DOMAIN_DEFINITIONS:
        assert VPSCoreDomainManager(key).list_offerings()["count"] == 20
def test_manager_status_is_not_live():
    manager = get_manager()
    assert manager.status()["provider_count"] == 20
    assert manager.health()["connected_provider_count"] == 0
    assert get_catalog()["live_connection_verified"] is False
def test_contract_blocks_secrets_and_unknown_provider():
    with pytest.raises(ValueError, match="SECRET_MATERIAL"):
        validate_request({"provider_id": "aws", "api_key": "x"})
    with pytest.raises(ValueError, match="UNKNOWN_VPS_PROVIDER"):
        validate_request({"provider_id": "not-a-provider"})
def test_provider_contract_enforces_its_own_identity():
    module = importlib.import_module(f"{__package__}.aws_vps_core_ecosystem.contracts")
    with pytest.raises(ValueError, match="PROVIDER_CONTEXT_MISMATCH"):
        module.validate_request({"provider_id": "google", "operation": "describe"})
def test_master_mapping_does_not_expand_taxonomy():
    mapping = get_master_catalog_mapping()
    assert mapping["success"] and mapping["target_unique_entries"] == 2468
    assert mapping["taxonomy_entries_added"] == 0
    assert {entry["entry_id"] for entry in mapping["entries"]} == {"S09_cloud_computing", "S10_global_server"}
