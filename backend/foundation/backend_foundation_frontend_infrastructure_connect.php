<?php
/** Backend Foundation -> Frontend Infrastructure structural connector. */
function backend_foundation_frontend_infrastructure(): array
{
    $repositoryRoot = dirname(__DIR__, 2);
    $backendFoundation = $repositoryRoot . '/backend/foundation';
    $frontendInfrastructure = $repositoryRoot . '/frontend/infrastructure';
    $checks = [
        'backend_foundation_root' => is_dir($backendFoundation),
        'backend_foundation_manager_py' => is_file($backendFoundation . '/manager.py'),
        'backend_foundation_manager_php' => is_file($backendFoundation . '/manager.php'),
        'frontend_infrastructure_root' => is_dir($frontendInfrastructure),
        'frontend_infrastructure_manager_py' => is_file($frontendInfrastructure . '/manager.py'),
        'frontend_infrastructure_manager_php' => is_file($frontendInfrastructure . '/manager.php'),
        'frontend_infrastructure_global_ecosystem' => is_dir($frontendInfrastructure . '/global_ecosystem'),
    ];
    $connected = !in_array(false, $checks, true);
    return [
        'name' => 'BACKEND FOUNDATION -> FRONTEND INFRASTRUCTURE',
        'status' => $connected ? 'CONNECTED' : 'INCOMPLETE',
        'checks' => $checks,
        'connected' => $connected,
        'connection_type' => 'repository structure validation; no runtime bridge or provider operation',
    ];
}
