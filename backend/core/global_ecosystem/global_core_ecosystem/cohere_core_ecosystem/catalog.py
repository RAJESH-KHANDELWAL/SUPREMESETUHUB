"""Provider-level Cohere CORE capability catalog."""
from .capabilities.catalog import CAPABILITIES
PROVIDER = "cohere"
LAYER = "CORE"
STATUS = "interface_only"
def list_capabilities():
    return dict(CAPABILITIES)
