<?php
/** Frontend-side status bridge for Frontend and Backend Foundation directories. */
function frontend_foundation_connection_status(): array {
    $repo = dirname(__DIR__, 2);
    $paths = [
        'frontend_foundation' => __DIR__ . '/frontend_foundation',
        'backend_foundation_contract' => __DIR__ . '/backend_foundation',
        'backend_foundation_runtime' => $repo . '/backend/foundation/backend_foundation',
        'backend_frontend_contract' => $repo . '/backend/foundation/frontend_foundation',
    ];
    $checks = [];
    foreach ($paths as $name => $path) { $checks[$name] = is_dir($path); }
    $connected = !in_array(false, $checks, true);
    return ['name' => 'FRONTEND-BACKEND FOUNDATION CONNECTION', 'status' => $connected ? 'CONNECTED' : 'INCOMPLETE', 'checks' => $checks, 'connected' => $connected];
}
