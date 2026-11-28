<?php
declare(strict_types=1);

/**
 * PHP interoperability facade for GLOBAL SERVER CORE.
 *
 * Python is the canonical metadata manager. This facade validates exchanged
 * results and scope catalogs; it does not call provider APIs or provision.
 */
require_once __DIR__ . '/php/GlobalServerCoreContract.php';
require_once __DIR__ . '/php/GlobalServerCoreScopeContract.php';

final class GlobalServerCoreManagerPHP
{
    public static function normalizeResult(array $payload): array
    {
        return GlobalServerCoreContract::fromArray($payload)->toArray();
    }

    public static function normalizeJson(string $json): string
    {
        return GlobalServerCoreContract::fromJson($json)->toJson();
    }

    public static function isLiveProviderConnectionVerified(array $payload): bool
    {
        return GlobalServerCoreContract::fromArray($payload)
            ->isLiveProviderConnectionVerified();
    }

    public static function normalizeScope(array $payload): array
    {
        return GlobalServerCoreScopeContract::normalize($payload);
    }
}
