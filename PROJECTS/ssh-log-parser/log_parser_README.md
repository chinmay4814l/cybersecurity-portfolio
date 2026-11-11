# Project 1: SSH Log Parser
**MITRE ATT&CK Mapping:** T1110.001 – Password Guessing (detects repeated failed SSH login attempts matching brute-force patterns)

## Description
Detects brute force attacks from SSH auth logs using regex pattern matching.

## Features
- Parses SSH failed login attempts
- Extracts source IPs using regex
- Identifies brute force attackers (5+ failed attempts)
- Generates summary report

## Usage
```bash
python3 log_parser.py
```

## Output
- Total unique IPs with failed logins
- Brute force attackers with attempt counts

## Data Source
Real SSH logs from SSHAnalyzer dataset (github.com/RasyKy/SSHAnalyzer)
