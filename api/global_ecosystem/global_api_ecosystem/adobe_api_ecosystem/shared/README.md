# Shared Adobe API transport

This package provides a conservative HTTPS JSON transport, token-provider boundary, normalized errors, retry policy and pagination helper.

- It does not implement an Adobe OAuth grant or token refresh.
- It does not invent product endpoint paths or base URLs.
- Product adapters must supply official HTTPS base URLs and documented relative paths.
- Retries are limited to idempotent methods; POST is never automatically retried.
- Tokens and response bodies are never included in raised error messages.
- Configure secrets in a managed secret store, not in source control.

A configured client is not a verified connection. Run an authenticated product-specific smoke test before marking any integration connected.
