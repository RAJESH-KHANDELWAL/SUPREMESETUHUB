"""Server Security Core: provider-neutral declarative contracts."""
from __future__ import annotations
from typing import Any
DOMAIN_ID = "server_security_core"
DOMAIN_LABEL = "Server Security Core"
DOMAIN_DESCRIPTION = "Security control taxonomy, access-policy metadata, and secure-by-default requirements."
LAYER = "CORE"
EXECUTION_ENABLED = False
REQUIRED_FIELDS = ("domain_id", "schema_version", "status")
def validate_descriptor(value: dict[str, Any]) -> tuple[str, ...]:
    if not isinstance(value, dict): return REQUIRED_FIELDS
    return tuple(key for key in REQUIRED_FIELDS if key not in value)
def get_domain_descriptor() -> dict[str, Any]:
    return {"domain_id": DOMAIN_ID, "label": DOMAIN_LABEL, "description": DOMAIN_DESCRIPTION, "layer": LAYER, "schema_version": "1.0.0", "status": "DECLARATIVE_CORE_CONTRACT", "execution_enabled": EXECUTION_ENABLED}
