<?php
declare(strict_types=1);
/** CORE caller context only; provider authentication belongs outside CORE. */
final class MicrosoftStorageCoreCallerContext {
 public const PROVIDER_ID='microsoft';
 public const LIVE_CONNECTION_VERIFIED=false;
 public static function isValid(array $context): bool {
  return isset($context['tenant_id'],$context['actor_id'])
   && is_string($context['tenant_id']) && trim($context['tenant_id'])!==''
   && is_string($context['actor_id']) && trim($context['actor_id'])!=='';
 }
}
