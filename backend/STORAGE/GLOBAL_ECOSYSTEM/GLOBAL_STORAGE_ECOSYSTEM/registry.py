"""Metadata-only provider registry; no network calls are made."""
PROVIDERS = [
 {"provider_id":"google","name":"Google Cloud Storage","status":"not_configured"},
 {"provider_id":"aws","name":"Amazon S3","status":"not_configured"},
 {"provider_id":"microsoft","name":"Azure Blob Storage","status":"not_configured"},
 {"provider_id":"hostinger","name":"Hostinger Storage","status":"not_configured"},
 {"provider_id":"proton","name":"Proton Drive","status":"not_configured"},
 {"provider_id":"mega","name":"MEGA","status":"not_configured"},
]
def list_providers(): return [dict(p) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p)
 raise KeyError(f"Unknown STORAGE provider: {provider_id!r}")
