# How the Zscaler Enrichment Script Works

This script integrates with the Zscaler API to enrich domains with URL categories, super categories, and risk scores. Zscaler uses a unique authentication method that requires hashing and session management, making it a more advanced API than typical threat intelligence services.

## 1. Authentication

Zscaler requires:
- Username
- Password
- API key
- A SHA-256 hash of (apiKey + username + password)

The script generates this hash and sends it to the `/authenticatedSession` endpoint to create a session.

## 2. Session-Based API Calls

Once authenticated, the script uses a persistent session to send requests. This mirrors how enterprise systems maintain authenticated state.

## 3. URL Category Lookup

The script calls:

      /urlLookup?url=<domain>

Zscaler returns:
- URL categories
- Super category
- Risk score

These fields help analysts understand how Zscaler classifies a domain.

## 4. Automation

The script reads domains from `domains.txt`, enriches each one, and prints structured JSON output.

## Summary

This script demonstrates:
- Hash-based authentication
- Session management
- Vendor-specific API logic
- URL categorization and risk scoring
- Real-world network security automation
