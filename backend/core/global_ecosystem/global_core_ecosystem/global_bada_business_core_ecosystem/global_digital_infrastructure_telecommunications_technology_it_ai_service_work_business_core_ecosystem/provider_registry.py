"""Provider capability metadata; no live integrations are implied."""
PROVIDERS = (
 {"provider_id":"APPLE","folder":"apple_business_core_ecosystem","capability_areas":("devices and operating systems","developer ecosystem","cloud and account services","enterprise device management")},
 {"provider_id":"AWS","folder":"aws_business_core_ecosystem","capability_areas":("cloud infrastructure","storage and databases","networking and edge","AI and data services","managed operations")},
 {"provider_id":"GOOGLE","folder":"google_business_core_ecosystem","capability_areas":("cloud infrastructure","workspace and productivity","search and advertising platforms","Android and developer tools","AI and data services")},
 {"provider_id":"IBM","folder":"ibm_business_core_ecosystem","capability_areas":("enterprise software","hybrid cloud","AI and data","consulting and managed services","infrastructure")},
 {"provider_id":"MICROSOFT","folder":"microsoft_business_core_ecosystem","capability_areas":("cloud infrastructure","business productivity","operating systems and endpoints","developer tools","AI and data services")},
 {"provider_id":"ORACLE","folder":"oracle_business_core_ecosystem","capability_areas":("enterprise applications","databases","cloud infrastructure","integration and analytics","managed services")},
)
def list_providers() -> list[dict]:
    return [dict(x, capability_areas=list(x["capability_areas"])) for x in PROVIDERS]
def get_provider(provider_id: str) -> dict | None:
    for x in PROVIDERS:
        if x["provider_id"] == provider_id: return dict(x, capability_areas=list(x["capability_areas"]))
    return None
