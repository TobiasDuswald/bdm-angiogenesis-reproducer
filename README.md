# Reproducer for the BDM-Angiogenesis project

This repository contains scripts and parameters to reproduce the results of the
hybrid model for vascular cancer growth and treatment simulation. 

To ensure reproducibility, we need to consider four major factors. 
1. The BioDynaMo repository
2. The application code in the angiogenesis repository
3. The parameters for the application
4. The postprocessing pipelines

In this repository, we specify the necessary code states of both repositories
and the parameters for each experiment. We wrap the compilation, simulation
runs, and postprocessing in convenient bash scripts to simplify reproducibility.

To reproduce an experiment, simply execute the `run.sh` in 
`experiments/<some-experiment>/` after following the instructions for setting
up your system below.

## 1. Update / Init Submodules

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

## 2. Docker container & reproducing of the results

We provide a docker container to manage all system dependencies. The docker
infrastructure is based on Lukas Breitwieser's work and we would like to thank
him for sharing it with us. Docker avoids
problems with setting up your system for the code to compile and run.

Having docker installed is, obviously, a prerequisite.
(Start docker.service if necessary)
The scripts assume that your `$USER` belongs to the docker
group. See [here](https://docs.docker.com/engine/install/linux-postinstall/).
(no sudo calls).

### 2.1 Loading the container (recommended)

```bash
wget http://cern.ch/biodynamo-lfs/cancer-model/bdm-reproducer-image-v1-docker-image-02a59fd5d670.tar.gz
docker/load.sh bdm-reproducer-image-v1-docker-image-02a59fd5d670.tar.gz
rm bdm-reproducer-image-v1-docker-image-02a59fd5d670.tar.gz # free space
```

### 2.1* Building the container (alternative, not recommended)

```bash
docker/build.sh
```

### 2.2 Running the container & reproducing the results

```bash
docker/run.sh ./run-experiments.sh
```

### 2.3 Retrieving the Results

All results are located in the experiments folder, e.g., they can be found in
`experiments/<experiment-name>/results/*`.

## 3. Reproducing with system installation

We (strongly) recommend using the Docker image. However, if for some reason you
wish to run
without docker, you will have to make sure that all dependencies are installed.
Ubuntu 20.04 or 22.04 are recommended. MacOS might work, but we expect that as
time progresses the shipped BioDynaMo version will no longer compile on macOS
and needs to be updated. Please open an issue if you encounter any issues.

In the first step, you'll need to install the packages listed in 3.1 and 3.2.
Note that you must install the pip packages in the same environment as BioDynaMo
uses. Afterward, you may run
```bash
./run-experiments.sh
```

### 3.1 Python packages

See `pip-packages.txt`:
```
numpy matplotlib seaborn pandas
```

### 3.2 System Dependencies

The system dependencies are identical to the ones of BioDynaMo.
They are detailed in the BioDynaMo repository
[`doc/user_guide/prerequisites.md`](https://github.com/BioDynaMo/biodynamo/blob/e327e53c4bec8f9a83d53562dbe6155bd43e032f/doc/user_guide/prerequisites.md).
To install the dependencies, you may either follow the description above 
or simply execute the script
```
./biodynamo/prerequisites.sh all
```
Additionally, the module `rsync` must be available on your system. The module
is used to extract and save the results after simulation/postprocessing.
