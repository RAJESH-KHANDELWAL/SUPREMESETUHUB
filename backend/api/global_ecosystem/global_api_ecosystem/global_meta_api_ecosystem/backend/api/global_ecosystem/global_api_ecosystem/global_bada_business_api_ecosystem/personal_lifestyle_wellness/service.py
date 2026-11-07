from .catalog import list_categories,get_category,CATEGORIES
class PersonalWellnessService:
 DOMAIN_ID="personal_lifestyle_wellness"
 def list_categories(self,query=None,include_adult=False):
  items=list_categories(include_adult=include_adult)
  if query:
   q=query.strip().casefold()
   items=[x for x in items if q in x["id"].casefold() or q in x["name"].casefold() or any(q in s.replace("_"," ").casefold() for s in x["subcategories"])]
  return items
 def get_category(self,category_id,include_adult=False): return get_category(category_id,include_adult=include_adult)
 def get_status(self):
  return {"success":True,"domain_id":self.DOMAIN_ID,"status":"taxonomy_scaffold","category_count":len(CATEGORIES),"default_discovery_count":len(list_categories()),"restricted_18_plus_count":sum(1 for x in CATEGORIES if x["access_class"]=="18_plus_restricted"),"coverage":["india","global"],"channels":["online","offline","hybrid"],"note":"Adult categories are excluded from default discovery and require age-gated access, lawful operation, informed consent and rights controls. Taxonomy only; no provider verification or professional licensing is implied."}
