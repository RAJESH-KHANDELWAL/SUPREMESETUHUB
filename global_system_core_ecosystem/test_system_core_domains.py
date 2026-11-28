"""Structural and behavior tests for the Global System Core Ecosystem."""
from __future__ import annotations
import importlib
from .catalog import list_system_providers
from .domain_catalog import DOMAIN_DEFINITIONS, system_domain_summary
from .domain_runtime import SystemCoreDomainManager
from .product_catalog import list_system_products
from .manager import get_manager


def test_provider_and_product_inventory_is_consistent():
    providers = list_system_providers()
    products = list_system_products()
    provider_ids = {item["provider_id"] for item in providers}
    assert len(provider_ids) == len(providers)
    assert products
    assert all(item["provider_id"] in provider_ids for item in products)
    assert all(item["domain_ids"] for item in products)


def test_every_provider_package_exports_a_working_manager():
    package_root = "backend.core.global_ecosystem.global_core_ecosystem.global_system_core_ecosystem"
    for provider in list_system_providers():
        package = importlib.import_module(f'{package_root}.{provider["provider_id"]}_system_core_ecosystem')
        manager = package.get_manager()
        assert manager.status()["provider_id"] == provider["provider_id"]
        assert manager.list_products()["success"] is True


def test_every_domain_package_exports_a_working_manager():
    package_root = "backend.core.global_ecosystem.global_core_ecosystem.global_system_core_ecosystem"
    assert len(DOMAIN_DEFINITIONS) == 18
    for domain_id in DOMAIN_DEFINITIONS:
        package_name = f"global_{domain_id.lower()}_core_ecosystem"
        package = importlib.import_module(f"{package_root}.{package_name}")
        manager = package.get_manager()
        assert manager.DOMAIN_ID == domain_id
        assert manager.status()["success"] is True


def test_domain_inventory_counts_match_domain_managers():
    summary = system_domain_summary()
    assert summary["domain_count"] == 18
    for domain in summary["domains"]:
        manager = SystemCoreDomainManager(domain["domain_id"])
        assert manager.list_products()["count"] == domain["product_count"]


def test_public_manager_is_read_only_and_reports_inventory():
    manager = get_manager()
    status = manager.status()
    assert status["success"] is True
    assert status["live_connections_verified"] is False
    assert status["host_operations_performed"] == 0
    assert manager.list_products()["count"] == len(list_system_products())
