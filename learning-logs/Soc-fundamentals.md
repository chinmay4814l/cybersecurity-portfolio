SOC Fundamentals (LetsDefend)

Notes from the free SOC Fundamentals course on LetsDefend. Finished on 28 Sep 2026.

Lessons I completed
Introduction to SOC
SOC Types and Roles
SOC Analyst and Their Responsibilities
SIEM and Analyst Relationship
Log Management
EDR
SOAR
Threat Intelligence Feed
Common Mistakes Made by SOC Analysts

I skipped the theory parts at first and came back to them later. The hands-on tasks were the best part.

Hands-on tasks
Log Management: searched logs using the source address, then looked at the destination port to figure out what type of log it was.
EDR (task 1): was given a file hash and had to find which device ran that file.
EDR (task 2): had to find the full command that was run on one particular device.
Threat Intel Feed: searched a hash to see if it is known as malicious.
What I learned
A hash is more reliable than a file name because anyone can rename a file.
The command line in EDR tells you what really ran, so it is very useful.
The port number tells you the service (80/443 web, 53 DNS, 22 SSH, 3389 RDP, 445 SMB), so I know which logs to check next.
.hta files run through mshta.exe, which attackers like to use because it is already on Windows.

Lab answers and flags are not included on purpose. This is only about my process.
