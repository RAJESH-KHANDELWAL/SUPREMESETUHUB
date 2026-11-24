"""GitHub Webhooks CORE family."""
from .contracts import validate_request
from .service import GitHubWebhooksCoreService
__all__=["validate_request","GitHubWebhooksCoreService"]
