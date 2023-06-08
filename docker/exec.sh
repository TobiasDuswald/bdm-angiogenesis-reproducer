#!/bin/bash

# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://doi.org/10.5281/zenodo.6463816
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#

set -e
if [[ $# -lt 1 ]]; then
  BDM_COMMAND=/bin/bash
else
  if [[ "$1" == "--help" ]]; then
    echo "
Description:
  Run a script inside a running docker container
Usage:
  $0 [COMMAND [COMMAND_ARGUMENTS]]
Arguments:
  COMMAND command to be executed inside the docker
          container. Default value: /bin/bash 
  COMMAND_ARGUMENTS arguments that are passed to COMMAND inside the docker
                   container (optional)
  "
    exit
  fi
BDM_COMMAND=$@
fi

BDM_SCRIPT_DIR=$(readlink -e $(dirname "${BASH_SOURCE[0]}"))
PROJECT_ROOT_DIR=$(readlink -e $BDM_SCRIPT_DIR/../..)

# include util functions
. $BDM_SCRIPT_DIR/util.sh

DockerChecks

# TODO check if container is running
if [ "$(docker ps -q -f name=$BDM_CONTAINER | wc -l)" = "0" ]; then
    echo "ERROR: Docker container $BDM_CONTAINER is not running."
    echo "       Use docker/run.sh to run a script in a new container."
    echo "       Aborting."
    exit 1
fi

# set number of available process ids - see Paraview MPI issue
ulimit -u 8096 || true

EchoNewStep "Execute ${BDM_COMMAND}..."
docker exec \
  --user testuser \
  -ti \
  $BDM_CONTAINER \
  $BDM_COMMAND

RETURN_VAL=$?
echo ""
EchoNewStep "Finished"
echo "$BDM_COMMAND return code was: $RETURN_VAL"
echo "The container '$BDM_CONTAINER' is still running."
echo "You can connect to it by calling 'docker/exec.sh /bin/bash'"
echo "from the directory $PROJECT_DIR"
exit $RETURN_VAL

