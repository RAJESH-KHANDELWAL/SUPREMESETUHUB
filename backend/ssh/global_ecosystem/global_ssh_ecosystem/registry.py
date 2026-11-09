"""SSH provider metadata; no remote sessions or commands are executed."""
PROVIDERS = [
 {"provider_id":"openssh","name":"OpenSSH","capabilities":["secure-shell-session-management"],"status":"not_configured"},
 {"provider_id":"aws-ssm","name":"AWS Systems Manager","capabilities":["managed-remote-access"],"status":"not_configured"},
 {"provider_id":"tailscale-ssh","name":"Tailscale SSH","capabilities":["identity-aware-ssh"],"status":"not_configured"},
 {"provider_id":"github-actions-ssh","name":"GitHub Actions SSH Deployment","capabilities":["authorized-ci-deployment"],"status":"not_configured"},
]
def list_providers(): return [dict(p, capabilities=list(p["capabilities"])) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p, capabilities=list(p["capabilities"]))
 raise KeyError(f"Unknown SSH provider: {provider_id!r}")
