#!/bin/bash



echo "[*] Deleting hidden binary..."

sudo rm -f /usr/bin/.hidden_binary



echo "[*] Removing hidden shell...

sudo rm -f /usr/bin/.bashhidden



echo "[] emoving ghost root user...

sudo userdel ghostuser 2/dev/null | echo ghostuser not found



echo [*] inal check listing all  0 users...

grep 'x0' /etc/passwd



echo [] leanup complete.


