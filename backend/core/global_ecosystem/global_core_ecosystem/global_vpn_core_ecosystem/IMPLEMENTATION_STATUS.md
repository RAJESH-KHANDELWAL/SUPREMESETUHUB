# Global VPN Core implementation status

- Four provider packages correspond exactly to the four entries in the existing VPN registry: WireGuard, OpenVPN, Tailscale and Proton VPN.
- Eighteen capability domains are centrally defined; no empty domain folders are created.
- Catalogue, contracts, policy, orchestrator, shared domain runtime, manager, service and PHP metadata facade are present.
- Master taxonomy mapping references six verified existing entries; adds zero entries and leaves the 2,468 target unchanged.
- Existing provider service modules are referenced as source metadata only. This Core package does not claim API adapters, installed clients or active VPN connectivity.
- Private keys, pre-shared keys, tokens and credentials are rejected from Core payloads and must remain in external secret storage/OS credential vaults.
- Tunnel setup/teardown, routing, DNS changes, kill-switch enforcement, billing and persistent device state are not implemented or enabled here.
