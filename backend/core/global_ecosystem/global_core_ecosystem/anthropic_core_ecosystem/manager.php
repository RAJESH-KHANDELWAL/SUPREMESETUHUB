<?php
declare(strict_types=1);

/** Anthropic Core metadata facade; no provider API calls or credential handling. */
require_once __DIR__ . '/php/AnthropicCoreContract.php';

final class AnthropicCoreManager
{
    public const NAME = 'ANTHROPIC CORE ECOSYSTEM';
    public const ECOSYSTEM_ID = 'ANTHROPIC-CORE-ECOSYSTEM';

    public static function normalize(array $payload): AnthropicCoreContract
    {
        return AnthropicCoreContract::fromArray($payload);
    }
}
