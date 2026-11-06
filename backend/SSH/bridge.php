<?php
/** Optional PHP interoperability boundary for the SSH domain.
 * This file is not executed by the Python backend. Do not put secrets here.
 */
final class SshDomainBridge {
    public static function domain(): string { return 'SSH'; }
    public static function status(): string { return 'scaffold'; }
}
