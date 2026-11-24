"""Safe validation for DigitalOcean operation plans; performs no network calls."""
from .catalog import CAPABILITY_BY_ID
from .models import OperationRequest

VALID_ACTIONS = {"list", "get", "create", "update", "delete", "deploy", "resize", "assign", "detach"}


def validate_request(request):
    errors = []
    if not isinstance(request, OperationRequest):
        return ["request must be an OperationRequest"]
    capability = CAPABILITY_BY_ID.get(request.capability_id)
    if capability is None:
        errors.append("unknown capability_id")
        return errors
    if request.action not in VALID_ACTIONS:
        errors.append("unsupported action")
    if request.action in {"create", "update", "delete", "deploy", "resize", "assign", "detach"} and not capability.requires_credentials:
        pass
    is_destructive = request.action == "delete" or capability.destructive and request.action in {"create", "update", "resize", "assign", "detach"}
    if is_destructive and not request.confirmation:
        errors.append("explicit confirmation is required for this potentially destructive action")
    if request.region and len(request.region) > 64:
        errors.append("region must be 64 characters or fewer")
    return errors
