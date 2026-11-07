<?php
/** Optional PHP interoperability boundary for the CLOUD domain.
 * This file is not executed by the Python backend. Do not put secrets here.
 */
final class CloudDomainBridge {
    public static function domain(): string { return 'CLOUD'; }
    public static function status(): string { return 'scaffold'; }
}
