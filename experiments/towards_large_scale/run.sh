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
# 2. Setup & build the first simulation
# -----------------------------------------------------------------------------

SIMCOMMIT=$(cat $DIR/sim-commit.txt)
checkout $SIMDIR $SIMCOMMIT
apply_patch $SIMDIR $DIR/sim.patch
build $SIMDIR
cp $SIMDIR/scripts/experiments/parameter/full_scale.json $SIMDIR/bdm.json

# -----------------------------------------------------------------------------
# 3. Run the simulation
# -----------------------------------------------------------------------------
cd $SIMDIR
run_simulation $SIMDIR
cd $DIR
python postprocess.py
copy_results $SIMDIR/output/angiogenesis $DIR/results/
mv large-scale.pdf $DIR/results/
echo ""
echo -e "${GREEN} ############################################### ${NC}"
echo -e "${GREEN} Success: result in $DIR/results/large-scale.pdf ${NC}"
echo -e "${GREEN} ############################################### ${NC}"
echo ""

# -----------------------------------------------------------------------------
# 4. Cleanup
# -----------------------------------------------------------------------------
reset_repository $SIMDIR
reset_repository $BDMDIR
rm -rf $SIMDIR/output
# rm -rf $SIMDIR/build
# rm -rf $BDMDIR/build




