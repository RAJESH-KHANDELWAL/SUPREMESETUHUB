<?php
declare(strict_types=1);

/**
 * SUPREMESETUHUB identity-gate foundation.
 *
 * One central database; one main identity and four logical brand gates.
 * This class validates identity selection and constructs safe scope predicates.
 * Authentication and role authorization must be performed by the host app.
 */
final class SupremeIdentityGate
{
    public const MAIN = 'SUPREMESETUHUB';

    /** @var list<string> */
    public const GATES = [
        'RAJESHKHANDELWALOFFICIAL',
        'RAJESHKHANDELWAL',
        'DRRAJESHKHANDELWALIBCOFFICIAL',
        'DRRAJESHKHANDELWALIBC',
    ];

    /** @var list<string> */
    public const ALL = [
        self::MAIN,
        'RAJESHKHANDELWALOFFICIAL',
        'RAJESHKHANDELWAL',
        'DRRAJESHKHANDELWALIBCOFFICIAL',
        'DRRAJESHKHANDELWALIBC',
    ];

    public static function normalize(string $identityCode): string
    {
        $code = strtoupper(trim($identityCode));
        if (!in_array($code, self::ALL, true)) {
            throw new InvalidArgumentException('Unknown SUPREMESETUHUB identity.');
        }
        return $code;
    }

    /**
     * Return SQL predicate and parameter separately; bind the parameter via PDO.
     * The column name must be a trusted schema constant, never request input.
     *
     * @return array{sql: string, params: array{identity_code: string}}
     */
    public static function scope(string $identityCode, string $column = 'identity_code'): array
    {
        if (!preg_match('/^[A-Za-z_][A-Za-z0-9_]*$/', $column)) {
            throw new InvalidArgumentException('Unsafe scope column.');
        }
        return [
            'sql' => $column . ' = :identity_code',
            'params' => ['identity_code' => self::normalize($identityCode)],
        ];
    }

    public static function assertSameIdentity(string $requested, string $active): void
    {
        if (self::normalize($requested) !== self::normalize($active)) {
            throw new RuntimeException('Cross-identity access is denied.');
        }
    }
}
