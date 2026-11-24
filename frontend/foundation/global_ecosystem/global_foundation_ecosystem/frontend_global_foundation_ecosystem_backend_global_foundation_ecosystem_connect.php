<?php
/**
 * Frontend-to-backend Global Foundation Ecosystem presence/contract check.
 * This verifies files; it does not bridge Python and PHP runtimes.
 */
final class FrontendGlobalFoundationEcosystemBackendConnector {
    private string $frontendRoot;
    private string $backendRoot;

    public function __construct() {
        $this->frontendRoot = __DIR__;
        $repositoryRoot = dirname(__DIR__, 4);
        $this->backendRoot = $repositoryRoot . '/backend/foundation/global_ecosystem/global_foundation_ecosystem';
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
        $frontend = $this->check($this->frontendRoot);
        $backend = $this->check($this->backendRoot);
        return [
            'name' => 'FRONTEND-BACKEND GLOBAL FOUNDATION ECOSYSTEM CONNECTOR',
            'frontend' => $frontend,
            'backend' => $backend,
            'connected' => $frontend['healthy'] && $backend['healthy'],
            'connection_type' => 'filesystem contract check; not a runtime bridge',
        ];
    }
}
