<?php
/**
 * PHP-facing metadata and structural status for GLOBAL CORE ECOSYSTEM.
 *
 * Catalog operations remain owned by the Python implementation. This PHP
 * entry point intentionally does not duplicate or mutate that registry.
 */
require_once __DIR__ . '/manager.php';

final class GlobalCoreEcosystem
{
    public const ID = 'GLOBAL-CORE-ECOSYSTEM';
    public const NAME = 'GLOBAL CORE ECOSYSTEM';
    public const VERSION = '1.0.0';

    /** @return array<string, mixed> */
    public static function status(): array
    {
        $health = (new GlobalCoreEcosystemManager())->health();

        return [
            'success' => $health['healthy'],
            'ecosystem_id' => self::ID,
            'ecosystem' => self::NAME,
            'version' => self::VERSION,
            'status' => $health['status'],
            'health' => $health,
        ];
    }
}
