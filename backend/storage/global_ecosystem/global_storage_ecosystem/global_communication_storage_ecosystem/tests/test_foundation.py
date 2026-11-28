"""Root ecosystem structure checks."""
import json
from pathlib import Path
ROOT = Path(__file__).parents[1]
def test_category_index_matches_direct_child_packages():
    data = json.loads((ROOT / "category_index.json").read_text())
    assert data["category_count"] == len(data["categories"])
    assert all((ROOT / name).is_dir() for name in data["categories"])
    assert not (ROOT / "categories").exists()
    assert not (ROOT / "providers").exists()
