<?php
/** PHP tests for the Backend Foundation root. */
require_once dirname(__DIR__) . '/foundation/manager.php';
require_once dirname(__DIR__) . '/foundation/backend_foundation_frontend_infrastructure_connect.php';

function assert_backend_foundation(bool $condition, string $message): void {
    if (!$condition) {
        throw new RuntimeException($message);
    }
}

$manager = new BackendFoundationManager();
$report = $manager->health();
assert_backend_foundation($report['healthy'] === true, 'Backend Foundation health check failed');
assert_backend_foundation($report['name'] === 'BACKEND FOUNDATION', 'Unexpected Backend Foundation name');
assert_backend_foundation(backend_foundation_frontend_infrastructure()['connected'] === true, 'Backend Foundation connector check failed');

echo "Backend Foundation PHP tests passed.\n";
