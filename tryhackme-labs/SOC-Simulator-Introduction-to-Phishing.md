# SOC Simulator: Introduction to Phishing

**Scenario:** Phishing attack investigation with 5 alerts

## Summary
- Total Alerts: 5
- True Positives: 2
- False Positives: 3
- Duration: ~1 hour

## Alerts Investigated

### Alert 8816 (Email)
- **Type:** Inbound Email - Suspicious Link
- **Verdict:** FALSE POSITIVE
- **Reason:** Email detected but user didn't access malicious domain

### Alert 8817 (Email) 
- **Type:** Inbound Email - Suspicious Link
- **Verdict:** TRUE POSITIVE
- **Reason:** Phishing email + User clicked link + Credentials at risk

### Alert 8815 (Email)
- **Type:** Inbound Email - Fake Amazon
- **Verdict:** FALSE POSITIVE
- **Reason:** Email blocked, user didn't click

### Alert 8818 (Email)
- **Type:** Inbound Email - HR Onboarding
- **Verdict:** TRUE POSITIVE
- **Reason:** Phishing campaign targeting employee

### Alert 8819 (Firewall)
- **Type:** Firewall - Blacklisted URL Blocked
- **Verdict:** TRUE POSITIVE (Contained)
- **Reason:** User attempted access to blacklisted domain, firewall blocked it

## Key Learnings
1. Always check MULTIPLE log sources (email, firewall, proxy, DNS)
2. TP vs FP depends on whether user actually clicked/accessed
3. Even blocked threats are TRUE POSITIVE if malicious intent exists
4. Document all entities: sender, recipient, domain, IPs, URLs
