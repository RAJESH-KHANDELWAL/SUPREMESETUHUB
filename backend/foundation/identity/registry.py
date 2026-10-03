class FoundationRegistry:
    """
    Central registry for Foundation-level components.

    यह components को register और lookup करता है।
    यह API, CORE या ENGINE का implementation नहीं है।
    """

    NAME = "MAIN BASE FOUNDATION REGISTRY"

    def __init__(self):
        self._components = {}

    def register(self, name, component):
        if not name:
            raise ValueError("Component name is required.")

        if component is None:
            raise ValueError("Component cannot be None.")

        self._components[name] = component

        return {
            "name": name,
            "status": "REGISTERED",
        }

    def get(self, name):
        return self._components.get(name)

    def exists(self, name):
        return name in self._components

    def unregister(self, name):
        if name in self._components:
            del self._components[name]

            return {
                "name": name,
                "status": "UNREGISTERED",
            }

        return {
            "name": name,
            "status": "NOT_FOUND",
        }

    def list_components(self):
        return {
            "registry": self.NAME,
            "count": len(self._components),
            "components": list(self._components.keys()),
        }

    def clear(self):
        self._components.clear()

        return {
            "registry": self.NAME,
            "status": "CLEARED",
        }
