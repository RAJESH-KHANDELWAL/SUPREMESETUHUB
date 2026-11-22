# NSFWinfra Product Core Standard

A product folder is an inventory boundary, not an excuse to generate boilerplate subfolders.

Implement a product-specific Core file or package only when its unique contract is required and testable. Shared catalog, tenant contracts, policy, domain inventory, readiness, orchestrator and manager stay at provider Core root. API transport and provider SDK clients stay in NSFWinfra API. Execution engines/runtime, database, storage and application flows stay in their owning ecosystems. Never duplicate client implementations.

Product package directory names remain stable; product-specific capabilities must be registered in canonical catalog and covered by domain taxonomy and tests before implementation is considered complete. All status defaults remain catalog-only/not-live-verified.
