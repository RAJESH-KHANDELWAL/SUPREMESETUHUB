<?php
declare(strict_types=1);

namespace SupremeSetuHub\AwsCore;

final class AwsCoreContract
{
    public static function normalize(array $payload): array
    {
        foreach (['success', 'ecosystem_id', 'status'] as $key) {
            if (!array_key_exists($key, $payload)) {
                throw new \InvalidArgumentException('AWS_CORE_FIELD_REQUIRED: ' . $key);
            }
        }
        if (!is_bool($payload['success']) || !is_string($payload['ecosystem_id']) || !is_string($payload['status'])) {
            throw new \InvalidArgumentException('AWS_CORE_CONTRACT_TYPE_INVALID');
        }
        return [
            'success' => $payload['success'],
            'ecosystem_id' => $payload['ecosystem_id'],
            'status' => $payload['status'],
            'data' => is_array($payload['data'] ?? null) ? $payload['data'] : [],
            'errors' => is_array($payload['errors'] ?? null) ? $payload['errors'] : [],
            'request_id' => isset($payload['request_id']) ? (string) $payload['request_id'] : null,
            'timestamp' => isset($payload['timestamp']) ? (string) $payload['timestamp'] : null,
        ];
    }
}
