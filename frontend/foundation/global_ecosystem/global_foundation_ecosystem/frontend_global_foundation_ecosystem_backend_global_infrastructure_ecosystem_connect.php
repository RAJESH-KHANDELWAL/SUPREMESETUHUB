<?php
/**
 * Frontend Global Foundation to Backend Global Infrastructure contract check.
 * Verifies required files only; it does not bridge Python and PHP runtimes.
 */
final class FrontendGlobalFoundationBackendGlobalInfrastructureConnector {
    private string $foundationRoot;
    private string $infrastructureRoot;

    public function __construct() {
        $this->foundationRoot = __DIR__;
        $repositoryRoot = dirname(__DIR__, 4);
        $this->infrastructureRoot = $repositoryRoot . '/backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem';
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
        $foundation = $this->check($this->foundationRoot);
        $infrastructure = $this->check($this->infrastructureRoot);
        return [
            'name' => 'FRONTEND GLOBAL FOUNDATION - BACKEND GLOBAL INFRASTRUCTURE CONNECTOR',
            'foundation' => $foundation,
            'infrastructure' => $infrastructure,
            'connected' => $foundation['healthy'] && $infrastructure['healthy'],
            'connection_type' => 'filesystem contract check; not a runtime bridge',
        ];
    }
}
