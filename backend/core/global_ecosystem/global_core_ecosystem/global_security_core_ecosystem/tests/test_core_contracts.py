from . import __name__ as _package_name
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.manager import get_domains, get_protected_group_safety
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.provider_catalog import get_provider_catalog
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.policy import redact_sensitive_metadata
def test_security_taxonomy_and_provider_inventory():
    domains = get_domains()
    domain_ids = [item["id"] for item in domains]
    assert len(domains) == 33
    assert len(domain_ids) == len(set(domain_ids))
    assert len({item["folder"] for item in domains}) == len(domains)
    assert len(get_provider_catalog()) == 6

    safety = get_protected_group_safety()
    assert set(safety["groups"]) == {"MEN", "WOMEN", "GIRLS", "BOYS"}
    assert safety["groups"]["GIRLS"]["adult_content_access"] == "PROHIBITED"
    assert safety["groups"]["BOYS"]["adult_content_access"] == "PROHIBITED"
    assert safety["universal_baseline"]["production_enforcement_verified"] is False
def test_sensitive_metadata_is_redacted():
    assert redact_sensitive_metadata({"token":"hidden","label":"safe"}) == {"label":"safe"}
