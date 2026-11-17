"""Structural and safety-boundary integrity checks for Global Security CORE."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_AREAS = {
    "compatibility", "configuration", "contracts", "documentation", "events",
    "exceptions", "orchestration", "security", "testing", "utilities", "validation",
}


def load_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def test_manifest_identity_and_canonical_path():
    manifest = load_json("ecosystem_manifest.json")
    assert manifest["ecosystem_id"] == "GLOBAL-SECURITY-CORE-ECOSYSTEM"
    assert manifest["parent_id"] == "GLOBAL-CORE-ECOSYSTEM"
    assert manifest["layer"] == "CORE"
    assert manifest["status"] == "CORE_CATALOG_ONLY"
    assert manifest["canonical_path"] == str(ROOT.relative_to(ROOT.parents[4])).replace("\\", "/")


def test_domain_catalog_matches_manifest_and_has_unique_ids():
    manifest = load_json("ecosystem_manifest.json")
    catalog = load_json("catalog.json")
    domains = catalog["domains"]
    ids = [item["id"] for item in domains]
    assert catalog["ecosystem_id"] == manifest["ecosystem_id"]
    assert len(domains) == manifest["domain_count"] == 18
    assert len(ids) == len(set(ids))
    assert catalog["domain_coverage_exhaustive"] is False


def test_provider_catalog_matches_provider_packages():
    manifest = load_json("ecosystem_manifest.json")
    catalog = load_json("provider_catalog.json")
    providers = catalog["providers"]
    provider_ids = [item["provider_id"] for item in providers]
    assert len(providers) == manifest["provider_count"] == 6
    assert len(provider_ids) == len(set(provider_ids))
    assert catalog["provider_coverage_exhaustive"] is False

    for provider in providers:
        folder = provider["folder"]
        package = ROOT / folder
        provider_manifest = json.loads(
            (package / "provider_manifest.json").read_text(encoding="utf-8")
        )
        assert package.is_dir()
        assert provider_manifest["provider_id"] == provider["provider_id"]
        assert provider_manifest["ecosystem_id"] == provider["ecosystem_id"]
        assert provider_manifest["parent_id"] == manifest["ecosystem_id"]
        assert provider_manifest["status"] == "CORE_CATALOG_ONLY"
        assert provider_manifest["live_connection_verified"] is False
        assert provider_manifest["api_calls_performed"] == 0
        assert provider_manifest["credential_storage"] == "EXTERNAL_SECRET_STORE_ONLY"


def test_shared_support_directories_match_manifest():
    manifest = load_json("ecosystem_manifest.json")
    declared = set(manifest["shared_support_areas"])
    actual = {path.name for path in (ROOT / "shared_support").iterdir() if path.is_dir()}
    assert declared == EXPECTED_AREAS
    assert actual == declared
    assert all((ROOT / "shared_support" / area / "README.md").is_file() for area in declared)


def test_security_boundary_is_explicit_and_non_operational():
    manifest = load_json("ecosystem_manifest.json")
    assert manifest["api_calls_performed"] == 0
    assert manifest["live_provider_connections_verified"] is False
    assert manifest["security_enforcement_verified"] is False
    assert manifest["credential_storage"] == "EXTERNAL_SECRET_STORE_ONLY"
    assert manifest["security_baseline"]["secrets_in_core"] is False
    assert set(manifest["layer_boundaries"]) == {
        "core", "api", "storage", "database", "runtime", "application"
    }


def test_policy_redacts_common_secret_and_personal_data_key_variants():
    from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.policy import (
        redact_sensitive_metadata,
    )

    source = {
        "api_key": "hidden",
        "accessToken": "hidden",
        "secret_value": "hidden",
        "private-key": "hidden",
        "email_address": "hidden",
        "phoneNumber": "hidden",
        "display_name": "visible",
        "nested": {"password_hash": "hidden", "region": "visible"},
    }
    assert redact_sensitive_metadata(source) == {
        "display_name": "visible",
        "nested": {"region": "visible"},
    }
