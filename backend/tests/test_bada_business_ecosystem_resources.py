"""Tests for the canonical nested Bada Business ecosystem and compatibility imports."""
from backend.bada_business_ecosystem import ECOSYSTEM
from backend.bada_business_ecosystem.global_bada_business_ecosystem import (
    ECOSYSTEM as GLOBAL_ECOSYSTEM,
    get_catalog,
    get_platform_resource_catalog,
)
from backend.api.global_ecosystem.global_api_ecosystem.bada_business_api_ecosystem.catalog import (
    get_catalog as get_legacy_catalog,
)

def test_top_level_and_child_ecosystem_hierarchy():
    assert ECOSYSTEM["id"] == "BADA_BUSINESS_ECOSYSTEM"
    assert "GLOBAL_BADA_BUSINESS_ECOSYSTEM" in ECOSYSTEM["child_ecosystems"]
    assert GLOBAL_ECOSYSTEM["id"] == "GLOBAL_BADA_BUSINESS_ECOSYSTEM"
    assert GLOBAL_ECOSYSTEM["parent"] == "BADA_BUSINESS_ECOSYSTEM"

def test_canonical_child_catalog_links_and_programs():
    catalog = get_catalog()
    assert get_platform_resource_catalog() == catalog
    assert catalog["ecosystem_id"] == "GLOBAL_BADA_BUSINESS_ECOSYSTEM"
    assert catalog["ecosystem_name"] == "GLOBAL BADA BUSINESS ECOSYSTEM"
    assert catalog["link_count"] >= 4
    urls = {item["url"] for item in catalog["links"]}
    assert "https://www.badabusiness.com/lfp?pp_code=BIRK076336" in urls
    assert "https://www.badabusiness.com/cash-growth-profit?pp_code=BIRK076336" in urls
    assert "https://www.badabusiness.com/ideatoipo?pp_code=BIRK076336" in urls
    assert "https://www.badabusiness.com/digitaldukan/BIRK076336" in urls
    assert {"lfp_digital", "bb_impact", "idea_to_ipo"} == set(catalog["programs"])

def test_old_api_resource_catalog_remains_compatible():
    canonical = get_catalog()
    legacy = get_legacy_catalog()
    assert legacy["links"] == canonical["links"]
    assert legacy["programs"] == canonical["programs"]
    assert legacy["official_public_api_verified"] is False
    assert legacy["live_connection_verified"] is False
