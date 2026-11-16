<?php
declare(strict_types=1);

/** Tenant-context contract only. This does not authenticate to Cloudflare. */
final class CloudflareR2AuthenticationContract {
 public const LIVE_CONNECTION_ENABLED = false;
 public static function validContext(array $context): bool {
  return isset($context['tenant_id'], $context['actor_id'])
   && is_string($context['tenant_id'])
   && is_string($context['actor_id'])
   && trim($context['tenant_id']) !== ''
   && trim($context['actor_id']) !== '';
 }
}
