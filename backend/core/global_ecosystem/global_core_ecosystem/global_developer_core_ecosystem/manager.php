<?php
declare(strict_types=1);

/**
 * PHP interoperability contract for Global Developer Core.
 * Python is canonical. This facade performs no provider API calls.
 */
final class GlobalDeveloperCoreManager
{
    public const ECOSYSTEM_ID = 'GLOBAL-DEVELOPER-CORE-ECOSYSTEM';
    public const STATUS = 'CORE_CATALOG_ONLY';

    public static function normalizeResult(array $payload): array
    {
        return [
            'success' => (bool)($payload['success'] ?? false),
            'ecosystem_id' => (string)($payload['ecosystem_id'] ?? self::ECOSYSTEM_ID),
            'status' => (string)($payload['status'] ?? self::STATUS),
            'live_connection_verified' => false,
            'api_calls_performed' => 0,
            'data' => is_array($payload['data'] ?? null) ? $payload['data'] : [],
            'errors' => is_array($payload['errors'] ?? null) ? $payload['errors'] : [],
        ];
    }
}
