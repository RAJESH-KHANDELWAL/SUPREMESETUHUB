"""WireGuard provider metadata; no network or tunnel calls."""
from typing import Any
from ..catalog import get_provider as _get_provider
from ..contracts import validate_request as _validate_request
PROVIDER_ID="wireguard"
def get_provider()->dict[str,Any]:
 record=_get_provider(PROVIDER_ID)
 if record is None:raise RuntimeError("PROVIDER_NOT_REGISTERED")
 return record
def validate_request(payload:dict[str,Any])->dict[str,Any]:return _validate_request(payload,provider_id=PROVIDER_ID)
