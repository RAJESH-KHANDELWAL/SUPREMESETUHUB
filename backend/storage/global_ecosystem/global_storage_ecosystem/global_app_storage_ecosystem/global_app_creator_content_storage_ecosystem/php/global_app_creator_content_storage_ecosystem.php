<?php
declare(strict_types=1);
/** Metadata contract for GLOBAL_APP_CREATOR_CONTENT_STORAGE_ECOSYSTEM. */
final class GlobalAppCreatorContentStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_CREATOR_CONTENT_STORAGE_ECOSYSTEM';
 public const CATEGORY='CREATOR_CONTENT';
 public const CATEGORY_GROUP='ENTERTAINMENT_AND_GAMING';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
