# Wireshark Cheat Sheet

## Common Display Filters

| Filter | Purpose |
|---------|---------|
| ftp | Show FTP traffic |
| http | Show HTTP traffic |
| dns | Show DNS packets |
| tcp | Show TCP packets |
| udp | Show UDP packets |
| icmp | Show ICMP packets |
| ip.addr == x.x.x.x | Filter a specific IP |
| tcp.port == 80 | Show TCP port 80 traffic |
| frame contains "text" | Search for text inside packets |

## Useful Actions

- Follow → TCP Stream
- Statistics → Conversations
- Statistics → Protocol Hierarchy
- Statistics → Endpoints

## Investigation Process

1. Identify the protocol.
2. Apply display filters.
3. Follow TCP Stream if needed.
4. Check conversations.
5. Look for filenames, credentials, IP addresses, and unusual activity.
6. Document findings.

## Key Lesson

Always investigate systematically instead of guessing.
