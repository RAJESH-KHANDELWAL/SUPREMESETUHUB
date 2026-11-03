"""Domain metadata lookup."""
from .subcategories import DOMAINS
DOMAIN_DETAILS = {item["id"]: item for item in DOMAINS}

def get_domain_details(domain_id):
    item = DOMAIN_DETAILS.get(domain_id)
    return dict(item) if item else None
