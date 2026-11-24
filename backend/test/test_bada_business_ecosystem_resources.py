"""Tests for the Global Bada Business ecosystem and external platform catalog."""
from backend.global_ecosystem.global_bada_business_ecosystem import (
    ECOSYSTEM,
    BADA_BUSINESS_ECOSYSTEM_ID,
    BADA_BUSINESS_ECOSYSTEM_NAME,
)
from backend.global_ecosystem.global_bada_business_ecosystem.platform_resources import (
    OFFICIAL_PUBLIC_API_VERIFIED,
    LIVE_CONNECTION_VERIFIED,
    get_catalog,
    get_program,
    list_programs,
)


def test_global_and_platform_ecosystem_identities_are_distinct():
    assert ECOSYSTEM["id"] == "GLOBAL_BADA_BUSINESS_ECOSYSTEM"
    assert ECOSYSTEM["name"] == "GLOBAL BADA BUSINESS ECOSYSTEM"
    assert BADA_BUSINESS_ECOSYSTEM_ID == "BADA_BUSINESS_ECOSYSTEM"
    assert BADA_BUSINESS_ECOSYSTEM_NAME == "BADA BUSINESS ECOSYSTEM"


def test_canonical_platform_resource_catalog():
    catalog = get_catalog()
    assert catalog["ecosystem_id"] == BADA_BUSINESS_ECOSYSTEM_ID
    assert catalog["ecosystem_name"] == BADA_BUSINESS_ECOSYSTEM_NAME
    assert catalog["status"] == "RESOURCE_CATALOG_ONLY"
    assert catalog["link_count"] == 9
    assert catalog["program_count"] == 3
    assert OFFICIAL_PUBLIC_API_VERIFIED is False
    assert LIVE_CONNECTION_VERIFIED is False


def test_program_lookup_and_listing():
    assert get_program("lfp_digital") is not None
    assert get_program("IDEA_TO_IPO") is not None
    assert len(list_programs()) == 3
