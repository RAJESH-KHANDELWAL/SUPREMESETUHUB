<?php
/**
 * Backend-side PHP connector for the Backend and Frontend Foundation packages.
 * Validates the shared repository contract without loading Python runtime code.
 */
function backend_foundation_frontend_foundation_connect(): array
{
    $repositoryRoot = dirname(__DIR__, 2);
    $paths = [
        'backend_foundation' => $repositoryRoot . '/backend/foundation/backend_foundation',
        'backend_frontend_contract' => $repositoryRoot . '/backend/foundation/frontend_foundation',
        'frontend_foundation' => $repositoryRoot . '/frontend/foundation/frontend_foundation',
        'frontend_backend_contract' => $repositoryRoot . '/frontend/foundation/backend_foundation',
    ];

    $checks = [];
    foreach ($paths as $name => $path) {
        $checks[$name] = is_dir($path);
    }

    $connected = !in_array(false, $checks, true);
    return [
        'name' => 'BACKEND FOUNDATION <-> FRONTEND FOUNDATION',
        'status' => $connected ? 'CONNECTED' : 'INCOMPLETE',
        'checks' => $checks,
        'connected' => $connected,
    ];
}
