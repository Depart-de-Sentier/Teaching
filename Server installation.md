# Users and groups

Create `class` group:

    sudo groupadd class

Add yourself to the group

    sudo usermod -a -G class <username>

**Need to logout for your group membership to be recognized**

# Miniconda

On Linux (64bit Intel/AMD) you can run:

    wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh
    chmod +x ./Miniconda3-py39_4.11.0-Linux-x86_64.sh
    ./Miniconda3-py39_4.11.0-Linux-x86_64.sh

Accept license

Answer yes to running conda init

Change group ownership of conda to let students have access:

    chgrp -h -R class miniconda3




Users:

- Add to group
- Clone `class` environment
- Add conda to user path
- Edit profile to autoactivate the cloned environment

conda create -n class -c conda-forge -c cmutel -c bsteubing activity-browser-dev jupyterlab seaborn tqdm
