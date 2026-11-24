"""Read-only DeepSeek storage taxonomy helpers."""
import json
from pathlib import Path
_TAXONOMY = Path(__file__).parent / "taxonomy" / "deepseek_storage_taxonomy.json"
def load_taxonomy() -> dict:
    return json.loads(_TAXONOMY.read_text(encoding="utf-8"))
def list_categories() -> list[dict]:
    return [{"category": c, "group": g["group"]} for g in load_taxonomy()["groups"] for c in g["categories"]]
