<?php
declare(strict_types=1);

/**
 * GitHub Core interoperability facade.
 * Python owns canonical discovery/orchestration; this facade handles metadata
 * normalization only and never authenticates or calls GitHub.
 */
final class GitHubCoreManager
{
    private const SECRET_KEYS = [
        'token', 'access_token', 'refresh_token', 'authorization',
        'api_key', 'client_secret', 'private_key', 'webhook_secret',
        'password', 'secret',
    ];

    public static function sanitize(array $payload): array
    {
        $safe = [];
        foreach ($payload as $key => $value) {
            if (in_array(strtolower((string) $key), self::SECRET_KEYS, true)) {
                continue;
            }
            $safe[$key] = is_array($value) ? self::sanitize($value) : $value;
        }
        return $safe;
    }

    public static function normalizeResult(array $payload): array
    {
        return self::sanitize($payload);
    }

    public static function isLiveConnectionVerified(array $payload): bool
    {
        return ($payload['live_connection_verified'] ?? false) === true;
    }
}
