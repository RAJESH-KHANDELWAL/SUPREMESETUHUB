<?php
/** Optional PHP bridge for GLOBAL_SERVER_ECOSYSTEM; metadata only, no live provider calls. */
final class ServerEcosystemBridge {
    public static function ecosystem(): string { return 'GLOBAL_SERVER_ECOSYSTEM'; }
    public static function connectionStatus(): string { return 'not_configured'; }
}
