# Race against daughters internet

Or: how to do security by obscurity and open a backdor.

Setting is that daughter is root anyway and we secretely deny her internet via
ufw default rules.

Get some python3 skills (back) during the way.

## The process

* Initially the firewall is set to block everything.
* Timed Un-locks can be defined (i.e. open the firewall for X minutes)
* A cronjob checks every minute if the firewall should be kept open.

* Opening rules are files named by timestamp.
* To prevent the opening rules persist after shutdown within an Un-Lock window
  (ufw doesnt know temporary rules), the cronjob will check if it already ran
once, if not, close the firewall.

* Because of insecure shebangs in python-scripts, wrote C wrappers.

* A tool exists to create opening rule timestamp files. The password check is
  done supersecure using base64 (she is root anyway).

## Installation

* Place everything in `/opt/pynternet`
* Compile the wrapper (daughter runs on ARM, have no cross-compiling expertise)
  ```
  gcc pynternet.c -o pynternet_open
  ```
* Add cronjob
  ```
  sudo crontab -u root -e
  # */1 * * * * /opt/pynternet/pynternetcheck.py
  ```


### Other approaches

Networking services and/or interfaces could be shut down instead:

```
sudo nmcli networking off

sudo systemctl stop NetworkManager
sudo systemctl disable NetworkManager
sudo systemctl mask NetworkManager


sudo systemctl unmask systemd-networkd.service
sudo systemctl enable systemd-networkd.service
sudo systemctl start systemd-networkd.service
```

