# DIGITALOCEAN API ECOSYSTEM

Canonical provider-owned API ecosystem for DigitalOcean, aligned with the Google, AWS, Apple and Adobe provider-root naming convention.

## Provider scope
- Droplets and compute
- App Platform and application deployments
- Managed Databases
- Spaces Object Storage
- Networking, firewalls, load balancers and DNS
- Projects, teams and account administration

## Shared category mappings
- `backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_cloud_api_ecosystem/` — Droplets, compute, networking and managed cloud services
- `backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_hosting_api_ecosystem/` — App Platform, application deployment and hosting lifecycle
- `backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_server_api_ecosystem/` — Droplet and server lifecycle, monitoring and administration
- `backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_storage_api_ecosystem/` — Spaces object storage and storage-related capabilities
- `backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_vps_api_ecosystem/` — Virtual private server provisioning and management

## Integration status
This is a provider catalog and architecture scaffold only. It does not authenticate or make live API calls. No credentials belong in source control. Use environment variables or a managed secret store, verify official endpoints and required scopes, then implement and test live operations separately.

Live connection verified: **No**.
