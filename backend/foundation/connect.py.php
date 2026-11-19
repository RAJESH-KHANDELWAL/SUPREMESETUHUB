<?php
/**
 * Backend Foundation connector.
 * Exact requested filename: connect.py.php
 * Provides a PHP entry point for checking both Backend and Frontend
 * Foundation packages without importing either runtime into the other.
 */
function backend_foundation_connect(): array {
    $repositoryRoot = dirname(__DIR__, 2);
    $paths = [
        'backend_foundation' => __DIR__ . '/backend_foundation',
        'frontend_foundation_contract' => __DIR__ . '/frontend_foundation',
        'frontend_foundation_runtime' => $repositoryRoot . '/frontend/foundation/frontend_foundation',
        'frontend_backend_contract' => $repositoryRoot . '/frontend/foundation/backend_foundation',
    ];
    $checks = [];
    foreach ($paths as $name => $path) {
        $checks[$name] = is_dir($path);
    }
    $connected = !in_array(false, $checks, true);
    return [
        'name' => 'BACKEND-FRONTEND FOUNDATION CONNECTION',
        'status' => $connected ? 'CONNECTED' : 'INCOMPLETE',
        'checks' => $checks,
        'connected' => $connected,
    ];
}
