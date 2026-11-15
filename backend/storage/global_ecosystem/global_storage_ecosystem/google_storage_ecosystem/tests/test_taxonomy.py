"""Tests for catalog taxonomy and PHP-shared JSON contract."""
import json
from pathlib import Path
from ..ecosystem_taxonomy import load_taxonomy, list_ecosystems, find_ecosystem

def test_taxonomy_has_expected_identity_and_names():
    data = load_taxonomy()
    assert data["ecosystem_id"] == "GOOGLE_STORAGE_ECOSYSTEM"
    rows = list_ecosystems()
    assert len(rows) >= 100
    assert all(r["name"].startswith("GOOGLE_") and r["name"].endswith("_STORAGE_ECOSYSTEM") for r in rows)

def test_adult_category_is_catalog_only_and_governed():
    row = find_ecosystem("GOOGLE_PORNOGRAPHIC_CONTENT_STORAGE_ECOSYSTEM")
    assert row is not None and row["status"] == "CATALOG_ONLY"
    assert "child sexual abuse material" in load_taxonomy()["governance"]["prohibited_content"]

def test_php_and_python_share_json_file():
    path = Path(__file__).parents[1] / "taxonomy" / "google_storage_taxonomy.json"
    assert json.loads(path.read_text(encoding="utf-8"))["provider"] == "GOOGLE"
