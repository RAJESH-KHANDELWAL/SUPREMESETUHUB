"""Company classification standards catalogue."""
from . import DOMAIN_ID,DOMAIN_NAME,ADULT_RESTRICTED,SUBCATEGORY_IDS
from .models import CategoryRecord
CATEGORIES=tuple(CategoryRecord(x,x.replace("_"," ").title(),DOMAIN_ID,ADULT_RESTRICTED) for x in SUBCATEGORY_IDS)
def list_categories(): return list(CATEGORIES)
def get_category(category_id): return next((x for x in CATEGORIES if x.id==category_id),None)
def search_categories(query):
 q=(query or "").strip().casefold()
 return [x for x in CATEGORIES if q and (q in x.id.casefold() or q in x.name.casefold())]
def get_catalogue_metadata(): return {"domain_id":DOMAIN_ID,"domain_name":DOMAIN_NAME,"category_count":len(CATEGORIES),"adult_restricted":ADULT_RESTRICTED,"catalogue_status":"taxonomy_only"}
