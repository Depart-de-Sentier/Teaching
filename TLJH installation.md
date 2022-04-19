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

# Configuring TLJH

## Resource limits

```
sudo tljh-config set limits.memory 16G
sudo tljh-config set limits.cpu 4
sudo tljh-config reload
```

## change default interface to `JupyterLab`

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
