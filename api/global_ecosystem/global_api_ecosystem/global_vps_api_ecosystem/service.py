"""Service metadata for the global VPS API ecosystem."""

from __future__ import annotations

VPS_PROVIDER_IDS: tuple[str, ...] = ("aws", "google", "microsoft", "oracle", "digitalocean", "alibaba_cloud", "tencent_cloud", "huawei_cloud", "rackspace", "scaleway", "ovhcloud", "hetzner_cloud", "vultr", "ibm", "cloudflare", "nvidia", "jd_cloud", "kingsoft_cloud", "baidu_cloud", "china_telecom_cloud",)

def get_vps_ecosystem_status() -> dict[str, object]:
    """Return honest catalog status; no external provider is contacted."""
    return {
        "ecosystem_id": "VPS",
        "provider_ids": list(VPS_PROVIDER_IDS),
        "provider_count": len(VPS_PROVIDER_IDS),
        "live_connections_verified": False,
    }
