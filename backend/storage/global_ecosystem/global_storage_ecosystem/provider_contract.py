"""Provider-neutral storage adapter contract; no cloud SDK is bundled."""
from abc import ABC, abstractmethod
from typing import BinaryIO

class StorageProviderAdapter(ABC):
    """Provider implementations supply authenticated, provider-specific behavior."""
    provider_id: str

    @abstractmethod
    def health_check(self) -> dict[str, object]:
        """Return a live authenticated health result."""

    @abstractmethod
    def list_objects(self, container: str, prefix: str = "") -> list[dict[str, object]]:
        """List objects visible to the configured identity."""

    @abstractmethod
    def upload(self, container: str, key: str, source: BinaryIO, *,
               content_type: str | None = None,
               metadata: dict[str, str] | None = None) -> dict[str, object]:
        """Stream an object to the provider."""

    @abstractmethod
    def download(self, container: str, key: str) -> BinaryIO:
        """Return a readable object stream."""

    @abstractmethod
    def delete(self, container: str, key: str) -> bool:
        """Delete an object subject to provider authorization."""
