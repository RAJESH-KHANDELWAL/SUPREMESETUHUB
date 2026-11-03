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
