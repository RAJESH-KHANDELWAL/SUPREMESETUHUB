# Universal Integrations Catalog

Catalog APIs, SDKs, webhooks, OAuth connections, connectors, imports/exports, FTP/SFTP, databases, identity providers, payment rails and automation links.

Each integration must declare source and destination, owner, supported API/version, scopes/permissions, secret source, data flow, schema mapping, rate limits, retry/idempotency behavior, error handling, audit events, data residency, health probes, read/write test evidence, rollback and revocation process.

States: CATALOG_ONLY → NOT_CONFIGURED → CONFIGURED → CONNECTED → READ_VERIFIED / WRITE_VERIFIED. Never store credentials in Git or claim a live connection without evidence.
