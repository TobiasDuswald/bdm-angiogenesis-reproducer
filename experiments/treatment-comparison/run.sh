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

# Define the number of simulation runs to perform
NUM_RUNS=10

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
# 2. Setup & build the DOX simulation
# -----------------------------------------------------------------------------

SIMCOMMIT=$(cat $DIR/sim-commit.txt)
checkout $SIMDIR $SIMCOMMIT
apply_patch $SIMDIR $DIR/dox.patch
build $SIMDIR

# -----------------------------------------------------------------------------
# 3. Run the DOX treatment
# -----------------------------------------------------------------------------

for i in $(seq 1 $NUM_RUNS); do
  echo -e "${GREEN}Running simulation $i/$NUM_RUNS...${NC}"
  run_simulation $SIMDIR
done
cd $SIMDIR
echo -e "${GREEN}Running post-processing script...${NC}"
replace $DIR/postprocess.py "yupper = 6000" "yupper = 14000"
python $DIR/postprocess.py
replace $DIR/postprocess.py "yupper = 14000" "yupper = 6000"
copy_results $SIMDIR/output $DIR/results/dox
rm -rf $SIMDIR/output
cd $DIR

# -----------------------------------------------------------------------------
# 4. Setup & build the TRA TRA simulation
# -----------------------------------------------------------------------------
reset_repository $SIMDIR
checkout $SIMDIR $SIMCOMMIT
apply_patch $SIMDIR $DIR/tra-tra.patch
build $SIMDIR

# -----------------------------------------------------------------------------
# 5. Run the TRA TRA simulation & analyze the results
# -----------------------------------------------------------------------------
for i in $(seq 1 $NUM_RUNS); do
  echo -e "${GREEN}Running simulation $i/$NUM_RUNS...${NC}"
  run_simulation $SIMDIR
done
cd $SIMDIR
echo -e "${GREEN}Running post-processing script...${NC}"
python $DIR/postprocess.py
copy_results $SIMDIR/output $DIR/results/tra-tra
rm -rf $SIMDIR/output
cd $DIR

# -----------------------------------------------------------------------------
# 6. Setup & build TRA TRA DOX simulation
# -----------------------------------------------------------------------------
reset_repository $SIMDIR
checkout $SIMDIR $SIMCOMMIT
apply_patch $SIMDIR $DIR/tra-tra-dox.patch
build $SIMDIR

# -----------------------------------------------------------------------------
# 7. Run the TRA TRA DOX simulation & analyze the results
# -----------------------------------------------------------------------------
for i in $(seq 1 $NUM_RUNS); do
  echo -e "${GREEN}Running simulation $i/$NUM_RUNS...${NC}"
  run_simulation $SIMDIR
done
cd $SIMDIR
echo -e "${GREEN}Running post-processing script...${NC}"
python $DIR/postprocess.py
copy_results $SIMDIR/output $DIR/results/tra-tra-dox
rm -rf $SIMDIR/output
cd $DIR

# -----------------------------------------------------------------------------
# 8. Setup & build DOX TRA TRA simulation
# -----------------------------------------------------------------------------
reset_repository $SIMDIR
checkout $SIMDIR $SIMCOMMIT
apply_patch $SIMDIR $DIR/dox-tra-tra.patch
build $SIMDIR

# -----------------------------------------------------------------------------
# 9. Run the DOX TRA TRA simulation & analyze the results
# -----------------------------------------------------------------------------
for i in $(seq 1 $NUM_RUNS); do
  echo -e "${GREEN}Running simulation $i/$NUM_RUNS...${NC}"
  run_simulation $SIMDIR
done
cd $SIMDIR
echo -e "${GREEN}Running post-processing script...${NC}"
replace $DIR/postprocess.py "yupper = 6000" "yupper = 14000"
python $DIR/postprocess.py
replace $DIR/postprocess.py "yupper = 14000" "yupper = 6000"
copy_results $SIMDIR/output $DIR/results/dox-tra-tra
rm -rf $SIMDIR/output
cd $DIR

# -----------------------------------------------------------------------------
# 10. Setup & build 2x(TRA + DOX) simulation
# -----------------------------------------------------------------------------
reset_repository $SIMDIR
checkout $SIMDIR $SIMCOMMIT
apply_patch $SIMDIR $DIR/tradox-tradox.patch
build $SIMDIR

# -----------------------------------------------------------------------------
# 9. Run the 2x(TRA + DOX) simulation & analyze the results
# -----------------------------------------------------------------------------
for i in $(seq 1 $NUM_RUNS); do
  echo -e "${GREEN}Running simulation $i/$NUM_RUNS...${NC}"
  run_simulation $SIMDIR
done
cd $SIMDIR
echo -e "${GREEN}Running post-processing script...${NC}"
replace $DIR/postprocess.py "simultaneously = False" "simultaneously = True"
python $DIR/postprocess.py
replace $DIR/postprocess.py "simultaneously = True" "simultaneously = False"
copy_results $SIMDIR/output $DIR/results/tradox-tradox
rm -rf $SIMDIR/output
cd $DIR

# -----------------------------------------------------------------------------
# 10. Cleanup
# -----------------------------------------------------------------------------
reset_repository $SIMDIR
reset_repository $BDMDIR
rm -rf $SIMDIR/output




