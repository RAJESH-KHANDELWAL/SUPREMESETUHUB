"""GitHub Issues CORE family."""
from .contracts import validate_request
from .service import GitHubIssuesCoreService
__all__=["validate_request","GitHubIssuesCoreService"]
