<?php
/**
 * Thin PHP interoperability metadata facade for NSFWinfra Core.
 * Python manager is canonical. This facade does not call provider endpoints.
 */
declare(strict_types=1);
final class NSFWinfraCoreMetadata
{
    public const ECOSYSTEM_ID = 'NSFWINFRA-CORE-ECOSYSTEM';
    public const STATUS = 'CORE_CATALOG_ONLY';
    public static function status(): array
    {
        return ['ecosystem_id' => self::ECOSYSTEM_ID, 'status' => self::STATUS, 'connected' => false, 'live_connection_verified' => false, 'api_calls_performed' => 0];
    }
}
