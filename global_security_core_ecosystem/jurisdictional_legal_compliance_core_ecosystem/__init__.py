"""Jurisdictional legal compliance metadata package; no live enforcement is implied."""
from __future__ import annotations
import json
from pathlib import Path

DOMAIN_MANIFEST = json.loads(Path(__file__).with_name("domain_manifest.json").read_text(encoding="utf-8"))

def get_domain_manifest() -> dict:
    """Return a defensive copy of this domain's metadata manifest."""
    return json.loads(json.dumps(DOMAIN_MANIFEST))
