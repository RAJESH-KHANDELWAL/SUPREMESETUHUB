"""Route registration placeholder for Cloudflare AI APIs.

No HTTP routes are mounted by this module. Wire routes only after a real adapter,
configuration, auth checks and tests are implemented.
"""
from .service import get_capabilities, get_status

ROUTE_PREFIX = "/api/v1/cloudflare/ai"

__all__ = ["ROUTE_PREFIX", "get_status", "get_capabilities"]
