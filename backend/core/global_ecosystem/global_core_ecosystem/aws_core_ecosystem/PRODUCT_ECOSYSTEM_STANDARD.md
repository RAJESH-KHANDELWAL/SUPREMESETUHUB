# AWS Product Core Ecosystem Standard

- Provider package: `aws_core_ecosystem`.
- Service-family package: `aws_<family>_core_ecosystem`.
- Domain package: `aws_<domain>_core_ecosystem`.
- Shared package: `aws_shared_<capability>_core_ecosystem`.

All provider-owned directories follow the AWS prefix and Core Ecosystem suffix. `php` and `tests` are intentional support directories.

Each family retains its AWS-specific service facade, manifest, configuration, contracts, capabilities, lifecycle, security, documentation and tests. The family manager delegates to that service. Domain managers expose read-only status, offering inventory and lookup through the provider's canonical inventory.

Core is metadata-only. AWS SDK clients, SigV4, credential resolution, transport, persistence, queues and infrastructure mutations remain outside this layer.
