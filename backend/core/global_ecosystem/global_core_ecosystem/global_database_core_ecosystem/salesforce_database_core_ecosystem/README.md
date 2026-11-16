# Provider Database Core Package

This directory is a provider-specific metadata and policy boundary for Global Database Core.

- Provider identity and lifecycle metadata are declared in `ecosystem_manifest.json`.
- Shared contract/configuration conventions are documented by the parent Global Database Core README.
- The ten responsibility folders separate authentication, capabilities, documentation, events, lifecycle, models, schemas, security, services and tests.
- This package is a scaffold only. It does not ship a database driver, credentials, connection pool, query executor or live adapter.
