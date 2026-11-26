<?php
declare(strict_types=1);

require_once __DIR__ . '/../core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/manager.php';

$normalized = AppleCoreManager::normalizeResult([
    'success' => true,
    'ecosystem_id' => 'APPLE-CORE-ECOSYSTEM',
    'status' => 'interface_only',
]);
if (($normalized['ecosystem_id'] ?? null) !== 'APPLE-CORE-ECOSYSTEM') {
    throw new RuntimeException('Apple ecosystem ID mismatch');
}
echo "Apple Core PHP test passed\n";
