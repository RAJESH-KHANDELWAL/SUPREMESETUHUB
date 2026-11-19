<?php
/** Frontend Infrastructure -> Backend Foundation structural connector. */
function frontend_infrastructure_backend_foundation(): array
{
    $repositoryRoot = dirname(__DIR__, 2);
    $frontendInfrastructure = $repositoryRoot . '/frontend/infrastructure';
    $backendFoundation = $repositoryRoot . '/backend/foundation';

    $check = static function (string $root): array {
        return [
            'root' => is_dir($root),
            'manager_py' => is_file($root . '/manager.py'),
            'manager_php' => is_file($root . '/manager.php'),
            'init_py' => is_file($root . '/__init__.py'),
        ];
    };

    $frontend = $check($frontendInfrastructure);
    $backend = $check($backendFoundation);
    $connected = !in_array(false, $frontend, true) && !in_array(false, $backend, true);

    return [
        'name' => 'FRONTEND INFRASTRUCTURE -> BACKEND FOUNDATION',
        'frontend_infrastructure' => ['checks' => $frontend, 'healthy' => !in_array(false, $frontend, true)],
        'backend_foundation' => ['checks' => $backend, 'healthy' => !in_array(false, $backend, true)],
        'connected' => $connected,
        'connection_type' => 'repository structure validation; no runtime bridge',
    ];
}
