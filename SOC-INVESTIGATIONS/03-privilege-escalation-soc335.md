# SOC335 - CVE-2024-49138 Privilege Escalation Exploitation

## Alert Summary
- **EventID:** 313
- **Severity:** Medium
- **Date:** 2025-01-22 02:37:00 UTC+3
- **Alert Type:** Privilege Escalation
- **Status:** TRUE POSITIVE

## What Happened

This was a privilege escalation attack using CVE-2024-49138. The attacker deployed a malicious executable disguised as a legitimate Windows service through PowerShell. Once executed, it exploited a Windows vulnerability to escalate privileges, then the attacker gained remote access to the compromised system.

## Attack Chain

**Step 1: Initial Execution via PowerShell**
- Parent Process: `powershell.exe`
- Spawned: `svohost.exe` (mimics legitimate Windows svchost.exe)
- Location: `C:\temp\service_installer\svohost.exe` (not a system directory)
- Hostname: Victor
- User: EC2AMAZ-ILGVOIN

**Step 2: Privilege Escalation Exploit**
- CVE-2024-49138 exploited to escalate privileges
- File Hash: b432dcf4a0f0b601b1d79848467137a5e25cab5a0b7b1224be9d3b6540122db9
- VirusTotal Detection: 44 out of 65 engines flagged it malicious

**Step 3: Remote Access Established**
Log evidence shows:
EventID: 4624 (Account Logon Success)
Username: Victor
Logon Type: 10 (RemoteInteractive - RDP)
Source IP: 185.107.56.141


The attacker used the elevated privileges to enable remote access and connected from an external IP. This means the system is fully compromised with the attacker having remote control.

## Evidence

| Evidence | Finding |
|----------|---------|
| File Hash Analysis (VirusTotal) | 44/65 engines detected malicious |
| Process Chain | PowerShell → svohost.exe → conhost.exe |
| Remote Access Log | RDP login from 185.107.56.141 after exploitation |
| EDR Status | NOT quarantined - file still on disk |
| File Location | C:\temp\service_installer\ (not legitimate system path) |
| Service Mimicry | Named svohost.exe (mimics svchost.exe) |

## MITRE ATT&CK Mapping

- **T1548** - Abuse Elevation Control Mechanism
- **T1068** - Exploitation for Privilege Elevation
- **T1055** - Process Injection
- **T1059.001** - Command Line Interface (PowerShell execution)
- **T1110** - Brute Force (part of attack chain)

## Why TRUE POSITIVE

1. **Real CVE exploited** - CVE-2024-49138 is a known Windows privilege escalation vulnerability
2. **Confirmed malicious** - 44/65 antivirus engines detected the file
3. **Privilege escalation verified** - attacker gained elevated access
4. **Remote access confirmed** - RDP login from external IP 185.107.56.141 proves attacker access
5. **System not protected** - EDR didn't quarantine, malware still on disk

This is a confirmed compromise. The attacker successfully escalated privileges and established remote access to the system.

## Recommended Actions

- [ ] Immediately isolate host "Victor" from the network
- [ ] Block source IP 185.107.56.141 at firewall
- [ ] Kill svohost.exe process and remove the file
- [ ] Disable RDP access or reset credentials for compromised user
- [ ] Run full forensic analysis on the system
- [ ] Reset all credentials for EC2AMAZ-ILGVOIN user account
- [ ] Check for lateral movement to other systems
- [ ] Add hash b432dcf4a0f0b601b1d79848467137a5e25cab5a0b7b1224be9d3b6540122db9 to blocklist

## Closing Notes

This attack demonstrates a multi-stage privilege escalation. The attacker didn't just exploit the vulnerability—they maintained access remotely. The mimicking of a legitimate Windows service name shows operational awareness. The EDR failure to quarantine is critical—endpoint protection needs updating.
