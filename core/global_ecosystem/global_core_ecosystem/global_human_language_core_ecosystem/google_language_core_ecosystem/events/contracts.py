"""Metadata event envelope for GOOGLE LANGUAGE; event creation performs no I/O."""
from datetime import datetime, timezone
from ..ecosystem_config import PROVIDER_ID


def make_event(event_type, tenant_id, payload=None):
    if not isinstance(event_type, str) or not event_type.strip():
        raise ValueError("EVENT_TYPE_REQUIRED")
    if not isinstance(tenant_id, str) or not tenant_id.strip():
        raise ValueError("TENANT_ID_REQUIRED")
    return {
        "provider_id": PROVIDER_ID,
        "event_type": event_type,
        "tenant_id": tenant_id,
        "occurred_at": datetime.now(timezone.utc).isoformat(),
        "payload": dict(payload or {}),
        "provider_call_performed": False,
    }
