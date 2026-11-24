<?php
/** Read-only PHP metadata contract for GOOGLE_CALENDAR_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GoogleCalendarStorageEcosystem
{
    public const ECOSYSTEM_ID = 'GOOGLE_CALENDAR_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'CALENDAR';
    public const CATEGORY_GROUP = 'COMMUNICATION';

    /** @return array<string,mixed> */
    public function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'provider' => 'GOOGLE',
            'category' => self::CATEGORY,
            'category_group' => self::CATEGORY_GROUP,
            'connection_state' => 'NOT_CONFIGURED',
            'provider_product_verified' => false,
            'storage_operations_enabled' => false,
        ];
    }
}
