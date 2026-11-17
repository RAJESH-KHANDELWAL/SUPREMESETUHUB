from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def test_manifest_and_catalog_domain_count_match():
    manifest=json.loads((ROOT/"ecosystem_manifest.json").read_text(encoding="utf-8"))
    catalog=json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))
    assert manifest["canonical_path"] == "backend/core/global_ecosystem/global_core_ecosystem/global_programming_language_core_ecosystem"
    assert manifest["domain_count"] == len(catalog["domains"])

def test_domain_folders_are_unique_and_canonical():
    catalog=json.loads((ROOT/"catalog.json").read_text(encoding="utf-8"))
    folders=[item["folder"] for item in catalog["domains"]]
    ids=[item["id"] for item in catalog["domains"]]
    assert len(folders)==len(set(folders))
    assert len(ids)==len(set(ids))
    assert all(folder == folder.lower() and folder.endswith("_core_ecosystem") for folder in folders)

def test_language_types_keep_markup_query_and_serialization_distinct():
    from backend.core.global_ecosystem.global_core_ecosystem.global_programming_language_core_ecosystem.language_catalog import get_language_record
    assert get_language_record("HTML")["language_type"] == "MARKUP"
    assert get_language_record("CSS")["language_type"] == "STYLESHEET"
    assert get_language_record("SQL")["language_type"] == "DATABASE_QUERY"
    assert get_language_record("JSON")["language_type"] == "DATA_SERIALIZATION"
