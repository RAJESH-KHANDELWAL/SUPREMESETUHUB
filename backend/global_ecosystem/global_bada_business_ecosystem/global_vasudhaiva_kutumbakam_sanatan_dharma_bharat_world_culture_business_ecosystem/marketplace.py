"""Business discovery helpers; no transaction or payment processing."""
from .business_domain import BusinessOffering
from .governance import assess_listing

def published_offerings(offerings, domain=None):
    """Return only offerings that pass the publication eligibility gates."""
    return tuple(
        item for item in offerings
        if (domain is None or item.domain == domain)
        and assess_listing(item).eligible_for_publication
    )
