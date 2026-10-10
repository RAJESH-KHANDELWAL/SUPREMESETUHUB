
"""GLOBAL ECOSYSTEM API."""

from backend.engines.global_ecosystem import (
    GlobalEcosystemManager,
)


class GlobalEcosystemAPI:
    """API facade for the GLOBAL ECOSYSTEM."""

    def __init__(self):
        self.engine = GlobalEcosystemManager()

    def status(self) -> dict:
        """Return GLOBAL ECOSYSTEM status."""
        return self.engine.status()

    def health(self) -> dict:
        """Return GLOBAL ECOSYSTEM health."""
        return self.engine.health()

    def list(self) -> list:
        """Return all registered ecosystems."""
        return self.engine.list()

    def names(self) -> list:
        """Return all registered ecosystem names."""
        return self.engine.names()

    def get(self, ecosystem_id: str) -> dict:
        """Return one registered ecosystem."""
        return self.engine.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        """Check whether an ecosystem exists."""
        return self.engine.exists(ecosystem_id)

    def tree(self) -> dict:
        """Return the GLOBAL ECOSYSTEM hierarchy."""
        return self.engine.tree()

    def connection_map(self) -> dict:
        """Return the connection map."""
        return self.engine.connection_map()


# Compatibility alias for existing app integrations.
EcosystemAPI = GlobalEcosystemAPI
