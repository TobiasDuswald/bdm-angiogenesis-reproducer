#!/bin/bash

# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://doi.org/10.5281/zenodo.6463816
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

BDM_IMAGE_ID=$(docker images --format="{{.ID}}" ${BDM_DOCKER_IMAGE})
BDM_FILE=$PROJECT_ROOT_DIR/${BDM_DOCKER_IMAGE}-docker-image-${BDM_IMAGE_ID}.tar.gz
docker save ${BDM_DOCKER_IMAGE} | gzip > $BDM_FILE 
echo "Successfully saved image ${BDM_DOCKER_IMAGE} with ID ${BDM_IMAGE_ID} to file"
echo "$BDM_FILE"
