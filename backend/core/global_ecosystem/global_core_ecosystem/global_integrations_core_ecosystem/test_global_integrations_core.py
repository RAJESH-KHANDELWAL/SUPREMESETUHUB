"""Structural and behavior tests for Global Integrations Core."""
import importlib
import json
from pathlib import Path
from .catalog import get_catalog,get_integration,get_provider,search_catalog
from .manager import get_manager
from .policy import IntegrationPolicyError,redact_sensitive_metadata,validate_domain_access
from .registry import INTEGRATION_DOMAIN_ROWS,PROVIDER_ROWS,validate_registry

def test_registry_and_manifest_are_consistent():
    validate_registry()
    manifest=json.loads(Path(__file__).with_name("ecosystem_manifest.json").read_text(encoding="utf-8"))
    assert len(INTEGRATION_DOMAIN_ROWS)==manifest["integration_domain_count"]==31
    assert len(PROVIDER_ROWS)==manifest["provider_family_count"]
    assert {x["id"] for x in manifest["domains"]}=={x["id"] for x in INTEGRATION_DOMAIN_ROWS}

def test_master_catalog_is_referenced_not_duplicated():
    data=get_catalog()
    assert data["source_of_truth"]=="backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    assert data["master_catalog_policy"]=="REFERENCE_ONLY_NO_ENTRY_COPYING"
    assert data["integration_domain_count"]==31

def test_lookup_search_and_all_domain_managers():
    assert get_integration("GOOGLE")["folder"]=="google_integrations_core_ecosystem"
    assert get_provider("google")["display_name"]=="Google"
    assert search_catalog("identity")
    package=__package__
    for row in INTEGRATION_DOMAIN_ROWS:
        module=importlib.import_module(f"{package}.{row['folder']}")
        manager=module.get_manager()
        assert manager.status()["domain_id"]==row["id"]
        assert manager.status()["live_connection_verified"] is False
        assert manager.describe()["capabilities"]==row["capabilities"]

def test_manager_health_and_dependency_boundaries():
    manager=get_manager()
    assert manager.health()["integration_domain_count"]==31
    assert manager.status()["provider_execution_enabled"] is False
    assert "API" in manager.dependency_map()["delegates_to"]

def test_sensitive_metadata_is_redacted_recursively():
    assert redact_sensitive_metadata({"name":"ok","access_token":"x","nested":{"email":"x","count":2}})=={"name":"ok","nested":{"count":2}}

def test_restricted_domain_requires_assurance_consent_and_authorization():
    domain=get_integration("ADULT_AGE_VERIFICATION_CONSENT")
    try: validate_domain_access(domain)
    except IntegrationPolicyError as exc: assert str(exc)=="AGE_ASSURANCE_REQUIRED"
    else: raise AssertionError("age assurance must be required")
    validate_domain_access(domain,age_assurance_verified=True,consent_verified=True,explicitly_authorized=True)

def test_no_live_connectivity_or_execution_is_claimed():
    health=get_manager().health()
    assert health["live_connections_verified"]==0
    assert health["api_calls_performed"]==0
    assert get_manager().catalog()["execution_enabled"] is False
