# GLOBAL HOSTING ECOSYSTEM

Canonical provider namespace for hosting integrations in the Backend Global Ecosystem.

- `hostinger_api.py`: read-only Hostinger inventory adapter for websites and VPS instances.
- Credentials are loaded only from deployment environment variables (`HOSTINGER_API_TOKEN`, with `HOSTINGER_API_KEY` as a compatibility alias).
- The adapter does not purchase plans, register or transfer domains, change DNS, deploy files, or mutate VPS state.
- Live connectivity is not implied by the presence of this module; it requires configured credentials and a verified provider response.
