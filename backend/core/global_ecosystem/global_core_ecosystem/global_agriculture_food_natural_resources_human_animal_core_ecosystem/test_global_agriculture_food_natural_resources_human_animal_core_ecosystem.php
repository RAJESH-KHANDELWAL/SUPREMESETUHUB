<?php
declare(strict_types=1);

require_once __DIR__ . '/manager.php';

$manager = new AgricultureFoodNaturalResourcesHumanAnimalCoreManager();
$result = $manager->normalizeStatus([
    'success' => true,
    'status' => 'READY',
]);

if ($result['ecosystem_id'] !== AgricultureFoodNaturalResourcesHumanAnimalCoreManager::ECOSYSTEM_ID) {
    throw new RuntimeException('Agriculture CORE identity mismatch');
}
if ($result['success'] !== true || $result['status'] !== 'READY') {
    throw new RuntimeException('Agriculture CORE status normalization failed');
}
if ($result['live_data_verified'] !== false || $result['provider_connections_verified'] !== false) {
    throw new RuntimeException('Unverified live connections must remain false');
}

echo "Agriculture CORE PHP interoperability test passed\n";
