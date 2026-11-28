"""Injected Tencent Cloud handlers; SDK clients and network calls remain external."""
from typing import Any, Callable
from .config import TencentCloudConfig

class TencentCloudAdapter:
    provider_id = "tencent_cloud"
    def __init__(self, config: TencentCloudConfig | None = None, handlers: dict[str, Callable[..., Any]] | None = None):
        self.config = config or TencentCloudConfig.from_env()
        self._handlers = dict(handlers or {})
    def supports(self, operation: str) -> bool:
        return operation in self._handlers
    def execute(self, operation: str, **kwargs: Any) -> Any:
        handler = self._handlers.get(operation)
        if handler is None:
            raise NotImplementedError(f"Tencent Cloud operation is not configured: {operation}")
        return handler(config=self.config, **kwargs)
