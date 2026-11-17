<?php
declare(strict_types=1);
/** Read-only metadata contract for GLOBAL_APP_PUBLIC_INFORMATION_STORAGE_ECOSYSTEM. */
final class GlobalAppPublicInformationStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_APP_PUBLIC_INFORMATION_STORAGE_ECOSYSTEM';
 public const CATEGORY='PUBLIC_INFORMATION';
 public const CATEGORY_GROUP='GENERAL_AND_SEARCH';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_APP','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
