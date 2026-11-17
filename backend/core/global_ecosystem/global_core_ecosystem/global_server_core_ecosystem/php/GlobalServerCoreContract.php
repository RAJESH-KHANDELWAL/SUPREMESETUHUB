<?php
declare(strict_types=1);

/** Read-only PHP 8+ contract normalizer for Server Core result payloads. */
final class GlobalServerCoreContract
{
    public static function normalize(array $payload): array
    {
        $required = ['success', 'ecosystem_id', 'status'];
        foreach ($required as $key) {
            if (!array_key_exists($key, $payload)) {
                throw new InvalidArgumentException("Missing required Core result field: {$key}");
            }
        }
        if (!is_bool($payload['success']) ||
            !is_string($payload['ecosystem_id']) ||
            !is_string($payload['status'])) {
            throw new InvalidArgumentException('Invalid Server Core result field types');
        }
        $data = $payload['data'] ?? [];
        $errors = $payload['errors'] ?? [];
        if (!is_array($data) || !is_array($errors)) {
            throw new InvalidArgumentException('Core result data and errors must be arrays');
        }
        return [
            'success' => $payload['success'],
            'ecosystem_id' => $payload['ecosystem_id'],
            'status' => $payload['status'],
            'data' => $data,
            'errors' => array_values($errors),
            'request_id' => isset($payload['request_id']) ? (string) $payload['request_id'] : null,
            'timestamp' => isset($payload['timestamp']) ? (string) $payload['timestamp'] : null,
            'remote_operations_enabled' => false,
        ];
    }
}
