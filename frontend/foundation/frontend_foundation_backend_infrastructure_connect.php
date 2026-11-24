<?php
/** Frontend Foundation -> Backend Infrastructure structural connector. */
function frontend_foundation_backend_infrastructure(): array
{
    $repositoryRoot = dirname(__DIR__, 2);
    $frontendFoundation = $repositoryRoot . '/frontend/foundation';
    $backendInfrastructure = $repositoryRoot . '/backend/infrastructure';
    $checks = [
        'frontend_foundation_root' => is_dir($frontendFoundation),
        'frontend_foundation_manager_py' => is_file($frontendFoundation . '/manager.py'),
        'frontend_foundation_manager_php' => is_file($frontendFoundation . '/manager.php'),
        'backend_infrastructure_root' => is_dir($backendInfrastructure),
        'backend_infrastructure_manager_py' => is_file($backendInfrastructure . '/manager.py'),
        'backend_infrastructure_manager_php' => is_file($backendInfrastructure . '/manager.php'),
        'backend_infrastructure_global_ecosystem' => is_dir($backendInfrastructure . '/global_ecosystem'),
    ];
    $connected = !in_array(false, $checks, true);
    return [
        'name' => 'FRONTEND FOUNDATION -> BACKEND INFRASTRUCTURE',
        'status' => $connected ? 'CONNECTED' : 'INCOMPLETE',
        'checks' => $checks,
        'connected' => $connected,
        'connection_type' => 'repository structure validation; no runtime bridge or provider operation',
    ];
}
