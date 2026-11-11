"""Provider-scoped DeepSeek ecosystem catalog and request-planning package."""
from .catalog import CAPABILITIES, PRODUCTS, get_catalog
from .health import get_health
from .registry import get_product, list_capabilities, list_products
from .service import DeepSeekEcosystemService
from .validation import ALLOWED_OPERATIONS, safe_input_summary, validate_request

PROVIDER_ID = "deepseek"
LAYER = "GLOBAL_ECOSYSTEM"
STATUS = "CATALOG_AND_REQUEST_PLANNING_READY"

__all__ = [
    "PROVIDER_ID", "LAYER", "STATUS", "CAPABILITIES", "PRODUCTS",
    "get_catalog", "get_health", "DeepSeekEcosystemService",
    "ALLOWED_OPERATIONS", "validate_request", "safe_input_summary",
    "get_product", "list_capabilities", "list_products",
]
