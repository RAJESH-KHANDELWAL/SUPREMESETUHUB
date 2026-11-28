"""Canonical read-only domain catalog."""
from .subcategories import DOMAINS
from .domains_catalog import DOMAIN_DETAILS
from .models import EcosystemDomain


def list_domains():
    return [EcosystemDomain(id=item["id"], name=item["name"], folder=item["folder"], description=DOMAIN_DETAILS[item["id"]]["description"]) for item in DOMAINS]


def get_domain(domain_id):
    for item in list_domains():
        if item.id == domain_id:
            return item
    return None
