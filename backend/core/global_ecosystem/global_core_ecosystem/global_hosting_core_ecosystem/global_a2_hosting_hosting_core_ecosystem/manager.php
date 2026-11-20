<?php
/** Read-only provider metadata facade; no network calls or secrets. */
function hosting_provider_status(): array {
    $provider = strtoupper(basename(__DIR__));
    $provider = preg_replace('/_hosting_core_ecosystem$/', '', $provider);
    return ['provider_id' => $provider, 'status' => 'CORE_CATALOG_ONLY', 'live_connection_verified' => false, 'api_transport_in_core' => false, 'persistence_enabled' => false];
}
