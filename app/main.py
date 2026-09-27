from fastapi import FastAPI
from app.routers.identities import router as identities_router

app = FastAPI(
    title="SUPREMESETUHUB",
    version="0.1.0",
    description=(
        "SUPREMESETUHUB MAIN BASE FOUNDATION "
        "AND CENTRAL DIGITAL ECOSYSTEM"
    ),
)

# USER_ID SYSTEM V1
app.include_router(identities_router)


@app.get("/")
def root():
    return {
        "success": True,
        "name": "SUPREMESETUHUB",
        "version": "0.1.0",
        "message": "MAIN BASE FOUNDATION AND CENTRAL DIGITAL ECOSYSTEM",
    }


@app.get("/health")
def health():
    return {
        "success": True,
        "status": "running",
    }


@app.get("/api/v1/foundation")
def foundation():
    return {
        "success": True,
        "name": "SUPREMESETUHUB MAIN BASE FOUNDATION",
        "version": "1.0.0",
        "status": "active",
    }
