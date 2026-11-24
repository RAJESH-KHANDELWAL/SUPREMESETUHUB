"""Email provider connector foundation for SUPREMESETUHUB."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class EmailProviderConnector(ABC):
    """Common contract for authorized email provider integrations."""

    provider_id: str = "UNKNOWN"

    @abstractmethod
    def health(self) -> dict[str, Any]:
        """Return non-sensitive connection health information."""
        raise NotImplementedError

    @abstractmethod
    def connect(self, **credentials: Any) -> dict[str, Any]:
        """Connect using the provider's official authorization mechanism."""
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> dict[str, Any]:
        """Disconnect the provider connection."""
        raise NotImplementedError

    def metadata(self) -> dict[str, Any]:
        """Return non-sensitive connector metadata."""
        return {
            "provider_id": self.provider_id,
            "status": "AVAILABLE",
        }
