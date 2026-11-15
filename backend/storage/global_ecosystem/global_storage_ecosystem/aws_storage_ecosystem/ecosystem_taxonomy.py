"""Canonical AWS storage category taxonomy loader."""
import json
from pathlib import Path

TAXONOMY_PATH = Path(__file__).parent / "taxonomy" / "aws_storage_taxonomy.json"

def load_taxonomy() -> dict:
    with TAXONOMY_PATH.open("r", encoding="utf-8") as stream:
        return json.load(stream)
