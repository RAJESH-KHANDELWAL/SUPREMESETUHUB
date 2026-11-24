"""Dependency-injected Google Cloud adapter; SDK clients are supplied by callers."""
from typing import Any, Callable
from .config import GoogleCloudConfig


class GoogleCloudAdapter:
    provider_id = "google_cloud"

    def __init__(self, config: GoogleCloudConfig | None = None, handlers: dict[str, Callable[..., Any]] | None = None):
        self.config = config or GoogleCloudConfig.from_env()
        self._handlers = dict(handlers or {})

    def supports(self, operation: str) -> bool:
        return operation in self._handlers

    def execute(self, operation: str, **kwargs: Any) -> Any:
        handler = self._handlers.get(operation)
        if handler is None:
            raise NotImplementedError(f"Google Cloud operation is not configured: {operation}")
        return handler(config=self.config, **kwargs)
