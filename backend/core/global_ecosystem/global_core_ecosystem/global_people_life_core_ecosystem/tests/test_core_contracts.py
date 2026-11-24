from pathlib import Path
import json
from backend.core.global_ecosystem.global_core_ecosystem.global_people_life_core_ecosystem.domain_catalog import (
    DOMAIN_DEFINITIONS, list_people_life_modules,
)

ROOT = Path(__file__).resolve().parents[1]

def test_manifest_and_catalog_counts_match():
    manifest = json.loads((ROOT / "ecosystem_manifest.json").read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    assert manifest["canonical_path"] == "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem"
    assert manifest["domain_count"] == len(DOMAIN_DEFINITIONS) == 24
    assert manifest["module_count"] == len(catalog["domains"]) == 28
    assert manifest["domain_package_count"] == 19

def test_module_folders_and_ids_are_unique():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    folders = [x["folder"] for x in catalog["domains"]]
    ids = [x["id"] for x in catalog["domains"]]
    assert len(folders) == len(set(folders)) and len(ids) == len(set(ids))
    assert all(x == x.lower() for x in folders)

def test_all_modules_are_mapped_or_are_service_tiers():
    assert len(list_people_life_modules()) == 28
    assert all(x.get("domain_ids") or x.get("service_tier_id") for x in list_people_life_modules())

def test_adult_module_directories_are_explicitly_age_restricted():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    adult = [x for x in catalog["domains"] if x["folder"].endswith("_18_plus")]
    assert len(adult) == 11
    assert all(x["age_restricted"] for x in adult)
