<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/core/global_ecosystem/global_core_ecosystem/manager.php';
require_once dirname(__DIR__, 2) . '/core/global_ecosystem/global_core_ecosystem/global_core_ecosystem.php';

function expectGlobalCore(bool $condition, string $message): void
{
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

$result = GlobalCoreEcosystem::status();
expectGlobalCore($result['success'] === true, 'core package health succeeds');
expectGlobalCore($result['ecosystem_id'] === 'GLOBAL-CORE-ECOSYSTEM', 'canonical core ecosystem ID');
expectGlobalCore($result['ecosystem'] === 'GLOBAL CORE ECOSYSTEM', 'canonical core ecosystem name');
expectGlobalCore($result['health']['execution_mode'] === 'STRUCTURAL_CHECK_ONLY', 'PHP reports structural-only execution');
expectGlobalCore($result['health']['python_catalog_executed'] === false, 'PHP does not claim to execute Python catalog');
expectGlobalCore($result['health']['live_provider_connections_verified'] === false, 'PHP does not claim live provider verification');

echo "All Global Core Ecosystem PHP tests passed.\n";
