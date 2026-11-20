<?php
declare(strict_types=1);

/**
 * PHP entry point for the Google Core Ecosystem contract.
 *
 * This is an interoperability facade only. Python remains the canonical
 * metadata orchestrator; this file does not call Google APIs or OAuth.
 */
require_once __DIR__ . '/php/GoogleCoreContract.php';
require_once __DIR__ . '/php/GoogleCoreDomainContract.php';

final class GoogleCoreManager
{
    public static function normalizeResult(array $payload): array
    {
        return GoogleCoreContract::fromArray($payload)->toArray();
    }

    public static function normalizeJson(string $json): string
    {
        return GoogleCoreContract::fromJson($json)->toJson();
    }

    public static function isLiveConnectionVerified(array $payload): bool
    {
        return GoogleCoreContract::fromArray($payload)->isLiveConnectionVerified();
    }
}
