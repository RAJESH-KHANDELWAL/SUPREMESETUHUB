"""Metadata-only provider registry; no network calls are made."""
PROVIDERS = [
 {"provider_id":"openssh","name":"OpenSSH","status":"not_configured"},
 {"provider_id":"aws-ssm","name":"AWS Systems Manager","status":"not_configured"},
 {"provider_id":"tailscale-ssh","name":"Tailscale SSH","status":"not_configured"},
 {"provider_id":"github-actions-ssh","name":"GitHub Actions SSH Deployment","status":"not_configured"},
]
def list_providers(): return [dict(p) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p)
 raise KeyError(f"Unknown SSH provider: {provider_id!r}")
