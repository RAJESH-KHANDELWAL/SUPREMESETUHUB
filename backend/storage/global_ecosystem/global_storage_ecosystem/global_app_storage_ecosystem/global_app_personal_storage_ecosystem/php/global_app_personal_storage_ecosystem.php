<?php
declare(strict_types=1);
/** Read-only metadata contract for GLOBAL_APP_PERSONAL_STORAGE_ECOSYSTEM. */
final class GlobalAppPersonalStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_PERSONAL_STORAGE_ECOSYSTEM';
 public const CATEGORY='PERSONAL';
 public const CATEGORY_GROUP='PERSONAL_AND_CLOUD_STORAGE';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
