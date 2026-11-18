"""Input validation for agriculture domain records."""
from .models import CropPlan, Farm

def validate_farm(farm: Farm) -> list[str]:
    errors = []
    if not farm.farm_id.strip():
        errors.append("farm_id is required")
    if not farm.name.strip():
        errors.append("name is required")
    if len(farm.country_code) != 2 or not farm.country_code.isalpha():
        errors.append("country_code must be a two-letter code")
    if farm.area_hectares <= 0:
        errors.append("area_hectares must be greater than zero")
    return errors

def validate_crop_plan(plan: CropPlan) -> list[str]:
    errors = []
    if not plan.farm_id.strip():
        errors.append("farm_id is required")
    if not plan.crop_name.strip():
        errors.append("crop_name is required")
    if plan.area_hectares <= 0:
        errors.append("area_hectares must be greater than zero")
    if not plan.season.strip():
        errors.append("season is required")
    if plan.reference_et0_mm_day is not None and plan.reference_et0_mm_day < 0:
        errors.append("reference_et0_mm_day cannot be negative")
    if plan.crop_coefficient is not None and plan.crop_coefficient < 0:
        errors.append("crop_coefficient cannot be negative")
    return errors
