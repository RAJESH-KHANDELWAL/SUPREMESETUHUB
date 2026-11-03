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

