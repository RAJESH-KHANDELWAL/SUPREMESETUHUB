from .catalog import list_categories,get_category
class MiningMetalsService:
 DOMAIN_ID="mining_metals_minerals"
 def list_categories(self,query=None):
  items=list_categories()
  if query:
   q=query.strip().casefold()
   items=[x for x in items if q in x["id"].casefold() or q in x["name"].casefold() or any(q in s.replace("_"," ").casefold() for s in x["subcategories"])]
  return items
 def get_category(self,category_id): return get_category(category_id)
 def get_status(self): return {"success":True,"domain_id":self.DOMAIN_ID,"status":"taxonomy_scaffold","category_count":len(list_categories()),"coverage":["india","global"],"channels":["online","offline","hybrid"],"note":"Taxonomy only; no mining rights, mineral reserves, supplier, environmental permit or regulatory compliance verification is implied."}
