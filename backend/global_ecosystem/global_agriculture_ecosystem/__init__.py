"""Bharat-to-global agriculture domain package."""
from ..domain_registry import get_domain_profile
from .catalog import list_modules, get_module
from .models import Farm, CropPlan, IrrigationEstimate
from .planning import estimate_irrigation_water_m3
from .validation import validate_crop_plan

_DOMAIN_ID = __name__.rsplit(".", 1)[-1]
DOMAIN_PROFILE = get_domain_profile(_DOMAIN_ID)

def get_profile() -> dict:
    """Return a detached copy of this domain's central metadata."""
    if DOMAIN_PROFILE is None:
        raise RuntimeError(f"No registered domain profile for {_DOMAIN_ID}")
    return get_domain_profile(_DOMAIN_ID)

__all__ = [
    "DOMAIN_PROFILE", "get_profile", "list_modules", "get_module",
    "Farm", "CropPlan", "IrrigationEstimate",
    "estimate_irrigation_water_m3", "validate_crop_plan",
]
