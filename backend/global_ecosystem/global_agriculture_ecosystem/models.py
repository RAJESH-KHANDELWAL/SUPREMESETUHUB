"""Core data models for agriculture workflows.

These are data structures only; persistence and external integrations are separate.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Farm:
    farm_id: str
    name: str
    country_code: str
    region: str
    area_hectares: float

@dataclass(frozen=True)
class CropPlan:
    farm_id: str
    crop_name: str
    area_hectares: float
    season: str
    reference_et0_mm_day: Optional[float] = None
    crop_coefficient: Optional[float] = None

@dataclass(frozen=True)
class IrrigationEstimate:
    water_depth_mm: float
    area_hectares: float
    water_volume_m3: float
    method: str = "ET0 x crop_coefficient; gross losses excluded"
