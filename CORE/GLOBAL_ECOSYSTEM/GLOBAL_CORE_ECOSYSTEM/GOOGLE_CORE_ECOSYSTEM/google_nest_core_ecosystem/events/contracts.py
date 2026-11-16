def make_event(event_type,tenant_id,payload=None):
 if not event_type or not tenant_id:raise ValueError('event type and tenant required')
 return {'provider':'google','product_id':"google_nest",'event_type':event_type,'tenant_id':tenant_id,'payload':dict(payload or {})}
