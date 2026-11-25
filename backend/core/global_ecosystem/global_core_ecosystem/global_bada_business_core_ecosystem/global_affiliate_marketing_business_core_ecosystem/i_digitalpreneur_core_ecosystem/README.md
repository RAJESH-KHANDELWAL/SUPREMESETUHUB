# iDigitalPreneur CORE ECOSYSTEM

**Canonical platform ID:** `I-DIGITALPRENEUR`  
**Parent:** GLOBAL AFFILIATE MARKETING BUSINESS CORE ECOSYSTEM  
**Layer:** CORE

This standalone CORE package owns iDigitalPreneur-specific identity boundaries and its adapter into the shared affiliate business contracts. It is located beside `platforms/`, not inside it.

## Scope
- Preserve the platform identity independently from LeadsGuru and Millionaire Track.
- Validate platform-specific routing at the CORE boundary.
- Reuse parent affiliate policies for disclosures, terms URLs, program activation and event invariants.
- Delegate persistence through the injected repository contract.
- Keep program terms, commission rules, eligibility, geography, fees and payouts unverified until supported by current official evidence.

## Not implemented here
No provider API calls, authentication, account linking, tracking redirects, attribution transport, payout execution, settlement or credential storage. Those belong to API, ENGINE, DATABASE, STORAGE and application layers.

No commission percentage, referral reward, joining fee, eligibility condition or program status is assumed.

## Package files
- `__init__.py`: public exports and identity constants.
- `manager.py`: identity/status manager.
- `models.py`: immutable identity model.
- `module_service.py`: read-only discovery facade.
- `policies.py`: platform identity and activation validation.
- `service.py`: repository-injected affiliate workflows.
