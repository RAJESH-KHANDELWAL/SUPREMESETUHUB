# GLOBAL DOMAIN Storage Ecosystem — Architecture

## Ownership
Storage owns domain taxonomy, internal identity, metadata contracts, lifecycle definitions, jurisdiction metadata, catalog discovery, and storage health metadata.

## Functional domains
1. Identity and portfolio
2. Registration and acquisition
3. DNS and nameservers
4. Hosting and infrastructure associations
5. Security and certificate metadata
6. Lifecycle, renewal, and transfer
7. Compliance and governance
8. Analytics and health

## Layer boundaries
- Storage: metadata and object lifecycle definitions only.
- API/integration: registrar, DNS, hosting, certificate, and external provider clients.
- Infrastructure: secrets, network, queues, databases, observability, deployment.
- Application: user-facing workflows and authorization.

Local package initialization is not external connectivity. No registrar, DNS, hosting, or certificate provider is connected by this foundation. Production persistence belongs in the approved central database.
