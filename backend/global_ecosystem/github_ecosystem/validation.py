"""Validation for GitHub operation plans; no network calls."""
from .catalog import CAPABILITY_BY_ID
from .models import OperationRequest

VALID_ACTIONS = {"list", "get", "search", "create", "update", "delete", "review", "merge", "dispatch", "download", "compare"}
WRITE_ACTIONS = {"create", "update", "delete", "review", "merge", "dispatch", "download"}

def validate_request(request):
    if not isinstance(request, OperationRequest):
        return ["request must be an OperationRequest"]
    errors = []
    if request.capability_id not in CAPABILITY_BY_ID:
        return ["unknown capability_id"]
    if request.action not in VALID_ACTIONS:
        errors.append("unsupported action")
    if request.action in WRITE_ACTIONS and not request.confirmation:
        errors.append("explicit confirmation is required for a write or state-changing action")
    if request.owner and (len(request.owner) > 100 or "/" in request.owner.strip("/")):
        errors.append("owner must be a single GitHub account or organization name")
    if request.repository and (len(request.repository) > 100 or "/" in request.repository.strip("/")):
        errors.append("repository must be a single repository name")
    if request.action in {"create", "update", "delete", "merge", "dispatch"} and not request.owner:
        errors.append("owner is required for this action")
    if request.repository and not request.owner:
        errors.append("owner is required when repository is supplied")
    return errors
