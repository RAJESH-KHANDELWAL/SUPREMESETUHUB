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
    assert len(domains) == manifest["domain_count"] == 33
    assert len(ids) == len(set(ids))
    assert catalog["domain_coverage_exhaustive"] is False
    assert catalog["taxonomy"]["domain_count"] == 33
    assert catalog["taxonomy"]["control_area_count"] == 330
    assert catalog["taxonomy"]["coverage_areas_per_domain"] == 10
    area_ids = [area["area_id"] for domain in domains for area in domain["coverage_areas"]]
    assert len(area_ids) == 330
    assert len(area_ids) == len(set(area_ids))
    assert all(area["scope"].strip() for domain in domains for area in domain["coverage_areas"])
    assert len({item["folder"] for item in domains}) == len(domains)
    for item in domains:
        package = ROOT / item["folder"]
        assert package.is_dir()
        assert package.parent == ROOT
        assert package.name.endswith("_core_ecosystem")
        assert (package / "__init__.py").is_file()
        assert (package / "domain_manifest.json").is_file()
        assert (package / "README.md").is_file()
        package_manifest = json.loads((package / "domain_manifest.json").read_text(encoding="utf-8"))
        assert package_manifest["domain_id"] == item["id"]
        assert package_manifest["parent_id"] == manifest["ecosystem_id"]
        assert package_manifest["status"] == "CORE_CATALOG_ONLY"


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


def test_jurisdiction_profiles_are_separate_and_review_gated():
    india = json.loads((ROOT / "jurisdictions/india/jurisdiction_manifest.json").read_text(encoding="utf-8"))
    global_profile = json.loads((ROOT / "jurisdictions/global/jurisdiction_manifest.json").read_text(encoding="utf-8"))
    assert india["jurisdiction_id"] == "IN"
    assert india["status"] == "PROFILE_METADATA_ONLY"
    assert india["source_review_required"] is True
    assert global_profile["jurisdiction_id"] == "GLOBAL"
    assert global_profile["country_profiles_required"] is True
    assert global_profile["legal_register_status"] == "NO_UNIVERSAL_GLOBAL_LAW_ASSUMED"


def test_adult_and_sensitive_content_safety_metadata_boundaries():
    from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.content_safety_policy import (
        content_safety_baseline,
        validate_content_safety_metadata,
    )
    baseline = content_safety_baseline()
    assert baseline["adult_restricted_access_requires_age_assurance"] is True
    assert baseline["non_consensual_intimate_imagery_prohibited"] is True
    assert baseline["media_storage_or_generation_in_core"] is False

    assert validate_content_safety_metadata({
        "content_class": "AGE_RESTRICTED_ADULT",
        "age_gate_configured": True,
        "age_assurance_policy_ref": "AGE-ASSURANCE-POLICY",
    })["accepted"] is True

    import pytest
    with pytest.raises(ValueError, match="PROHIBITED_CONTENT_CLASS"):
        validate_content_safety_metadata({"content_class": "CHILD_SEXUAL_ABUSE_MATERIAL"})
    with pytest.raises(ValueError, match="PROHIBITED_CONTENT_CLASS"):
        validate_content_safety_metadata({"content_class": "NON_CONSENSUAL_INTIMATE_IMAGERY"})
    with pytest.raises(ValueError, match="AGE_GATE_CONFIGURATION_REQUIRED"):
        validate_content_safety_metadata({"content_class": "AGE_RESTRICTED_ADULT"})
    with pytest.raises(ValueError, match="MEDIA_PAYLOADS_NOT_ACCEPTED"):
        validate_content_safety_metadata({"content_class": "GENERAL", "media_bytes": b"not accepted"})


def test_runtime_catalog_exposes_all_domains_providers_and_jurisdictions():
    from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.catalog import get_catalog
    catalog = get_catalog()
    assert catalog["domain_count"] == 33
    assert catalog["taxonomy"]["control_area_count"] == 330
    assert catalog["provider_count"] == 6
    assert catalog["jurisdiction_profile_count"] == 2
    assert {item["jurisdiction_id"] for item in catalog["jurisdictions"]} == {"IN", "GLOBAL"}
    assert catalog["security_enforcement_verified"] is False
    assert catalog["legal_compliance_verified"] is False


def test_domain_catalog_rejects_unregistered_or_unknown_domain():
    from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.domain_catalog import (
        get_domain,
        get_domains,
    )
    assert len(get_domains()) == 33
    assert get_domain("AGE_ASSURANCE")["folder"] == "age_assurance_core_ecosystem"
    assert get_domain("NOT_A_REAL_DOMAIN") is None


def test_service_exposes_jurisdiction_and_content_safety_metadata():
    from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.service import (
        SecurityCoreEcosystemService,
    )
    service = SecurityCoreEcosystemService()
    assert service.get_jurisdiction("IN")["jurisdiction_id"] == "IN"
    assert {x["jurisdiction_id"] for x in service.list_jurisdictions()["jurisdictions"]} == {"IN", "GLOBAL"}
    baseline = service.content_safety()
    assert baseline["media_storage_or_generation_in_core"] is False
    assert baseline["production_enforcement_verified"] is False
