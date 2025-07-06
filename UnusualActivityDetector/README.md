Unusual Activity Detector
=========================

Description:
------------
This is a lightweight Python tool that scans running system processes and detects unusual activity by comparing them against a predefined list of known good processes. It's useful for quick audits or as part of a larger security monitoring setup.

Setup Instructions:
-------------------
1. Create a project folder and set up a virtual environment:
   
   mkdir UnusualActivityDetector && cd UnusualActivityDetector
   python3 -m venv venv && source venv/bin/activate

2. Install the required Python dependency:

   pip install psutil

Script: activity_detector.py
----------------------------
This script uses the psutil library to iterate over all running processes and flags any that are not included in the `KNOWN_PROCESSES` set.

Example process whitelist:
   KNOWN_PROCESSES = {
       "systemd", "bash", "sshd", "python3", "zsh", "firefox", "chrome", "Xorg"
   }

Usage:
------
Run the script manually:

   python3 activity_detector.py

Optional - Continuous Monitoring:
---------------------------------
To run the check continuously every 10 seconds, wrap the function in a loop:

   while True:
       detect_unusual_processes()
       time.sleep(10)

Optional - Cron Job:
--------------------
To automate checks every minute, use a cron job:

1. Open crontab:
   crontab -e

2. Add the following line:
   * * * * * /path/to/venv/bin/python /path/to/UnusualActivityDetector/activity_detector.py

Customization:
--------------
You can update the `KNOWN_PROCESSES` set to match your specific environment and expected software stack.

License:
--------
This project is provided for educational and research purposes only.
