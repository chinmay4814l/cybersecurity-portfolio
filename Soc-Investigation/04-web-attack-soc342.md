# SOC342: CVE-2025-53770 SharePoint ToolShell Auth Bypass and RCE

## 1. Summary
An alert fired for a suspicious unauthenticated POST request to
`/_layouts/15/ToolPane.aspx` on SharePoint01 (172.16.20.17). The source was
an external IP, 107.191.58.76. The endpoint logs showed that commands really
ran on the server, so this was a successful compromise and not just an
attempt. I escalated it to Tier 2.

## 2. What I looked at first
- **Rule name:** it names CVE-2025-53770 and SharePoint, so my starting
  hypothesis was a ToolShell exploitation attempt against SharePoint01.
- **Referer:** `/_layouts/SignOut.aspx`. A sign-out page has no reason to
  send a POST to an edit tool, so this looked spoofed.
- **Content-Length:** 7699 bytes. That is large for a normal request and
  fits an encoded payload.
- **Device Action: Allowed.** This only means the request reached the
  server. It does not prove the exploit worked, so I needed more evidence.

## 3. Traffic direction
107.191.58.76 is a public IP (Internet). 172.16.20.17 is a private IP
(internal server). Direction: **Internet -> Company Network** (inbound).

## 4. Planned test check
I searched Email Security for the source IP, destination IP, hostname, and
testing-related keywords. I found no authorization or scheduled-test email.
The source is external and no attack simulation product was identified.
Conclusion: **not a planned test.**

## 5. Attack type
Insecure deserialization combined with an authentication bypass, resulting
in remote code execution. It was not in the answer list, so I chose
**Other** by eliminating command injection, IDOR, LFI/RFI, SQL injection,
XML injection, and XSS. I confirmed the class from the CVE description:
[FILL IN: source you read, e.g. NVD or Microsoft advisory].

## 6. Evidence that the attack succeeded
Command history from Endpoint Security on SharePoint01:

| Time | Command | What it means |

| 13:07:29 | `cmd.exe /c echo <form runat="server">...` written to `...\TEMPLATE\LAYOUTS\spinstall0.aspx` | A web shell was written to a web-served folder. The file references `http://107.191.58.76/payload.exe`, the same IP as the attacker. |
| 13:07:34 | `powershell.exe -Command "[System.Web.Configuration.MachineKeySection]::GetApplicationConfig()"` | The attacker tried to read the ASP.NET machine key. |

The commands ran 19 and 24 seconds after the exploit request at 13:07:10.
That timing ties them to this attack. [FILL IN: confirm the alert time and
the EDR timestamps use the same timezone.]

**Why the machine key matters:** with it, an attacker can forge requests the
server trusts, even after patching. So patching alone is not enough. The
keys must be rotated.

## 7.
| Finding | 

| Commands executed on SharePoint01 | 
| Web shell file written | 
| Machine key access attempted | 
| `w3wp.exe` was the parent process |
| `payload.exe` downloaded or executed | 
| Lateral movement | 

## 8. Threat intel
107.191.58.76: [FILL IN: what VirusTotal and AbuseIPDB showed, and the date
you checked].

## 9. IOCs
| Type | Value |

| Attacker IP | 107.191.58.76 |
| File | `spinstall0.aspx` (LAYOUTS folder) |
| URL | `http://107.191.58.76/payload.exe` |
| Targeted endpoint | `/_layouts/15/ToolPane.aspx` |
| Victim host | SharePoint01 (172.16.20.17) |

## 10. MITRE ATT&CK (mapped from my evidence only)
- T1190: Exploit Public-Facing Application
- T1059.003: Windows Command Shell
- T1059.001: PowerShell
- T1505.003: Web Shell

The alert listed 16 techniques. I only mapped the ones I could support.

## 11. Response
**Done in the lab:** 
isolated SharePoint01 using Endpoint
Security containment
**Recommended:**
1. Isolate the host but keep it powered on, so memory evidence is kept.
2. Preserve `spinstall0.aspx`, its hash, IIS logs, and the EDR timeline
   before deleting anything.
3. Block 107.191.58.76 at the firewall.
4. Scope the incident: search the whole network for this IP and check for
   other vulnerable SharePoint servers.
5. Patch CVE-2025-53770, remove the web shell, **rotate the machine keys**,
   and restart IIS (verify the steps against Microsoft's advisory).
6. Rebuild the server if I cannot prove it is clean, and reset related
   credentials.
7. Monitor SharePoint01 after recovery.

## 12. Escalation
**Tier 2: Yes.** The attack succeeded and Tier 2 needs to handle key
rotation, network-wide hunting, and forensics.

## 13. What I learned
- "Allowed" does not mean "successful." I need evidence from the endpoint.
- True Positive and "server compromised" are two different findings.
- The alert's MITRE list is not my evidence, so I map from what I see.
- Powering off a compromised server destroys memory evidence. Isolation is
  the better first step.
- The playbook answer list does not always fit the attack, and "Other" can
  be the honest answer.
