<?php
declare(strict_types=1);

require_once __DIR__ . '/manager.php';

$manager = new AgricultureFoodNaturalResourcesBusinessManager();
$result = $manager->normalizeStatus([
    'success' => true,
    'domain_count' => 3,
]);

if ($result['ecosystem_id'] !== AgricultureFoodNaturalResourcesBusinessManager::ECOSYSTEM_ID) {
    throw new RuntimeException('Bada Business Agriculture CORE identity mismatch');
}
if ($result['success'] !== true || $result['domain_count'] !== 3) {
    throw new RuntimeException('Bada Business Agriculture CORE status normalization failed');
}
if ($result['live_providers_verified'] !== false) {
    throw new RuntimeException('Unverified live providers must remain false');
}

echo "Bada Business Agriculture CORE PHP interoperability test passed\n";
