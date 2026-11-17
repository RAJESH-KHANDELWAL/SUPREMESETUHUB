import json
from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.global_language_core_ecosystem import (
    GlobalLanguageCoreOrchestrator, GlobalLanguageCoreService,
    get_catalog, get_domain, get_domains, get_service_tiers,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_language_core_ecosystem.policy import adult_content_policy,redact_sensitive_metadata

def test_two_separate_language_divisions_exist():
    c=get_catalog()
    assert [x["division_id"] for x in c["divisions"]]==["HUMAN-LANGUAGES","PROGRAMMING-LANGUAGES"]
    assert len(get_domains("HUMAN"))>0
    assert len(get_domains("PROGRAMMING"))>0

def test_catalog_domain_ids_are_unique():
    ids=[x["id"] for x in get_catalog()["domains"]]
    assert len(ids)==len(set(ids))

def test_programming_language_group_is_separate():
    assert get_domain("GLOBAL_PROGRAMMING_LANGUAGES") is not None
    assert get_domain("PYTHON") is None  # individual language records are a later catalog population task

def test_bharat_and_global_human_language_domains_exist():
    assert get_domain("BHARAT_INDIC_LANGUAGES") is not None
    assert get_domain("GLOBAL_NATURAL_HUMAN_LANGUAGES") is not None
    assert get_domain("SIGNED_LANGUAGES") is not None

def test_adult_language_scope_requires_age_and_consent():
    adult=get_domain("ADULT_LANGUAGE")
    assert adult["age_restricted"] is True and adult["consent_required"] is True
    policy=adult_content_policy()
    assert policy["verified_adults_only"] is True
    assert "sexual content involving minors" in policy["prohibited"]

def test_service_tiers_cover_normal_to_supreme():
    tiers=get_service_tiers()
    assert tiers[0]["tier_id"]=="NORMAL"
    assert tiers[-1]["tier_id"]=="SUPREME"
    assert [x["rank"] for x in tiers]==list(range(1,8))

def test_catalog_is_read_only_and_redacts_secrets():
    service=GlobalLanguageCoreService()
    assert service.health()["success"] is True
    data={"provider":"google","api_key":"hidden","region":"global"}
    clean=redact_sensitive_metadata(data)
    assert "api_key" not in clean and clean["region"]=="global"
    assert GlobalLanguageCoreOrchestrator().health()["execution_enabled"] is False


def test_global_division_folders_are_direct_siblings_of_shared_package():
    core_root = Path(__file__).resolve().parents[1] / "core" / "global_ecosystem" / "global_core_ecosystem"
    assert (core_root / "global_human_language_core_ecosystem").is_dir()
    assert (core_root / "global_programming_language_core_ecosystem").is_dir()
    assert not (core_root / "global_language_core_ecosystem" / "human_languages_core_ecosystem").exists()
    assert not (core_root / "global_language_core_ecosystem" / "programming_languages_core_ecosystem").exists()

def test_division_catalogs_and_paths_are_consistent():
    core_root = Path(__file__).resolve().parents[1] / "core" / "global_ecosystem" / "global_core_ecosystem"
    human_root = core_root / "global_human_language_core_ecosystem"
    programming_root = core_root / "global_programming_language_core_ecosystem"
    human_catalog = json.loads((human_root / "catalog.json").read_text(encoding="utf-8"))
    programming_catalog = json.loads((programming_root / "catalog.json").read_text(encoding="utf-8"))

    assert all((human_root / item["folder"]).is_dir() for item in human_catalog["domains"])
    assert all((programming_root / item["folder"]).is_dir() for item in programming_catalog["domains"])
    assert not (programming_root / "transliteration_core_ecosystem").exists()
    assert not (programming_root / "global_programming_languages_core_ecosystem").exists()
    assert (human_root / "transliteration_language_core_ecosystem").is_dir()

    shared_root = core_root / "global_language_core_ecosystem"
    assert all(item.is_file() for item in shared_root.iterdir())
    parent_catalog = (core_root / "catalog.py").read_text(encoding="utf-8")
    assert f'"human_division_path": "{human_root.as_posix()}"' in parent_catalog
    assert f'"programming_division_path": "{programming_root.as_posix()}"' in parent_catalog
