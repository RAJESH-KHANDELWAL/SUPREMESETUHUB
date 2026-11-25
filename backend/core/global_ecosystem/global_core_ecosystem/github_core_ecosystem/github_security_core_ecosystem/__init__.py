"""GitHub Security CORE family."""
from .contracts import validate_request
from .service import GitHubSecurityCoreService
__all__=["validate_request","GitHubSecurityCoreService"]
