"""GitHub GraphQL CORE family."""
from .contracts import validate_request
from .service import GitHubGraphqlCoreService
__all__=["validate_request","GitHubGraphqlCoreService"]
