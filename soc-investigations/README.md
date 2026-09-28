Alert #1 - SOC101 Phishing Mail Detected (Event ID 87)

Platform: LetsDefend (free tier) | Date done: 28 Sep 2026

Alert details
Type / severity: Exchange, Medium
Alert time: 2021-04-04 23:00:15 (+03:00). Email Security showed 2021-04-05 01:30:15. The times don't match, so I just noted it.
Sender: lethuyan852@gmail[.]com
Sent to: mark@letsdefend[.]io
SMTP IP: 146.56.195[.]192
Subject: "Its a Must have for your Phone"
Device action: Allowed (so it was delivered)
What I did
Took ownership of the alert.
Read the email. Random Gmail sender, generic message, no attachment, only one link: hxxp://nuangaybantiep[.]xyz
Checked the link on VirusTotal since the built-in sandbox needs a paid plan. Result: 1 malicious and 3 suspicious out of 91 vendors. That is a low number, but the site looked dead and it is a random .xyz domain, so I looked at everything together: unknown Gmail sender, generic bait, plain http link, weird domain, and some vendors flagging it.
Checked if the mail was delivered. Device action was Allowed, so yes.
Searched Log Management for the domain and found a log with chrome.exe (parent process explorer.exe) making a GET request to the URL, and it was allowed. So the link was opened.
Log source host: (fill this in)
Contained the machine from the EDR page.
Verdict

True Positive. Phishing email was delivered and the user opened the link.

Artifacts I added
nuangaybantiep[.]xyz
lethuyan852@gmail[.]com
146.56.195[.]192
What I would do next
Block the domain and the sender.
Check if anyone else got the same email.
Look in EDR for anything that ran on that machine after the click.
Check the SMTP IP in threat intel before blocking it, because it could be a shared server.
What I learned
If a log search comes back empty, that does not mean "not opened". First check the date range (these logs are from April 2021) and search the domain, the IP and the full URL.
A log hit only proves the request happened. It does not prove anything bad was downloaded, so EDR still needs to be checked.
The lab dashboards reset when I switch between them, so I keep my notes in a separate file.
