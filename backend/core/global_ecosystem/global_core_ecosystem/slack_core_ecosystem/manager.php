<?php
declare(strict_types=1);
require_once __DIR__ . '/slack_php_core_ecosystem/SlackCoreContract.php';
/** PHP metadata facade only; no OAuth or Slack API transport. */
final class SlackCoreManager {
 public static function normalizeResult(array $payload): array { return SlackCoreContract::fromArray($payload)->toArray(); }
 public static function normalizeJson(string $json): string { return SlackCoreContract::fromJson($json)->toJson(); }
 public static function isLiveConnectionVerified(array $payload): bool { return SlackCoreContract::fromArray($payload)->isLiveConnectionVerified(); }
}
