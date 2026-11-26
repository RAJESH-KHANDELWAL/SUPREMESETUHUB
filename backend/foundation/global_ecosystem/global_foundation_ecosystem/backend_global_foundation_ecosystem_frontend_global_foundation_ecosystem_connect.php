<?php
/**
 * Backend-to-frontend Global Foundation Ecosystem presence/contract check.
 * This verifies files; it does not bridge Python and PHP runtimes.
 */
final class BackendGlobalFoundationEcosystemFrontendConnector {
    private string $backendRoot;
    private string $frontendRoot;

    public function __construct() {
        $this->backendRoot = __DIR__;
        $repositoryRoot = dirname(__DIR__, 4);
        $this->frontendRoot = $repositoryRoot . '/frontend/foundation/global_ecosystem/global_foundation_ecosystem';
    }

    private function check(string $root): array {
        $required = ['__init__.py', 'manager.py', 'manager.php'];
        $checks = [];
        foreach ($required as $name) {
            $checks[$name] = is_file($root . '/' . $name);
        }
        return ['path' => $root, 'checks' => $checks, 'healthy' => !in_array(false, $checks, true)];
    }

    public function connect(): array {
        $backend = $this->check($this->backendRoot);
        $frontend = $this->check($this->frontendRoot);
        return [
            'name' => 'BACKEND-FRONTEND GLOBAL FOUNDATION ECOSYSTEM CONNECTOR',
            'backend' => $backend,
            'frontend' => $frontend,
            'connected' => $backend['healthy'] && $frontend['healthy'],
            'connection_type' => 'filesystem contract check; not a runtime bridge',
        ];
    }
}
