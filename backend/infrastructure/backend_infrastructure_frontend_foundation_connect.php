<?php
/** Backend Infrastructure -> Frontend Foundation structural connector. */
function backend_infrastructure_frontend_foundation_connect(): array
{
    $repositoryRoot = dirname(__DIR__, 2);
    $backendInfrastructure = $repositoryRoot . '/backend/infrastructure';
    $frontendFoundation = $repositoryRoot . '/frontend/foundation';

    $check = static function (string $root): array {
        return [
            'root' => is_dir($root),
            'manager_py' => is_file($root . '/manager.py'),
            'manager_php' => is_file($root . '/manager.php'),
            'init_py' => is_file($root . '/__init__.py'),
        ];
    };

    $backend = $check($backendInfrastructure);
    $frontend = $check($frontendFoundation);
    $connected = !in_array(false, $backend, true) && !in_array(false, $frontend, true);

    return [
        'name' => 'BACKEND INFRASTRUCTURE -> FRONTEND FOUNDATION',
        'backend_infrastructure' => ['checks' => $backend, 'healthy' => !in_array(false, $backend, true)],
        'frontend_foundation' => ['checks' => $frontend, 'healthy' => !in_array(false, $frontend, true)],
        'connected' => $connected,
        'connection_type' => 'repository structure validation; no runtime bridge',
    ];
}
