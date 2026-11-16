<?php
declare(strict_types=1);
/** Authenticated caller context only; credentials are resolved outside CORE. */
final class DeepSeekCallerContext {
 public const PROVIDER='deepseek';
 public const LIVE_CONNECTION_ENABLED=false;
 public static function validContext(array $c): bool {
  return isset($c['tenant_id'],$c['actor_id']) && is_string($c['tenant_id']) && is_string($c['actor_id']) && trim($c['tenant_id'])!=='' && trim($c['actor_id'])!=='';
 }
}
