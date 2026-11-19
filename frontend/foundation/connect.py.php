<?php
/**
 * Frontend Foundation connector.
 * Exact requested filename: connect.py.php
 * Provides a PHP entry point for checking both Frontend and Backend
 * Foundation packages without importing either runtime into the other.
 */
function frontend_foundation_connect(): array {
    $repositoryRoot = dirname(__DIR__, 2);
    $paths = [
        'frontend_foundation' => __DIR__ . '/frontend_foundation',
        'backend_foundation_contract' => __DIR__ . '/backend_foundation',
        'backend_foundation_runtime' => $repositoryRoot . '/backend/foundation/backend_foundation',
        'backend_frontend_contract' => $repositoryRoot . '/backend/foundation/frontend_foundation',
    ];
    $checks = [];
    foreach ($paths as $name => $path) {
        $checks[$name] = is_dir($path);
    }
    $connected = !in_array(false, $checks, true);
    return [
        'name' => 'FRONTEND-BACKEND FOUNDATION CONNECTION',
        'status' => $connected ? 'CONNECTED' : 'INCOMPLETE',
        'checks' => $checks,
        'connected' => $connected,
    ];
}
