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
apply_patch $SIMDIR $DIR/sim-1.patch
build $SIMDIR

# -----------------------------------------------------------------------------
# 3. Run the first simulation & analyze the results
# -----------------------------------------------------------------------------
run_simulation $SIMDIR
cd $SIMDIR
mkdir -p $SIMDIR/output/angiogenesis/ParaView
echo -e "${GREEN}Running post-processing script...${NC}"
pvpython $DIR/pv-postprocess.py $SIMDIR/output/angiogenesis
copy_results $SIMDIR/output/angiogenesis $DIR/results/no-coupling
cd $DIR

# -----------------------------------------------------------------------------
# 4. Setup & build the second simulation
# -----------------------------------------------------------------------------
reset_repository $SIMDIR
checkout $SIMDIR $SIMCOMMIT
apply_patch $SIMDIR $DIR/sim-2.patch
build $SIMDIR

# -----------------------------------------------------------------------------
# 5. Run the second simulation & analyze the results
# -----------------------------------------------------------------------------
run_simulation $SIMDIR
cd $SIMDIR
mkdir -p $SIMDIR/output/angiogenesis/ParaView
echo -e "${GREEN}Running post-processing script...${NC}"
pvpython $DIR/pv-postprocess.py $SIMDIR/output/angiogenesis
copy_results $SIMDIR/output/angiogenesis $DIR/results/coupling
cd $DIR

# -----------------------------------------------------------------------------
# 6. Cleanup
# -----------------------------------------------------------------------------
reset_repository $SIMDIR
reset_repository $BDMDIR
rm -rf $SIMDIR/output
# rm -rf $SIMDIR/build
# rm -rf $BDMDIR/build




