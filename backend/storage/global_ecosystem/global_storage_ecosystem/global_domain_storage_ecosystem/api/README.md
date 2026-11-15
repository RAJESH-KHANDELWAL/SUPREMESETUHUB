# API Boundary

Registrar, DNS, hosting, and certificate provider clients belong in the API/integration layer, not storage. No network client, credential flow, or external operation is implemented here. Future adapters require authorization, least privilege, timeouts, retries, audit events, and explicit capability checks.
