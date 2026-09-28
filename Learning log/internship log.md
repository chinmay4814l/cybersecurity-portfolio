# Internship Log

## Sep 26, 2026 - Day 1
Started my cybersecurity internship today - role is focused on finding vulnerabilities in websites, mostly red teaming work.

Spent today setting up my lab environment:
- Installed VirtualBox and Kali Linux
- Configured memory and RAM allocation for the VM
- Set up guest configuration
- Created a shared folder between host and Kali so I can move files between my main system and the VM

This is the environment I'll be doing the actual testing/vulnerability work in going forward.

## Sep 28, 2026 - Burp Suite Setup and Traffic Interception

installed burp suite community edition on kali, tried professional 
first but had license issues so went with community which does 
everything needed anyway

sudo apt update && sudo apt install burpsuite -y

it was already installed on kali so just confirmed it and opened it up

set up foxyproxy extension on firefox and configured it to point 
to 127.0.0.1:8080 which routes all firefox traffic through burp

downloaded the portswigger ca certificate and imported it into 
firefox certificate manager under authorities tab, this stops 
firefox from showing ssl errors when burp intercepts https traffic

tested everything by turning intercept on and visiting google.com, 
burp caught the traffic and showed all the GET and POST requests 
in http history, everything working
