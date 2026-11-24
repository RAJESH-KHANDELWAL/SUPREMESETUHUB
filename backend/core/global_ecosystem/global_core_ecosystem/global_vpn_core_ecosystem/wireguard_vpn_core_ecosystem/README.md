# WireGuard VPN Core Ecosystem

Provider-specific capability metadata for WireGuard; no tunnel or network operation is executed here.

- Provider ID: `wireguard`
- Existing VPN service module: `backend/vpn/global_ecosystem/global_vpn_ecosystem/wireguard_vpn/service.py`
- Parent: `GLOBAL-VPN-CORE-ECOSYSTEM`
- Layer: CORE
- Live connection: not configured / not verified
- Secrets and private keys: external secret manager or OS credential vault only

The package exposes provider metadata and delegates request validation to the shared Core contract. Client installation, provider API transport and tunnel lifecycle remain outside this package.
