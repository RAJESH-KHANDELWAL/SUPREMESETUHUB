<?php
declare(strict_types=1);
/** Read-only metadata contract for GLOBAL_APP_YOUTUBE_STORAGE_ECOSYSTEM. */
final class GlobalAppYoutubeStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_YOUTUBE_STORAGE_ECOSYSTEM';
 public const CATEGORY='YOUTUBE';
 public const CATEGORY_GROUP='PHOTO_VIDEO_AND_MEDIA';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
