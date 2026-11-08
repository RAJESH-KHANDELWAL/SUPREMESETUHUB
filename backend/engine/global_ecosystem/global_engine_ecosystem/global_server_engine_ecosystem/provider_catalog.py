"""Explicit provider catalog for GLOBAL SERVER ENGINE adapters."""
PROVIDERS = (
    {"provider_id":"aws","package":"aws_server_engine_ecosystem","adapter":"ProviderEngine"},
    {"provider_id":"google","package":"google_server_engine_ecosystem","adapter":"ProviderEngine"},
    {"provider_id":"microsoft","package":"microsoft_server_engine_ecosystem","adapter":"ProviderEngine"},
    {"provider_id":"cloudflare","package":"cloudflare_server_engine_ecosystem","adapter":"ProviderEngine"},
    {"provider_id":"digitalocean","package":"digitalocean_server_engine_ecosystem","adapter":"ProviderEngine"},
    {"provider_id":"abelohost","package":"abelohost_server_engine_ecosystem","adapter":"ProviderEngine"},
    {"provider_id":"vicetemple","package":"vicetemple_server_engine_ecosystem","adapter":"ProviderEngine"},
)
def list_providers():
    return [dict(item) for item in PROVIDERS]
def get_provider(provider_id):
    key = str(provider_id).strip().lower()
    for item in PROVIDERS:
        if item["provider_id"] == key:
            return dict(item)
    raise KeyError(f"Unknown SERVER ENGINE provider: {provider_id!r}")
