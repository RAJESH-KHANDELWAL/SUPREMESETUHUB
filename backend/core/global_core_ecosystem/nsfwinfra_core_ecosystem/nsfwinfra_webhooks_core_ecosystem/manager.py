"""Webhooks infrastructure Core metadata manager."""
from __future__ import annotations
from typing import Any
from ..contracts import result
ECOSYSTEM_ID = "NSFW-INFRA-WEBHOOKS-CORE"
NAME = "WEBHOOKS INFRA CORE ECOSYSTEM"
DESCRIPTION = "Contracts/policy for subscriptions, event schemas, endpoints, signing refs, retries, timeouts, limits, delivery attempts, dead-letter, idempotency, ordering, SSRF validation and readiness. Delivery external."
CAPABILITIES = ["SUBSCRIPTION_METADATA","EVENT_REGISTRY_AND_SCHEMAS","ENDPOINT_METADATA","DELIVERY_CONFIGURATION","SIGNING_AND_SECRET_REFERENCES","RETRY_AND_BACKOFF_POLICY","TIMEOUTS_AND_RATE_LIMITS","DELIVERY_ATTEMPT_METADATA","FAILED_DELIVERY_AND_DEAD_LETTER_REFERENCES","IDEMPOTENCY","ORDERING_GUARANTEE_METADATA","ENDPOINT_HEALTH_METADATA","SSRF_AND_ENDPOINT_VALIDATION_POLICY","AUDIT_REFERENCES","READINESS"]
class WebhooksInfraCoreManager:
    NAME = NAME
    ECOSYSTEM_ID = ECOSYSTEM_ID
    def status(self) -> dict[str, Any]:
        return result(success=True, ecosystem_id=ECOSYSTEM_ID, status="CORE_CATALOG_ONLY", data={"name": NAME, "description": DESCRIPTION, "capabilities": list(CAPABILITIES)})
    def capabilities(self) -> dict[str, Any]:
        return {"success": True, "ecosystem_id": ECOSYSTEM_ID, "count": len(CAPABILITIES), "capabilities": list(CAPABILITIES), "live_connection_verified": False, "execution_performed": False}
def get_manager() -> WebhooksInfraCoreManager: return WebhooksInfraCoreManager()
__all__ = ["WebhooksInfraCoreManager", "get_manager"]
