<?php
declare(strict_types=1);

/** Executable contract tests for the Adobe Core PHP interoperability facade. */
require_once __DIR__ . '/manager.php';

function check(bool $condition, string $message): void {
    if (!$condition) {
        throw new RuntimeException('ADOBE_CORE_TEST_FAILED: ' . $message);
    }
}

$payload = [
    'success' => true,
    'ecosystem_id' => 'ADOBE-CORE-ECOSYSTEM',
    'status' => 'ready',
    'live_connection_verified' => false,
    'metadata' => ['provider' => 'Adobe', 'api_key' => 'must-not-leak'],
];

$normalized = AdobeCoreManager::normalizeResult($payload);
check($normalized['ecosystem_id'] === 'ADOBE-CORE-ECOSYSTEM', 'ecosystem ID is preserved');
check(!array_key_exists('api_key', $normalized['metadata']), 'nested secret fields are removed');
check(AdobeCoreManager::isLiveConnectionVerified($normalized) === false, 'unverified connection remains false');

$json = AdobeCoreManager::normalizeJson(json_encode($payload, JSON_THROW_ON_ERROR));
$decoded = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
check($decoded['success'] === true, 'JSON round-trip preserves success');
check(!array_key_exists('api_key', $decoded['metadata']), 'JSON round-trip does not expose secrets');

$missingFieldRejected = false;
try {
    AdobeCoreManager::normalizeResult(['success' => true, 'status' => 'ready']);
} catch (InvalidArgumentException $exception) {
    $missingFieldRejected = str_contains($exception->getMessage(), 'ADOBE_CORE_FIELD_REQUIRED');
}
check($missingFieldRejected, 'missing required contract fields are rejected');

$typeRejected = false;
try {
    AdobeCoreManager::normalizeResult([
        'success' => 'yes',
        'ecosystem_id' => 'ADOBE-CORE-ECOSYSTEM',
        'status' => 'ready',
    ]);
} catch (InvalidArgumentException $exception) {
    $typeRejected = str_contains($exception->getMessage(), 'ADOBE_CORE_CONTRACT_TYPE_INVALID');
}
check($typeRejected, 'invalid contract field types are rejected');

echo "Adobe Core Ecosystem PHP tests passed.\n";
