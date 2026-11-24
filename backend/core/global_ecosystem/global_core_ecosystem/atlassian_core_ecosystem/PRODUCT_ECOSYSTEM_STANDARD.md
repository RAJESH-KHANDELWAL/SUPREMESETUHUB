# Atlassian Product Core Package Standard

Family package: `atlassian_<family>_core_ecosystem`. Domain package: `atlassian_<domain>_core_ecosystem`. Shared package: `atlassian_shared_<capability>_core_ecosystem`.

Each product family package contains only justified product-specific Core metadata, contracts, capability definitions, lifecycle/readiness, security boundaries, service facade, documentation and tests. Avoid empty boilerplate and duplicate provider managers. API transport, OAuth/token handling and SDK implementation belong to Atlassian API Ecosystem.
