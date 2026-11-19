<?php
/**
 * Backend-side PHP connector for the Backend and Frontend Foundation roots.
 * Checks the root manager entry points; it does not bridge Python and PHP runtimes.
 */
function backend_foundation_frontend_foundation_connect(): array
{
    $repositoryRoot = dirname(__DIR__, 2);
    $backendRoot = $repositoryRoot . '/backend/foundation';
    $frontendRoot = $repositoryRoot . '/frontend/foundation';
    $paths = [
        'backend_foundation_root' => $backendRoot,
        'backend_manager_py' => $backendRoot . '/manager.py',
        'backend_manager_php' => $backendRoot . '/manager.php',
        'frontend_foundation_root' => $frontendRoot,
        'frontend_manager_py' => $frontendRoot . '/manager.py',
        'frontend_manager_php' => $frontendRoot . '/manager.php',
    ];

    $checks = [];
    foreach ($paths as $name => $path) {
        $checks[$name] = $name === 'backend_foundation_root' || $name === 'frontend_foundation_root'
            ? is_dir($path)
            : is_file($path);
    }

    $connected = !in_array(false, $checks, true);
    return [
        'name' => 'BACKEND FOUNDATION <-> FRONTEND FOUNDATION',
        'status' => $connected ? 'CONNECTED' : 'INCOMPLETE',
        'checks' => $checks,
        'connected' => $connected,
    ];
}
