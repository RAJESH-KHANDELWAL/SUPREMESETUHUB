from . import __name__ as _package_name
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.domain_catalog import get_domains
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.provider_catalog import get_provider_catalog
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.policy import redact_sensitive_metadata
def test_security_taxonomy_and_provider_inventory():
    assert len(get_domains()) == 33
    assert len(get_provider_catalog()) == 6
def test_sensitive_metadata_is_redacted():
    assert redact_sensitive_metadata({"token":"hidden","label":"safe"}) == {"label":"safe"}
