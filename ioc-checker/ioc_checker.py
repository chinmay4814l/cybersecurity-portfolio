#!/usr/bin/env python3

import requests
import sys
from dotenv import load_dotenv
import os

load_dotenv()

VIRUSTOTAL_API_KEY = os.getenv("REMOVED_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("REMOVED_API_KEY")

def check_virustotal(indicator):
    """Check VirusTotal for IP reputation"""
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + indicator
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
            malicious = stats.get("malicious", 0)
            undetected = stats.get("undetected", 0)
            total = malicious + undetected
            
            return {
                "malicious": malicious,
                "total": total,
                "ratio": f"{malicious}/{total}"
            }
        else:
            return {"error": f"VirusTotal API returned status {response.status_code}"}
    except Exception as e:
        return {"error": f"VirusTotal error: {str(e)}"}

def check_abuseipdb(ip):
    """Check AbuseIPDB for IP reputation"""
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            abuse_score = data.get("data", {}).get("abuseConfidenceScore", 0)
            return {
                "abuse_score": abuse_score,
                "is_whitelisted": data.get("data", {}).get("isWhitelisted", False)
            }
        else:
            return {"error": f"AbuseIPDB API returned status {response.status_code}"}
    except Exception as e:
        return {"error": f"AbuseIPDB error: {str(e)}"}

def verdict(indicator, vt_data, aip_data):
    """Determine if IP is malicious based on both APIs"""
    
    print("\n" + "="*50)
    print("IOC CHECKER REPORT")
    print(f"Indicator: {indicator}")
    print("="*50)
    
    # VirusTotal verdict
    if "error" not in vt_data:
        print(f"\n✓ VirusTotal: {vt_data['ratio']} vendors flagged as malicious")
    else:
        print(f"\n✗ VirusTotal: {vt_data.get('error')}")
    
    # AbuseIPDB verdict
    if "error" not in aip_data:
        score = aip_data["abuse_score"]
        print(f"✓ AbuseIPDB: {score}% abuse confidence score")
        
        if aip_data["is_whitelisted"]:
            print("   ✓ IP is whitelisted (trusted)")
    else:
        print(f"✗ AbuseIPDB: {aip_data.get('error')}")
    
    # Final verdict
    print("\n" + "-"*50)
    
    # Safe handling of errors
    vt_malicious = vt_data.get("malicious", 0) > 0 if "error" not in vt_data else False
    aip_dangerous = aip_data.get("abuse_score", 0) >= 75 if "error" not in aip_data else False
    is_whitelisted = aip_data.get("is_whitelisted", False) if "error" not in aip_data else False
    
    if vt_malicious or aip_dangerous:
        print("🚨 VERDICT: SUSPICIOUS/MALICIOUS - BLOCK THIS IP")
    elif is_whitelisted:
        print("✅ VERDICT: SAFE - IP is whitelisted")
    else:
        print("⚠️ VERDICT: LOW RISK - Monitor")
    print("="*50 + "\n")

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python3 ioc_checker.py <IP_ADDRESS>")
        print("Example: python3 ioc_checker.py 203.0.113.5")
        sys.exit(1)
    
    indicator = sys.argv[1]
    print(f"\n[*] Checking {indicator}...\n")
    
    # Query both APIs
    vt_result = check_virustotal(indicator)
    aip_result = check_abuseipdb(indicator)
    
    # Show verdict
    verdict(indicator, vt_result, aip_result)

if __name__ == "__main__":
    main()
