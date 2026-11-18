"""Corporate-group subcategory accessors."""
from . import DOMAIN_ID,SUBCATEGORY_IDS
def list_subcategories(): return [{"id":x,"name":x.replace("_"," ").title(),"domain_id":DOMAIN_ID} for x in SUBCATEGORY_IDS]
__all__=["SUBCATEGORY_IDS","list_subcategories"]
