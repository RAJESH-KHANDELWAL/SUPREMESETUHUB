"""Repository-level integrity checks for the Human Language CORE ecosystem."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def test_manifest_identity_and_registry_counts_match_source_catalogs():
    manifest = _load_json("ecosystem_manifest.json")
    domains = _load_json("catalog.json")["domains"]
    providers_data = _load_json("provider_catalog.json")
    providers = providers_data["providers"]

    assert manifest["ecosystem_id"] == "GLOBAL-HUMAN-LANGUAGE-CORE-ECOSYSTEM"
    assert manifest["parent_id"] == "GLOBAL-CORE-ECOSYSTEM"
    assert manifest["layer"] == "CORE"
    assert manifest["status"] == "CORE_CATALOG_ONLY"
    assert manifest["domain_count"] == len(domains)
    assert manifest["provider_count"] == len(providers)
    assert manifest["provider_metadata_count"] == len(providers)


def test_domain_registry_has_unique_ids_and_existing_canonical_folders():
    domains = _load_json("catalog.json")["domains"]
    domain_ids = [item["id"] for item in domains]
    domain_folders = [item["folder"] for item in domains]

    assert len(domain_ids) == len(set(domain_ids))
    assert len(domain_folders) == len(set(domain_folders))
    for item in domains:
        assert item["id"].strip()
        assert item["name"].strip()
        assert item["scope"].strip()
        assert (ROOT / item["folder"]).is_dir(), f"Missing domain folder: {item['folder']}"
        if item.get("age_restricted", False):
            assert item.get("scope")
            assert item["age_restricted"] is True


def test_provider_registry_has_unique_ids_and_canonical_module_folders():
    providers = _load_json("provider_catalog.json")["providers"]
    provider_ids = [item["provider_id"] for item in providers]
    provider_keys = [item["provider_key"] for item in providers]
    provider_folders = [item["folder"] for item in providers]

    assert len(provider_ids) == len(set(provider_ids))
    assert len(provider_keys) == len(set(provider_keys))
    assert len(provider_folders) == len(set(provider_folders))
    for item in providers:
        assert item["status"] == "CORE_CATALOG_ONLY"
        assert item["integration_mode"] == "METADATA_ONLY"
        assert item["live_connection_verified"] is False
        assert item["api_availability"] == "NOT_VERIFIED"
        assert item["credential_storage"] == "EXTERNAL_SECRET_STORE_ONLY"
        assert (ROOT / item["folder"]).is_dir(), f"Missing provider folder: {item['folder']}"


def test_manifest_preserves_layer_boundaries_and_non_live_claims():
    manifest = _load_json("ecosystem_manifest.json")

    assert manifest["live_provider_connections_verified"] is False
    assert manifest["api_calls_performed"] == 0
    assert manifest["credential_storage"] == "EXTERNAL_SECRET_STORE_ONLY"
    boundaries = manifest["layer_boundaries"]
    for layer in ("core", "api", "storage", "database", "runtime", "application"):
        assert boundaries.get(layer)
