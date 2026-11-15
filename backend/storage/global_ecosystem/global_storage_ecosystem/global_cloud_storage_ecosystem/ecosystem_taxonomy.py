"""Load and validate the static GLOBAL CLOUD taxonomy."""
import json
from pathlib import Path

TAXONOMY_PATH = Path(__file__).parent / "taxonomy" / "global_cloud_storage_taxonomy.json"


def load_taxonomy() -> dict:
    with TAXONOMY_PATH.open("r", encoding="utf-8") as stream:
        data = json.load(stream)
    provider_ids = [item["provider_id"] for item in data["providers"]]
    if len(provider_ids) != len(set(provider_ids)):
        raise ValueError("DUPLICATE_PROVIDER_ID")
    return data
