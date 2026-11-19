<?php
/**
 * Frontend-side PHP connector for the Frontend and Backend Foundation roots.
 * Checks the root manager entry points; it does not bridge Python and PHP runtimes.
 */
function frontend_foundation_backend_foundation_connect(): array
{
    $repositoryRoot = dirname(__DIR__, 2);
    $frontendRoot = $repositoryRoot . '/frontend/foundation';
    $backendRoot = $repositoryRoot . '/backend/foundation';
    $paths = [
        'frontend_foundation_root' => $frontendRoot,
        'frontend_manager_py' => $frontendRoot . '/manager.py',
        'frontend_manager_php' => $frontendRoot . '/manager.php',
        'backend_foundation_root' => $backendRoot,
        'backend_manager_py' => $backendRoot . '/manager.py',
        'backend_manager_php' => $backendRoot . '/manager.php',
    ];

    $checks = [];
    foreach ($paths as $name => $path) {
        $checks[$name] = $name === 'frontend_foundation_root' || $name === 'backend_foundation_root'
            ? is_dir($path)
            : is_file($path);
    }

    $connected = !in_array(false, $checks, true);
    return [
        'name' => 'FRONTEND FOUNDATION <-> BACKEND FOUNDATION',
        'status' => $connected ? 'CONNECTED' : 'INCOMPLETE',
        'checks' => $checks,
        'connected' => $connected,
    ];
}
