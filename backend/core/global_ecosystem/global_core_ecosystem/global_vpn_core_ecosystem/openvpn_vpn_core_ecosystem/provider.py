"""openvpn VPN provider metadata only; no tunnel calls."""
from typing import Any
from ..catalog import get_provider as _get_provider
PROVIDER_ID="openvpn"
def get_provider()->dict[str,Any]:
 record=_get_provider(PROVIDER_ID)
 if record is None:raise RuntimeError("PROVIDER_NOT_REGISTERED")
 return record
