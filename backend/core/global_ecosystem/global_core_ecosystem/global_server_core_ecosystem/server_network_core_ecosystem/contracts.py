"""Server Network Core: declarative provider-neutral contracts."""
from __future__ import annotations
from typing import Any
DOMAIN_ID="server_network_core"
DOMAIN_LABEL="Server Network Core"
DOMAIN_DESCRIPTION="Network topology, endpoint, connectivity, and segmentation metadata."
LAYER="CORE"
EXECUTION_ENABLED=False
REQUIRED_FIELDS=("domain_id","schema_version","status")
def validate_descriptor(value: dict[str, Any]) -> tuple[str, ...]:
    if not isinstance(value, dict): return REQUIRED_FIELDS
    return tuple(k for k in REQUIRED_FIELDS if k not in value)
def get_domain_descriptor() -> dict[str, Any]:
    return {"domain_id":DOMAIN_ID,"label":DOMAIN_LABEL,"description":DOMAIN_DESCRIPTION,"layer":LAYER,"schema_version":"1.0.0","status":"DECLARATIVE_CORE_CONTRACT","execution_enabled":EXECUTION_ENABLED}
