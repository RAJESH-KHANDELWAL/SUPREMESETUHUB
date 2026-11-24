from .catalog import list_categories,get_category
class ScienceResearchService:
 DOMAIN_ID="science_research_innovation"
 def list_categories(self,query=None):
  items=list_categories()
  if query:
   q=query.strip().casefold()
   items=[x for x in items if q in x["id"].casefold() or q in x["name"].casefold() or any(q in s.replace("_"," ").casefold() for s in x["subcategories"])]
  return items
 def get_category(self,category_id): return get_category(category_id)
 def get_status(self): return {"success":True,"domain_id":self.DOMAIN_ID,"status":"taxonomy_scaffold","category_count":len(list_categories()),"coverage":["india","global"],"channels":["online","offline","hybrid"],"note":"Research taxonomy only; no institution, publication, patent, laboratory accreditation or research outcome verification is implied."}
