class FoundationFileManager:
    """
    MAIN BASE FOUNDATION file manager.

    Foundation-level file operations को coordinate करता है।

    Actual storage implementation existing
    backend/storage/ में रहेगा।
    """

    NAME = "FOUNDATION FILE MANAGER"

    def __init__(self):
        self._files = {}

    def register(self, name, location=None, metadata=None):
        if not name:
            raise ValueError("File name is required.")

        self._files[name] = {
            "location": location,
            "metadata": metadata or {},
        }

        return {
            "name": name,
            "status": "REGISTERED",
        }

    def get(self, name):
        return self._files.get(name)

    def exists(self, name):
        return name in self._files

    def list_files(self):
        return {
            "manager": self.NAME,
            "count": len(self._files),
            "files": list(self._files.keys()),
        }

    def remove(self, name):
        if name not in self._files:
            return {
                "name": name,
                "status": "NOT_FOUND",
            }

        del self._files[name]

        return {
            "name": name,
            "status": "UNREGISTERED",
        }
