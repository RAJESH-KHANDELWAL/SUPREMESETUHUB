# Adobe Product Core Ecosystem Standard

The existing Adobe runtime catalog declares 32 product and service domains. The Adobe Core catalog mirrors these domains as provider-neutral inventory entries.

## Product-family package standard

When a product-family package is implemented, it should contain these ten directories:
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

A completed package should also contain `README.md`, `__init__.py`, `ecosystem_config.py`, `ecosystem_manifest.json` and `service.py`.

## Current implementation scope

The current scaffold includes the shared provider Core foundation and one product-family package: Adobe Creative Cloud. The remaining 31 domains are catalog entries, not completed package implementations. Do not infer package completeness from catalog presence.

Core owns identity, capability metadata, policy, lifecycle and readiness. API transport/OAuth, storage, database, runtime and UI remain in their respective layers. Catalog entries and generated scaffolds do not imply API entitlement or live integration.
