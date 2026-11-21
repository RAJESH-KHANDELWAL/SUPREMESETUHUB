# GLOBAL VPN CORE ECOSYSTEM

**Layer:** CORE · **Parent:** GLOBAL CORE ECOSYSTEM

## Purpose

Canonical, read-only control-plane catalogue for VPN providers, protocols, device coverage, tunnel/mesh capabilities, privacy controls, routing policy, security boundaries and readiness. Core does not establish, disconnect, reconfigure or monitor live VPN tunnels.

## Existing provider inventory (4)

1. **WireGuard** — `wireguard_vpn_core_ecosystem/` (source: existing VPN service module)
2. **OpenVPN** — `openvpn_vpn_core_ecosystem/` (source: existing VPN service module)
3. **Tailscale** — `tailscale_vpn_core_ecosystem/` (source: existing VPN service module)
4. **Proton VPN** — `proton_vpn_core_ecosystem/` (source: existing VPN service module)

Provider inventory is aligned to the existing registry at `backend/vpn/global_ecosystem/global_vpn_ecosystem/registry.py`. No unverified vendors are added.

## Capability domains (18)

1. Provider Governance — `PROVIDER_GOVERNANCE`
2. VPN Protocols and Standards — `VPN_PROTOCOLS_AND_STANDARDS`
3. Tunnel Lifecycle — `TUNNEL_LIFECYCLE`
4. Device and Client Coverage — `DEVICE_AND_CLIENT_COVERAGE`
5. Mesh Networking and Overlay — `MESH_NETWORKING_AND_OVERLAY`
6. Routing and Traffic Policy — `ROUTING_AND_TRAFFIC_POLICY`
7. DNS and Leak Protection — `DNS_AND_LEAK_PROTECTION`
8. Encryption and Cryptography — `ENCRYPTION_AND_CRYPTOGRAPHY`
9. Key and Credential Governance — `KEY_AND_CREDENTIAL_GOVERNANCE`
10. Identity, Authentication and MFA — `IDENTITY_AUTHENTICATION_AND_MFA`
11. Access Control and Device Trust — `ACCESS_CONTROL_AND_DEVICE_TRUST`
12. Kill Switch and Fail-Closed Policy — `KILL_SWITCH_AND_FAIL_CLOSED`
13. Privacy, Telemetry and Logging — `PRIVACY_TELEMETRY_AND_LOGGING`
14. Threat Protection and Network Security — `THREAT_PROTECTION_AND_NETWORK_SECURITY`
15. Connectivity Diagnostics and Health — `CONNECTIVITY_DIAGNOSTICS_AND_HEALTH`
16. Exit Nodes, Relays and Gateways — `EXIT_NODES_RELAYS_AND_GATEWAYS`
17. Geolocation and Jurisdiction — `GEOLOCATION_AND_JURISDICTION`
18. Compliance and Audit — `COMPLIANCE_AND_AUDIT`

## Core files

- `catalog.py`: canonical provider and capability declarations.
- `domain_catalog.py`: 18 centrally maintained VPN domains.
- `contracts.py`: metadata request validation and secret-material rejection.
- `policy.py`: tenant authorization boundary and operation classification.
- `orchestrator.py`: read-only provider/domain discovery and health summary.
- `domain_runtime.py`: shared read-only domain manager.
- `manager.py` / `service.py`: stable Python entry points.
- `master_catalog.py`: read-only mapping to verified existing taxonomy entries.
- `manager.php`: PHP interoperability status facade.
- `test_vpn_core.py`: offline structural and behavior tests.

Each provider package contains only `README.md`, `__init__.py`, `provider.py` and `contracts.py`. Shared logic stays in the parent Core.

## Layer boundaries and security

CORE owns metadata, contracts and policy declarations. VPN client/tunnel execution belongs to the existing VPN runtime and controlled device agents; provider API transport belongs in API; persistent configuration and audit records belong in database/storage. Secrets and private keys must remain in an external secret manager or OS credential vault, never in source control or Core request payloads.

## Master taxonomy

Maps to existing entries `S09_internet`, `S09_cybersecurity`, `S09_global_networks`, `S10_global_network`, `S10_global_security` and `S07_privacy_and_data_protection`. This mapping adds zero taxonomy entries and does not change the 2,468 target.

**Status:** Core catalogue and contracts foundation only. No live VPN connection, tunnel, DNS, firewall or routing operation is enabled by this package.
