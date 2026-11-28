from datetime import datetime,timezone
def make_event(event_type,tenant_id,payload=None):
 if not event_type or not tenant_id:raise ValueError("event_type and tenant_id required")
 return {"provider":"google","product_id":"google_maps_time_zone","event_type":event_type,"tenant_id":tenant_id,"occurred_at":datetime.now(timezone.utc).isoformat(),"payload":dict(payload or {})}
