#!/bin/bash

# This script reproduces the large-scale experiment from the paper.

# Source the util/main.sh script for ParaView if hostename is "docker-container"
if [ "$HOSTNAME" = "docker-container" ]; then
    . util/main.sh
fi

# Run the experiments for the paper
./experiments/towards_large_scale/run.sh
