import os

from flask import Flask, jsonify, request
from supreme_config import (
    APP_NAME,
    PORT,
    SUPREME_ID,
    BUSINESS_ID,
    COMPANY_ID,
    PERSON_ID,
    USERNAME,
)
from identity_service import (
    get_supreme_profile,
    get_person_profile,
    search_entities,
)
from backend.auth.service import AuthenticationService

app = Flask(__name__)
authentication_service = AuthenticationService()

# CORS is browser policy, not authentication. Keep it limited to known
# SUPREME frontends; all private routes still require an authenticated owner.
DEFAULT_ALLOWED_ORIGINS = {
    "https://rajeshkhandelwal.github.io",
    "https://rajeshkhandelwalofficial.github.io",
    "https://drrajeshkhandelwalibc.github.io",
    "https://drrajeshkhandelwalibcofficial.github.io",
    "https://rajeshkhandelwal.com",
    "https://www.rajeshkhandelwal.com",
    "https://rajeshkhandelwalofficial.com",
    "https://www.rajeshkhandelwalofficial.com",
    "https://drrajeshkhandelwalibc.com",
    "https://www.drrajeshkhandelwalibc.com",
    "https://drrajeshkhandelwalibcofficial.com",
    "https://www.drrajeshkhandelwalibcofficial.com",
    "https://rajeshkhandelwal.onrender.com",
    "https://rajeshkhandelwalofficial.onrender.com",
    "https://drrajeshkhandelwalibc.onrender.com",
    "https://drrajeshkhandelwalibcofficial.onrender.com",
    "https://supremesetuhub-3v4e.onrender.com",
}
ALLOWED_ORIGINS = {
    origin.strip()
    for origin in os.getenv(
        "SUPREME_ALLOWED_ORIGINS",
        ",".join(sorted(DEFAULT_ALLOWED_ORIGINS)),
    ).split(",")
    if origin.strip()
}


@app.before_request
def require_supreme_owner():
    # A minimal health probe remains public for deployment monitoring.
    # It deliberately reveals no owner, identity, or business identifiers.
    if request.path == "/health":
        return None

    # Allow browser CORS preflight; the actual request remains protected.
    if request.method == "OPTIONS":
        return None

    authorization = request.headers.get("Authorization", "")
    if not authorization.startswith("Bearer "):
        return jsonify({
            "error": "AUTHENTICATION_REQUIRED",
            "message": "Sign in as the SUPREME owner to access private data.",
        }), 401

    token = authorization[len("Bearer "):].strip()
    result = authentication_service.validate_token(token)
    if not result.get("authenticated"):
        return jsonify({
            "error": "INVALID_OR_EXPIRED_TOKEN",
            "message": "A valid active session is required.",
        }), 401

    username = str(result.get("username", "")).strip()
    if username.casefold() != USERNAME.casefold():
        return jsonify({
            "error": "SUPREME_OWNER_ACCESS_REQUIRED",
            "message": "This private endpoint is restricted to the SUPREME owner.",
        }), 403

    return None


@app.after_request
def after_request(response):
    origin = request.headers.get("Origin")
    if origin and origin in ALLOWED_ORIGINS:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Vary"] = "Origin"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET,PUT,POST,DELETE,OPTIONS"
    return response


@app.get("/")
def root():
    return jsonify({
        "service": APP_NAME,
        "status": "running",
        "supreme_id": SUPREME_ID,
        "owner_person_id": PERSON_ID,
        "version": "1.0.0"
    }), 200


@app.get("/health")
def health():
    return jsonify({
        "service": APP_NAME,
        "status": "healthy",
    }), 200


@app.get("/supreme/status")
def supreme_status():
    profile = get_supreme_profile()
    return jsonify({
        "service": APP_NAME,
        "status": "active",
        "supreme_id": profile["supreme_id"],
        "owner_person_id": profile["owner_person_id"],
        "business_id": BUSINESS_ID,
        "company_id": COMPANY_ID,
        "role": profile["role"]
    }), 200


@app.get("/supreme/profile")
def supreme_profile():
    return jsonify(get_supreme_profile()), 200


@app.get("/supreme/person")
def supreme_person():
    return jsonify(get_person_profile()), 200


@app.get("/supreme/search")
def supreme_search():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"error": "Missing q query parameter"}), 400
    results = search_entities(q)
    return jsonify({"query": q, "results": results, "count": len(results)}), 200


@app.get("/supreme/persons")
def persons_list():
    return jsonify({"service": APP_NAME, "people": [get_person_profile()]}), 200


@app.get("/supreme/businesses")
def businesses_list():
    return jsonify({"service": APP_NAME, "businesses": [{
        "business_id": BUSINESS_ID,
        "owner_person_id": PERSON_ID,
        "supreme_id": SUPREME_ID,
        "name": "RAJESH KHANDELWAL OFFICIAL",
        "display_name": "👑 RAJESH KHANDELWAL OFFICIAL 👑"
    }]}), 200


@app.get("/supreme/companies")
def companies_list():
    return jsonify({"service": APP_NAME, "companies": [{
        "company_id": COMPANY_ID,
        "owner_person_id": PERSON_ID,
        "business_id": BUSINESS_ID,
        "supreme_id": SUPREME_ID,
        "name": "DR RAJESH KHANDELWAL IBC",
        "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑"
    }]}), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found", "message": "The requested endpoint does not exist"}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Server error", "message": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)
