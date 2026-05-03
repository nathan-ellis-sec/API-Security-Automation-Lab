import requests
import json

API_TOKEN = "YOUR_API_TOKEN_HERE"
IPINFO_URL = "https://ipinfo.io"

def enrich_ip(ip):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

    response = requests.get(f"{IPINFO_URL}/{ip}/json", headers=headers)

    if response.status_code != 200:
        return {"ip": ip, "error": response.status_code}

    data = response.json()

    # Extract fields safely using .get()
    return {
        "ip": ip,
        "asn": data.get("asn", {}).get("asn"),
        "asn_org": data.get("asn", {}).get("name"),
        "country": data.get("country"),
        "region": data.get("region"),
        "city": data.get("city"),
        "latitude": data.get("loc", "").split(",")[0] if "loc" in data else None,
        "longitude": data.get("loc", "").split(",")[1] if "loc" in data else None,
        "company": data.get("company", {}).get("name"),
        "privacy": data.get("privacy", {}),
        "hostname": data.get("hostname"),
        "anycast": data.get("anycast")
    }

# Automation: read IPs from a file
with open("ips.txt") as f:
    ips = [line.strip() for line in f.readlines()]

for ip in ips:
    result = enrich_ip(ip)
    print(json.dumps(result, indent=4))
