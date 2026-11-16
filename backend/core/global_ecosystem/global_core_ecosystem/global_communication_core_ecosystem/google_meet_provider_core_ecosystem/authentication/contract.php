<?php
/** Provider-neutral tenant context contract. No secrets or transport logic. */
return [
    'layer' => 'CORE',
    'provider_id' => getenv('COMMUNICATION_PROVIDER_ID') ?: null,
    'tenant_id_required' => true,
    'region_required' => true,
    'live_connection_verified' => false,
];
