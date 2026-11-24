"""Cloudflare vendor ecosystem namespace.

Provider-specific catalog and adapter stay here. Shared cloud orchestration,
domain contracts, persistence and security remain in their canonical layers.
"""

from .catalog import CLOUDFLARE_CAPABILITIES, get_cloudflare_catalog, validate_cloudflare_catalog
from .client import CloudflareAPIError, CloudflareClient

__all__ = [
    "CLOUDFLARE_CAPABILITIES",
    "get_cloudflare_catalog",
    "validate_cloudflare_catalog",
    "CloudflareAPIError",
    "CloudflareClient",
]
