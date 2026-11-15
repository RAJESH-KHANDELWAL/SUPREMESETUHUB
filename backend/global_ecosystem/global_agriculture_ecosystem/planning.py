"""Transparent, input-driven irrigation planning calculations."""
from .models import IrrigationEstimate

def estimate_irrigation_water_m3(
    area_hectares: float,
    reference_et0_mm_day: float,
    crop_coefficient: float,
    days: float = 1.0,
) -> IrrigationEstimate:
    """Estimate net crop water use from ET0 x Kc.

    1 mm over 1 hectare equals 10 m3. Excludes rainfall, stored soil moisture,
    application/conveyance losses and local restrictions. ET0 and Kc must come
    from appropriate local agronomic data.
    """
    values = (area_hectares, reference_et0_mm_day, crop_coefficient, days)
    if any(value < 0 for value in values):
        raise ValueError("Inputs cannot be negative")
    if area_hectares == 0 or days == 0:
        raise ValueError("area_hectares and days must be greater than zero")
    depth_mm = reference_et0_mm_day * crop_coefficient * days
    volume_m3 = depth_mm * area_hectares * 10
    return IrrigationEstimate(depth_mm, area_hectares, volume_m3)
