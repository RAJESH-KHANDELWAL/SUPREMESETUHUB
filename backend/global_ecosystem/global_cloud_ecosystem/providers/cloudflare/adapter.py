"""Dependency-injected Cloudflare adapter; no implicit network calls."""
from typing import Any, Callable
from .config import CloudflareConfig

class CloudflareAdapter:
    provider_id = "cloudflare"
    def __init__(self, config: CloudflareConfig | None = None, handlers: dict[str, Callable[..., Any]] | None = None):
        self.config = config or CloudflareConfig.from_env()
        self._handlers = dict(handlers or {})
    def supports(self, operation: str) -> bool:
        return operation in self._handlers
    def execute(self, operation: str, **kwargs: Any) -> Any:
        handler = self._handlers.get(operation)
        if handler is None:
            raise NotImplementedError(f"Cloudflare operation is not configured: {operation}")
        return handler(config=self.config, **kwargs)
