"""Read-only domain catalog."""
from .subcategories import DOMAINS
from .models import HealthcareDomain

def list_domains():
    return [HealthcareDomain(**item) for item in DOMAINS]

def get_domain(domain_id):
    for item in list_domains():
        if item.id == domain_id:
            return item
    return None
