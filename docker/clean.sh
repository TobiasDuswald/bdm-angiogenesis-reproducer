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

set -e
. util.sh

DockerChecks

EchoNewStep "Stop and remove all containers based on image ${BDM_DOCKER_IMAGE} ..."
BDM_CONTAINERS=$(docker ps -a --filter ancestor=$BDM_DOCKER_IMAGE -q)
if [ ! -z "$BDM_CONTAINERS" ]; then
  docker stop $BDM_CONTAINERS 
  docker rm $BDM_CONTAINERS
fi

EchoNewStep "Remove image ${BDM_DOCKER_IMAGE} ..."
docker rmi $BDM_DOCKER_IMAGE

