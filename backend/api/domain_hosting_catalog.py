"""Public, read-only domain and hosting service discovery catalog.

This catalog is intentionally inquiry-only until registrar, hosting-provider,
tax, billing, provisioning, refund, and support integrations are configured.
It must never imply that a domain is available or a service is purchasable.
"""
from fastapi import APIRouter

router = APIRouter(tags=["Domain & Hosting Catalog"])

_SERVICES = [
    {
        "id": "domain-registration",
        "name": "Domain Registration & Renewal",
        "description": "Domain search, registration, renewal, transfer, and ownership support.",
        "availability": "inquiry_only",
        "provider_connection": "not_configured",
        "live_availability_check": False,
        "checkout_enabled": False,
    },
    {
        "id": "shared-hosting",
        "name": "Shared Web Hosting",
        "description": "Website hosting options for personal sites, creators, and small businesses.",
        "availability": "inquiry_only",
        "provider_connection": "not_configured",
        "live_availability_check": False,
        "checkout_enabled": False,
    },
    {
        "id": "wordpress-hosting",
        "name": "Managed WordPress Hosting",
        "description": "Hosting setup and WordPress deployment support for websites and stores.",
        "availability": "inquiry_only",
        "provider_connection": "not_configured",
        "live_availability_check": False,
        "checkout_enabled": False,
    },
    {
        "id": "vps-cloud",
        "name": "VPS & Cloud Infrastructure",
        "description": "Virtual servers, cloud resources, and deployment assistance.",
        "availability": "inquiry_only",
        "provider_connection": "not_configured",
        "live_availability_check": False,
        "checkout_enabled": False,
    },
    {
        "id": "dns-ssl",
        "name": "DNS & SSL Setup",
        "description": "DNS configuration, nameserver changes, HTTPS setup, and troubleshooting.",
        "availability": "inquiry_only",
        "provider_connection": "not_configured",
        "live_availability_check": False,
        "checkout_enabled": False,
    },
]


@router.get("/api/v1/domain-hosting/public/catalog")
def public_domain_hosting_catalog():
    """Return service categories without private account or provider data."""
    return {
        "success": True,
        "catalog": "SUPREMESETUHUB_DOMAIN_HOSTING",
        "catalog_version": "1.0.0",
        "mode": "inquiry_only",
        "currency": None,
        "services": [dict(service) for service in _SERVICES],
        "notice": (
            "No live domain availability, provider pricing, checkout, payment, "
            "registration, or hosting provisioning is enabled by this catalog. "
            "Confirm a written quote and provider terms before purchasing."
        ),
    }
