<?php
/**
 * SUPREMESETUHUB global algorithm primitives.
 *
 * Framework-neutral helpers for deterministic processing, safe diagnostics,
 * pagination and bounded retry scheduling. Domain modules remain responsible
 * for authorization, persistence and business-specific rules.
 */
declare(strict_types=1);

namespace SupremeSetuHub\\GlobalCore;

use InvalidArgumentException;
use JsonException;

final class GlobalAlgorithmKernel
{
    private const SENSITIVE_KEY_PATTERN = '/(?:pass(?:word)?|secret|token|api[_-]?key|authorization|cookie|credential|private[_-]?key)/i';

    private function __construct()
    {
    }

    public static function normalizeIdentifier(string $value, int $maxLength = 128): string
    {
        if ($maxLength < 1) {
            throw new InvalidArgumentException('maxLength must be positive.');
        }

        $value = strtolower(trim($value));
        $value = preg_replace('/[^a-z0-9._:-]+/', '-', $value) ?? '';
        $value = trim($value, '-');

        return substr($value, 0, $maxLength);
    }

    /**
     * Canonical JSON for stable hashes/signatures. Associative keys are sorted;
     * list order is retained because it can be semantically meaningful.
     *
     * @throws JsonException
     */
    public static function canonicalJson(mixed $value): string
    {
        return json_encode(
            self::canonicalize($value),
            JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE
        );
    }

    /** @throws JsonException */
    public static function stableHash(mixed $value, string $algorithm = 'sha256'): string
    {
        if (!in_array($algorithm, hash_algos(), true)) {
            throw new InvalidArgumentException('Unsupported hash algorithm.');
        }

        return hash($algorithm, self::canonicalJson($value));
    }

    /**
     * Return a bounded page of items with explicit metadata.
     *
     * @param array<int, mixed> $items
     * @return array{items: array<int, mixed>, page: int, per_page: int, total: int, total_pages: int}
     */
    public static function paginate(array $items, int $page = 1, int $perPage = 25, int $maxPerPage = 100): array
    {
        if ($page < 1 || $perPage < 1 || $maxPerPage < 1) {
            throw new InvalidArgumentException('Page and page-size values must be positive.');
        }

        $perPage = min($perPage, $maxPerPage);
        $total = count($items);

        return [
            'items' => array_values(array_slice($items, ($page - 1) * $perPage, $perPage)),
            'page' => $page,
            'per_page' => $perPage,
            'total' => $total,
            'total_pages' => $total === 0 ? 0 : (int) ceil($total / $perPage),
        ];
    }

    /** Exponential retry delay capped to prevent unbounded waits. */
    public static function retryDelaySeconds(int $attempt, int $baseSeconds = 1, int $maxSeconds = 60): int
    {
        if ($attempt < 1 || $baseSeconds < 0 || $maxSeconds < 0) {
            throw new InvalidArgumentException('Attempt must be positive and delay bounds non-negative.');
        }

        if ($baseSeconds === 0 || $maxSeconds === 0) {
            return 0;
        }

        $exponent = min($attempt - 1, 30);
        $delay = $baseSeconds * (2 ** $exponent);

        return (int) min($delay, $maxSeconds);
    }

    /**
     * Redact likely secret values before diagnostic output.
     * This is a safety net, not a substitute for data-minimization in logging.
     */
    public static function redact(mixed $value): mixed
    {
        if (!is_array($value)) {
            return $value;
        }

        $redacted = [];
        foreach ($value as $key => $item) {
            if (is_string($key) && preg_match(self::SENSITIVE_KEY_PATTERN, $key) === 1) {
                $redacted[$key] = '[REDACTED]';
            } else {
                $redacted[$key] = self::redact($item);
            }
        }

        return $redacted;
    }

    private static function canonicalize(mixed $value): mixed
    {
        if (!is_array($value)) {
            if (is_object($value)) {
                return self::canonicalize(get_object_vars($value));
            }
            return $value;
        }

        if (array_is_list($value)) {
            return array_map([self::class, 'canonicalize'], $value);
        }

        ksort($value, SORT_STRING);
        foreach ($value as $key => $item) {
            $value[$key] = self::canonicalize($item);
        }

        return $value;
    }
}
