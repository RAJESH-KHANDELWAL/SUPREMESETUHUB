# DIGITALOCEAN CORE ECOSYSTEM

Canonical DigitalOcean provider CORE control plane with five domain packages: Cloud, Hosting, Server, Storage and VPS.

CORE owns provider capability registration, request contracts, caller/tenant security boundaries, policy and orchestration metadata. Existing DigitalOcean API ecosystem is the canonical transport/catalog dependency; ENGINE owns SDK execution, retries, timeouts and scheduling. DATABASE and STORAGE retain persistence and artifact ownership.

Live provider calls remain disabled until secure runtime adapters, tenant authorization, official API capability verification and integration smoke tests are complete.
