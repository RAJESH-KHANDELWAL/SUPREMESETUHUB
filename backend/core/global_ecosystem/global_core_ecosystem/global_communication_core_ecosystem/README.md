# Global Communication Core Ecosystem

A provider-neutral global communication taxonomy and discovery catalog.

## Coverage
- 28 communication domains spanning telecom networks, email, OTT messaging, SMS/MMS/RCS, voice, video, UCaaS, CPaaS, CCaaS, customer engagement, push notifications, RTC SDKs, AI voice, verification, legacy channels, satellite/IoT, analytics, privacy, trust and safety, accessibility, and India-specific regulation.
- 95 provider reference records across telecom operators, cloud/workspace platforms, CPaaS, UCaaS, CCaaS, OTT messaging, email delivery, customer engagement, real-time SDKs and notifications.
- The 19 directories already present in this repository remain separately tracked; the provider directory is not restricted to those folders.

## Canonical implementation
- `manager.py`: Python manager and read-only master-catalog bridge.
- `manager.php`: PHP interoperability facade.
- `product_catalog.py`: provider reference inventory and filters.
- `domain_catalog.py`: domain taxonomy.
- `orchestrator.py`: read-only orchestration.
- `service.py`: status and health.
- `policy.py`: authorization, privacy and restricted-service boundaries.
- `test_global_communication_core.py`: validation tests.

## Master catalog
Reads `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` only. Does not duplicate or alter the 2468-entry master catalog.

## Accuracy and implementation status
Provider records are research/discovery references, not endorsements, live API connections, or proof of current product availability. Some products/brands change names, merge, retire or vary by country; verify official documentation, service availability, regulatory status and current product lifecycle before implementation. Duplicate brand aliases are kept only where they represent a distinct known product identity and must be reconciled during provider governance.

No provider OAuth, message sending, phone calling, or video delivery is enabled by this catalog. Credentials belong in an external secret store.
