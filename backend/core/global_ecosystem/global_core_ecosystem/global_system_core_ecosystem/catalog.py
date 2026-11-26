"""Canonical provider inventory for the Global System Core layer.

System Core describes operating-system and host-platform metadata. It does not
install systems, change host configuration, execute commands or claim a live
connection to any provider.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

ROOT = "backend/core/global_ecosystem/global_core_ecosystem/global_system_core_ecosystem"

_PROVIDER_ROWS = [["apple","Apple","PROPRIETARY_OS_VENDOR"],["microsoft","Microsoft","PROPRIETARY_OS_VENDOR"],["google","Google","MOBILE_AND_CLOUD_OS_VENDOR"],["canonical","Canonical","LINUX_DISTRIBUTION_VENDOR"],["redhat","Red Hat","LINUX_DISTRIBUTION_VENDOR"],["debian","Debian","COMMUNITY_LINUX_DISTRIBUTION"],["suse","SUSE","LINUX_DISTRIBUTION_VENDOR"],["oracle","Oracle","ENTERPRISE_OS_VENDOR"],["amazon","Amazon Web Services","CLOUD_AND_EMBEDDED_OS_VENDOR"],["ibm","IBM","ENTERPRISE_AND_MAINFRAME_OS_VENDOR"],["freebsd","FreeBSD Project","BSD_OS_PROJECT"],["openbsd","OpenBSD Project","BSD_OS_PROJECT"],["netbsd","NetBSD Project","BSD_OS_PROJECT"],["vmware","VMware by Broadcom","VIRTUALIZATION_VENDOR"],["proxmox","Proxmox","VIRTUALIZATION_VENDOR"],["qnx","BlackBerry QNX","REAL_TIME_OS_VENDOR"],["zephyr","Zephyr Project","REAL_TIME_OS_PROJECT"],["freertos","FreeRTOS","REAL_TIME_OS_PROJECT"],["linux_foundation","Linux Foundation","KERNEL_AND_OPEN_SOURCE_GOVERNANCE"],["community_linux","Independent Linux Distributions","COMMUNITY_LINUX_DISTRIBUTIONS"],["illumos","illumos Foundation and Community","UNIX_DERIVATIVE_PROJECT"]]

SYSTEM_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "GLOBAL-SYSTEM-CORE-ECOSYSTEM",
    "name": "GLOBAL SYSTEM CORE ECOSYSTEM",
    "ecosystem_type": "GLOBAL_SYSTEM_CONTROL_PLANE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "CORE_CATALOG_ONLY",
    "enabled": True,
    "provider_count": len(_PROVIDER_ROWS),
    "product_index_ref": f"{ROOT}/product_ecosystem_index.json",
    "master_catalog_ref": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
    "live_connections_verified": False,
    "api_transport_in_core": False,
    "capabilities": [
        "SYSTEM_PROVIDER_DISCOVERY", "OS_PRODUCT_INVENTORY",
        "OS_FAMILY_AND_RELEASE_CLASSIFICATION", "SYSTEM_DOMAIN_CLASSIFICATION",
        "SUPPORT_LIFECYCLE_METADATA", "HOST_PLATFORM_COMPATIBILITY_METADATA",
        "SYSTEM_SECURITY_POSTURE_METADATA", "VIRTUALIZATION_AND_RTOS_CLASSIFICATION",
    ],
    "providers": [
        {
            "provider_id": provider_id,
            "name": name,
            "provider_type": provider_type,
            "package_path": f"{ROOT}/{provider_id}_system_core_ecosystem",
            "manager_path": f"{ROOT}/{provider_id}_system_core_ecosystem/manager.py",
            "status": "CORE_CATALOG_ONLY",
            "live_connection_verified": False,
        }
        for provider_id, name, provider_type in _PROVIDER_ROWS
    ],
}


def get_system_core_catalog() -> dict[str, Any]:
    return deepcopy(SYSTEM_CORE_ECOSYSTEM)


def list_system_providers() -> list[dict[str, Any]]:
    return deepcopy(SYSTEM_CORE_ECOSYSTEM["providers"])
