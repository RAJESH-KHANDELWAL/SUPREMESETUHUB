<?php
/** Read-only PHP metadata contract for GOOGLE_MULTIMEDIA_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GoogleMultimediaStorageEcosystem
{
    public const ECOSYSTEM_ID = 'GOOGLE_MULTIMEDIA_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'MULTIMEDIA';
    public const CATEGORY_GROUP = 'PHOTO_VIDEO_AND_MEDIA';

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
