# SOC Investigation: VPN Brute Force Attack

## Overview

This investigation involved a high-severity alert for a possible brute force attack against a VPN service.

The alert was triggered after the VPN detected multiple failed authentication attempts from the same external IP address, followed by a successful authentication from that IP.

The objective of the investigation was to determine whether the activity was actually a brute force attack, identify the scope of the activity, verify whether authentication was successful, and determine the appropriate containment actions.

---

## Alert Information

**Alert:** SOC210 - Possible Brute Force Detected on VPN  
**Event ID:** 162  
**Severity:** High  
**Alert Type:** Brute Force  
**Source IP:** 37.19.221.229  
**Destination IP:** 33.33.33.33  
**Username:** mane@letsdefend.io  
**MITRE ATT&CK:** T1110 - Brute Force  
**MITRE ATT&CK:** T1133 - External Remote Services  

---

## Initial Analysis

The first step was to determine whether the source IP address was internal or external.

The source address `37.19.221.229` is a public IP address and does not belong to the private IPv4 ranges used by internal networks. This indicated that the authentication attempts were originating from outside the organization's network.

I then performed reputation checks on the source IP using VirusTotal, AbuseIPDB, and LetsDefend Threat Intelligence.

VirusTotal did not report any malicious detections for the IP. AbuseIPDB showed an abuse confidence score of 14%, while LetsDefend Threat Intelligence did not return any intelligence for the address.

The reputation results alone were not enough to determine whether the IP was malicious, so I continued the investigation using the authentication logs.

---

## Traffic and Authentication Analysis

I searched Log Management for activity associated with the source IP `37.19.221.229`.

The logs showed repeated authentication attempts against the VPN service.

A total of 10 login attempts were observed over approximately 8 minutes. The initial attempts failed, and the same source IP was also observed attempting authentication using different usernames.

The activity was directed toward the same destination host:

`33.33.33.33`

The most significant finding was that a successful VPN authentication occurred after the repeated failed attempts.

The successful authentication was associated with:

`mane@letsdefend.io`

The sequence of events was consistent with a brute force attack in which repeated authentication attempts eventually resulted in valid credentials being accepted.

---

## Scope of the Attack

I searched for additional activity from the attacker IP to determine whether other systems were being targeted.

The investigation identified only one destination host:

`33.33.33.33`

No additional target hosts were identified in the activity reviewed.

This indicates that the observed activity was focused on a single VPN target rather than multiple systems.

---

## Attack Timeline

The investigation revealed the following sequence:

1. An external IP address, `37.19.221.229`, initiated VPN authentication attempts.
2. Multiple authentication attempts failed.
3. The source IP continued attempting authentication against the VPN.
4. A total of 10 failed attempts were observed within approximately 8 minutes.
5. A successful authentication occurred from the same source IP.
6. The successful authentication was associated with `mane@letsdefend.io`.
7. The activity remained focused on the same destination host, `33.33.33.33`.

The combination of repeated failures followed by a successful authentication from the same source to the same target was the key evidence in determining that the brute force attempt was successful.

---

## Investigation Result

The alert was determined to be a **True Positive**.

The evidence showed a clear pattern of repeated VPN authentication failures followed by a successful authentication from the same external source IP.

The successful login indicates that valid credentials were eventually accepted. However, the available evidence does not by itself establish what actions were performed after the successful VPN login or whether the destination system was compromised beyond the authentication event.

---

## Containment

Because a successful authentication occurred following repeated suspicious login attempts, the affected account should be contained to prevent further unauthorized access.

The account involved in the successful authentication was:

`mane@letsdefend.io`

Appropriate containment would include disabling or locking the account, resetting its credentials, and reviewing or revoking active VPN sessions.

The evidence available in this investigation does not establish that the endpoint itself was compromised, so endpoint isolation should be based on additional evidence of malicious activity on the system.

---

## Lessons Learned

This investigation showed the importance of correlating authentication events instead of relying only on IP reputation.

The source IP did not have a strong malicious reputation across the threat intelligence sources checked, but the behavior observed in the authentication logs was significantly more relevant to the investigation.

The most important indicator was the sequence of repeated failed authentication attempts followed by a successful login from the same source IP to the same target.

To reduce the likelihood of similar attacks, the organization could implement or strengthen:

- Multi-factor authentication for VPN access
- Account lockout and authentication rate limiting
- Detection for repeated failures followed by successful authentication
- Monitoring of authentication attempts against multiple usernames
- Monitoring of unusual VPN access patterns
- Regular review of externally exposed remote access services

Future detections should pay particular attention to repeated authentication failures, password spraying patterns, unusual external VPN sources, and successful authentication immediately following a series of failed attempts.

---

## Conclusion

The investigation confirmed a successful VPN brute force attack originating from the external IP `37.19.221.229`.

The source generated 10 failed authentication attempts against `33.33.33.33` over approximately 8 minutes before successfully authenticating as `mane@letsdefend.io`.

The activity was limited to a single target host, and the authentication pattern provided sufficient evidence to classify the alert as a **True Positive**.

This investigation helped me practice alert triage, IP enrichment, authentication log analysis, attack scoping, timeline construction, and incident containment using a SOC investigation workflow.
