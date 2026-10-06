#!/usr/bin/env python3

import re
from collections import defaultdict

# Read log file
log_file = "test.log"

failed_logins = defaultdict(int)
ips = defaultdict(list)

with open(log_file, 'r') as f:
    for line in f:
        # Look for failed login attempts
        if "Failed password" in line or "Invalid user" in line:
            # Extract IP address
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip = match.group(1)
                failed_logins[ip] += 1
                ips[ip].append(line.strip())

# Detect brute force (5+ attempts = brute force)
brute_forcers = {ip: count for ip, count in failed_logins.items() if count >= 5}

print(f"\n=== LOG PARSER REPORT ===")
print(f"Total unique IPs with failed logins: {len(failed_logins)}")
print(f"Brute force attackers (5+ attempts): {len(brute_forcers)}\n")

for ip, count in sorted(brute_forcers.items(), key=lambda x: x[1], reverse=True):
    print(f"IP: {ip} | Failed Attempts: {count}")
