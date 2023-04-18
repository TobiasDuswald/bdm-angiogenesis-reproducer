#!/bin/bash

# This script is used to define a list of colors that can be used in bash 
# scripts. 
# Usage: source scripts/util.sh

# Define a list of colors
BLACK='\033[0;30m'
DARKGRAY='\033[1;30m'
RED='\033[0;31m'
LIGHTRED='\033[1;31m'
GREEN='\033[0;32m'
LIGHTGREEN='\033[1;32m'
ORANGE='\033[0;33m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
LIGHTBLUE='\033[1;34m'
PURPLE='\033[0;35m'
LIGHTPURPLE='\033[1;35m'
CYAN='\033[0;36m'
LIGHTCYAN='\033[1;36m'
LIGHTGRAY='\033[0;37m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

echo -e "${PURPLE}Co${BLUE}lo${LIGHTCYAN}rs ${GREEN}lo${YELLOW}ad${RED}ed${NC}"

# Define UTILDIR variable
UTILDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Define ROOTDIR variable
ROOTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
# Define SIMDIR variable
SIMDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../angiogenesis" && pwd )"
# Define BDMDIR variable
BDMDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../biodynamo" && pwd )"

# This function wraps the sed command to replace a string in a file. The
# function evaluates if we are running on a Mac or Linux and uses the
# appropriate sed command. The function takes three arguments:
# 1. The file to be modified
# 2. The string to be replaced
# 3. The string to replace the first string
function replace() {
    # Verify that the function is called with the correct number of arguments
    if [[ $# -ne 3 ]]; then
        echo -e "${RED}Error: replace() takes 3 arguments${NC}"
        echo -e "${RED}Usage: replace <file> <string to replace> <replacement>${NC}"
        return 1
    fi
    # Verify that file exists
    if [[ ! -f "$1" ]]; then
        echo -e "${RED}Error: File <$1> does not exist${NC}"
        return 1
    fi
    # Check if <string to replace> is in <file>
    if ! grep -q "$2" "$1"; then
        echo -e "${RED}Error: <$2> not found in $1${NC}"
        return 1htop
    fi
    # Call sed with the appropriate arguments
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s/$2/$3/g" $1
    else
        sed -i "s/$2/$3/g" $1
    fi
    # Check if the replacement was successful
    if ! grep -q "$3" "$1"; then
        echo -e "${RED}Error: Replacement failed${NC}"
        return 1
    else
        echo -e "${GREEN}Success: <$2> replaced with <$3>${NC}"
    fi
    return 0
}

# This function resets a git repository to a clean state. The function takes
# one argument:
# 1. The path to the source code
function reset_repository(){
    # Verify that the function is called with the correct number of arguments
    if [[ $# -ne 1 ]]; then
        echo -e "${RED}<reset_repository> Error: reset_repository() takes 1 argument${NC}"
        echo -e "${RED}<reset_repository> Usage: reset_repository <path to source code>${NC}"
        return 1
    fi
    # Verify that the path exists
    if [[ ! -d "$1" ]]; then
        echo -e "${RED}<reset_repository> Error: Directory <$1> does not exist${NC}"
        return 1
    fi
    # Print Info
    echo -e "${GREEN}<reset_repository> Resetting repository <$1>${NC}"
    # Reset the repository
    git -C "$1" reset --hard
    git -C "$1" clean -fd
    git -C "$1" checkout master
    git -C "$1" pull
}

# This function takes to arguments:
# 1. The path to the source code
# 2. The git commit hash
# The function checks out the git commit hash and prints the commit message
function checkout(){
    # Verify that the function is called with the correct number of arguments
    if [[ $# -ne 2 ]]; then
        echo -e "${RED}<checkout> Error: checkout() takes 2 arguments${NC}"
        echo -e "${RED}<checkout> Usage: checkout <path to source code> <git commit hash>${NC}"
        return 1
    fi
    # Verify that the path exists
    if [[ ! -d "$1" ]]; then
        echo -e "${RED}<checkout> Error: Directory <$1> does not exist${NC}"
        return 1
    fi
    # Verify that the commit hash is valid
    if ! git -C "$1" cat-file -e "$2^{commit}"; then
        echo -e "${RED}<checkout> Error: Commit hash <$2> does not exist${NC}"
        return 1
    fi
    # Print green status message
    echo -e "${GREEN}<checkout> Checking out commit <$2> in <$1>${NC}"
    # Checkout the commit hash
    git -C "$1" checkout "$2"
    # Print the commit message to stdout
    git -C "$1" log -1 --pretty=%B > "$1"/commit_message.txt
    echo -e "${GREEN}<checkout> Commit message:${NC}"
    cat "$1"/commit_message.txt
    echo -e "${GREEN}<checkout> Commit message end${NC}"
    # Clean up
    rm "$1"/commit_message.txt
}

# This function takes a path to a source code directory and applies a patch
# file to the source code. The function takes two arguments:
# 1. The path to the source code
# 2. The path to the patch file
function apply_patch(){
    # Verify that the function is called with the correct number of arguments
    if [[ $# -ne 2 ]]; then
        echo -e "${RED}<apply_patch> Error: apply_patch() takes 2 arguments${NC}"
        echo -e "${RED}<apply_patch> Usage: apply_patch <path to source code> <path to patch file>${NC}"
        return 1
    fi
    # Verify that the path exists
    if [[ ! -d "$1" ]]; then
        echo -e "${RED}<apply_patch> Error: Directory <$1> does not exist${NC}"
        return 1
    fi
    # Verify that the patch file exists
    if [[ ! -f "$2" ]]; then
        echo -e "${RED}<apply_patch> Error: File <$2> does not exist${NC}"
        return 1
    fi
    # Print green status message
    echo -e "${GREEN}<apply_patch> Applying patch file <$2> to <$1>${NC}"
    # Apply the patch file
    git -C "$1" apply "$2"
}

# This function takes the path to a source code directory and builds the source
# code with cmake. The function takes one argument:
# 1. The path to the source code
function build(){
    # Verify that the function is called with the correct number of arguments
    if [[ $# -ne 1 ]]; then
        echo -e "${RED}<build> Error: build() takes 1 argument${NC}"
        echo -e "${RED}<build> Usage: build <path to source code>${NC}"
        return 1
    fi
    # Verify that the path exists
    if [[ ! -d "$1" ]]; then
        echo -e "${RED}<build> Error: Directory <$1> does not exist${NC}"
        return 1
    fi
    # Get the number of cores
    if [[ "$OSTYPE" == "darwin"* ]]; then
        CORES=$(sysctl -n hw.ncpu)
    else
        CORES=$(nproc)
    fi
    # Print green status message
    echo -e "${GREEN}<build> Building <$1> with $CORES cores${NC}"
    # Build the source code
    mkdir -p "$1/build"
    cd "$1/build"
    cmake ..
    make -j $CORES
}

# This function takes the path to a source code directory and runs the tests
# with bdm test. The function takes one argument:
# 1. The path to the source code
function run_tests(){
    # Verify that the function is called with the correct number of arguments
    if [[ $# -ne 1 ]]; then
        echo -e "${RED}<run_tests> Error: run_tests() takes 1 argument${NC}"
        echo -e "${RED}<run_tests> Usage: run_tests <path to source code>${NC}"
        return 1
    fi
    # Verify that the path exists
    if [[ ! -d "$1" ]]; then
        echo -e "${RED}<run_tests> Error: Directory <$1> does not exist${NC}"
        return 1
    fi
    # Print green status message
    echo -e "${GREEN}<run_tests> Running tests in <$1>${NC}"
    # Run the tests
    cd "$1"
    bdm test
}

# This function takes the path to a source code directory and runs the 
# simulation with bdm run. The function takes one argument:
# 1. The path to the source code
function run_simulation(){
    # Verify that the function is called with the correct number of arguments
    if [[ $# -ne 1 ]]; then
        echo -e "${RED}<run_simulation> Error: run_simulation() takes 1 argument${NC}"
        echo -e "${RED}<run_simulation> Usage: run_simulation <path to source code>${NC}"
        return 1
    fi
    # Verify that the path exists
    if [[ ! -d "$1" ]]; then
        echo -e "${RED}<run_simulation> Error: Directory <$1> does not exist${NC}"
        return 1
    fi
    # Print green status message
    echo -e "${GREEN}<run_simulation> Running simulation in <$1>${NC}"
    # Run the simulation
    cd "$1"
    bdm run
}


# This function sources the BioDynaMo environment script. It is located at
# $BDMDIR/build/bin/thisbdm.sh
function source_bdm(){
    # Verify that the function is called with the correct number of arguments
    if [[ $# -ne 0 ]]; then
        echo -e "${RED}<source_bdm> Error: source_bdm() takes 0 arguments${NC}"
        echo -e "${RED}<source_bdm> Usage: source_bdm${NC}"
        return 1
    fi
    # Verify that the BioDynaMo environment script exists
    if [[ ! -f "$BDMDIR/build/bin/thisbdm.sh" ]]; then
        echo -e "${RED}<source_bdm> Error: File <$BDMDIR/build/bin/thisbdm.sh> does not exist${NC}"
        return 1
    fi
    # Print green status message
    echo -e "${GREEN}<source_bdm> Sourcing <$BDMDIR/build/bin/thisbdm.sh>${NC}"
    # Source the BioDynaMo environment script
    source "$BDMDIR/build/bin/thisbdm.sh"
}

# This function uses rsync to copy all png files from a spcified input directory
# to a specified output directory. The function takes two arguments:
# 1. The path to the input directory
# 2. The path to the output directory
# If the output directory does not exist, it will be created.
function copy_results(){
    # Verify that the function is called with the correct number of arguments
    if [[ $# -ne 2 ]]; then
        echo -e "${RED}<copy_results> Error: copy_results() takes 2 arguments${NC}"
        echo -e "${RED}<copy_results> Usage: copy_results <path to input directory> <path to output directory>${NC}"
        return 1
    fi
    # Verify that the input directory exists
    if [[ ! -d "$1" ]]; then
        echo -e "${RED}<copy_results> Error: Directory <$1> does not exist${NC}"
        return 1
    fi
    # Verify that the output directory exists
    if [[ ! -d "$2" ]]; then
        echo -e "${GREEN}<copy_results> Directory <$2> does not exist. Creating directory${NC}"
        mkdir -p "$2"
    fi
    # Print green status message
    echo -e "${GREEN}<copy_results> Copying png files from <$1> to <$2>${NC}"
    # Use rsync to copy the files from the input directory to the output directory
    # but exclude the file types that are not needed (*.pvsm, *.vti, *.vtu, *.pvti,
    # *.pvtu)
    rsync -av --exclude="*.pvsm" --exclude="*.vti" --exclude="*.vtu" --exclude="*.pvti" --exclude="*.pvtu" $1/ $2
}
