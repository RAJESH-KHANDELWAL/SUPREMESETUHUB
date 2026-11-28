<?php
declare(strict_types=1);
/** PHP interoperability facade for Apple Core metadata only; no Apple API calls. */
final class AppleCoreManager
{
    public static function normalizeResult(array $payload): array
    {
        foreach (['success', 'ecosystem_id', 'status'] as $required) {
            if (!array_key_exists($required, $payload)) {
                throw new InvalidArgumentException('APPLE_CORE_FIELD_REQUIRED: ' . $required);
            }
        }
        if (!is_bool($payload['success']) || !is_string($payload['ecosystem_id']) || !is_string($payload['status'])) {
            throw new InvalidArgumentException('APPLE_CORE_CONTRACT_TYPE_INVALID');
        }
        return self::sanitize($payload);
    }
    public static function normalizeJson(string $json): string
    {
        $payload = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($payload)) { throw new InvalidArgumentException('APPLE_CORE_JSON_OBJECT_REQUIRED'); }
        return json_encode(self::normalizeResult($payload), JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES);
    }
    public static function isLiveConnectionVerified(array $payload): bool
    {
        $normalized = self::normalizeResult($payload);
        return (($normalized['live_connection_verified'] ?? false) === true);
    }
    private static function sanitize(array $payload): array
    {
        $blocked = ['token','access_token','refresh_token','client_secret','api_key','secret','authorization','password','private_key','key_material'];
        $clean = [];
        foreach ($payload as $key => $value) {
            if (in_array(strtolower((string)$key), $blocked, true)) { continue; }
            if (is_array($value)) { $value = self::sanitize($value); }
            $clean[$key] = $value;
        }
        return $clean;
    }
}
