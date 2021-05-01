#!/usr/bin/python3

# Run me as a cronjob

from datetime import datetime
import os.path
import os
import glob

LOCK_FILE = '/tmp/pynternet.lock'

# Shall be locked
if os.path.isfile(LOCK_FILE):
    # Check if we have to relock (find last .ufw file)
    ufw_files = glob.glob('/tmp/*ufw')
    if ufw_files:
        print("Countdown is running")
        # Check if we are within time, if so: exit
        ts = float(ufw_files[0][5:22])
        over_at = datetime.fromtimestamp(ts)
        now = datetime.now()
        if now > over_at:
            print("now is over")
            os.system("rm " + ufw_files[0])
        else:
            print("Time to go")
            exit()
    print("Nothing to be done")
    exit()
else:
    # Initialize, close firewall
    os.system("touch " + LOCK_FILE)

os.system("ufw default deny outgoing")
os.system("ufw default deny incoming")

exit()
