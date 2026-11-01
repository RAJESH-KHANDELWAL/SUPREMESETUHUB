"""Regression tests for canonical record types and taxonomy API packages."""
from ..classification_registry import list_record_classes
from ..entity_registry import classify_entity_type
from ..industry_api_ecosystems.registry import list_industries,validate_industry_registry
from ..sectors.catalog import list_sectors,validate_sector_catalog
from ..provider_api_ecosystems.service import list_providers,get_provider_status
from ..routes import router
from ..integrations.catalog import list_integrations,get_integration_status
from ..services.catalog import list_services
from ..tools.tools import classify_entity,validate_registry_payload,find_duplicate_ids

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

def test_integrations_and_services_have_real_catalogue_entries():
    assert len(list_integrations()) >= 5
    assert get_integration_status()["live_connections"] is False
    assert len(list_services()) >= 7

def test_company_directory_tools_are_deterministic():
    assert classify_entity("small_business")["record_type"] == "enterprise"
    assert validate_registry_payload({"company_id":"c1","name":"Example","entity_type":"registered_company"})["valid"]
    assert not validate_registry_payload({"company_id":"c1","name":"Example","entity_type":"registered_company","verification_status":"registry_verified"})["valid"]
    assert find_duplicate_ids([{"company_id":"x"},{"company_id":"x"}]) == ["x"]

def test_integration_service_and_tool_routes_are_mounted():
    paths={route.path for route in router.routes}
    assert "/global/company-directory/integrations" in paths
    assert "/global/company-directory/services" in paths
    assert "/global/company-directory/tools" in paths
    assert "/global/company-directory/tools/classify/{entity_type}" in paths


def test_openai_company_profile_is_source_aware_and_route_is_mounted():
    from ..global_companies_ecosystem.openai.service import get_company_profile
    profile = get_company_profile()
    assert profile["company_id"] == "openai"
    assert profile["record_type"] == "company"
    assert profile["data_status"] == "no_verified_profile_record"
    assert profile["sources"][0]["url"] == "https://openai.com/"
    assert profile["sources"][0]["live_connection"] is False
    paths = {route.path for route in router.routes}
    assert "/global/company-profile-adapters/openai" in paths
    assert "/global/company-directory/company-profiles/openai/sources" in paths


def test_company_profile_directory_covers_all_26_without_fabricating_verification():
    from ..company_profile_directory import COMPANIES, _profile
    assert len(COMPANIES) == 26
    for company_id in COMPANIES:
        profile = _profile(company_id)
        assert profile["record_type"] == "company"
        assert profile["profile_status"] == "source_registered_unverified"
        assert profile["data_status"] == "no_verified_profile_record"
        assert profile["sources"][0]["live_connection"] is False
    paths = {route.path for route in router.routes}
    assert "/global/company-directory/company-profiles" in paths
    assert "/global/company-directory/company-profiles/{company_id}" in paths


def test_all_26_company_profile_adapters_are_mounted_and_source_aware():
    from ..global_companies_ecosystem.routes import COMPANY_ADAPTER_IDS, router as adapters_router
    from ..global_companies_ecosystem import adobe, alibaba, amazon, apple, atlassian, aws, bytedance, cisco, cloudflare, github, google, ibm, intel, meta, microsoft, netflix, nvidia, openai, oracle, paypal, salesforce, samsung, shopify, stripe, tencent, zoom
    assert len(COMPANY_ADAPTER_IDS) == 26
    assert len(set(COMPANY_ADAPTER_IDS)) == 26
    for company_id in COMPANY_ADAPTER_IDS:
        package = __import__(f"backend.api.global_ecosystem.global_api_ecosystem.global_company_companies_api_ecosystem.global_companies_ecosystem.{company_id}", fromlist=["router"])
        paths = {route.path for route in package.router.routes}
        assert f"/global/company-profile-adapters/{company_id}" in paths
        assert f"/global/company-profile-adapters/{company_id}/sources" in paths
        assert f"/global/company-profile-adapters/{company_id}/status" in paths
    packages = [adobe, alibaba, amazon, apple, atlassian, aws, bytedance, cisco, cloudflare, github, google, ibm, intel, meta, microsoft, netflix, nvidia, openai, oracle, paypal, salesforce, samsung, shopify, stripe, tencent, zoom]
    for package in packages:
        profile = package.get_profile()
        assert profile["record_type"] == "company"
        assert profile["profile_status"] == "source_registered_unverified"
        assert profile["data_status"] in {"no_verified_profile_record", "no_verified_legal_entity_record"}
        assert profile["sources"] and profile["sources"][0]["live_connection"] is False
        assert package.get_adapter_status()["live_connection"] is False
