<?php
declare(strict_types=1);

/**
 * PHP interoperability facade for OpenAI Core metadata.
 * This file does not perform API transport, credential handling or inference.
 */
require_once __DIR__ . '/openai_php_core_ecosystem/OpenAICoreContract.php';
require_once __DIR__ . '/openai_php_core_ecosystem/OpenAICoreDomainContract.php';

final class OpenAICoreManager
{
    public static function normalizeResult(array $payload): array
    {
        return OpenAICoreContract::fromArray($payload)->toArray();
    }

    public static function normalizeJson(string $json): string
    {
        return OpenAICoreContract::fromJson($json)->toJson();
    }

    public static function isLiveConnectionVerified(array $payload): bool
    {
        return OpenAICoreContract::fromArray($payload)->isLiveConnectionVerified();
    }
}
