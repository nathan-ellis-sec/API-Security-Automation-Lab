import requests
import hashlib
import json
import time

# -----------------------------
# Zscaler API Credentials
# -----------------------------
ZSCALER_USERNAME = "YOUR_USERNAME"
ZSCALER_PASSWORD = "YOUR_PASSWORD"
ZSCALER_API_KEY = "YOUR_API_KEY"
ZSCALER_BASE_URL = "https://admin.zscaler.net/api/v1"

# -----------------------------
# Helper: Generate the Zscaler Auth Hash
# -----------------------------
def generate_auth_hash(api_key, username, password):
    """
    Zscaler requires a special SHA-256 hash for authentication.
    The formula is: SHA256(api_key + username + password)
    """
    raw = api_key + username + password
    return hashlib.sha256(raw.encode()).hexdigest()

# -----------------------------
# Authenticate and Create Session
# -----------------------------
def zscaler_login():
    auth_hash = generate_auth_hash(ZSCALER_API_KEY, ZSCALER_USERNAME, ZSCALER_PASSWORD)

    payload = {
        "username": ZSCALER_USERNAME,
        "password": ZSCALER_PASSWORD,
        "apiKey": ZSCALER_API_KEY,
        "authHash": auth_hash
    }

    session = requests.Session()
    response = session.post(f"{ZSCALER_BASE_URL}/authenticatedSession", json=payload)

    if response.status_code != 200:
        print("Login failed:", response.text)
        return None

    print("Zscaler session created.")
    return session

# -----------------------------
# Enrich a Domain via URL Category Lookup
# -----------------------------
def enrich_domain(session, domain):
    response = session.get(f"{ZSCALER_BASE_URL}/urlLookup?url={domain}")

    if response.status_code != 200:
        return {"domain": domain, "error": response.status_code}

    data = response.json()

    return {
        "domain": domain,
        "categories": data[0].get("urlClassifications", []),
        "super_category": data[0].get("superCategory", "Unknown"),
        "risk_score": data[0].get("riskScore", "Unknown")
    }

# -----------------------------
# Automation: Read Domains from File
# -----------------------------
def main():
    session = zscaler_login()
    if not session:
        return

    with open("domains.txt") as f:
        domains = [line.strip() for line in f.readlines()]

    for domain in domains:
        result = enrich_domain(session, domain)
        print(json.dumps(result, indent=4))

    # Logout cleanly
    session.delete(f"{ZSCALER_BASE_URL}/authenticatedSession")
    print("Zscaler session closed.")

if __name__ == "__main__":
    main()
