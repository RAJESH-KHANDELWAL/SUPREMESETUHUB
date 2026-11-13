-- SUPREMESETUHUB multi-tenant infrastructure foundation
-- Target: MySQL 8+ / compatible MariaDB with InnoDB.
-- Safe-by-design: creates only ss_* tables; does not alter WordPress tables.
-- This file is a reviewed migration artifact. It is NOT auto-executed by application startup.
-- Generate UUIDs in the application and never store raw FTP/database passwords here.

CREATE TABLE IF NOT EXISTS ss_identity_gates (
    gate_code VARCHAR(64) NOT NULL,
    gate_label VARCHAR(160) NOT NULL,
    gate_type ENUM('MAIN', 'IDENTITY') NOT NULL DEFAULT 'IDENTITY',
    status ENUM('ACTIVE', 'DISABLED') NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (gate_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO ss_identity_gates (gate_code, gate_label, gate_type) VALUES
    ('SUPREMESETUHUB', 'SUPREMESETUHUB Main', 'MAIN'),
    ('RAJESHKHANDELWALOFFICIAL', 'RAJESHKHANDELWALOFFICIAL', 'IDENTITY'),
    ('RAJESHKHANDELWAL', 'RAJESHKHANDELWAL', 'IDENTITY'),
    ('DRRAJESHKHANDELWALIBCOFFICIAL', 'DRRAJESHKHANDELWALIBCOFFICIAL', 'IDENTITY'),
    ('DRRAJESHKHANDELWALIBC', 'DRRAJESHKHANDELWALIBC', 'IDENTITY')
ON DUPLICATE KEY UPDATE
    gate_label = VALUES(gate_label),
    gate_type = VALUES(gate_type);

CREATE TABLE IF NOT EXISTS ss_tenants (
    tenant_id CHAR(36) NOT NULL,
    tenant_name VARCHAR(190) NOT NULL,
    tenant_type ENUM('INDIVIDUAL', 'BUSINESS', 'ORGANIZATION') NOT NULL DEFAULT 'INDIVIDUAL',
    owner_user_ref VARCHAR(128) NOT NULL,
    status ENUM('PENDING', 'ACTIVE', 'SUSPENDED', 'CLOSED') NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (tenant_id),
    KEY idx_ss_tenants_owner (owner_user_ref),
    KEY idx_ss_tenants_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS ss_tenant_memberships (
    membership_id CHAR(36) NOT NULL,
    tenant_id CHAR(36) NOT NULL,
    user_ref VARCHAR(128) NOT NULL,
    gate_code VARCHAR(64) NOT NULL,
    member_role ENUM('OWNER', 'ADMIN', 'OPERATOR', 'VIEWER') NOT NULL DEFAULT 'VIEWER',
    status ENUM('INVITED', 'ACTIVE', 'REVOKED') NOT NULL DEFAULT 'INVITED',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (membership_id),
    UNIQUE KEY uq_ss_membership (tenant_id, user_ref, gate_code),
    KEY idx_ss_membership_user (user_ref, status),
    CONSTRAINT fk_ss_membership_tenant FOREIGN KEY (tenant_id)
        REFERENCES ss_tenants (tenant_id) ON DELETE CASCADE,
    CONSTRAINT fk_ss_membership_gate FOREIGN KEY (gate_code)
        REFERENCES ss_identity_gates (gate_code) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS ss_domains (
    domain_id CHAR(36) NOT NULL,
    tenant_id CHAR(36) NOT NULL,
    domain_name VARCHAR(253) NOT NULL,
    registrar VARCHAR(120) NULL,
    expires_at DATE NULL,
    verification_status ENUM('UNVERIFIED', 'PENDING', 'VERIFIED', 'FAILED') NOT NULL DEFAULT 'UNVERIFIED',
    status ENUM('ACTIVE', 'EXPIRED', 'DISCONNECTED', 'CLOSED') NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (domain_id),
    UNIQUE KEY uq_ss_domain_name (domain_name),
    KEY idx_ss_domains_tenant (tenant_id, status),
    CONSTRAINT fk_ss_domains_tenant FOREIGN KEY (tenant_id)
        REFERENCES ss_tenants (tenant_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS ss_hosting_accounts (
    hosting_account_id CHAR(36) NOT NULL,
    tenant_id CHAR(36) NOT NULL,
    provider VARCHAR(120) NOT NULL,
    account_label VARCHAR(190) NOT NULL,
    external_account_ref VARCHAR(190) NULL,
    control_panel_url VARCHAR(500) NULL,
    ownership_confirmed TINYINT(1) NOT NULL DEFAULT 0,
    status ENUM('PENDING', 'ACTIVE', 'DISCONNECTED', 'SUSPENDED') NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (hosting_account_id),
    KEY idx_ss_hosting_tenant (tenant_id, status),
    CONSTRAINT fk_ss_hosting_tenant FOREIGN KEY (tenant_id)
        REFERENCES ss_tenants (tenant_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS ss_ftp_connections (
    ftp_connection_id CHAR(36) NOT NULL,
    tenant_id CHAR(36) NOT NULL,
    hosting_account_id CHAR(36) NOT NULL,
    profile_label VARCHAR(160) NOT NULL,
    protocol ENUM('FTPS', 'SFTP') NOT NULL,
    hostname VARCHAR(253) NOT NULL,
    port SMALLINT UNSIGNED NOT NULL,
    username VARCHAR(190) NOT NULL,
    root_directory VARCHAR(500) NOT NULL,
    credential_secret_ref VARCHAR(500) NOT NULL COMMENT 'Vault/secret-manager reference only; never a password',
    status ENUM('PENDING', 'ACTIVE', 'REVOKED', 'FAILED') NOT NULL DEFAULT 'PENDING',
    last_verified_at TIMESTAMP NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ftp_connection_id),
    KEY idx_ss_ftp_tenant (tenant_id, status),
    CONSTRAINT fk_ss_ftp_tenant FOREIGN KEY (tenant_id)
        REFERENCES ss_tenants (tenant_id) ON DELETE CASCADE,
    CONSTRAINT fk_ss_ftp_hosting FOREIGN KEY (hosting_account_id)
        REFERENCES ss_hosting_accounts (hosting_account_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS ss_database_connections (
    db_connection_id CHAR(36) NOT NULL,
    tenant_id CHAR(36) NOT NULL,
    hosting_account_id CHAR(36) NOT NULL,
    provider VARCHAR(120) NOT NULL,
    hostname VARCHAR(253) NOT NULL,
    port SMALLINT UNSIGNED NOT NULL,
    database_name VARCHAR(190) NOT NULL,
    username VARCHAR(190) NOT NULL,
    access_mode ENUM('READ_ONLY', 'READ_WRITE', 'ADMIN') NOT NULL DEFAULT 'READ_ONLY',
    credential_secret_ref VARCHAR(500) NOT NULL COMMENT 'Vault/secret-manager reference only; never a password',
    status ENUM('PENDING', 'ACTIVE', 'REVOKED', 'FAILED') NOT NULL DEFAULT 'PENDING',
    last_verified_at TIMESTAMP NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (db_connection_id),
    KEY idx_ss_dbconn_tenant (tenant_id, status),
    CONSTRAINT fk_ss_dbconn_tenant FOREIGN KEY (tenant_id)
        REFERENCES ss_tenants (tenant_id) ON DELETE CASCADE,
    CONSTRAINT fk_ss_dbconn_hosting FOREIGN KEY (hosting_account_id)
        REFERENCES ss_hosting_accounts (hosting_account_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS ss_deployment_targets (
    deployment_target_id CHAR(36) NOT NULL,
    tenant_id CHAR(36) NOT NULL,
    domain_id CHAR(36) NOT NULL,
    ftp_connection_id CHAR(36) NOT NULL,
    repository_full_name VARCHAR(190) NOT NULL,
    branch_name VARCHAR(190) NOT NULL DEFAULT 'main',
    remote_path VARCHAR(500) NOT NULL,
    approval_required TINYINT(1) NOT NULL DEFAULT 1,
    status ENUM('PENDING', 'ACTIVE', 'PAUSED', 'REVOKED') NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (deployment_target_id),
    KEY idx_ss_deploy_tenant (tenant_id, status),
    CONSTRAINT fk_ss_deploy_tenant FOREIGN KEY (tenant_id)
        REFERENCES ss_tenants (tenant_id) ON DELETE CASCADE,
    CONSTRAINT fk_ss_deploy_domain FOREIGN KEY (domain_id)
        REFERENCES ss_domains (domain_id) ON DELETE CASCADE,
    CONSTRAINT fk_ss_deploy_ftp FOREIGN KEY (ftp_connection_id)
        REFERENCES ss_ftp_connections (ftp_connection_id) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS ss_audit_logs (
    audit_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    tenant_id CHAR(36) NULL,
    actor_ref VARCHAR(128) NOT NULL,
    action VARCHAR(120) NOT NULL,
    resource_type VARCHAR(120) NOT NULL,
    resource_ref VARCHAR(190) NULL,
    outcome ENUM('SUCCESS', 'DENIED', 'FAILED') NOT NULL,
    details_redacted TEXT NULL COMMENT 'Do not log passwords, tokens, private keys or full connection strings',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (audit_id),
    KEY idx_ss_audit_tenant_time (tenant_id, created_at),
    KEY idx_ss_audit_actor_time (actor_ref, created_at),
    CONSTRAINT fk_ss_audit_tenant FOREIGN KEY (tenant_id)
        REFERENCES ss_tenants (tenant_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
