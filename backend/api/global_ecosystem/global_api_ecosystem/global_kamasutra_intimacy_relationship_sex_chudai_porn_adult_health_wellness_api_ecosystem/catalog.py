"""Master category catalog. No live provider or business claims."""
from .models import EcosystemCategory
from .subcategories import SUBCATEGORIES
from .domains_catalog import DOMAIN_CATALOG

CATEGORIES = tuple(EcosystemCategory(id=x["id"], name=x["name"], folder=x["folder"], subdomains=tuple(DOMAIN_CATALOG[x["id"]])) for x in SUBCATEGORIES)
