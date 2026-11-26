<?php
declare(strict_types=1);

require_once __DIR__ . '/../manager.php';

$manager = new CohereCoreManager();
$status = $manager->status();
if (($status['ecosystem_id'] ?? null) !== 'COHERE-CORE-ECOSYSTEM') {
    throw new RuntimeException('Cohere ecosystem ID mismatch');
}
$result = $manager->validateCapability('classify', []);
if (($result['success'] ?? false) !== true || ($result['api_call_performed'] ?? true) !== false) {
    throw new RuntimeException('Cohere capability contract check failed');
}
echo "Cohere Core PHP test passed\\n";
