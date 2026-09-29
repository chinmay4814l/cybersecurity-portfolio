# Internship Log

## Sep 26, 2026
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

## Sep 28, 2026- SQl injection Lab-01

Started working on the SQL Injection labs today. Before jumping into the actual attack, I wanted to properly understand what SQL injection is and why it matters, so I read up on it and also found Rana Khalil's Web Security Academy series on YouTube, which walks through each PortSwigger lab one by one — really helpful for following along instead of just copy-pasting payloads blindly.

What I learned:
SQL injection happens when user input (like a category filter or search box) gets inserted directly into a database query without being checked. Since the app trusts whatever you type, you can sneak your own logic into the query and make the database do things it was never supposed to — like showing hidden/unreleased data.

Lab worked on: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

What I did:

Opened the lab and noted the category parameter in the URL (/filter?category=Gifts)
Tried adding a single quote (') to the URL to test if the input was vulnerable — got an Internal Server Error, which confirmed the input was going straight into a SQL query
Tried commenting out the rest of the query using '-- but it wasn't working through the browser URL bar directly (turned out to be a URL encoding/whitespace issue), so I moved the payload into Burp Repeater instead, which let me edit the raw request without the browser messing with the characters
Sent the payload ' OR 1=1-- which made the WHERE clause true for every row, bypassing the filter that was hiding unreleased products
Lab solved 
