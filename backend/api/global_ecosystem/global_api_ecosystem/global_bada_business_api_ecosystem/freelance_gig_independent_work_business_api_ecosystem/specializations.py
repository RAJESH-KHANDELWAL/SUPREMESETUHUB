"""Aggregate router for all independent freelance specialization APIs."""
from importlib import import_module
from fastapi import APIRouter
from . import SUBCATEGORY_IDS

router = APIRouter(tags=["Freelance & Gig Specializations"])
for specialization_id in SUBCATEGORY_IDS:
    specialization_router = import_module(f"{__package__}.{specialization_id}.routes").router
    router.include_router(specialization_router)
