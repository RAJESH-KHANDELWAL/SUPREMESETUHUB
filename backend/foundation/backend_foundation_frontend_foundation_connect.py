"""Backend-side connector for the Backend and Frontend Foundation packages.

This module validates the repository contract without importing frontend runtime code.
"""
from pathlib import Path


def connect_foundations() -> dict:
    """Check that both foundation packages and their mirrored contracts exist."""
    repository_root = Path(__file__).resolve().parents[2]
    checks = {
        "backend_foundation": (repository_root / "backend/foundation/backend_foundation").is_dir(),
        "backend_frontend_contract": (repository_root / "backend/foundation/frontend_foundation").is_dir(),
        "frontend_foundation": (repository_root / "frontend/foundation/frontend_foundation").is_dir(),
        "frontend_backend_contract": (repository_root / "frontend/foundation/backend_foundation").is_dir(),
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
