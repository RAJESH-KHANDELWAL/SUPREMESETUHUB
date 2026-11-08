"""Tests for canonical Bada Business Ecosystem platform resources."""
from backend.bada_business_ecosystem import (
    ECOSYSTEM,
    get_platform_resource_catalog,
)
from backend.api.global_ecosystem.global_api_ecosystem.bada_business_api_ecosystem.catalog import (
    get_catalog as get_legacy_catalog,
)


def test_canonical_ecosystem_identity_and_links():
    catalog = get_platform_resource_catalog()
    assert ECOSYSTEM["name"] == "BADA BUSINESS ECOSYSTEM"
    assert catalog["ecosystem_name"] == "BADA BUSINESS ECOSYSTEM"
    assert catalog["link_count"] >= 4
    urls = {item["url"] for item in catalog["links"]}
    assert "https://www.badabusiness.com/lfp?pp_code=BIRK076336" in urls
    assert "https://www.badabusiness.com/cash-growth-profit?pp_code=BIRK076336" in urls
    assert "https://www.badabusiness.com/ideatoipo?pp_code=BIRK076336" in urls
    assert "https://www.badabusiness.com/digitaldukan/BIRK076336" in urls


def test_programs_are_available_from_canonical_catalog():
    catalog = get_platform_resource_catalog()
    assert {"lfp_digital", "bb_impact", "idea_to_ipo"} == set(catalog["programs"])
    assert catalog["program_count"] == 3


def test_legacy_api_catalog_is_only_a_compatibility_facade():
    canonical = get_platform_resource_catalog()
    legacy = get_legacy_catalog()
    assert legacy["ecosystem_name"] == canonical["ecosystem_name"]
    assert legacy["links"] == canonical["links"]
    assert legacy["programs"] == canonical["programs"]
    assert legacy["official_public_api_verified"] is False
    assert legacy["live_connection_verified"] is False
