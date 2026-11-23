"""Guardrails: relationship claims must be evidence-based and privacy-minimal."""
from __future__ import annotations
from .catalog import RELATIONSHIP_TYPES
class RelationshipPolicyError(ValueError): pass
class RelationshipPolicy:
    @staticmethod
    def validate(record):
        required=("relationship_id","source_entity_id","target_entity_id","relationship_type","verification_status")
        missing=[k for k in required if not record.get(k)]
        if missing: raise RelationshipPolicyError("Missing required fields: "+", ".join(missing))
        if record["source_entity_id"] == record["target_entity_id"]: raise RelationshipPolicyError("Self-edge not allowed")
        if record["relationship_type"] not in RELATIONSHIP_TYPES: raise RelationshipPolicyError("Unsupported relationship type")
        status=record["verification_status"]
        if status not in {"UNVERIFIED","PENDING_REVIEW","VERIFIED","REJECTED","EXPIRED"}: raise RelationshipPolicyError("Invalid verification status")
        urls=record.get("source_urls") or []
        if status=="VERIFIED" and not urls: raise RelationshipPolicyError("Verified claims require evidence source URLs")
        if status=="VERIFIED" and not all(str(u).startswith(("https://","http://")) for u in urls): raise RelationshipPolicyError("Evidence URLs must be HTTP(S)")
        return True
