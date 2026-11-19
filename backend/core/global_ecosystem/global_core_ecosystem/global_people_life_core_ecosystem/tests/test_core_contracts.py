from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def test_manifest_and_catalog_domain_count_match():
    manifest=json.loads((ROOT/"ecosystem_manifest.json").read_text(encoding="utf-8"))
    catalog=json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))
    assert manifest["canonical_path"]=="backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem"
    assert manifest["domain_count"]==len(catalog["domains"])==28

def test_domain_folders_are_unique_and_canonical():
    catalog=json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))
    folders=[x["folder"] for x in catalog["domains"]]
    ids=[x["id"] for x in catalog["domains"]]
    assert len(folders)==len(set(folders)) and len(ids)==len(set(ids))
    assert all(x==x.lower() for x in folders)

def test_adult_domains_are_explicitly_age_restricted():
    catalog=json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))
    adult=[x for x in catalog["domains"] if x["folder"].endswith("_18_plus")]
    assert len(adult)==11
    assert all(x["age_restricted"] for x in adult)
