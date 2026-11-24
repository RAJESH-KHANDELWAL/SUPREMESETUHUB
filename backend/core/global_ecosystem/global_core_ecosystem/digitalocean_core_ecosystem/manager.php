<?php
declare(strict_types=1);

/**
 * PHP interoperability facade for DigitalOcean Core result metadata.
 * It does not resolve credentials or call DigitalOcean APIs.
 */
require_once __DIR__ . '/digitalocean_php_core_ecosystem/DigitalOceanCoreContract.php';

final class DigitalOceanCoreManager
{
    public static function normalizeResult(array $payload): array
    {
        return DigitalOceanCoreContract::fromArray($payload)->toArray();
    }

    public static function normalizeJson(string $json): string
    {
        return DigitalOceanCoreContract::fromJson($json)->toJson();
    }

    public static function isLiveConnectionVerified(array $payload): bool
    {
        return DigitalOceanCoreContract::fromArray($payload)->isLiveConnectionVerified();
    }
}
