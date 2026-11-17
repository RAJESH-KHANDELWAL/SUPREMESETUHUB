<?php
declare(strict_types=1);

namespace SupremeSetu\Core\SocialMedia;

final class SocialMediaCoreContract
{
    public static function normalize(array $payload): array
    {
        $required = ['success', 'ecosystem_id', 'status'];
        foreach ($required as $key) {
            if (!array_key_exists($key, $payload)) {
                throw new \InvalidArgumentException('Missing required field: ' . $key);
            }
        }
        if (!is_bool($payload['success']) || !is_string($payload['ecosystem_id']) || !is_string($payload['status'])) {
            throw new \InvalidArgumentException('Invalid Social Media Core result contract');
        }
        return [
            'success' => $payload['success'],
            'ecosystem_id' => $payload['ecosystem_id'],
            'status' => $payload['status'],
            'data' => is_array($payload['data'] ?? null) ? $payload['data'] : [],
            'errors' => is_array($payload['errors'] ?? null) ? $payload['errors'] : [],
            'request_id' => is_string($payload['request_id'] ?? null) ? $payload['request_id'] : null,
            'timestamp' => is_string($payload['timestamp'] ?? null) ? $payload['timestamp'] : null,
        ];
    }
}
