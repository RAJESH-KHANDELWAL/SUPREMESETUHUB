<?php
/** PHP tests for Backend Global Foundation Ecosystem. */
require_once dirname(__DIR__) . '/foundation/global_ecosystem/manager.php';
require_once dirname(__DIR__) . '/foundation/global_ecosystem/global_foundation_ecosystem/manager.php';

function assert_global_foundation_ecosystem(bool $condition, string $message): void {
    if (!$condition) {
        throw new RuntimeException($message);
    }
}

$globalManager = new BackendGlobalEcosystemManager();
$globalReport = $globalManager->health();
assert_global_foundation_ecosystem($globalReport['healthy'] === true, 'Backend Global Ecosystem health check failed');

$foundationManager = new BackendGlobalFoundationEcosystemManager();
$foundationReport = $foundationManager->health();
assert_global_foundation_ecosystem($foundationReport['healthy'] === true, 'Backend Global Foundation Ecosystem health check failed');
assert_global_foundation_ecosystem($foundationReport['name'] === 'BACKEND GLOBAL FOUNDATION ECOSYSTEM', 'Unexpected Global Foundation Ecosystem name');

echo "Backend Global Foundation Ecosystem PHP tests passed.\n";
