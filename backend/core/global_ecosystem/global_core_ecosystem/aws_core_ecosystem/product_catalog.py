"""AWS service-family offering inventory sourced from the AWS Core catalog."""
from __future__ import annotations
from typing import Any
from .catalog import get_aws_core_catalog

def list_aws_offerings() -> list[dict[str, Any]]:
    return [{"id": item["ecosystem_id"], "name": item["name"], "family": item["ecosystem_id"].removeprefix("AWS-").removesuffix("-CORE-ECOSYSTEM"), "core_module": item["core_module"], "api_catalog_ref": item["api_catalog_ref"], "capabilities": list(item["capabilities"]), "domains": list(item["domains"]), "api_available": None, "live_connection_verified": False} for item in get_aws_core_catalog()["children"]]

def aws_offerings_summary() -> dict[str, Any]:
    offerings = list_aws_offerings()
    return {"success": True, "provider": "aws", "count": len(offerings), "api_available_count": 0, "live_connections_verified": 0, "offerings": offerings}
