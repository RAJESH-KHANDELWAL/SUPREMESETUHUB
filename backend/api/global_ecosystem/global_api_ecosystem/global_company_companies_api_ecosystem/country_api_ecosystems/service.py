"""Country source-directory service backed by the Company source file."""
from ..service import list_country_sources,get_country_source,load_country_sources
class CountrySourceService:
 def list_sources(self,country_code=None): return list_country_sources(country_code)
 def get_source(self,source_id): return get_country_source(source_id)
 def list_countries(self):
  grouped={}
  for item in load_country_sources():
   code=item["country_code"]
   grouped.setdefault(code,{"country_code":code,"country_name":item["country_name"],"source_count":0})
   grouped[code]["source_count"]+=1
  return {"count":len(grouped),"items":sorted(grouped.values(),key=lambda x:x["country_name"].casefold()),"registry_status":"source_directory_only","live_government_connections":False}
