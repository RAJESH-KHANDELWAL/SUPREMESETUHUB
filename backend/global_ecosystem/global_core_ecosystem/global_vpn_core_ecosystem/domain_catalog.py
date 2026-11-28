"""Canonical VPN capability-domain taxonomy."""
from typing import Any
DOMAIN_DEFINITIONS:dict[str,dict[str,str]]={
 "PROVIDER_GOVERNANCE":{"name":"Provider Governance","purpose":"Provider identity, registry lifecycle, capability declarations and service status."},
 "VPN_PROTOCOLS_AND_STANDARDS":{"name":"VPN Protocols and Standards","purpose":"VPN protocol families, version metadata and interoperability declarations."},
 "TUNNEL_LIFECYCLE":{"name":"Tunnel Lifecycle","purpose":"Tunnel configuration metadata, desired state and lifecycle status; no tunnel changes are executed."},
 "DEVICE_AND_CLIENT_COVERAGE":{"name":"Device and Client Coverage","purpose":"Desktop, mobile, server and router client platform metadata."},
 "MESH_NETWORKING_AND_OVERLAY":{"name":"Mesh Networking and Overlay","purpose":"Peer identity, mesh topology, relay and overlay-network metadata."},
 "ROUTING_AND_TRAFFIC_POLICY":{"name":"Routing and Traffic Policy","purpose":"Route intent, gateway selection, full-tunnel and split-tunnel policy metadata."},
 "DNS_AND_LEAK_PROTECTION":{"name":"DNS and Leak Protection","purpose":"DNS resolver policy, leak-protection capabilities and resolution metadata."},
 "ENCRYPTION_AND_CRYPTOGRAPHY":{"name":"Encryption and Cryptography","purpose":"Cipher suites, cryptographic primitives and protocol security metadata."},
 "KEY_AND_CREDENTIAL_GOVERNANCE":{"name":"Key and Credential Governance","purpose":"Key lifecycle, credential references, rotation policy and external secret-store boundaries."},
 "IDENTITY_AUTHENTICATION_AND_MFA":{"name":"Identity, Authentication and MFA","purpose":"User/device identity, authentication methods and multi-factor policy metadata."},
 "ACCESS_CONTROL_AND_DEVICE_TRUST":{"name":"Access Control and Device Trust","purpose":"Device posture, peer authorization, access rules and trust boundaries."},
 "KILL_SWITCH_AND_FAIL_CLOSED":{"name":"Kill Switch and Fail-Closed Policy","purpose":"Traffic-blocking and fail-closed capability declarations; no local firewall rules are changed."},
 "PRIVACY_TELEMETRY_AND_LOGGING":{"name":"Privacy, Telemetry and Logging","purpose":"Data collection, diagnostics, telemetry minimization, retention and logging declarations."},
 "THREAT_PROTECTION_AND_NETWORK_SECURITY":{"name":"Threat Protection and Network Security","purpose":"Malware/phishing protection, hostile-network safeguards and threat-control metadata."},
 "CONNECTIVITY_DIAGNOSTICS_AND_HEALTH":{"name":"Connectivity Diagnostics and Health","purpose":"Connection health, latency, reachability and diagnostic capability metadata."},
 "EXIT_NODES_RELAYS_AND_GATEWAYS":{"name":"Exit Nodes, Relays and Gateways","purpose":"Exit-node, relay, gateway and egress-location capability metadata."},
 "GEOLOCATION_AND_JURISDICTION":{"name":"Geolocation and Jurisdiction","purpose":"Server-location, jurisdiction, data-residency and legal-scope metadata."},
 "COMPLIANCE_AND_AUDIT":{"name":"Compliance and Audit","purpose":"Privacy commitments, compliance references, auditability and evidence status."},
}
def list_domain_inventory()->list[dict[str,str]]:return [{"domain_id":k,**v} for k,v in DOMAIN_DEFINITIONS.items()]
def domain_summary()->dict[str,Any]:return {"success":True,"ecosystem_id":"GLOBAL-VPN-CORE-ECOSYSTEM","domain_count":len(DOMAIN_DEFINITIONS),"domains":list_domain_inventory()}
