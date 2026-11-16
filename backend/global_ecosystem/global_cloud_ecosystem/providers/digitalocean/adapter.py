"""Dependency-injected DigitalOcean adapter; no implicit network calls."""
from typing import Any, Callable
from .config import DigitalOceanConfig

class DigitalOceanAdapter:
    provider_id = "digitalocean"
    def __init__(self, config: DigitalOceanConfig | None = None, handlers: dict[str, Callable[..., Any]] | None = None):
        self.config = config or DigitalOceanConfig.from_env()
        self._handlers = dict(handlers or {})
    def supports(self, operation: str) -> bool:
        return operation in self._handlers
    def execute(self, operation: str, **kwargs: Any) -> Any:
        handler = self._handlers.get(operation)
        if handler is None:
            raise NotImplementedError(f"DigitalOcean operation is not configured: {operation}")
        return handler(config=self.config, **kwargs)
