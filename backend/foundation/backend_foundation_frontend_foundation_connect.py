"""Backend-side connector for the Backend and Frontend Foundation roots."""
from pathlib import Path


def connect_foundations() -> dict:
    """Validate the two foundation roots and their manager entry points."""
    repository_root = Path(__file__).resolve().parents[2]
    backend_root = repository_root / "backend/foundation"
    frontend_root = repository_root / "frontend/foundation"
    checks = {
        "backend_foundation_root": backend_root.is_dir(),
        "backend_manager_py": (backend_root / "manager.py").is_file(),
        "backend_manager_php": (backend_root / "manager.php").is_file(),
        "frontend_foundation_root": frontend_root.is_dir(),
        "frontend_manager_py": (frontend_root / "manager.py").is_file(),
        "frontend_manager_php": (frontend_root / "manager.php").is_file(),
    }
    connected = all(checks.values())
    return {
        "name": "BACKEND FOUNDATION ↔ FRONTEND FOUNDATION",
        "status": "CONNECTED" if connected else "INCOMPLETE",
        "checks": checks,
        "connected": connected,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(connect_foundations(), indent=2))
