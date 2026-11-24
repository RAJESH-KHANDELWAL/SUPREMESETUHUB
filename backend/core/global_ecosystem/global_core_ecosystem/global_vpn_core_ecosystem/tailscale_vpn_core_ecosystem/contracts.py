"""tailscale provider contract delegating to shared VPN Core validation."""
from typing import Any
from ..contracts import validate_request as _validate_request
from .provider import PROVIDER_ID
def validate_request(payload:dict[str,Any])->dict[str,Any]:return _validate_request(payload,provider_id=PROVIDER_ID)
