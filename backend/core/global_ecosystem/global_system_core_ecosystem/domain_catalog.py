"""System responsibility taxonomy mapped to the canonical product inventory."""
from __future__ import annotations

from typing import Any
from .product_catalog import list_system_products

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    "SYSTEM_GOVERNANCE": {"name": "System Governance", "purpose": "Provider identity, product lifecycle, support status, release provenance and system inventory."},
    "DESKTOP_OPERATING_SYSTEMS": {"name": "Desktop Operating Systems", "purpose": "Desktop and workstation operating systems and their supported editions."},
    "SERVER_OPERATING_SYSTEMS": {"name": "Server Operating Systems", "purpose": "Enterprise, cloud and general-purpose server operating systems."},
    "MOBILE_OPERATING_SYSTEMS": {"name": "Mobile Operating Systems", "purpose": "Phone, tablet, wearable, TV and automotive operating systems."},
    "LINUX_DISTRIBUTIONS": {"name": "Linux Distributions", "purpose": "Linux distribution families, release channels, package ecosystems and support models."},
    "UNIX_AND_BSD_SYSTEMS": {"name": "UNIX and BSD Systems", "purpose": "Commercial UNIX, BSD, illumos and Unix-like operating system families."},
    "REAL_TIME_AND_EMBEDDED_SYSTEMS": {"name": "Real-time and Embedded Systems", "purpose": "RTOS, embedded Linux, appliance and safety/mission-oriented operating systems."},
    "KERNELS_AND_BOOT": {"name": "Kernels and Boot", "purpose": "Kernel families, bootloaders, init systems, boot chains and kernel lifecycle metadata."},
    "FIRMWARE_AND_DRIVERS": {"name": "Firmware and Drivers", "purpose": "Device firmware, hardware abstraction, drivers, compatibility and update boundaries."},
    "VIRTUALIZATION_AND_HYPERVISORS": {"name": "Virtualization and Hypervisors", "purpose": "Type-1 and Type-2 hypervisors, virtual machine hosts and management platforms."},
    "CONTAINERS_AND_SYSTEM_RUNTIME": {"name": "Containers and System Runtime", "purpose": "Container runtime, system service managers, isolation and host runtime metadata."},
    "SYSTEM_SECURITY_AND_HARDENING": {"name": "System Security and Hardening", "purpose": "Secure boot, encryption, access control, patch posture and baseline hardening."},
    "NETWORKING_AND_SYSTEM_SERVICES": {"name": "Networking and System Services", "purpose": "Host networking, DNS, firewall, remote access, service discovery and core system services."},
    "FILESYSTEMS_AND_STORAGE": {"name": "Filesystems and Storage", "purpose": "Local, network and distributed filesystems, volumes, snapshots and storage drivers."},
    "UPDATES_AND_LIFECYCLE": {"name": "Updates and Lifecycle", "purpose": "Installation, release channels, patching, end-of-life and long-term support."},
    "OBSERVABILITY_AND_DIAGNOSTICS": {"name": "Observability and Diagnostics", "purpose": "System health, logs, metrics, tracing, crash reporting and troubleshooting."},
    "BACKUP_AND_RECOVERY": {"name": "Backup and Recovery", "purpose": "System images, configuration backup, restore, disaster recovery and rollback."},
    "LICENSING_AND_INTEROPERABILITY": {"name": "Licensing and Interoperability", "purpose": "Licensing, standards, compatibility, migration and cross-platform interoperability."},
}


def list_system_domain_inventory() -> list[dict[str, Any]]:
    products = list_system_products()
    inventory = []
    for domain_id, definition in DOMAIN_DEFINITIONS.items():
        members = [item for item in products if domain_id in item.get("domain_ids", [])]
        inventory.append({
            "domain_id": domain_id,
            **definition,
            "product_count": len(members),
            "product_ids": [item["product_id"] for item in members],
        })
    return inventory


def system_domain_summary() -> dict[str, Any]:
    domains = list_system_domain_inventory()
    return {
        "success": True,
        "domain_count": len(domains),
        "product_count": len(list_system_products()),
        "unassigned_product_count": sum(1 for item in list_system_products() if not item.get("domain_ids")),
        "domains": domains,
    }
