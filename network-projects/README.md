# Network Projects

This folder contains networking projects I built hands-on using Cisco Packet Tracer.


## LAN Topology Simulation

**Tool:** Cisco Packet Tracer  
**Date:** July 2026

### What I built

I designed a basic office-style Local Area Network from scratch — one router, one switch, and three PCs all connected and communicating with each other. The goal was to simulate how a real company's internal network is structured at its most fundamental level.

### What I actually did

I assigned unique IP addresses to each PC, configured the router's interface through the Cisco IOS command line, set the default gateway on every PC so they could reach the router, and brought the interface up using the no shutdown command. Everything was done through CLI, not point and click.

### Did it work?

Yes. I ran ping tests from PC0 to every other device on the network and got zero packet loss across all three tests — PC0 to PC1, PC0 to PC2, and PC0 to the router itself.

### What I learned

This project gave me a real feel for how IP addressing works in practice, why default gateways matter, and how CLI-based router configuration works — the same way network engineers and SOC analysts interact with routers in real enterprise environments.

### Screenshots
See topology and ping result images in this folder.
