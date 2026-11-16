<?php
declare(strict_types=1);
/** JSON contract helper only; no provider authentication or inference. */
final class GlobalAICoreContract {
 public const ECOSYSTEM_ID='GLOBAL-AI-CORE-ECOSYSTEM';
 public const RUNTIME_EXECUTION_ENABLED=false;
 public static function validateTenantContext(array $c): bool {
  return isset($c['tenant_id'],$c['actor_id']) && is_string($c['tenant_id']) && trim($c['tenant_id'])!=='' && is_string($c['actor_id']) && trim($c['actor_id'])!=='';
 }
 public static function rejectSecretMaterial(array $payload): void {
  $blocked=['token','access_token','refresh_token','authorization','api_key','client_secret','private_key','secret','password'];
  foreach($payload as $key=>$value) {
   if(is_string($key) && in_array(strtolower($key),$blocked,true)) throw new InvalidArgumentException('SECRET_MATERIAL_FORBIDDEN_IN_CORE');
   if(is_array($value)) self::rejectSecretMaterial($value);
  }
 }
}
