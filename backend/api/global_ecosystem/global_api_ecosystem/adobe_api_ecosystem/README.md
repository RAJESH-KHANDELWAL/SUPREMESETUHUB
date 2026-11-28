# Adobe API Ecosystem

Canonical Adobe API provider catalog for SUPREMESETUHUB.

## API families (8)

| Family | Responsibility |
|---|---|
| PDF Services | Document conversion and PDF operations |
| Acrobat Sign | Agreements, participants and signing workflows |
| Firefly Services | Supported generative services |
| Creative Cloud and Assets | Documented asset and Creative Cloud APIs |
| Experience Platform | Product- and organization-scoped Experience Platform APIs |
| Commerce | Adobe Commerce APIs for deployed/authorized instances |
| Video and Frame.io | Media collaboration and Frame.io APIs |
| OAuth and Identity | OAuth configuration boundary and Developer Console metadata |

Each family has a Python adapter boundary, machine-readable API contract and offline contract test. A blank endpoint catalog is intentional until exact endpoints, API versions, OAuth scopes and entitlements are verified against applicable official Adobe documentation.

## Shared transport

`shared/` contains HTTPS transport, a token-provider protocol, normalized errors, conservative idempotent retries and a pagination helper. It does not guess API hosts or implement a universal OAuth grant. Family clients must receive an official HTTPS base URL and a secure token provider.

## Security and setup

- Configure the required API product and OAuth scopes in Adobe Developer Console: https://developer.adobe.com/console/
- Store credentials and refresh/access tokens only in a managed secret store.
- Use least-privilege scopes and tenant/organization isolation.
- Never commit credentials, log tokens, or expose secrets to browser code.
- Validate ownership and authorization before each operation.
- Add product-specific webhook signature verification only from official specifications.
- Do not retry non-idempotent POST requests automatically.

## Status semantics

`ADAPTER_SCAFFOLD` means structure and offline contracts exist. It does not mean an API endpoint is implemented, the account has entitlement, OAuth works, or a live connection is verified. Mark connected only after a successful authenticated product-specific smoke test.

No shared live Adobe provider adapter was found at the previously referenced integration path during this repository review; this API layer does not claim one exists.
