# GLOBAL SERVER ENGINE

Independent ENGINE implementation for GLOBAL SERVER operations.

- Provider-specific execution boundaries for AWS, Google, Microsoft, Cloudflare, DigitalOcean, Abelohost and ViceTemple.
- Engine descriptor catalog, provider catalog, runtime registry, manager and lifecycle tests.
- Provider handlers are injected explicitly; credentials are not stored in source.
- No provider account is considered connected until a real authorized handler is configured.
- No remote provisioning or reachability check runs by default.
- ENGINE owns execution adapters; SERVER owns inventory; DATABASE owns persistence; STORAGE owns file/object storage.