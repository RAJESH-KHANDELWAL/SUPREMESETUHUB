<?php
declare(strict_types=1);
/** Read-only PHP contract for Energy Utilities Environment business CORE. */
final class EnergyEnvironmentBusinessCoreContract {
 public const ECOSYSTEM_ID='GLOBAL-BADA-BUSINESS-ENERGY-UTILITIES-ENVIRONMENT-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM';
 public const CANONICAL_CORE_ID='GLOBAL-ENERGY-UTILITIES-ENVIRONMENT-CORE-ECOSYSTEM';
 public const MODE='CLASSIFICATION_ONLY';
 public static function allows(string $operation): bool { return in_array(strtoupper(trim($operation)),['LIST_DOMAINS','GET_DOMAIN','SEARCH_DOMAINS','CLASSIFY_SERVICE','VALIDATE_MAPPING','HEALTH'],true); }
}
