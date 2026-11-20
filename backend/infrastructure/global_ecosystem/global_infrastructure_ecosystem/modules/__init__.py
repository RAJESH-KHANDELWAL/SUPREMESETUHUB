"""Lazy adapters for existing infrastructure root modules."""
from importlib import import_module

ROOT_MODULES = {
    "controller": "backend.infrastructure.controller",
    "hostinger_api": "backend.infrastructure.global_ecosystem.hostinger_api",
    "hostinger_catalog": "backend.infrastructure.hostinger_catalog",
    "nsfwinfra": "backend.infrastructure.global_ecosystem.nsfwinfra",
    "repository": "backend.infrastructure.repository",
    "service": "backend.infrastructure.service",
}


def load_module(name: str):
    """Load one canonical infrastructure root module by registered name."""
    try:
        package = ROOT_MODULES[name]
    except KeyError as exc:
        raise KeyError(f"Unknown infrastructure module: {name}") from exc
    return import_module(package)


__all__ = ["ROOT_MODULES", "load_module"]
