# DIGITALOCEAN SERVER CORE ECOSYSTEM

Provider capability contract package.

Scope: Droplet and server lifecycle, monitoring and administration.

API catalog dependency: `backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_server_api_ecosystem`.

CORE owns request contracts, tenant/security policy and orchestration metadata. API transport belongs to the DigitalOcean API ecosystem; runtime execution belongs in ENGINE. No live provider calls are enabled.
