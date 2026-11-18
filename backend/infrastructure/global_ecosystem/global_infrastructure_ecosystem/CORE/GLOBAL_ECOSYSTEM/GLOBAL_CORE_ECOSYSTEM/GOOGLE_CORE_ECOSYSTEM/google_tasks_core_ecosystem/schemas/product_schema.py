REQUIRED=("provider","product_id","product_name","category","availability")
def validate(m):
 missing=[x for x in REQUIRED if not m.get(x)]
 if missing: raise ValueError("missing: "+", ".join(missing))
 if m["provider"]!="google": raise ValueError("provider mismatch")
 return True
