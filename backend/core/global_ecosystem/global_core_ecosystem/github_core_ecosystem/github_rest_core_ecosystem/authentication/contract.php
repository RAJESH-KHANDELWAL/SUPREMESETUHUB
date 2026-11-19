<?php
declare(strict_types=1);
/** Caller context only. Never stores or resolves GitHub tokens. */
final class GitHubRestCoreServiceCallerContext {
 public const PROVIDER='github'; public const FAMILY='rest'; public const LIVE_PROVIDER_CALLS_ENABLED=false;
 public static function isValid(array $c): bool { return isset($c['tenant_id'],$c['actor_id']) && is_string($c['tenant_id']) && trim($c['tenant_id'])!=='' && is_string($c['actor_id']) && trim($c['actor_id'])!==''; }
}
