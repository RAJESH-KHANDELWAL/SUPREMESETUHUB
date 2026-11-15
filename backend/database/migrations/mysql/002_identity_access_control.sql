-- Identity-level RBAC for the one central SUPREMESETUHUB database.
-- Apply only after reviewing 001_identity_gate_foundation.sql and taking a backup.
-- This migration creates authorization metadata; it does not create user accounts
-- or grant access automatically.

CREATE TABLE IF NOT EXISTS ss_identity_principal_roles (
    principal_id VARCHAR(190) NOT NULL,
    identity_code VARCHAR(80) NOT NULL,
    role_code VARCHAR(64) NOT NULL,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (principal_id, identity_code, role_code),
    KEY idx_ss_identity_roles_identity (identity_code, is_active),
    CONSTRAINT fk_ss_identity_roles_identity
        FOREIGN KEY (identity_code) REFERENCES ss_identity_gates(identity_code)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS ss_identity_role_permissions (
    role_code VARCHAR(64) NOT NULL,
    permission_code VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (role_code, permission_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Standard role definitions only. No principal is assigned a role by this migration.
INSERT INTO ss_identity_role_permissions (role_code, permission_code) VALUES
    ('OWNER', 'IDENTITY.READ'),
    ('OWNER', 'IDENTITY.MANAGE'),
    ('OWNER', 'DATA.READ'),
    ('OWNER', 'DATA.WRITE'),
    ('OWNER', 'USERS.MANAGE'),
    ('ADMIN', 'IDENTITY.READ'),
    ('ADMIN', 'DATA.READ'),
    ('ADMIN', 'DATA.WRITE'),
    ('ADMIN', 'USERS.MANAGE'),
    ('EDITOR', 'IDENTITY.READ'),
    ('EDITOR', 'DATA.READ'),
    ('EDITOR', 'DATA.WRITE'),
    ('VIEWER', 'IDENTITY.READ'),
    ('VIEWER', 'DATA.READ')
ON DUPLICATE KEY UPDATE permission_code = VALUES(permission_code);
