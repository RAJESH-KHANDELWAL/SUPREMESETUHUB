"""Provider-neutral domain event envelope; no event transport."""
from datetime import datetime, timezone

def make_event(event_type: str, tenant_id: str, payload: dict | None = None) -> dict:
    if not event_type or not tenant_id:
        raise ValueError("event_type and tenant_id required")
    return {"provider":"anthropic","product_id":"anthropic_files",
            "event_type":event_type,"tenant_id":tenant_id,
            "occurred_at":datetime.now(timezone.utc).isoformat(),
            "payload":dict(payload or {})}
