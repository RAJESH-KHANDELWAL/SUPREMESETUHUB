"""Regression tests for canonical record types and taxonomy API packages."""
from ..classification_registry import list_record_classes
from ..entity_registry import classify_entity_type
from ..industry_api_ecosystems.registry import list_industries,validate_industry_registry
from ..sectors.catalog import list_sectors,validate_sector_catalog
from ..provider_api_ecosystems.service import list_providers,get_provider_status
from ..routes import router

def test_enterprise_is_canonical_and_business_is_legacy_name():
    classes={item["record_type"] for item in list_record_classes()}
    assert classes=={"company","enterprise","corporate_group"}
    assert classify_entity_type("small_business")=="enterprise"
    assert classify_entity_type("corporate_group")=="corporate_group"
    assert classify_entity_type("freelancer") is None

def test_industry_taxonomy_is_nonempty_and_unique():
    assert validate_industry_registry()["structurally_valid"]
    assert len(list_industries()) >= 15

def test_sector_taxonomy_is_nonempty_and_unique():
    assert validate_sector_catalog()["structurally_valid"]
    assert len(list_sectors()) >= 10

def test_provider_directory_does_not_claim_live_adapters():
    assert len(list_providers()) >= 3
    assert get_provider_status()["live_company_data_connected"] is False

def test_new_company_directory_routes_are_mounted():
    paths={route.path for route in router.routes}
    assert "/global/company-directory/industries" in paths
    assert "/global/company-directory/sectors" in paths
    assert "/global/company-directory/countries" in paths
    assert "/global/company-directory/providers" in paths
    assert "/global/company-directory/enterprises/catalog" in paths
