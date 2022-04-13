# NOTE: Best practice is to use Jupter hub, not RDP!!!

Usage of Windows servers is not recommended, as having more than 1 RDP connection requires setting up RDP licensing. Instead, we can use Linux and XRDP, and script the creation of student user accounts.

# Cloud Setup

Start server with public IP and ports 22 (SSH) and 3389 (RDP) open.

# Server

Run commands in bash:

    sudo apt-get update
    sudo apt-get install xrdp xubuntu-desktop

Note that this needs manual intervention

Give XRDP permission to SSL cert:

    sudo adduser xrdp ssl-cert

(Following change to security layer might not be needed)

Edit xrdp config to change security layer:

    sudo nano /etc/xrdp/xrdp.ini

Set the following:

    security_layer=rdp

Start the correct desktop:

    sudo nano /etc/xrdp/startwm.sh

Comment out:

    # test -x /etc/X11/Xsession && exec /etc/X11/Xsession
    # exec /bin/sh /etc/X11/Xsession

And add:

    startxfce4

Restart XRDP with new config:

    sudo systemctl restart xrdp

Check status:

    sudo systemctl status xrdp

Might need to reboot system:

    sudo reboot now

Sources:

* https://linuxize.com/post/how-to-install-xrdp-on-ubuntu-20-04/
* https://stackoverflow.com/questions/67017493/remote-desktop-connection-crashing-when-connecting-to-wsl-ubuntu-20-04-lts
