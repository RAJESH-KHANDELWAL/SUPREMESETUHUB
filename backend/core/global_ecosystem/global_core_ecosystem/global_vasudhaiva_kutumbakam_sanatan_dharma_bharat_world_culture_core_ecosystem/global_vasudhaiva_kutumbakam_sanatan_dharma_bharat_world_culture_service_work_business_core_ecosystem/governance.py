"""Validation and readiness rules for capability records; no live listings."""
from __future__ import annotations
from typing import Any
from .catalog import CAPABILITIES
_IDS = {x["id"] for x in CAPABILITIES}
_DOMAINS = {"SERVICE","WORK","BUSINESS"}
_STATUSES = {"DRAFT","REVIEW","APPROVED","REJECTED","ARCHIVED"}
def validate_record(record: Any) -> list[str]:
 errors=[]
 if not isinstance(record,dict): return ["record must be a dictionary"]
 if not record.get("capability_id"): errors.append("capability_id is required")
 elif record["capability_id"] not in _IDS: errors.append("unknown capability_id")
 if str(record.get("domain","")).upper() not in _DOMAINS: errors.append("domain must be SERVICE, WORK or BUSINESS")
 if not record.get("title"): errors.append("title is required")
 status=str(record.get("status","DRAFT")).upper()
 if status not in _STATUSES: errors.append("status is invalid")
 if status == "APPROVED" and not record.get("source_refs"): errors.append("approved records require source_refs")
 if record.get("consent_required") and not record.get("consent_reference"): errors.append("consent reference required")
 return errors
def is_publishable(record: Any) -> bool:
 return isinstance(record,dict) and str(record.get("status","")).upper()=="APPROVED" and not validate_record(record)
