# Install useful libraries for this project:


Download Miniconda3 from the [conda website](https://conda.io/miniconda.html)
```
bash Miniconda3-latest-MacOSX-x86_64.sh
bash
conda update conda
conda create --name pangeo python
source activate pangeo
conda install xarray -c conda-forge
conda install -c conda-forge python-graphviz
conda install cartopy -c conda-forge
conda install jupyter -c conda-forge
```

In order to use xarray master (see [here](https://github.com/pangeo-data/pangeo/issues/1))

```
pip install git+https://github.com/pydata/xarray.git --upgrade
```


In order to add the environnement to kernels available to jupyter, you need to run:
```
python -m ipykernel install --user --name pangeo --display-name "pangeo project env"
```

# Miniconda in general:

## Overview

Miniconda installers contain the conda package manager and Python.
Once Miniconda is installed, you can use the conda command to install any other packages and create environments.
There are two variants of the installer: Miniconda is Python 2 based and Miniconda3 is Python 3 based.
The other difference is that the Python 3 version of Miniconda will default to Python 3 when creating new environments and building packages
Miniconda
Installation

After downloading Miniconda3-latest-Linux-x86_64.sh or Miniconda3-latest-MacOSX-x86_64.sh

Miniconda must be used with bash. If you want to use it with csh, add in your .cshrc (pas terrible!!!)
```
#
#----------------------------------------------------------------
# alias Miniconda
#----------------------------------------------------------------
#
setenv PATH ${PATH}: /home/mulroy/slgentil/miniconda3/bin
alias source_activate 'setenv OLDPATH ${PATH};setenv PATH /home/mulroy/slgentil/miniconda2/envs/\!*/bin:${PATH}'
alias source_deactivate 'setenv PATH $OLDPATH'
```

## Main commands:
What version, update conda
```
conda --version
conda update conda
```
Create new environment myenv
```
conda create --name myenv python
```
Switch to another environment (activate/deactivate) (or source_activate in csh)
```
source activate myenv
```
To change your path from the current environment back to the root (or source_deactivate in csh)
```
source deactivate
```
List all environments
```
conda info --envs
```
Delete an environment
```
conda remove --name myenv --all
```
View a list of packages and versions installed in an environmentSearch for a package
```
conda list
```
Check to see if a package is available for conda to install
```
conda search packagename
```
Install a new package
```
conda install packagename
```
Remove conda
```
rm -rf /home/mulroy/slgentil/miniconda2 
```

## Install a package from Anaconda.org

For packages that are not available using conda install, we can next look on Anaconda.org. Anaconda.org is a package management service for both public and private package repositories. Anaconda.org is a Continuum Analytics product, just like Anaconda and Miniconda.

In a browser, go to http://anaconda.org. We are looking for a package named “pestc4py”
There are more than a dozen copies of petsc4py available on Anaconda.org, first select your platform, then you can sort by number of downloads by clicking the “Downloads” heading.

Select the version that has the most downloads by clicking the package name. This brings you to the Anaconda.org detail page that shows the exact command to use to download it:

Check to see that the package downloaded
```
conda list
```

## Install a package with pip

For packages that are not available from conda or Anaconda.org, we can often install the package with pip (short for “pip installs packages”).
Exporting environment

```
conda env export > environment.yml on a machine
conda env create -f environment.yml -n $ENV_NAME on the new machine
```


