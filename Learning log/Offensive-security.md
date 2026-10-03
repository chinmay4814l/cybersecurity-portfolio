# Port Scanning & Exploitation Basics - Learning Log

## Sep 27, 2026 - nmap, searchsploit, exploit basics

learned about port scanning today using nmap on a legal practice target (scanme.nmap.org - made by nmap creators specifically for practice).

basic nmap scan:
`nmap scanme.nmap.org` - scans around 1000 common ports and tells me which ones are open and what service is running there

targeted scan (faster):
`nmap -p 22,80,443 scanme.nmap.org` - only checks those specific ports instead of all 1000

version detection:
`nmap -sV -p 22,80 scanme.nmap.org` - finds the exact software version running on each open port

results from scanme.nmap.org:
- port 22 open - running OpenSSH 6.6.1p1
- port 80 open - running Apache httpd 2.4.7
- port 443 closed - nothing listening there

the -y flag in sudo apt install just means auto confirm yes so it skips the "do you want to continue" prompt

non-authoritative answer in nslookup means the dns resolver gave a cached answer instead of asking the domain's own servers directly. not an error, just means it used a saved copy.

port states:
- open - something is actively listening and will respond
- closed - nothing listening, connection refused immediately
- filtered - firewall blocking it, no response at all

searchsploit:
installed exploitdb from gitlab since it wasnt in ubuntu's default repositories. searchsploit searches a local offline database of already documented, already written exploits. it matches software name and version to known vulnerabilities.

`searchsploit openssh 6.6` - found real documented exploits for that version
`searchsploit apache 2.4.7` - found exploits specifically matching that exact version

read the actual exploit code using cat:
`cat ~/exploitdb/exploits/php/remote/40142.php`
this was a real php exploit targeting apache 2.4.7 + php 7.0.2. it had three main parts:
- memory mapping section - scans server memory to find where php and apache are loaded
- rop chain - hijacks the programs normal execution flow by chaining small pieces of existing code in memory
- shellcode - raw machine code injected into memory, in this case just printed hello world but in a real attack would be something malicious

how the full exploitation chain actually works:
- nmap finds open ports (find the door)
- version detection finds exact software version (find which lock type)
- searchsploit finds documented exploit for that version (find the tool for that lock)
- running the exploit points that tool at the target ip and port (use the tool against the lock)
- if vulnerability exists and conditions are right, you get unintended access

cat just reads the exploit file locally on my own machine - it has nothing to do with connecting to any port on another system. cat = reading the tool's manual, not using it.

searchsploit finds already known, already documented exploits. it doesnt discover new ones, doesnt tell you if the exploit will work, and doesnt run anything. its a starting point not the whole job.

legal line:
- reading exploit code = fine, its just text
- running exploits on authorized targets (internship scope, metasploitable2, tryhackme rooms) = fine
- running exploits on real systems without permission = illegal

next step will be setting up metasploitable2 on virtualbox to practice actual exploitation legally and safely.
