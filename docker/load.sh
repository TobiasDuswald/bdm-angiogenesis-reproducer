#!/bin/bash

# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://zenodo.org/record/5121618
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#

if [[ $# != 1 ]]; then
  echo "Wrong number of arguments.
Description:
  Load a docker image
Usage:
  $0 PATH_TO_IMAGE.tar.gz
  "
  exit 1
fi

BDM_SCRIPT_DIR=$(readlink -e $(dirname "${BASH_SOURCE[0]}"))
PROJECT_ROOT_DIR=$BDM_SCRIPT_DIR/../..

set -e
. $BDM_SCRIPT_DIR/util.sh

DockerChecks

docker load --input $1

