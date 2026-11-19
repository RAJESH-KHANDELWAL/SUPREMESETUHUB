<?php
/** Backend-side status bridge for Backend and Frontend Foundation directories. */
function backend_foundation_connection_status(): array {
    $repo = dirname(__DIR__, 2);
    $paths = [
        'backend_foundation' => __DIR__ . '/backend_foundation',
        'frontend_foundation_contract' => __DIR__ . '/frontend_foundation',
        'frontend_foundation_runtime' => $repo . '/frontend/foundation/frontend_foundation',
        'frontend_backend_contract' => $repo . '/frontend/foundation/backend_foundation',
    ];
    $checks = [];
    foreach ($paths as $name => $path) { $checks[$name] = is_dir($path); }
    $connected = !in_array(false, $checks, true);
    return ['name' => 'BACKEND-FRONTEND FOUNDATION CONNECTION', 'status' => $connected ? 'CONNECTED' : 'INCOMPLETE', 'checks' => $checks, 'connected' => $connected];
}
