from .catalog import CROSS_ECOSYSTEM_LINKS, get_category, list_categories

class HomeServicesFacilityService:
 DOMAIN_ID = "home_services_property_maintenance_facility_management"
 def list_categories(self, query: str | None = None, channel: str | None = None):
  items=list_categories()
  if channel: items=[x for x in items if channel in x["channels"]]
  if query:
   term=query.strip().casefold()
   items=[x for x in items if term in x["id"].casefold() or term in x["name"].casefold() or any(term in s.replace("_"," ").casefold() for s in x["subcategories"])]
  return items
 def get_category(self, category_id: str): return get_category(category_id)
 def get_cross_ecosystem_links(self): return {k:dict(v,canonical_categories=list(v["canonical_categories"])) for k,v in CROSS_ECOSYSTEM_LINKS.items()}
 def get_status(self):
  return {"success":True,"domain_id":self.DOMAIN_ID,"status":"taxonomy_scaffold","category_count":len(list_categories()),"coverage":["india","global"],"channels":["online","offline","hybrid"],"focus":["home_services","property_maintenance","facility_management"],"note":"Taxonomy only; no provider verification, live booking, dispatch, payment, licence validation or service-level guarantee is implied. Gym, fitness, spa and massage categories are linked from healthcare_wellness_fitness rather than duplicated."}
