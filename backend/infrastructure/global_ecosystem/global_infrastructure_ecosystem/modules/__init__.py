"""Canonical infrastructure modules and provider adapters owned by the Global Ecosystem."""
from importlib import import_module

ROOT_MODULES = {
    "controller": "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules.controller",
    "repository": "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules.repository",
    "service": "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules.service",
    "hostinger_catalog": "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules.hostinger_catalog",
    "hostinger_api": "backend.global_ecosystem.global_hosting_ecosystem.hostinger_api",
    "nsfwinfra": "backend.global_ecosystem.nsfwinfra_ecosystem.nsfwinfra",
}

def load_module(name: str):
    try:
        package = ROOT_MODULES[name]
    except KeyError as exc:
        raise KeyError(f"Unknown infrastructure module: {name}") from exc
    return import_module(package)

__all__ = ["ROOT_MODULES", "load_module"]
