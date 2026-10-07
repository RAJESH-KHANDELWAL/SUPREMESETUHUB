from fastapi import FastAPI

from backend.supreme.personal_ai.api import router as supreme_personal_ai_router


app = FastAPI(
    title="SUPREMESETUHUB",
    version="1.0.0",
)


# ---------------------------------------------------------
# SUPREME PERSONAL AI
# ---------------------------------------------------------

app.include_router(
    supreme_personal_ai_router
)


# ---------------------------------------------------------
# HEALTH
# ---------------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "running",
        "system": "SUPREMESETUHUB",
    }


# ---------------------------------------------------------
# FOUNDATION
# ---------------------------------------------------------

@app.get("/api/v1/foundation")
def foundation():
    return {
        "name": "SUPREMESETUHUB",
        "version": "1.0.0",
        "status": "active",
    }
