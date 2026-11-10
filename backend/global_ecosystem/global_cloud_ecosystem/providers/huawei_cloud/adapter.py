"""Injected Huawei Cloud handlers; SDK clients and network calls remain external."""
from typing import Any, Callable
from .config import HuaweiCloudConfig

class HuaweiCloudAdapter:
    provider_id = "huawei_cloud"
    def __init__(self, config: HuaweiCloudConfig | None = None, handlers: dict[str, Callable[..., Any]] | None = None):
        self.config = config or HuaweiCloudConfig.from_env()
        self._handlers = dict(handlers or {})
    def supports(self, operation: str) -> bool:
        return operation in self._handlers
    def execute(self, operation: str, **kwargs: Any) -> Any:
        handler = self._handlers.get(operation)
        if handler is None:
            raise NotImplementedError(f"Huawei Cloud operation is not configured: {operation}")
        return handler(config=self.config, **kwargs)
