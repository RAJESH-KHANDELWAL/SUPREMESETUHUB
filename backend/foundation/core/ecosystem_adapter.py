"""Shared adapter contract for Foundation ecosystem managers."""


class FoundationEcosystemAdapter:
    """Expose an existing Foundation component through an ecosystem boundary."""

    NAME = "FOUNDATION_ECOSYSTEM"
    COMPONENT_KEY = "component"

    def __init__(self, component):
        if component is None:
            raise ValueError("Foundation component is required.")
        self._component = component

    def get_component(self):
        """Return the original component; no duplicate implementation is made."""
        return self._component

    def status(self):
        """Report integration state and the wrapped component type."""
        return {
            "ecosystem": self.NAME,
            "status": "INTEGRATED",
            "component_key": self.COMPONENT_KEY,
            "component_type": type(self._component).__name__,
        }
