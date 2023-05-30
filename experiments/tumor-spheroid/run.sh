#!/bin/bash

# This script runs the vessel growth simulation and saves the results to this
# directory.

set -e

# Get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Source the util.sh script
source $DIR/../../util/util.sh

# Create a results directory
mkdir -p $DIR/results

# -----------------------------------------------------------------------------
# 0. Make sure that the repositories are clean and up-to-date
# -----------------------------------------------------------------------------
reset_repository $BDMDIR
reset_repository $SIMDIR

# -----------------------------------------------------------------------------
# 1. Setup & build BioDynaMo
# -----------------------------------------------------------------------------

BDMCOMMIT=$(cat $DIR/bdm-commit.txt)
checkout $BDMDIR $BDMCOMMIT
build $BDMDIR
source_bdm

# -----------------------------------------------------------------------------
# 2. Setup & build the simulation
# -----------------------------------------------------------------------------

SIMCOMMIT=$(cat $DIR/sim-commit.txt)
checkout $SIMDIR $SIMCOMMIT
apply_patch $SIMDIR $DIR/sim.patch
build $SIMDIR
cp $DIR/bdm.json $SIMDIR/bdm.json

# -----------------------------------------------------------------------------
# 3. Run the simulations
# -----------------------------------------------------------------------------

x_list=( 0.15 0.13 0.12 0.11 )
PATTERN="hypoxic_threshold\": 0.13"
for x in "${x_list[@]}"
do
    # Replace the parameter x in the config file
    replace "$SIMDIR/bdm.json" "$PATTERN" "hypoxic_threshold\": $x"

    # Run the application
    run_simulation $SIMDIR

    # Reeplace the parameter x in the config file with the original value
    replace "$SIMDIR/bdm.json" "hypoxic_threshold\": $x" "$PATTERN"
done

# -----------------------------------------------------------------------------
# 4. Post-processing
# -----------------------------------------------------------------------------

# Prepare for visualization (fix for transparent background in later commit)
reset_repository $SIMDIR
VIZCOMMIT=$(cat $DIR/viz-commit.txt)
checkout $SIMDIR $VIZCOMMIT
cd $SIMDIR
# Set the parameters for the visualization script
replace "scripts/visualize-tumor-cells.sh" "BACKGROUND=0" "BACKGROUND=1"
replace "scripts/visualize-tumor-cells.sh" "AXES=1" "AXES=0"
replace "scripts/visualize-tumor-cells.sh" "COLORBAR=1" "COLORBAR=0"
# Trigger the visualization script
./scripts/visualize-tumor-cells.sh
# Copy the results to the results directory
copy_results $SIMDIR/output/angiogenesis $DIR/results
cd $DIR

# -----------------------------------------------------------------------------
# 6. Cleanup
# -----------------------------------------------------------------------------
reset_repository $SIMDIR
reset_repository $BDMDIR
# rm -rf $SIMDIR/output
# rm -rf $SIMDIR/build
# rm -rf $BDMDIR/build




