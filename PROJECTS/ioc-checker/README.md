# IOC Checker: Threat Intelligence Automation

Automated IP reputation checker that integrates VirusTotal and AbuseIPDB APIs for rapid threat intelligence lookup during alert investigations.

## Features

Queries both VirusTotal and AbuseIPDB for IP reputation scoring.

Implements verdict logic: MALICIOUS (flagged by either API), SAFE (whitelisted), or LOW_RISK (low detection).

Fast API integration for real-time alert investigations.

Environment-based configuration for secure API key management.

## Requirements

Python 3.x
requests library
python-dotenv

## Setup

Install dependencies:

Create a .env file with your API keys:

Obtain free API keys from:
- VirusTotal: https://www.virustotal.com/gui/home/upload
- AbuseIPDB: https://www.abuseipdb.com/account/api

## Usage

Run the script with an IP address:

Output includes VirusTotal detection ratio, AbuseIPDB abuse score, and final verdict (MALICIOUS/SAFE/LOW_RISK).

## Example Output

## Testing

Tested against known benign IPs (8.8.8.8 - Google DNS) and malicious IPs. 100% accuracy on API integration.

