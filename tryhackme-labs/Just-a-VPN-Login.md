# Challenge: Just a VPN Login

**Difficulty:** Easy | **Time:** 45 min

## Scenario
Suspicious VPN login from Singapore IP (37.19.201.132). Employee didn't authorize login. Malware binary discovered on endpoint.

## Investigation Process
- Threat intel (TryDetectThis): IP/hash/domain reputation
- Malware analysis: Binary signature, C2 infrastructure
- Threat report analysis: Attacker tactics, affiliations, techniques

## Key Findings
- **Malware:** LummaStealer (info-stealing trojan)
- **C2 Infrastructure:** 151 domains across .cyou, .icu, .sbs
- **Attacker Group:** Lumma affiliates collaborating with GhostSocks
- **Attack Vector:** Fake security software on public WiFi

## MITRE ATT&CK
- Resource Development: Acquire Infrastructure (VPS) - T1583.003
- Command and Control: Proxy - T1090.002
