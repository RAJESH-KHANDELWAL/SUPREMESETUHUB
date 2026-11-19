"""GitHub Pull Requests CORE family."""
from .contracts import validate_request
from .service import GitHubPullRequestsCoreService
__all__=["validate_request","GitHubPullRequestsCoreService"]
