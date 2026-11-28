"""Shared, source-aware relationships between canonical global entities."""
import json
from pathlib import Path
from typing import Any

DATA_PATH = Path(__file__).resolve().parent / "data" / "entity_relationships.json"
ALLOWED_RELATIONSHIPS = {"owns", "operates", "publishes", "distributes", "parent_of", "subsidiary_of", "brand_of", "founded_by", "partner_of", "resells", "provides_api_to", "hosts_content_for", "licenses_content_to", "age_verifies_for", "verifies_consent_for", "moderates_for", "processes_payments_for", "handles_payouts_for", "provides_safety_support_to", "supplies_technology_to", "affiliated_with"}


def load_relationships() -> list[dict[str, Any]]:
    if not DATA_PATH.exists():
        return []
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("records", []), list):
        raise ValueError("Relationship registry must contain a records list")
    seen = set()
    for i, item in enumerate(payload.get("records", [])):
        rid = str(item.get("relationship_id", "")).strip()
        if not rid or rid in seen:
            raise ValueError(f"Relationship record {i} has missing or duplicate relationship_id")
        seen.add(rid)
        if item.get("relationship_type") not in ALLOWED_RELATIONSHIPS:
            raise ValueError(f"Unsupported relationship_type in {rid}")
        if not item.get("source_entity_id") or not item.get("target_entity_id"):
            raise ValueError(f"Relationship {rid} requires source and target entity IDs")
        if item.get("verification_status") in {"source_checked", "verified"} and not item.get("source_urls"):
            raise ValueError(f"Verified relationship {rid} requires source_urls")
    return payload.get("records", [])


def search_relationships(entity_id: str | None = None, relationship_type: str | None = None) -> list[dict[str, Any]]:
    records = load_relationships()
    return [r for r in records if (not entity_id or entity_id in {r["source_entity_id"], r["target_entity_id"]}) and (not relationship_type or r["relationship_type"] == relationship_type)]
