"""Category facade resolving its canonical taxonomy entry."""
from ..domain_catalog import get_domain
CATEGORY_ID=__package__.rsplit(".",1)[-1]
def get_category(): return get_domain(CATEGORY_ID)
class CategoryManager:
 CATEGORY_ID=CATEGORY_ID
 def get(self): return get_category()
 def status(self): return {"status":"REGISTERED" if get_category() else "MISSING","category_id":CATEGORY_ID}
