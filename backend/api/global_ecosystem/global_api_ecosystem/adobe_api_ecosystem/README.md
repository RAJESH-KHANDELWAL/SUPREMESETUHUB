# Adobe API Ecosystem

Canonical Adobe provider catalog for SUPREMESETUHUB.

## API families
- PDF Services API: supported PDF creation, conversion and document operations.
- Acrobat Sign API: e-signature agreements and signing workflows.
- Firefly Services API: supported generative and creative services.
- Creative Cloud and Assets APIs: supported asset and product integrations.
- Experience Platform APIs: only products enabled for the Adobe organization.
- Adobe Commerce APIs: commerce integrations where deployed and authorized.
- Video and Frame.io APIs: media collaboration where available.
- OAuth and Developer Console: application registration, scopes and token lifecycle.

## Product boundaries
Photoshop, Illustrator, Premiere Pro and other desktop applications are not automatically exposed as general-purpose APIs. Integrate only documented Adobe developer APIs for which the account has entitlement. Each API may require distinct OAuth scopes, product profiles and organization permissions.

## Backend integration
The shared adapter is backend/integrations/providers/adobe.py and is registered as ADOBE in backend/integrations/registry.py. It reports OAuth configuration readiness only; it does not prove that an Adobe API request succeeded.

## Setup
1. Configure an integration in Adobe Developer Console: https://developer.adobe.com/console/
2. Select the required product API and OAuth scopes.
3. Store credentials server-side as ADOBE_CLIENT_ID and ADOBE_CLIENT_SECRET in the deployment secret manager.
4. Add organization/account identifiers only when the selected API requires them.
5. Never commit credentials or expose them to browser code.
6. Implement and test each API family separately.

## Status
NEEDS_CONFIGURATION means required OAuth configuration is absent. CONFIGURED_NOT_VERIFIED means configuration exists but no live API operation has been tested. Only report CONNECTED after a successful authenticated API operation.

Child folders are catalog/documentation scaffolds, not completed live connectors.
