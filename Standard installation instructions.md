1. Download Windows 64-bit anaconda or miniconda (skip if you have it already):

https://docs.conda.io/en/latest/miniconda.html

2. Run the installer

Installation type doesn't matter, all users is maybe preferable but requires admin.

Under advanced installation options, don't click "Add miniconda to system PATH" but leave checked "Register Miniconda as system python".

3. Launch "Anaconda prompt" (or Anaconda powershell prompt if you know powershell).

4. In the terminal window, run:

conda create -n class -c conda-forge -c cmutel -c bsteubing activity-browser-dev jupyterlab seaborn tqdm

5. In the same terminal window, activate your new "ab_dev" environment:

conda activate class

6. Download the project file "brightway2-project-bw-intro-backup.21-February-2022-12-10PM.tar.gz" from https://drive.switch.ch/index.php/s/Ug55VWoZ2xsNRWa

7. In the same terminal window, change to your "Downloads" folder with e.g.

cd Downloads

8. In the same terminal window, open iPython with:

ipython

9. In the iPython shell, import this project with:

import bw2io as bi
bi.restore_project_directory("brightway2-project-bw-intro-backup.21-February-2022-12-10PM.tar.gz")

10. Exit the iPython shell with <ctrl>-d or "quit()".

11. In the same terminal window, start up the activity browser:

activity-browser

Make sure you can load the "bw-intro" project.
