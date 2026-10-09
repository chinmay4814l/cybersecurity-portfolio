# Incident Report — SSH Brute Force Attack

**Date:** 09-10-2026  
**Analyst:** Chinmaya Jal  
**Severity:** Medium  
**Status:** Resolved  

---

## 1. Summary
A brute force attack was detected against the SSH service on host CHINMAYA123. 
The attacker made 240 failed login attempts over approximately 7 minutes targeting 
the root account. The attack was detected using Splunk SIEM with auth.log ingestion.

---

## 2. Timeline
| Time | Event |
|------|-------|
| 06:46:25 AM | First failed SSH login attempt detected |
| 06:46 - 06:53 AM | Continuous brute force attempts (240 total) |
| 06:53:28 AM | Last failed attempt recorded |
| — | No successful login at any point |

---

## 3. Indicators of Compromise (IOCs)
| IOC | Value |
|-----|-------|
| Attacker IP | 127.0.0.1 |
| Target User | root |
| Target Port | 22 (SSH) |
| Attack Tool | Hydra |
| Total Attempts | 240 |

---

## 4. Detection
- **SIEM:** Splunk Enterprise
- **Log Source:** /var/log/auth.log (sourcetype: linux_secure)
- **Detection Logic:** Failed password count > 10 from single IP within timeframe

**SPL Query Used:**
index=* sourcetype=linux_secure “Failed password”
| rex field=_raw “from (?P<src_ip>\d+.\d+.\d+.\d+)”
| stats count by src_ip
| where count > 10
| sort -count


**Result:** 127.0.0.1 flagged with 240 failed attempts

---

## 5. Investigation
- Searched for successful logins after brute force — none found
- Attack was sustained and consistent (visible in timeline chart)
- All attempts targeted root account via SSH port 22
- No lateral movement or privilege escalation detected

---

## 6. Verdict
**True Positive — Brute Force Attack Confirmed**  
Attack was unsuccessful. No unauthorized access gained.

---

## 7. Recommendations
1. Block attacker IP at firewall level immediately
2. Disable root SSH login (`PermitRootLogin no` in sshd_config)
3. Install and configure fail2ban to auto-block brute force IPs
4. Switch to SSH key-based authentication only
5. Alert threshold: flag any IP with >10 failed logins in 5 minutes

---

## 8. Evidence
- `01_brute_force_events_detected.png` — 240 failed password events in Splunk
- `02_brute_force_detection_query.png` — Detection query flagging 127.0.0.1
- `03_brute_force_timeline.png` — Attack timeline visualization