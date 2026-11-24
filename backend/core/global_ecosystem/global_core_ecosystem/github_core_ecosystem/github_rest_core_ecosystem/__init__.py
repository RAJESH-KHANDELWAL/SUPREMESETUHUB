"""GitHub REST CORE family."""
from .contracts import validate_request
from .service import GitHubRestCoreService
__all__=["validate_request","GitHubRestCoreService"]
