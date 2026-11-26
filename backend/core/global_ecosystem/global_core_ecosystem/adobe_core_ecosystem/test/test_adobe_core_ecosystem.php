<?php
declare(strict_types=1);

require_once __DIR__ . '/../manager.php';

$payload = [
    'success' => true,
    'ecosystem_id' => 'ADOBE-CORE-ECOSYSTEM',
    'status' => 'interface_only',
    'api_key' => 'must-not-survive',
];
$normalized = AdobeCoreManager::normalizeResult($payload);
if (($normalized['ecosystem_id'] ?? null) !== 'ADOBE-CORE-ECOSYSTEM') {
    throw new RuntimeException('Adobe ecosystem ID mismatch');
}
if (array_key_exists('api_key', $normalized)) {
    throw new RuntimeException('Adobe contract leaked a secret field');
}
echo "Adobe Core PHP test passed\\n";
