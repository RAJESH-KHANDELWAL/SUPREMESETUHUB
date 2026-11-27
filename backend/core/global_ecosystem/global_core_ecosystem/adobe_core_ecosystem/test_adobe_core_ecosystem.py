"""Structural and behavior tests for the Adobe Core Ecosystem."""
from .catalog import get_adobe_core_catalog
from .domain_catalog import adobe_domain_summary, list_adobe_domain_inventory
from .domain_runtime import AdobeCoreDomainManager
from .manager import get_manager


def test_catalog_and_domain_inventory_are_consistent():
    catalog = get_adobe_core_catalog()
    domains = list_adobe_domain_inventory()
    assert catalog["ecosystem_id"] == "ADOBE-CORE-ECOSYSTEM"
    assert len(catalog["children"]) == catalog["product_domain_count"]
    assert len(domains) == len(catalog["children"]) + 1
    assert len({domain["domain_id"] for domain in domains}) == len(domains)


def test_manager_exposes_google_parallel_surface():
    manager = get_manager()
    assert manager.status()["ecosystem_id"] == "ADOBE-CORE-ECOSYSTEM"
    assert manager.health()["live_connections_verified"] == 0
    assert manager.list_products()["count"] == len(get_adobe_core_catalog()["children"])
    assert manager.list_domains()["domain_count"] == len(list_adobe_domain_inventory())
    assert manager.list_domain_inventory()


def test_product_domain_manager_discovers_registered_family():
    manager = AdobeCoreDomainManager("PHOTOSHOP")
    status = manager.status()
    assert status["success"]
    assert status["domain_id"] == "PHOTOSHOP"
    offerings = manager.list_offerings()
    assert offerings["count"] == 1
    assert offerings["offerings"][0]["product_key"] == "photoshop"


def test_provider_governance_domain_is_available():
    manager = AdobeCoreDomainManager("PROVIDER_GOVERNANCE")
    assert manager.status()["success"]
    assert manager.list_offerings()["count"] == 1


def test_unknown_domain_fails_explicitly():
    try:
        AdobeCoreDomainManager("NOT_A_REAL_DOMAIN")
    except ValueError as exc:
        assert "UNKNOWN_ADOBE_CORE_DOMAIN" in str(exc)
    else:
        raise AssertionError("Unknown domain should raise ValueError")
