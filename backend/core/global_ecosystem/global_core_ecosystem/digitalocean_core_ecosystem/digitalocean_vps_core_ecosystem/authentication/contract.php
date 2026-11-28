<?php
declare(strict_types=1);
/** Caller/tenant context only. Tokens are never stored or resolved by CORE. */
final class DigitalOceanCallerContext {
 public const PROVIDER='digitalocean';
 public const CAPABILITY='vps';
 public const LIVE_CONNECTION_ENABLED=false;
 public static function validContext(array $context): bool { return isset($context['tenant_id'],$context['actor_id']) && is_string($context['tenant_id']) && is_string($context['actor_id']) && trim($context['tenant_id'])!=='' && trim($context['actor_id'])!==''; }
}
