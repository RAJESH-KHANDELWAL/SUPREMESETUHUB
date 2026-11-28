<?php
declare(strict_types=1);
/** Read-only metadata contract for GLOBAL_APP_ANALYTICS_STORAGE_ECOSYSTEM. */
final class GlobalAppAnalyticsStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_ANALYTICS_STORAGE_ECOSYSTEM';
 public const CATEGORY='ANALYTICS';
 public const CATEGORY_GROUP='BUSINESS_AND_ENTERPRISE';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
