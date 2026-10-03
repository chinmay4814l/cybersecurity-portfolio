# Linux Fundamentals - Learning Log

## Sep 24, 2026 - TryHackMe Linux Fundamentals Part 1
Did this room today. Already knew basic commands like whoami, echo, ls, pwd, cat, cd, grep so that part was easy.

New thing I learned - operators:
- `>` puts output into a file but overwrites whatever was already there
- `>>` same thing but doesn't overwrite, just adds to the bottom
- `&&` runs the second command only after the first one finishes properly

## Sep 25, 2026 - File Permissions
Learned how Linux file permissions actually work today, this took a while to click.

Every file has 3 permission groups - owner, group, others. Each one can have read(r), write(w), execute(x).

Numbers work like this:
- 4 = read
- 2 = write  
- 1 = execute
add them up for what you want. so 777 = everyone can do everything, 644 = owner can read/write but everyone else just reads, 700 = only owner can do anything, no one else gets access.

Checked a real file - /etc/shadow (this is where password hashes are stored on linux). Its permissions are rw-r----- owned by root and shadow group. Tried to cat it and got "permission denied" even though ls -l could show me the file exists. Learned that listing a file and actually reading its content are two different permission checks.

If /etc/shadow was set to something like 777, literally anyone on the system could read password hashes and try cracking them offline. That's a real vulnerability, not just a theory thing.

Got confused for a bit on why ls -l worked but cat didn't - figured out ls just shows file info/metadata, cat actually needs read access to the content.
