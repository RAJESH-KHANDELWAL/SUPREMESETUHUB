"""Canonical registry for the four primary SUPREME owner identities.

Uses the richer top-level identity records so the registry retains internal IDs,
domain metadata and taglines. The separate personal-brand variant is excluded.
"""
from ..rajesh_khandelwal import IDENTITY as RAJESH_KHANDELWAL
from ..rajesh_khandelwal_official import IDENTITY as RAJESH_KHANDELWAL_OFFICIAL
from ..dr_rajesh_khandelwal_ibc import IDENTITY as DR_RAJESH_KHANDELWAL_IBC
from ..dr_rajesh_khandelwal_ibc_official import IDENTITY as DR_RAJESH_KHANDELWAL_IBC_OFFICIAL

IDENTITIES = {
    "rajesh_khandelwal": RAJESH_KHANDELWAL,
    "rajesh_khandelwal_official": RAJESH_KHANDELWAL_OFFICIAL,
    "dr_rajesh_khandelwal_ibc": DR_RAJESH_KHANDELWAL_IBC,
    "dr_rajesh_khandelwal_ibc_official": DR_RAJESH_KHANDELWAL_IBC_OFFICIAL,
}

__all__ = ["IDENTITIES"]
