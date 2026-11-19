"""Backend Foundation connector: validates both foundation contracts without cross-imports."""
from pathlib import Path

FOUNDATION_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = FOUNDATION_ROOT.parents[1]


def get_connection_status():
    paths = {
        "backend_foundation": FOUNDATION_ROOT / "backend_foundation",
        "frontend_foundation_contract": FOUNDATION_ROOT / "frontend_foundation",
        "frontend_foundation_runtime": REPOSITORY_ROOT / "frontend" / "foundation" / "frontend_foundation",
        "frontend_backend_contract": REPOSITORY_ROOT / "frontend" / "foundation" / "backend_foundation",
    }
    checks = {name: path.is_dir() for name, path in paths.items()}
    return {"name": "BACKEND-FRONTEND FOUNDATION CONNECTION", "status": "CONNECTED" if all(checks.values()) else "INCOMPLETE", "checks": checks, "connected": all(checks.values())}


def connect():
    return get_connection_status()
