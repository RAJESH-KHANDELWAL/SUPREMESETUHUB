<?php
declare(strict_types=1);

/**
 * PHP interoperability facade for DeepSeek Core result metadata.
 * This file does not resolve credentials or call DeepSeek APIs.
 */
require_once __DIR__ . '/deepseek_php_core_ecosystem/DeepSeekCoreContract.php';

final class DeepSeekCoreManager
{
    public static function normalizeResult(array $payload): array
    {
        return DeepSeekCoreContract::fromArray($payload)->toArray();
    }

    public static function normalizeJson(string $json): string
    {
        return DeepSeekCoreContract::fromJson($json)->toJson();
    }

    public static function isLiveConnectionVerified(array $payload): bool
    {
        return DeepSeekCoreContract::fromArray($payload)->isLiveConnectionVerified();
    }
}
