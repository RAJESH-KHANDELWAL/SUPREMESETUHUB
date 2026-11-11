"""GitHub product and API capability catalog; metadata only."""
from .models import Capability

CAPABILITIES = (
    Capability("repositories", "Repositories", "source_control", "Repository metadata, contents, branches, tags, and visibility.", ("repository", "branch", "tag"), destructive=True),
    Capability("git_data", "Git Data", "source_control", "Blobs, trees, commits, refs, and commit comparison.", ("blob", "tree", "commit", "ref"), destructive=True),
    Capability("pull_requests", "Pull Requests", "collaboration", "Create, inspect, review, update, and merge pull requests.", ("pull_request", "review", "review_thread"), destructive=True),
    Capability("issues_projects", "Issues and Projects", "planning", "Issues, labels, milestones, project workflows, and discussions.", ("issue", "label", "milestone", "project"), destructive=True),
    Capability("actions", "GitHub Actions", "automation", "Workflow definitions, runs, jobs, artifacts, and logs.", ("workflow", "run", "job", "artifact"), destructive=True),
    Capability("packages", "GitHub Packages", "distribution", "Package and container registry metadata and lifecycle.", ("package", "container_image"), destructive=True),
    Capability("security", "Code Security", "security", "Dependabot alerts, code scanning, secret scanning, and advisories.", ("alert", "advisory"), destructive=True),
    Capability("webhooks", "Webhooks", "integration", "Webhook configuration and delivery events.", ("webhook",), destructive=True),
    Capability("apps_oauth", "GitHub Apps and OAuth", "identity", "App installation metadata, permissions, and authorization contracts.", ("app_installation", "oauth_grant")),
    Capability("teams_access", "Teams and Access", "governance", "Team membership, repository roles, rulesets, and access governance.", ("team", "collaborator", "ruleset"), destructive=True),
    Capability("search", "Code and Repository Search", "discovery", "Search repositories, code, commits, issues, and pull requests.", ("search_query",)),
    Capability("releases", "Releases", "delivery", "Release metadata, tags, and downloadable assets.", ("release", "release_asset"), destructive=True),
    Capability("discussions_wiki", "Discussions and Wikis", "collaboration", "Community discussions and repository knowledge spaces.", ("discussion", "wiki_page"), destructive=True),
    Capability("gists", "Gists", "sharing", "Create and manage versioned code snippets.", ("gist",), destructive=True),
    Capability("enterprise", "Enterprise Administration", "enterprise", "Enterprise-level policy and organization governance metadata.", ("enterprise", "organization")),
    Capability("billing_usage", "Billing and Usage", "administration", "Plan, metered usage, and billing metadata where authorized.", ("billing_record", "usage_metric")),
    Capability("audit_compliance", "Audit and Compliance", "governance", "Audit events, repository policy, attestations, and compliance evidence.", ("audit_event", "attestation")),
)
CAPABILITY_BY_ID = {item.id: item for item in CAPABILITIES}

def list_capabilities(category=None):
    items = CAPABILITIES if category is None else tuple(x for x in CAPABILITIES if x.category == category)
    return [item.to_dict() for item in items]

def get_capability(capability_id):
    item = CAPABILITY_BY_ID.get(capability_id)
    return item.to_dict() if item else None

def search_capabilities(query):
    needle = (query or "").strip().casefold()
    if not needle:
        return []
    return [item.to_dict() for item in CAPABILITIES if needle in " ".join(
        (item.id, item.name, item.category, item.description, *item.resource_types)
    ).casefold()]
