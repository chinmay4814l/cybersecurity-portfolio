# Networking - Learning Log

## Sep 26, 2026 - Networking Basics + DNS

router is a device that acts as a connection between private network and internet, it connects us to the whole world. switch acts as a medium that helps in interaction between multiple home devices. switch lets us talk to each other and router makes the whole home network reach internet.

ip address is a unique address of every device that helps as the address on internet when we connect to the internet. mac address is a fixed address of the device that is imprinted at the time of manufacturing.

dns makes the ip address easy to understand for humans by giving them names. when i type a website name the dns changes it into ip address and searches the address on the internet and displays on my browser.

record types:
- A record - maps a domain straight to an ipv4 address
- CNAME record - maps a domain to another domain name instead of an ip directly, basically like a nickname pointing to the real one

installed dnsutils to get nslookup working, had to reset my wsl password along the way since i forgot it - used `wsl -u root` then `passwd chinmaya` to fix it.

ran real lookups:
- `nslookup google.com` - got googles actual ip, saw "non-authoritative answer" which just means the dns resolver gave a cached answer instead of asking googles own servers directly
- `nslookup www.github.com` - saw a real cname in action, www.github.com points to github.com which then resolves to the actual ip
- `nslookup -type=MX google.com` - found the mail server handling googles email
- `nslookup -type=TXT google.com` - found a bunch of domain verification records and an spf record

spf tells other mail servers which servers are allowed to send email on behalf of a domain. if spf is missing anyone could act as a genuine person and send mails to do attacks since theres no check to catch it. connects to red teaming since phishing simulations are part of it and checking a targets spf setup would be a real recon step.

ports are like doors on a device, each one runs a specific type of traffic. port 80/443 for web, 22 for ssh, 53 for dns. port scanning is one of the first things done in a real vulnerability test to see whats open and possibly exploitable.
