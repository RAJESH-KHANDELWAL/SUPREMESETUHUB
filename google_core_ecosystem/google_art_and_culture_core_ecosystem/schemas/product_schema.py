def validate(m):
 required=('provider','product_id','product_name','category')
 missing=[x for x in required if not m.get(x)]
 if missing:raise ValueError('missing fields: '+', '.join(missing))
 return m.get('provider')=='google'
