import requests
import json

API_KEY = "YOUR_API_KEY_HERE"
VT_URL = "https://www.virustotal.com/api/v3/urls"

def lookup_url(url):
    # VirusTotal requires URL to be base64 encoded (without padding)
    import base64
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

    headers = {
        "x-apikey": API_KEY
    }

    response = requests.get(f"{VT_URL}/{url_id}", headers=headers)

    if response.status_code != 200:
        return {"error": f"Request failed: {response.status_code}"}

    data = response.json()

    return {
        "url": url,
        "malicious_votes": data["data"]["attributes"]["last_analysis_stats"]["malicious"],
        "harmless_votes": data["data"]["attributes"]["last_analysis_stats"]["harmless"],
        "suspicious_votes": data["data"]["attributes"]["last_analysis_stats"]["suspicious"],
        "categories": data["data"]["attributes"].get("categories", {})
    }

# Example usage
test_url = "http://example.com"
result = lookup_url(test_url)
print(json.dumps(result, indent=4))
