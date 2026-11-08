"""Metadata catalog for database infrastructure providers."""
from copy import deepcopy

PROVIDERS = [
    {"provider_id":"google","name":"Google Cloud database services","products":["Cloud SQL","AlloyDB","Spanner","Firestore","Bigtable"],"status":"not_configured"},
    {"provider_id":"aws","name":"AWS database services","products":["RDS","Aurora","DynamoDB","DocumentDB","ElastiCache"],"status":"not_configured"},
    {"provider_id":"microsoft","name":"Microsoft database services","products":["Azure SQL","Cosmos DB","Azure Database for PostgreSQL","Managed Instance"],"status":"not_configured"},
    {"provider_id":"oracle","name":"Oracle database services","products":["Autonomous Database","Base Database Service","MySQL HeatWave"],"status":"not_configured"},
    {"provider_id":"digitalocean","name":"DigitalOcean database services","products":["Managed PostgreSQL","Managed MySQL","Managed Valkey","Managed MongoDB"],"status":"not_configured"},
    {"provider_id":"mongodb","name":"MongoDB database services","products":["MongoDB Atlas"],"status":"not_configured"},
    {"provider_id":"supabase","name":"Supabase database services","products":["Managed PostgreSQL","Realtime"],"status":"not_configured"},
    {"provider_id":"neon","name":"Neon database services","products":["Serverless PostgreSQL"],"status":"not_configured"},
]

def list_providers():
    return deepcopy(PROVIDERS)

def get_provider(provider_id):
    key = str(provider_id).strip().lower()
    for provider in PROVIDERS:
        if provider["provider_id"] == key:
            return deepcopy(provider)
    raise KeyError(f"Unknown database provider: {provider_id!r}")
