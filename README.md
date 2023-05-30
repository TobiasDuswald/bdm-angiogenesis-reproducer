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

## Known issues

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
