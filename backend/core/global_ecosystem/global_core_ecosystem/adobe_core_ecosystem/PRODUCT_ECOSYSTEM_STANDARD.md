# Adobe Product Core Ecosystem Standard

The existing Adobe runtime catalog declares 32 product and service domains, mapped to dedicated Core family packages.

Each package contains ten standard directories:
- `authentication`
- `capabilities`
- `docs`
- `events`
- `lifecycle`
- `models`
- `schemas`
- `security`
- `services`
- `tests`

Each package also contains README.md, __init__.py, ecosystem_config.py, ecosystem_manifest.json and service.py.

Core owns identity, capability metadata, policy, lifecycle and readiness. API transport/OAuth, storage, database, runtime and UI remain in their respective layers. Catalog entries and generated scaffolds do not imply API entitlement or live integration.
