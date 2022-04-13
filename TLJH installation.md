# Installation

Follow the latest instructions

# Using custom `conda` environments

Using conda appears to require loggin into a Hub session and opening a terminal, connecting directly to a jupyter-* user doesn't make conda available for some reason.

## Allow multiple kernel environments

    sudo -E conda install -c conda-forge nb_conda_kernels

## `bw2-stable`

    conda create -n bw2-stable -c conda-forge -c cmutel -c bsteubing brightway2 jupyterlab seaborn tqdm
