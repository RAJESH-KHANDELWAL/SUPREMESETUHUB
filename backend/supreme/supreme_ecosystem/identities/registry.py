"""Canonical registry for the four primary SUPREME ECOSYSTEM owner identities.

The separate rajesh_khandelwal_personal variant is intentionally not included.
"""
from .rajesh_khandelwal.identity import IDENTITY as RAJESH_KHANDELWAL
from .rajesh_khandelwal_official.identity import IDENTITY as RAJESH_KHANDELWAL_OFFICIAL
from .dr_rajesh_khandelwal_ibc.identity import IDENTITY as DR_RAJESH_KHANDELWAL_IBC
from .dr_rajesh_khandelwal_ibc_official.identity import IDENTITY as DR_RAJESH_KHANDELWAL_IBC_OFFICIAL

IDENTITIES = {
    "rajesh_khandelwal": RAJESH_KHANDELWAL,
    "rajesh_khandelwal_official": RAJESH_KHANDELWAL_OFFICIAL,
    "dr_rajesh_khandelwal_ibc": DR_RAJESH_KHANDELWAL_IBC,
    "dr_rajesh_khandelwal_ibc_official": DR_RAJESH_KHANDELWAL_IBC_OFFICIAL,
}

__all__ = ["IDENTITIES"]
