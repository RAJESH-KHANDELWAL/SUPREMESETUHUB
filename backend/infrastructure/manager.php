<?php
/** Backend Infrastructure canonical-module structural manager. */
final class BackendInfrastructureManager {
    public const NAME = 'BACKEND INFRASTRUCTURE';
    public const VERSION = '1.1.0';
    public function health(): array {
        $root = __DIR__;
        $global = $root . '/global_ecosystem';
        $ecosystem = $global . '/global_infrastructure_ecosystem';
        $modules = $ecosystem . '/modules';
        $required = ['controller.py','repository.py','service.py','hostinger_catalog.py','__init__.py'];
        $checks = [];
        foreach ($required as $name) { $checks['canonical_module_' . $name] = is_file($modules . '/' . $name); }
        $checks['root_compatibility_package'] = is_file($root . '/__init__.py');
        $checks['global_ecosystem'] = is_dir($global);
        $backendGlobal = dirname($root) . '/global_ecosystem';
        $checks['backend_global_hostinger_api'] = is_file($backendGlobal . '/global_hosting_ecosystem/hostinger_api.py');
        $checks['backend_global_nsfwinfra'] = is_file($backendGlobal . '/nsfwinfra_ecosystem/nsfwinfra.py');
        $checks['global_infrastructure_manager'] = is_file($ecosystem . '/manager.py');
        $healthy = !in_array(false, $checks, true);
        return ['name'=>self::NAME,'version'=>self::VERSION,'status'=>$healthy?'READY':'INCOMPLETE',
                'checks'=>$checks,'healthy'=>$healthy,'provider_operations_enabled'=>false];
    }
}
