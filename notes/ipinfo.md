# IPinfo IP Enrichment Script

This script enriches IP addresses using the IPinfo API. It retrieves detailed information about an IP, including ASN, geolocation, privacy indicators, and company ownership. This type of enrichment is commonly used in SOC investigations, Zero Trust decisions, and threat hunting workflows.

## What the Script Does

- Accepts one or many IP addresses  
- Sends each IP to the IPinfo API  
- Extracts key intelligence fields:
  - ASN (Autonomous System Number)
  - Organization name
  - Country, region, city
  - Latitude and longitude
  - Hostname
  - Company information
  - Privacy flags (VPN, proxy, hosting provider, TOR)
  - Anycast status
- Outputs structured JSON for each IP
- Automates enrichment by reading IPs from `ips.txt`

## Why This Matters

IP enrichment is a core part of security engineering. It helps analysts:

- Identify suspicious or foreign IPs  
- Determine whether an IP belongs to a cloud provider  
- Detect VPNs, proxies, or anonymizers  
- Understand geographic patterns  
- Add context to SIEM alerts  
- Support Zero Trust access decisions  

This script demonstrates my ability to:

- Authenticate using Bearer tokens  
- Work with REST APIs  
- Parse nested JSON structures  
- Build reusable enrichment functions  
- Automate analysis across multiple inputs  

## Key Takeaways

- IPinfo returns more complex data than VirusTotal, making this a medium‑difficulty API  
- Privacy flags (VPN, proxy, hosting) are extremely useful in real investigations  
- ASN and company data help identify cloud infrastructure vs. residential IPs  
- Automating enrichment across many IPs mirrors real SOC workflows  
