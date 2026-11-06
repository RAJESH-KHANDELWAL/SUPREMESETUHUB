# Global Adobe API Ecosystem

Canonical Adobe provider catalog for SUPREMESETUHUB.

## API families
- PDF Services API: document operations and supported PDF workflows.
- Acrobat Sign API: e-signature agreements and signing workflows.
- Firefly Services API: supported generative and creative services.
- Creative Cloud and Assets APIs: asset access and product-specific workflows.
- Experience Platform APIs: only products enabled for the Adobe organization.
- Adobe Commerce APIs: commerce integrations where licensed and enabled.
- Video and Frame.io APIs: media collaboration workflows where available.
- OAuth and Developer Console: application registration, scopes and token lifecycle.

## Important product boundaries
Photoshop, Illustrator, Premiere Pro and other desktop applications are not automatically exposed as general-purpose APIs. Integrate only documented Adobe developer APIs and product services for which the account has entitlement. Each API family may require different OAuth scopes, organization permissions, product profiles and credentials.

## Backend integration
The shared adapter is backend/integrations/providers/adobe.py and is registered as ADOBE in backend/integrations/registry.py. It reports OAuth configuration readiness only; it does not prove that an Adobe API call succeeded.

## Setup
1. Create/configure an integration in Adobe Developer Console: https://developer.adobe.com/console/
2. Select the required product API and OAuth scopes for the target Adobe organization.
3. Store client credentials server-side as ADOBE_CLIENT_ID and ADOBE_CLIENT_SECRET in the deployment secret manager.
4. Configure ADOBE_ORGANIZATION_ID and ADOBE_ACCOUNT_ID only when required by the selected API.
5. Never commit credentials or expose them to browser code.
6. Implement and test each API family separately, including token acquisition, scopes, permissions, rate limits and error handling.

## Status semantics
- NEEDS_CONFIGURATION: required OAuth configuration is absent.
- CONFIGURED_NOT_VERIFIED: configuration exists, but no live Adobe API operation has been tested.
- CONNECTED: must only be reported after a successful authenticated operation against the selected Adobe API.

Child folders are catalog/documentation scaffolds, not completed service adapters.
