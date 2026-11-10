"""Coverage tests for the Bharat-to-global AI domain catalog."""
import importlib
from .domain_catalog import list_domain_ids, list_domain_profiles

def test_domain_catalog_and_package_coverage():
    ids = list_domain_ids()
    assert len(ids) == len(set(ids)) == 28
    for profile in list_domain_profiles():
        assert "basic_normal" in profile["maturity"]
        assert "frontier_supreme" in profile["maturity"]
        assert "bharat_india" in profile["geographic_scope"]
        assert "global_cross_border" in profile["geographic_scope"]
    for domain_id in ids:
        module = importlib.import_module(f"{__package__}.domains.{domain_id}_ecosystem")
        assert module.DOMAIN_ID == domain_id
        assert module.DOMAIN_PROFILE["id"] == domain_id

def test_adult_domain_guardrails():
    for domain_id in ("relationships_intimacy", "adult_entertainment", "porn_platform_governance"):
        profile = next(p for p in list_domain_profiles() if p["id"] == domain_id)
        assert profile["status"] == "POLICY_GATED_SCOPE"
        assert "no_minors" in profile["safeguards"]
        assert "informed_consent" in profile["safeguards"]
