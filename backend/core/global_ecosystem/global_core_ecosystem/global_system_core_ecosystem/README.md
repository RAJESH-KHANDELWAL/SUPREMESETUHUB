# GLOBAL SYSTEM CORE ECOSYSTEM

**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_system_core_ecosystem/`  
**Parent:** GLOBAL CORE ECOSYSTEM

## Mission

A provider-neutral, read-only control plane for operating-system families, system platforms, kernels, boot chains, firmware/driver boundaries, virtualization, host security, lifecycle and interoperability.

## Architecture

- `catalog.py`: provider identity and provider package registry.
- `product_ecosystem_index.json`: curated product-family inventory and domain mappings.
- `product_catalog.py`: validated product discovery and filtering.
- `domain_catalog.py`: responsibility taxonomy and coverage inventory.
- `domain_runtime.py`: shared domain manager runtime.
- `contracts.py`: tenant, secret-reference, readiness and result contracts.
- `policy.py`: metadata policy classification and safe output filtering.
- `module_service.py`: reusable provider/product facades.
- `orchestrator.py`: provider, product, domain, health and dependency discovery.
- `service.py` and `manager.py`: public service and canonical entry point.
- `manager.php`: read-only PHP interoperability facade.
- `integrations/registry.py`: explicit boundaries to API, Security, Server and Software layers.
- `services/system_inventory_service.py`: read-only inventory service.
- `tools/validate_system_catalog.py`: structural and referential integrity validation.
- `global_*_core_ecosystem/`: domain facades backed by the shared runtime.
- `*_system_core_ecosystem/`: provider facades backed by the shared provider service.

## Coverage domains

1. System Governance (`SYSTEM_GOVERNANCE`)
2. Desktop Operating Systems (`DESKTOP_OPERATING_SYSTEMS`)
3. Server Operating Systems (`SERVER_OPERATING_SYSTEMS`)
4. Mobile Operating Systems (`MOBILE_OPERATING_SYSTEMS`)
5. Linux Distributions (`LINUX_DISTRIBUTIONS`)
6. UNIX and BSD Systems (`UNIX_AND_BSD_SYSTEMS`)
7. Real-time and Embedded Systems (`REAL_TIME_AND_EMBEDDED_SYSTEMS`)
8. Kernels and Boot (`KERNELS_AND_BOOT`)
9. Firmware and Drivers (`FIRMWARE_AND_DRIVERS`)
10. Virtualization and Hypervisors (`VIRTUALIZATION_AND_HYPERVISORS`)
11. Containers and System Runtime (`CONTAINERS_AND_SYSTEM_RUNTIME`)
12. System Security and Hardening (`SYSTEM_SECURITY_AND_HARDENING`)
13. Networking and System Services (`NETWORKING_AND_SYSTEM_SERVICES`)
14. Filesystems and Storage (`FILESYSTEMS_AND_STORAGE`)
15. Updates and Lifecycle (`UPDATES_AND_LIFECYCLE`)
16. Observability and Diagnostics (`OBSERVABILITY_AND_DIAGNOSTICS`)
17. Backup and Recovery (`BACKUP_AND_RECOVERY`)
18. Licensing and Interoperability (`LICENSING_AND_INTEROPERABILITY`)

## Provider and product coverage

The inventory groups OS and system platform families across Apple, Microsoft, Google, major Linux distribution vendors/projects, BSD, UNIX derivatives, RTOS projects and virtualization vendors. Product entries are curated families, not every release, SKU, architecture, derivative distribution or device image.

## Layer boundaries

System Core owns identity, taxonomy, lifecycle metadata, compatibility classification, readiness and orchestration metadata. It does not own:

- OS installation, package execution, shell/PowerShell commands or host mutation.
- Firmware flashing, bootloader changes, kernel replacement or driver installation.
- Provider control-plane API transport, OAuth, credential storage or live host agents.
- Persistent system telemetry, backup payloads or software distribution.

Those functions belong to authorized execution, API, security, server, storage and software layers. A catalog record is not proof of support entitlement, installation, authorization or live connectivity.

## Safety and security

1. Tenant/actor identity must come from the authenticated application layer.
2. Secret values are never stored in this Core package; use opaque secret references in the dedicated secret manager.
3. Installation, formatting, encryption, firmware, kernel, boot, patch, reboot and shutdown actions require explicit authorization in their execution layer.
4. Inventory operations are read-only and perform zero host operations.
5. Product lifecycle and support dates must be verified against the publisher before operational decisions.
