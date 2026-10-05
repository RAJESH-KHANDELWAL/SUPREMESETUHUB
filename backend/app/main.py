from fastapi import FastAPI


app = FastAPI(
    title="SUPREMESETUHUB",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {
        "status": "running"
    }


@app.get("/api/v1/foundation")
def foundation():
    return {
        "name": "SUPREMESETUHUB",
        "version": "1.0.0",
        "status": "active",
    }
