"""Typed metadata for company-specific modules.

These records describe code modules, not verified company profiles.
"""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CompanyModule:
    company_id: str
    name: str
    package_path: str
    module_status: str = "package_present"
    profile_registry_status: str = "not_connected"
    data_status: str = "module_index_only"
