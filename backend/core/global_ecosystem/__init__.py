"""GLOBAL ECOSYSTEM layer under CORE; implementations live in GLOBAL CORE ECOSYSTEM."""
from importlib import import_module

_EXPORTS = {
    "EcosystemIdentity": "models",
    "GlobalEcosystemIdentity": "models",
    "EcosystemManager": "manager",
    "GlobalEcosystemManager": "manager",
    "EcosystemRegistry": "registry",
    "GlobalEcosystemRegistry": "registry",
}
__all__ = list(_EXPORTS)

def __getattr__(name: str):
    module_name = _EXPORTS.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = import_module(f".global_core_ecosystem.{module_name}", __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value
