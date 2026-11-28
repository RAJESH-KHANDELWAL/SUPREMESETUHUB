"""tailscale VPN Core provider package."""
from .provider import get_provider
from .contracts import validate_request
__all__=["get_provider","validate_request"]
