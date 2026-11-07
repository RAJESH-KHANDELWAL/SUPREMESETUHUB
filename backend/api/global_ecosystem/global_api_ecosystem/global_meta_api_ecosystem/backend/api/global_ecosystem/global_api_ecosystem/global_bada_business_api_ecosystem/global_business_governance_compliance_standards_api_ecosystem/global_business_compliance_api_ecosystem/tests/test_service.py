from .service import BusinessComplianceService


def test_status_exposes_honest_coverage():
    result = BusinessComplianceService().get_status()
    assert result["india_requirement_topics"] == 12
    assert result["jurisdictions"][1]["coverage_status"] == "framework_only"


def test_india_requirements_and_filtering():
    service = BusinessComplianceService()
    items = service.list_requirements("IN")
    assert len(items) == 12
    assert service.list_requirements("IN", area="tax")[0]["id"] == "tax_registration_and_returns"
    assert service.list_requirements("IN", query="FSSAI")[0]["id"] == "food_business_licensing"


def test_uncurated_country_is_not_fabricated():
    assert BusinessComplianceService().list_requirements("US") is None


def test_unknown_topic_returns_none():
    assert BusinessComplianceService().get_requirement("not_a_real_topic") is None


def test_india_subdivision_index_has_28_states_and_8_union_territories():
    service = BusinessComplianceService()
    states = service.list_india_subdivisions("state")
    uts = service.list_india_subdivisions("union_territory")
    assert len(states) == 28
    assert len(uts) == 8
    assert service.get_india_subdivision("RJ")["name"] == "Rajasthan"


def test_unknown_india_subdivision_is_not_treated_as_curated():
    service = BusinessComplianceService()
    assert service.get_india_subdivision("ZZ") is None
    assert service.list_requirements("IN", subdivision_code="ZZ") is None


def test_unified_country_master_has_india_and_priority_country_profiles():
    service = BusinessComplianceService()
    items = service.list_jurisdictions()
    codes = {item["country_code"] for item in items}
    assert "IN" in codes and "US" in codes and "AE" in codes
    assert len(items) == 14
    assert service.get_jurisdiction("IN")["coverage_status"] == "starter_reference"
    assert service.get_jurisdiction("US")["coverage_status"] == "framework_only"



def test_compliance_rules_have_source_and_review_metadata():
    from .rules_catalog import list_rules
    items = list_rules("IN")
    assert len(items) == 12
    assert all(item["applicability_status"] for item in items)
    assert all(item["rule_status"] == "discovery_topic_only" for item in items)
    assert all(item["last_source_checked_on"] is None for item in items)
    assert all(item["source_link_added_on"] == "2026-11-03" for item in items)
    assert any(item["official_sources"] for item in items)


def test_rule_filtering_and_detail():
    service = BusinessComplianceService()
    tax = service.list_compliance_rules("IN", area="tax")
    assert len(tax) == 1
    assert tax[0]["id"] == "tax_registration_and_returns"
    assert service.get_compliance_rule("food_business_licensing")["official_sources"][0]["url"] == "https://foscos.fssai.gov.in/"


def test_unresearched_country_rules_are_not_fabricated():
    assert BusinessComplianceService().list_compliance_rules("US") is None


def test_rajasthan_state_rules_are_filtered_and_scoped():
    service = BusinessComplianceService()
    items = service.list_compliance_rules("IN", subdivision_code="RJ")
    state_items = [item for item in items if item["subdivision_code"] == "RJ"]
    assert len(state_items) == 6
    assert all(item["country_code"] == "IN" for item in state_items)
    assert service.get_compliance_rule("rajasthan_fire_noc", "IN", "RJ")["subdivision_code"] == "RJ"
    assert service.get_compliance_rule("rajasthan_fire_noc", "IN") is None


def test_rajasthan_rules_have_official_sources_and_review_metadata():
    from .rules_catalog import list_rules
    items = [item for item in list_rules("IN", subdivision_code="RJ") if item["subdivision_code"] == "RJ"]
    assert len(items) == 6
    assert all(item["official_sources"] for item in items)
    assert all(item["last_source_checked_on"] is None for item in items)
    assert all(item["legal_review_status"] == "not_legal_reviewed" for item in items)


def test_subdivision_filter_includes_national_and_matching_state_records_only():
    from .rules_catalog import list_rules
    items = list_rules("IN", subdivision_code="RJ")
    assert any(item["subdivision_code"] is None for item in items)
    assert any(item["subdivision_code"] == "RJ" for item in items)
    assert not any(item["subdivision_code"] not in (None, "RJ") for item in items)
