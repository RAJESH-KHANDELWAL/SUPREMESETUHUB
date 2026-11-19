"""Backend-owned view of the Frontend Foundation contract; no frontend runtime imports."""
from pathlib import Path

class FrontendFoundationContractManager:
    NAME = "FRONTEND FOUNDATION CONTRACT"
    def __init__(self):
        self.root = Path(__file__).resolve().parent
    def health(self):
        checks = {"package": (self.root / "__init__.py").is_file(), "manager": (self.root / "manager.py").is_file(), "php_bridge": (self.root / "manager.php").is_file()}
        return {"name": self.NAME, "status": "READY" if all(checks.values()) else "INCOMPLETE", "checks": checks, "healthy": all(checks.values())}

def get_manager():
    return FrontendFoundationContractManager()
