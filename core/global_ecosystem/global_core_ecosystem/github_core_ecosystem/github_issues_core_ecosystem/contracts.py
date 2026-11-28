"""Issues family request contract; no network or credential access."""
from ..request_contracts import validate_family_request
FAMILY="issues"
def validate_request(payload): return validate_family_request(payload,FAMILY)
