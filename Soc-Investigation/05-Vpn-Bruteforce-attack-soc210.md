# SOC210: VPN Brute Force Attack

**Platform:** LetsDefend | **Event ID:** 162 | **Difficulty:** Medium
**Alert type:** Brute Force | **Severity:** High
**Alert time:** 2023-06-21 13:43:00 UTC (first attempt)
**Verdict:** True Positive. The exploit succeeded, but the account is a test account.

## 1. Summary
An alert fired for a brute force attack on the VPN service. An external attacker tried five
different usernames over about 8 minutes. On the 5th attempt, they guessed the correct
password for mane@letsdefend.io and got in. I confirmed the attack, scoped it, and
recommended containment. This taught me why timing and username patterns matter.

## 2. What I looked at first
- **Source IP:** 37.19.221.229 is public, so it is external.
- **Destination IP:** 33.33.33.33 is the VPN host.
- **Direction:** Internet -> Company Network (inbound).
- **Rule name:** SOC210 says "Possible Brute Force Detected on VPN," so my hypothesis
  was repeated login attempts leading to a successful login.

## 3. Threat Intel check
I checked the source IP on VirusTotal, AbuseIPDB, and LetsDefend Threat Intelligence.

- **VirusTotal:** no malicious detections.
- **AbuseIPDB:** abuse confidence score 14% (low).
- **LetsDefend Threat Intelligence:** no intelligence available.

The IP had a weak reputation, so I could not rely on that alone. I moved to the logs.

## 4. Authentication log analysis
I searched VPN logs for the source IP 37.19.221.229.

**Failed attempts:**
- First attempt: 2023-06-21 13:43 UTC (sane@letsdefend.io)
- Second attempt: 13:45 UTC (zane@letsdefend.io)
- Third attempt: 13:46 UTC (fane@letsdefend.io)
- Fourth attempt: 13:48 UTC (tane@letsdefend.io)
- Fifth attempt: 13:50 UTC (mane@letsdefend.io) — **failed**

**Successful attempt:**
- 2023-06-21 13:51 UTC (mane@letsdefend.io) — **success**

The attacker tried five different usernames in about 8 minutes. This is a common pattern
called **username enumeration** or **password spraying**. They used the same password
against different usernames until it worked.

## 5. Attack pattern
The sequence matters:

| Time | Username | Result |
|------|----------|--------|
| 13:43 | sane@ | Failed |
| 13:45 | zane@ | Failed |
| 13:46 | fane@ | Failed |
| 13:48 | tane@ | Failed |
| 13:50 | mane@ | Failed |
| 13:51 | mane@ | **Success** |

The attacker found the right username (mane@) and tried the password twice. The second
attempt succeeded. This tells me they either guessed the right password, or the account
has a weak password.

## 6. Scope and post-login investigation
I searched the logs for what mane@letsdefend.io did *after* the successful login.

**Finding:** No post-login activity was recorded in the available logs. This gap was not
covered in the LetsDefend playbook, so I did not investigate further during this lab.
In a real SOC, I would check file access logs, database connection logs, and VPN session
duration to confirm whether the attacker remained connected or accessed sensitive data.

I also searched for lateral movement: did the attacker use mane@letsdefend.io to reach
other internal systems?

**Finding:** No evidence of lateral movement to other hosts was observed in the logs
reviewed.

**Account details:** mane@letsdefend.io is a **test account** created for this LetsDefend
lab simulation. In a real environment, I would check the account's privilege level, group
memberships, and whether it is an active user or a service account.

## 7. Confirmed vs. unknown
| Finding | Status |
|---------|--------|
| Brute force attack occurred | Confirmed |
| 5 usernames were tried | Confirmed |
| Successful login for mane@ | Confirmed |
| Password spraying pattern | Confirmed |
| Post-login actions | Not investigated (not in playbook) |
| Lateral movement | No activity found in logs |
| Account privilege level | Not investigated (not in playbook) |
| Attacker identity | Unknown |

## 8. MITRE ATT&CK (mapped from evidence only)
- T1110: Brute Force (repeated authentication attempts)
- T1110.001: Password Guessing (trying different passwords against different usernames)
- T1133: External Remote Services (VPN is externally accessible)

## 9. Containment and response
**Done in the lab:** marked as True Positive and recommended containment.

**Recommended immediate actions:**
1. Reset the password for mane@letsdefend.io (it is weak if it was guessed in 8 minutes).
2. Check if this account has been used for legitimate access recently. If not, disable it.
3. Review the VPN session logs to see if the attacker stayed logged in and for how long.
4. Check if any files or resources were accessed by mane@letsdefend.io during or after
   the 13:51 UTC login.

**Recommended long-term:**
1. Implement multi-factor authentication (MFA) on VPN access.
2. Add account lockout after 5 failed login attempts.
3. Implement rate limiting on authentication requests (max 1 request per second per IP).
4. Create a detection rule for "5+ failed logins followed by a successful login from
   the same IP within 10 minutes."
5. Monitor for repeated username variations, which suggest password spraying.

## 10. Why this was a True Positive
The alert correctly identified a brute force attack. The evidence is clear:
- 5 different usernames in 8 minutes from the same external IP.
- A successful login immediately after repeated failures.
- The pattern and timing match a real attack, not normal admin work.

Even though the account is a test account in a lab, the *attack itself* was real. The
attacker used a real technique. That makes it a True Positive.

## 11. What I learned
- **Weak passwords are the enemy.** The attacker guessed this one in two tries.
- **Username enumeration works.** The attacker found a valid username (mane@) by trying
  variations.
- **Timing tells the story.** 13:43 to 13:51 is too fast for normal admin work. That
  8-minute burst is a red flag.
- **The playbook is a minimum, not a ceiling.** I should have checked post-login
  activity and lateral movement even if the playbook didn't ask. I marked these as gaps
  in this investigation, and I will check them in future cases.
- **Test accounts matter.** If this were a real user account with post-login activity, the
  containment would be faster and more urgent.

## 12. Escalation
**Tier 2: No.** The account is a test account and no lateral movement occurred. This
is a contained incident. If it were a real user account with confirmed post-login activity
or lateral movement, I would escalate immediately.

## 13. Conclusion
The investigation confirmed a successful VPN brute force attack from external IP
37.19.221.229. The attacker tried five usernames in 8 minutes and successfully logged
in as mane@letsdefend.io on the second attempt with that username. No lateral movement
was detected. The verdict is True Positive. The main lesson is that weak passwords and
lack of MFA create an easy path for attackers. Future investigations should include
post-login activity checks to fully scope the breach.
