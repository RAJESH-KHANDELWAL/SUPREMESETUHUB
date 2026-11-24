# Atlassian Product Ecosystem Standard

Every Atlassian product-family Core package follows the Google Core package boundary and naming convention while keeping Atlassian-specific capabilities.

Required package files: README.md, __init__.py, ecosystem_config.py, ecosystem_manifest.json and service.py.

Required subfolders: authentication, capabilities, docs, events, lifecycle, models, schemas, security, services and tests.

The Core layer is metadata-first and read-only. Authentication folders define contracts only; API token/OAuth handling and HTTP calls belong to the Atlassian API layer. Persistence, database operations, background execution and UI belong to their respective layers.

A family may be marked live only after independent deployment-level authorization and smoke tests. A registry entry alone is not proof of an integration.
