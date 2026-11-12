<?php
declare(strict_types=1);

namespace SupremeSetuHub\GlobalEcosystem\PHP;

final class GlobalAlgorithmKernel
{
    private const SECRET_KEYS = [
        'password', 'passwd', 'secret', 'token', 'access_token',
        'refresh_token', 'api_key', 'apikey', 'authorization',
        'client_secret', 'private_key',
    ];

    public static function normalizeIdentifier(string $value): string
    {
        $value = strtolower(trim($value));
        $value = preg_replace('/[^a-z0-9]+/', '-', $value) ?? '';
        return trim($value, '-');
    }

    public static function canonicalJson(mixed $value): string
    {
        $json = json_encode(
            self::sortRecursively($value),
            JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRESERVE_ZERO_FRACTION
        );
        if ($json === false) {
            throw new \\InvalidArgumentException('Canonical JSON encoding failed: ' . json_last_error_msg());
        }
        return $json;
    }

    public static function stableHash(mixed $value, string $algorithm = 'sha256'): string
    {
        if (!in_array($algorithm, hash_algos(), true)) {
            throw new \\InvalidArgumentException('Unsupported hash algorithm.');
        }
        return hash($algorithm, self::canonicalJson($value));
    }

    public static function paginate(array $items, int $page = 1, int $perPage = 25, int $maxPerPage = 100): array
    {
        if ($page < 1 || $perPage < 1 || $maxPerPage < 1) {
            throw new \\InvalidArgumentException('Page and page-size values must be positive.');
        }
        $perPage = min($perPage, $maxPerPage);
        $total = count($items);
        return [
            'items' => array_slice($items, ($page - 1) * $perPage, $perPage),
            'page' => $page,
            'per_page' => $perPage,
            'total' => $total,
            'total_pages' => $total === 0 ? 0 : (int) ceil($total / $perPage),
        ];
    }

    public static function retryDelaySeconds(int $attempt, int $baseSeconds = 1, int $maxSeconds = 60): int
    {
        if ($attempt < 1 || $baseSeconds < 0 || $maxSeconds < 0) {
            throw new \\InvalidArgumentException('Invalid retry delay parameters.');
        }
        return min($maxSeconds, $baseSeconds * (2 ** min($attempt - 1, 30)));
    }

    public static function redact(mixed $value): mixed
    {
        if (!is_array($value)) {
            return $value;
        }
        $clean = [];
        foreach ($value as $key => $item) {
            $normalized = is_string($key)
                ? strtolower(preg_replace('/[^a-z0-9]+/i', '_', $key) ?? $key)
                : '';
            $secret = in_array($normalized, self::SECRET_KEYS, true)
                || str_ends_with($normalized, '_token')
                || str_ends_with($normalized, '_secret')
                || str_ends_with($normalized, '_api_key');
            $clean[$key] = $secret ? '[REDACTED]' : self::redact($item);
        }
        return $clean;
    }

    private static function sortRecursively(mixed $value): mixed
    {
        if (is_object($value)) {
            $value = get_object_vars($value);
        }
        if (!is_array($value)) {
            if (is_resource($value)) {
                throw new \\InvalidArgumentException('Resources cannot be serialized.');
            }
            return $value;
        }
        if (array_is_list($value)) {
            return array_map([self::class, 'sortRecursively'], $value);
        }
        ksort($value, SORT_STRING);
        foreach ($value as $key => $item) {
            $value[$key] = self::sortRecursively($item);
        }
        return $value;
    }
}
