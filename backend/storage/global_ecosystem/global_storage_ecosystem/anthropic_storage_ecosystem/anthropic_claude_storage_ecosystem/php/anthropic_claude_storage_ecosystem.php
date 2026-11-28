<?php
/** Read-only metadata helper for ANTHROPIC_CLAUDE_STORAGE_ECOSYSTEM. */
declare(strict_types=1);
final class AnthropicCLAUDEStorageEcosystem {
    public const ECOSYSTEM_ID = 'ANTHROPIC_CLAUDE_STORAGE_ECOSYSTEM';
    public const CONNECTION_STATE = 'NOT_CONFIGURED';
    public static function isConnected(): bool { return false; }
}
