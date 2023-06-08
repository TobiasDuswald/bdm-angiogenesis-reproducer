#!/bin/bash

# This script reproduces all experiments in the paper. Note that it does not
# run the large-scale simulation because it is expected to run for several
# days. The lagre-scale simulation can be run by executing a different script.


# Run the experiments for the paper
./experiments/initial-state/run.sh
./experiments/vessel_growth/run.sh
./experiments/full-treatment-run/run.sh
./experiments/treatment-comparison/run.sh
./experiments/tumor-spheroid/run.sh
