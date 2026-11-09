<?php
declare(strict_types=1);

namespace SupremeSetuHub\\GlobalCore;

/**
 * Deterministic, framework-neutral primitives for PHP integrations.
 * This kernel is intentionally independent from the Python/FastAPI runtime.
 */
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
        $normalized = self::sortRecursively($value);
        $json = json_encode(
            $normalized,
            JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRESERVE_ZERO_FRACTION
        );

        if ($json === false) {
            throw new \\InvalidArgumentException('Value cannot be encoded as canonical JSON: ' . json_last_error_msg());
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

    /**
     * @param array<mixed> $items
     * @return array{items: array<mixed>, page: int, per_page: int, total: int, total_pages: int}
     */
    public static function paginate(array $items, int $page = 1, int $perPage = 25, int $maxPerPage = 100): array
    {
        if ($page < 1 || $perPage < 1 || $maxPerPage < 1) {
            throw new \\InvalidArgumentException('Page and page-size values must be positive.');
        }

        $perPage = min($perPage, $maxPerPage);
        $total = count($items);
        $totalPages = $total === 0 ? 0 : (int) ceil($total / $perPage);
        $offset = ($page - 1) * $perPage;

        return [
            'items' => array_slice($items, $offset, $perPage),
            'page' => $page,
            'per_page' => $perPage,
            'total' => $total,
            'total_pages' => $totalPages,
        ];
    }

    public static function retryDelaySeconds(int $attempt, int $baseSeconds = 1, int $maxSeconds = 60): int
    {
        if ($attempt < 1 || $baseSeconds < 0 || $maxSeconds < 0) {
            throw new \\InvalidArgumentException('Retry attempt must be positive and delay bounds non-negative.');
        }

        $exponent = min($attempt - 1, 30);
        return min($maxSeconds, $baseSeconds * (2 ** $exponent));
    }

    public static function redact(mixed $value): mixed
    {
        if (!is_array($value)) {
            return $value;
        }

        $clean = [];
        foreach ($value as $key => $item) {
            if (is_string($key) && self::isSecretKey($key)) {
                $clean[$key] = '[REDACTED]';
            } else {
                $clean[$key] = self::redact($item);
            }
        }

        return $clean;
    }

    private static function isSecretKey(string $key): bool
    {
        $normalized = strtolower(preg_replace('/[^a-z0-9]+/i', '_', $key) ?? $key);
        return in_array($normalized, self::SECRET_KEYS, true)
            || str_ends_with($normalized, '_token')
            || str_ends_with($normalized, '_secret')
            || str_ends_with($normalized, '_api_key');
    }

    private static function sortRecursively(mixed $value): mixed
    {
        if (!is_array($value)) {
            if (is_object($value)) {
                return self::sortRecursively(get_object_vars($value));
            }
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
