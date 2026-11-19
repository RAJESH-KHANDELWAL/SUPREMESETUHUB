"""Frontend Foundation connector: validates both foundation contracts without cross-imports."""
from pathlib import Path

FOUNDATION_ROOT = Path(__file__).resolve().parent
REPOSITORY_ROOT = FOUNDATION_ROOT.parents[1]


def get_connection_status():
    paths = {
        "frontend_foundation": FOUNDATION_ROOT / "frontend_foundation",
        "backend_foundation_contract": FOUNDATION_ROOT / "backend_foundation",
        "backend_foundation_runtime": REPOSITORY_ROOT / "backend" / "foundation" / "backend_foundation",
        "backend_frontend_contract": REPOSITORY_ROOT / "backend" / "foundation" / "frontend_foundation",
    }
    checks = {name: path.is_dir() for name, path in paths.items()}
    return {"name": "FRONTEND-BACKEND FOUNDATION CONNECTION", "status": "CONNECTED" if all(checks.values()) else "INCOMPLETE", "checks": checks, "connected": all(checks.values())}


def connect():
    return get_connection_status()
