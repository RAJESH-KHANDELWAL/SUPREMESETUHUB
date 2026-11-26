<?php
declare(strict_types=1);

require_once __DIR__ . '/../manager.php';

$contract = AnthropicCoreManager::normalize([
    'success' => true,
    'ecosystem_id' => 'ANTHROPIC-CORE-ECOSYSTEM',
    'status' => 'interface_only',
]);
if (!$contract instanceof AnthropicCoreContract) {
    throw new RuntimeException('Anthropic manager did not return its contract');
}
if (($contract->toArray()['ecosystem_id'] ?? null) !== 'ANTHROPIC-CORE-ECOSYSTEM') {
    throw new RuntimeException('Anthropic ecosystem ID mismatch');
}
echo "Anthropic Core PHP test passed\\n";
