# Scaleway VPS Core Ecosystem

Provider-specific metadata package under Global VPS Core.

- Provider ID: `scaleway`
- Canonical registry: `../catalog.py`
- API layer: `backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem`
- Status: metadata/catalogue only
- Live API calls, provisioning, SSH execution, billing mutations and credentials are not implemented in this Core package.

Provider operations require a separately verified API adapter, tenant authorization, audit logging and external secret storage.
