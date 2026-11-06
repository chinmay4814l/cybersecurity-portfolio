# Wazuh SIEM - SSH Brute Force Detection

## What I did

I set up Wazuh (an open-source SIEM/XDR tool) using Docker on my Windows machine with WSL2 Ubuntu. 
Once it was running, I installed a Wazuh agent on my own Ubuntu system so it could monitor and send logs 
to the Wazuh manager.

To test if the detection actually works, I simulated a real SSH brute-force attack against my own 
machine using Hydra (a password-cracking tool). I created a small wordlist with 5 fake passwords and 
pointed Hydra at my own SSH service.

## What happened

Hydra tried all 5 passwords and all 5 failed (as expected, since none were my real password). 
I then checked the Wazuh dashboard to see if it picked up the attack.

Wazuh flagged it immediately. It logged:
- 5 "sshd: authentication failed" events (rule 5760)
- 5 "PAM: User login failed" events (rule 5503)

Both rule sets triggered at severity level 5, with the correct source IP (my own machine's IP, 
172.25.28.246) and the correct target username. Every failed attempt from Hydra was captured and 
correctly attributed.

## What this shows

- I can deploy a SIEM from scratch (Docker setup, agent install, manager-agent connection)
- I understand how SSH authentication failures get logged and decoded
- I can simulate a real attack technique (brute force) safely in my own environment
- I can verify detection end-to-end: attack → log → decoder → rule → alert
- I know how to read Wazuh's rule IDs and severity levels to triage an alert

## Screenshots

1. `screenshots/wazuh-01-dashboard-overview.png` - Wazuh overview dashboard showing active agent and alert severity counts
2. `screenshots/wazuh-02-alert-detail.png` - Full alert detail showing source IP, target user, and raw log
3. `screenshots/wazuh-03-alert-list.png` - List view of all 10 authentication failure events from the attack

## Tools used

- Wazuh 4.9.2 (Docker single-node deployment)
- Docker Desktop with WSL2 backend
- Hydra 9.5 (brute-force tool)
- WSL2 Ubuntu
