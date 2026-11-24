"""Read-only hosting provider registry."""
class HostingProviderRegistry:
 def __init__(self,records):
  self._records={}
  for x in records:
   k=x["ecosystem_id"]
   if k in self._records:raise ValueError(f"duplicate hosting provider id: {k}")
   self._records[k]=dict(x)
 def list(self):return [dict(x) for x in self._records.values()]
 def get(self,key):
  if key in self._records:return dict(self._records[key])
  key=key.strip().casefold()
  return next((dict(x) for x in self._records.values() if x.get("provider_id","").casefold()==key),None)
 def count(self):return len(self._records)
