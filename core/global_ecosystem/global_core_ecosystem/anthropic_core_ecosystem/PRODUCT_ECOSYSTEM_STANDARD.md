# Anthropic Product Core Ecosystem Standard

Each Anthropic product-family Core package contains ten standard subfolders: authentication, capabilities, docs, events, lifecycle, models, schemas, security, services and tests. Each package also has an ecosystem config, machine-readable manifest, README and Python service entry point.

Core owns provider/product identity, capability metadata, tenant context, policy classification, lifecycle and readiness. API owns Anthropic authentication, transport and endpoint operations. Storage, Database, Runtime/Engine and Application/UI retain their own responsibilities.

A catalog entry does not imply a public API, account entitlement, authorization or live integration. No live connections are claimed.
