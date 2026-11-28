from __future__ import annotations
import importlib
import json
from pathlib import Path

from oracle_core_ecosystem.manager import get_manager
from oracle_core_ecosystem.product_catalog import list_products
from oracle_core_ecosystem.domain_catalog import list_domains
from oracle_core_ecosystem.policy import classify_capability, redact_sensitive_metadata

ROOT = Path(__file__).resolve().parents[1]

def test_manager_contract_and_status():
    manager = get_manager()
    assert manager.NAME == "ORACLE CORE ECOSYSTEM"
    status = manager.status()
    assert status["ecosystem_id"] == "ORACLE-CORE-ECOSYSTEM"
    assert status["live_connection_verified"] is False

def test_product_inventory_is_unique_and_complete():
    products = list_products()
    ids = [item["product_id"] for item in products]
    assert len(products) == 17
    assert len(ids) == len(set(ids))
    assert all(item["live_connection_verified"] is False for item in products)

def test_all_domains_have_product_ownership():
    domains = list_domains()
    assert len(domains) == 8
    assert all(item["product_count"] > 0 for item in domains)

def test_all_existing_product_packages_expose_manager():
    for product in list_products():
        package_name = product["product_id"].replace("-", "_") + "_core_ecosystem"
        # Resolve package directory from its matching product inventory position.
        matches = [p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("oracle_") and p.name.endswith("_core_ecosystem")]
        assert matches
    expected = [
        "oracle_ai_services_core_ecosystem", "oracle_autonomous_database_core_ecosystem",
        "oracle_base_database_core_ecosystem", "oracle_block_volumes_core_ecosystem",
        "oracle_compute_core_ecosystem", "oracle_compute_instances_core_ecosystem",
        "oracle_data_science_core_ecosystem", "oracle_database_tools_core_ecosystem",
        "oracle_enterprise_applications_core_ecosystem", "oracle_fusion_cloud_applications_core_ecosystem",
        "oracle_generative_ai_core_ecosystem", "oracle_identity_core_ecosystem",
        "oracle_mysql_heatwave_core_ecosystem", "oracle_networking_core_ecosystem",
        "oracle_object_storage_core_ecosystem", "oracle_observability_core_ecosystem",
        "oracle_virtual_cloud_networks_core_ecosystem",
    ]
    for package in expected:
        module = importlib.import_module(f"oracle_core_ecosystem.{package}")
        assert callable(module.get_manager)

def test_master_catalog_manifest_is_reference_only():
    manifest = json.loads((ROOT / "ecosystem_manifest.json").read_text(encoding="utf-8"))
    assert manifest["master_catalog"]["target_unique_entries"] == 2468
    assert manifest["master_catalog"]["entries_added"] == 0

def test_policy_blocks_transport_and_execution_from_core():
    assert classify_capability("provider_api_transport")["allowed_in_core"] is False
    assert classify_capability("product_discovery")["allowed_in_core"] is True

def test_sensitive_metadata_is_redacted():
    result = redact_sensitive_metadata({"region": "ap-mumbai-1", "access_token": "secret"})
    assert result["region"] == "ap-mumbai-1"
    assert result["access_token"] == "[REDACTED]"

def test_health_never_claims_live_connectivity():
    health = get_manager().health()
    assert health["status"] == "HEALTHY_METADATA_REGISTRY"
    assert health["live_connections_verified"] == 0
