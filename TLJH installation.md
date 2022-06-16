# Installation

Follow the latest instructions

# Using custom `conda` environments

Using conda appears to require login into a Hub session and opening a terminal, connecting directly to a jupyter-* user doesn't make conda available for some reason.

## Allow multiple kernel environments

    sudo -E conda install -c conda-forge nb_conda_kernels

## Teaching environmennts

```
sudo -E conda create -n bw2 -c conda-forge -c cmutel brightway2 ipykernel seaborn tqdm
sudo -E conda create -n bw25 -c conda-forge -c cmutel brightway25 ipykernel seaborn tqdm
sudo -E conda create -n regional -c conda-forge -c cmutel brightway25 bw2regional ipykernel seaborn tqdm geopandas
```

**Note**: Must be run with `sudo -E`.

## Adding on to teaching environments after creation

Note: This needs to be done in an SSH session, not via the terminal in the hub.

```
source /opt/tljh/user/etc/profile.d/conda.sh
conda activate <env>
sudo -E /opt/tljh/user/condabin/conda install <library>
```

## Removing environments

```
sudo -E /opt/tljh/user/condabin/conda remove --name myenv --all
```

# Make conda use mamba

[Mamba is a faster conda](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community).

```
sudo -E conda update -n base conda
sudo -E conda install -c conda-forge conda-libmamba-solver
sudo -E conda config --set experimental_solver libmamba --env
```

# Configuring TLJH

## Concept

The `tljh-config` program modifies the file `/opt/tljh/config/config.yaml` - you can also browse or edit this file directly.

## Resource limits

```
sudo tljh-config set limits.memory 16G
sudo tljh-config set limits.cpu 4
sudo tljh-config set services.cull.timeout 3600
sudo tljh-config reload
```

## Change default interface to `JupyterLab`

```
sudo tljh-config set user_environment.default_app jupyterlab
```

(From https://tljh.jupyter.org/en/latest/howto/env/notebook-interfaces.html)

# Adding users

Our current security model is built around classes, where we can create users by username, and they can set their own passwords when logging on the first time. Here is the authentication documentation: https://tljh.jupyter.org/en/latest/howto/auth/firstuse.html

The command to create a new user is:

```
sudo tljh-config add-item users.allowed <username>
```

This can be run in an SSH session.

## Switching authentication modes:

Switch to anonymous usage:

```
sudo tljh-config set auth.type tmpauthenticator.TmpAuthenticator
sudo tljh-config reload
```

Switch to only registered users:

```
sudo tljh-config set auth.type firstuseauthenticator.FirstUseAuthenticator
sudo tljh-config reload
```

## Setting user data

Adding an approved user name **does not** create the Linux user - this happens on first login. To customize the new user, change the skeleton directory `/etc/skel/`.

To create a more accessible Brightway data directory:

```
sudo mkdir /etc/skel/bw_data
```

And then edit `/etc/skel/.profile` to add:

```
export BRIGHTWAY2_DIR=$HOME/bw_data
```

However, this doesn't work as `.profile` is not sourced when opening JupyterHub. For now we stick with the standard directory location, namely:

```
/home/jupyter-<username>/.local/share/Brightway3/
```

### Setting environment variables

You can put standard JupyterHub config directives under `/opt/tljh/config/jupyterhub_config.d/<some-config-file-name>`. So you may create a file at `/opt/tljh/config/jupyterhub_config.d/environment.py` and add the following contents:

```
c.Spawner.environment = {
        'TEST': 'blah'
}
```

(From https://github.com/jupyterhub/the-littlest-jupyterhub/issues/308)

# Deleting users

You need to delete from both the JupyterHub registry and from the linux system:

```
sudo tljh-config remove-item users.allowed <username>
sudo userdel jupyter-<username>
```

# User starting configuration

Files are stored in:

    /etc/skel/

# Sharing data

Following https://tljh.jupyter.org/en/latest/howto/content/share-data.html.

Shared data is in `/srv/data/`

# Specifics on read-only errors

Some libraries want or require write permissions.

Rower:

```
sudo chmod +777 /opt/tljh/user/envs/regional/lib/python3.10/site-packages/rower/data/ecoinvent\ 3.8\ cutoff/
```

bw2_lcimpact:

```
sudo chmod 666 /opt/tljh/user/envs/regional/lib/python3.10/site-packages/bw2_lcimpact/data/*.gpkg
sudo chmod 777 /opt/tljh/user/envs/regional/lib/python3.10/site-packages/bw2_lcimpact/data
```

# Libraries that use absolute paths

* bw2regional: for geocollections. needs to be copied to a read-all directory, and filepaths updated.
