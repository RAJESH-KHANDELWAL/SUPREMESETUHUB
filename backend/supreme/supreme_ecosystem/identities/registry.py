"""Registry connecting all four identity modules to SUPREME ECOSYSTEM."""
from .dr_rajesh_khandelwal_ibc import DR_RAJESH_KHANDELWAL_IBC_BRAND
from .dr_rajesh_khandelwal_ibc_official import DR_RAJESH_KHANDELWAL_IBC_OFFICIAL_BRAND
from .rajesh_khandelwal_official import RAJESH_KHANDELWAL_OFFICIAL_BRAND
from .rajesh_khandelwal_personal import RAJESH_KHANDELWAL_PERSONAL_BRAND

IDENTITIES = {
    "dr_rajesh_khandelwal_ibc": DR_RAJESH_KHANDELWAL_IBC_BRAND,
    "dr_rajesh_khandelwal_ibc_official": DR_RAJESH_KHANDELWAL_IBC_OFFICIAL_BRAND,
    "rajesh_khandelwal_official": RAJESH_KHANDELWAL_OFFICIAL_BRAND,
    "rajesh_khandelwal_personal": RAJESH_KHANDELWAL_PERSONAL_BRAND,
}
__all__ = ["IDENTITIES"]
