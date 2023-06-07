# Reproducer for the BDM-Angiogenesis project

This repository contains scripts and parameters to reproduce the results of the
hybrid model for vascular cancer growth and treatment simulation. 

To ensure reproducibility, we need to consider three major factors. 
1. The BioDynaMo repository
2. The application code in the angiogenesis repository
3. The parameters for the application

In this repository, we specify the necessary code states of both repositories
and the parameters for each experiment. We wrap the compilation, simulation
runs, and postprocessing in convenient bash scripts to simplify reproducibility.

To reproduce an experiment, simply execute the `run.sh` in 
`experiments/<some-experiment>/`.

## Update / Init Submodules

If you clone this repository, it might happen that the submodules are not
cloned. E.g., if you
```bash
git pull https://github.com/TobiasDuswald/bdm-angiogenesis-reproducer.git
cd bdm-angiogenesis-reproducer
ls angiogenesis
```
will show an empty directory. You must make sure that the submodules are loaded,
e.g., run
```bash
git submodule update --init --force --remote
```

## Python packages

See `pip-packages.txt`:
```
numpy matplotlib seaborn pandas
```

## System Dependencies

The system dependencies are identical to the ones of BioDynaMo.
They are detailed in the BioDynaMo repository
[`doc/user_guide/prerequisites.md`](https://github.com/BioDynaMo/biodynamo/blob/e327e53c4bec8f9a83d53562dbe6155bd43e032f/doc/user_guide/prerequisites.md).
To install the dependencies, you may either follow the description above 
or simply execute the script
```
./biodynamo/prerequisites.sh all
```
Additionally, the module `rsync` must be available on your system. The module
is used to extract and save the results after simulation / postprocessing.
