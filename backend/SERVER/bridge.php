<?php
/** Optional PHP interoperability boundary for the SERVER domain.
 * This file is not executed by the Python backend. Do not put secrets here.
 */
final class ServerDomainBridge {
    public static function domain(): string { return 'SERVER'; }
    public static function status(): string { return 'scaffold'; }
}
