#!/bin/bash

# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://zenodo.org/record/5121618
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#

BDM_SCRIPT_DIR=$(readlink -e $(dirname "${BASH_SOURCE[0]}"))
PROJECT_ROOT_DIR=$BDM_SCRIPT_DIR/../..
cd $BDM_SCRIPT_DIR

# include util functions
. util.sh

set -e
EchoNewStep "Build docker image..."
DockerChecks

# make tmp copy of pom such that it can be copied into the 
# container. Docker doesn't support copying files outside
# the build context.
cp ../other-tools/cx3d/pom.xml .
cp ../util/setup-profiling-env.sh .
cp -r ../util/vim .

docker build \
  --network=host \
  -t $BDM_DOCKER_IMAGE .

rm pom.xml
rm setup-profiling-env.sh
rm -rf vim
