"""Top-level BADA BUSINESS ECOSYSTEM package."""
from .platform_resources import get_catalog, get_program, list_programs
ECOSYSTEM = {"id":"BADA_BUSINESS_ECOSYSTEM","name":"BADA BUSINESS ECOSYSTEM","parent":"GLOBAL ECOSYSTEM","components":["platform","links","programs","courses","products","events","registration","referrals","api_ecosystem"]}
__all__ = ["ECOSYSTEM","get_catalog","get_program","list_programs"]
