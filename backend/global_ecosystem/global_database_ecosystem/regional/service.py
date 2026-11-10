"""Regional deployment and data-residency classification helpers."""
from ..catalog import REGIONS
def list_regions():
    return {key: tuple(value) for key, value in REGIONS.items()}
def describe_residency_scope(region: str):
    if region not in REGIONS:
        raise KeyError(f"unknown region: {region}")
    return {"region":region,"locations":list(REGIONS[region]),"checks":["applicable_law","contractual_residency","transfer_mechanism","backup_location","subprocessor_locations"],"legal_review_required":True}
