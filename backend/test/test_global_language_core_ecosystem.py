import json
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.global_human_language_core_ecosystem import (
    GlobalHumanLanguageCoreOrchestrator,
    GlobalHumanLanguageCoreService,
    get_catalog,
    get_domain,
    get_domains,
    get_service_tiers,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_human_language_core_ecosystem.policy import (
    adult_content_policy,
    redact_sensitive_metadata,
)


def test_human_language_catalog_is_independent():
    catalog = get_catalog()
    assert catalog["ecosystem_id"] == "GLOBAL-HUMAN-LANGUAGE-CORE-ECOSYSTEM"
    assert [item["division_id"] for item in catalog["divisions"]] == ["HUMAN-LANGUAGES"]
    assert get_domains("HUMAN")
    assert get_domains("PROGRAMMING") == []


def test_catalog_domain_ids_are_unique():
    ids = [item["id"] for item in get_catalog()["domains"]]
    assert len(ids) == len(set(ids))


def test_programming_domains_are_not_registered_as_human_languages():
    assert get_domain("GLOBAL_PROGRAMMING_LANGUAGES") is None
    assert get_domain("PYTHON") is None


def test_bharat_and_global_human_language_domains_exist():
    assert get_domain("BHARAT_INDIC_LANGUAGES") is not None
    assert get_domain("GLOBAL_NATURAL_HUMAN_LANGUAGES") is not None
    assert get_domain("SIGNED_LANGUAGES") is not None


def test_adult_language_scope_requires_age_and_consent():
    adult = get_domain("ADULT_LANGUAGE")
    assert adult["age_restricted"] is True
    assert adult["consent_required"] is True
    policy = adult_content_policy()
    assert policy["verified_adults_only"] is True
    assert "sexual content involving minors" in policy["prohibited"]


def test_service_tiers_cover_normal_to_supreme():
    tiers = get_service_tiers()
    assert tiers[0]["tier_id"] == "NORMAL"
    assert tiers[-1]["tier_id"] == "SUPREME"
    assert [item["rank"] for item in tiers] == list(range(1, 8))


def test_catalog_is_read_only_and_redacts_secrets():
    service = GlobalHumanLanguageCoreService()
    assert service.health()["success"] is True
    data = {"provider": "google", "api_key": "hidden", "region": "global"}
    clean = redact_sensitive_metadata(data)
    assert "api_key" not in clean and clean["region"] == "global"
    assert GlobalHumanLanguageCoreOrchestrator().health()["execution_enabled"] is False


def test_human_and_programming_ecosystems_are_direct_siblings():
    core_root = Path(__file__).resolve().parents[1] / "core" / "global_ecosystem" / "global_core_ecosystem"
    human_root = core_root / "global_human_language_core_ecosystem"
    programming_root = core_root / "global_programming_language_core_ecosystem"
    assert human_root.is_dir()
    assert programming_root.is_dir()
    assert not (core_root / "global_language_core_ecosystem").exists()


def test_division_catalogs_match_their_directories():
    core_root = Path(__file__).resolve().parents[1] / "core" / "global_ecosystem" / "global_core_ecosystem"
    human_root = core_root / "global_human_language_core_ecosystem"
    programming_root = core_root / "global_programming_language_core_ecosystem"
    human_catalog = json.loads((human_root / "catalog.json").read_text(encoding="utf-8"))
    programming_catalog = json.loads((programming_root / "catalog.json").read_text(encoding="utf-8"))
    assert all((human_root / item["folder"]).is_dir() for item in human_catalog["domains"])
    assert all((programming_root / item["folder"]).is_dir() for item in programming_catalog["domains"])
    assert (human_root / "transliteration_language_core_ecosystem").is_dir()
    assert not (programming_root / "transliteration_language_core_ecosystem").exists()


def test_human_manifest_and_parent_registry_use_canonical_path():
    core_root = Path(__file__).resolve().parents[1] / "core" / "global_ecosystem" / "global_core_ecosystem"
    manifest = json.loads((core_root / "global_human_language_core_ecosystem" / "ecosystem_manifest.json").read_text(encoding="utf-8"))
    assert manifest["ecosystem_id"] == "GLOBAL-HUMAN-LANGUAGE-CORE-ECOSYSTEM"
    parent_catalog = (core_root / "catalog.py").read_text(encoding="utf-8")
    assert "global_human_language_core_ecosystem" in parent_catalog
    assert "global_programming_language_core_ecosystem" in parent_catalog
    assert "global_language_core_ecosystem" not in parent_catalog



def test_human_and_programming_catalogs_are_disjoint_and_canonical():
    core_root = Path(__file__).resolve().parents[1] / "core" / "global_ecosystem" / "global_core_ecosystem"
    human_root = core_root / "global_human_language_core_ecosystem"
    programming_root = core_root / "global_programming_language_core_ecosystem"

    human_catalog = json.loads((human_root / "catalog.json").read_text(encoding="utf-8"))
    programming_catalog = json.loads((programming_root / "catalog.json").read_text(encoding="utf-8"))
    human_manifest = json.loads((human_root / "ecosystem_manifest.json").read_text(encoding="utf-8"))

    human_ids = [item["id"] for item in human_catalog["domains"]]
    programming_ids = [item["id"] for item in programming_catalog["domains"]]
    human_folders = {item["folder"] for item in human_catalog["domains"]}
    programming_folders = {item["folder"] for item in programming_catalog["domains"]}

    assert len(human_ids) == len(set(human_ids))
    assert len(programming_ids) == len(set(programming_ids))
    assert human_folders.isdisjoint(programming_folders)
    assert all(Path(folder).name == folder and "/" not in folder and "\\\\" not in folder for folder in human_folders | programming_folders)
    assert human_manifest["domain_count"] == len(human_catalog["domains"])
    assert human_manifest["division"]["folder"] == human_root.name

    parent_catalog = (core_root / "catalog.py").read_text(encoding="utf-8")
    assert '"core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_human_language_core_ecosystem"' in parent_catalog
    assert '"core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_programming_language_core_ecosystem"' in parent_catalog
