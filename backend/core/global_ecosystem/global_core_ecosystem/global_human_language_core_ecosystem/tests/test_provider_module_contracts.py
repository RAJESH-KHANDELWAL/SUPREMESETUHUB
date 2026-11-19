"""Architecture regression tests for the Human Language provider modules."""
import json
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.global_human_language_core_ecosystem import (
    GlobalHumanLanguageCoreService,
    HumanLanguageProviderCoreService,
    get_catalog,
    get_human_language_core_catalog,
)


ROOT = Path(__file__).resolve().parents[1]
PROVIDER_PARTS = (
    "authentication", "capabilities", "docs", "events", "lifecycle",
    "models", "schemas", "security", "services", "tests",
)


def test_google_core_style_catalog_separation_and_counts():
    catalog = get_catalog()
    registry = get_human_language_core_catalog()
    assert catalog["domain_count"] == len(catalog["domains"])
    assert catalog["provider_count"] == len(catalog["providers"]) == len(registry["children"])
    assert len({item["id"] for item in catalog["domains"]}) == catalog["domain_count"]
    assert len({item["provider_id"] for item in catalog["providers"]}) == catalog["provider_count"]


def test_every_registered_provider_has_the_canonical_module_layout():
    catalog = get_catalog()
    for provider in catalog["providers"]:
        provider_root = ROOT / provider["folder"]
        assert provider_root.is_dir()
        for part in PROVIDER_PARTS:
            assert (provider_root / part).is_dir(), f"{provider['provider_id']} missing {part}"
        manifest = json.loads((provider_root / "ecosystem_manifest.json").read_text(encoding="utf-8"))
        assert manifest["provider_id"] == provider["provider_id"]
        assert manifest["live_connection"] is False
        assert (provider_root / "services" / "core_service.py").is_file()


def test_provider_service_is_metadata_only():
    provider = get_catalog()["providers"][0]
    service = HumanLanguageProviderCoreService(provider["provider_id"])
    assert service.describe()["live_connection_verified"] is False
    assert service.readiness()["api_calls_performed"] == 0
    assert service.capabilities()["count"] > 0


def test_ecosystem_facade_reports_no_live_connections():
    status = GlobalHumanLanguageCoreService().status()
    assert status["provider_count"] == status["module_count"]
    assert status["live_connection_verified"] is False
    assert status["api_calls_performed"] == 0


def test_shared_support_matches_google_core_separation():
    shared = ROOT / "shared_support"
    expected = {
        "compatibility", "configuration", "contracts", "documentation", "events",
        "exceptions", "orchestration", "security", "testing", "utilities", "validation",
    }
    assert expected.issubset({item.name for item in shared.iterdir() if item.is_dir()})
