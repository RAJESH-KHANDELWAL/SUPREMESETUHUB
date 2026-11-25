"""GitHub Authentication CORE family."""
from .contracts import validate_request
from .service import GitHubAuthenticationCoreService
__all__=["validate_request","GitHubAuthenticationCoreService"]
