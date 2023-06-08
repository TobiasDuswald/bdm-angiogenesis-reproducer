#!/bin/bash

# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://doi.org/10.5281/zenodo.6463816
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#

if [[ "$1" == "--help" ]]; then
  echo "
Description:
  Starts a new docker container and optionally runs a script inside it.
  If there is already a docker container with the same name it will be stopped
  and removed.
Usage:
  $0 [SCRIPT [SCRIPT_ARGUMENTS]]
Arguments:
  SCRIPT absolute path to script that should be executed inside the container
         or relative path to PROJECT_ROOT_DIR.
         NB: In both cases the script must be inside PROJECT_ROOT_DIR
  SCRIPT_ARGUMENTS arguments that are passed to the script inside the docker
                   container (optional)
  "
  exit 0
fi

set -e
BDM_SCRIPT_DIR=$(readlink -e $(dirname "${BASH_SOURCE[0]}"))
PROJECT_ROOT_DIR=$(readlink -e $BDM_SCRIPT_DIR/../..)

# include util functions
. $BDM_SCRIPT_DIR/util.sh

DockerChecks
CheckImage $BDM_DOCKER_IMAGE

EchoNewStep "Stop and remove any previously created $BDM_CONTAINER container..."
docker stop $BDM_CONTAINER &> /dev/null || true
docker rm $BDM_CONTAINER &> /dev/null || true

# Check if host system has dedicated GPU
if docker run --rm --gpus=all hello-world &> /dev/null; then
  export BDM_ENABLE_GPU="--gpus=all"
fi

if [ "${BPE_ENABLE_SSH_XFORWARDING}" = "1" ]; then
  export BPE_SSH_XFORWARDING="--env XAUTHORITY=/home/testuser/.Xauthority
  --volume /tmp/.X11-unix:/tmp/.X11-unix"
 echo "INFO: Enabling SSH Xforwarding" 
 # Requires the following sshd configuration on the server side in /etc/ssh/sshd_config
 # X11Forwarding yes
 # X11DisplayOffset 10
 # X11UseLocalhost no
 #
 # after editing the file test that the configuration works: sudo sshd -t
 # and restart the serice: sudo service sshd restart
 #
 # Requirements on the client side:
 #  installed X server
 #  ssh connection with X forwarding enabled
fi

# set number of available process ids - see Paraview MPI issue
ulimit -u 8096 || true

EchoNewStep "Create new container..."

# --pid=host is required to use Intel Vtune's event-based sampling driver
# --volume /lib/modules:/lib/modules to access kernel modules
docker run \
  --name $BDM_CONTAINER \
  --user root \
  --net=host \
  --pid=host \
  --ipc=host \
  --hostname=docker-container \
  --privileged \
  $BDM_ENABLE_GPU \
  $BPE_SSH_XFORWARDING \
  --security-opt seccomp=unconfined \
  --env="DISPLAY" \
  --env="BDM_DOCKER_IMAGE_ID=$(docker images --format="{{.ID}}" $BDM_DOCKER_IMAGE)" \
  --env="BDM_HOST_ULIMIT_U=$(ulimit -u)" \
  --env="GIT_AUTHOR_NAME=$(git config user.name)" \
  --env="GIT_AUTHOR_EMAIL=$(git config user.email)" \
  --env="GIT_COMMITTER_NAME=$(git config user.name)" \
  --env="GIT_COMMITTER_EMAIL=$(git config user.email)" \
  --volume ${PROJECT_ROOT_DIR}:${PROJECT_ROOT_DIR} \
  --volume /dev/shm:/dev/shm \
  --volume /lib/modules:/lib/modules \
  --volume /dev/dri:/dev/dri \
  --volume /var/run/docker.sock:/var/run/docker.sock \
  --workdir $(readlink -e $PWD) \
  -dit \
  ${BDM_DOCKER_IMAGE} /entrypoint.sh `id -u` `id -g`

if [ "${BPE_ENABLE_SSH_XFORWARDING}" = "1" ]; then
  docker cp ~/.Xauthority $BDM_CONTAINER:/home/testuser/.Xauthority
fi

# if no script is specified, just output the info that a new container was started.
if [[ $# -lt 1 ]]; then
  EchoSuccess "A new container '$BDM_CONTAINER' was started and is running in the background."
  echo "You can connect to it by calling 'docker/exec.sh'"
  echo "from the directory $PROJECT_ROOT_DIR/bdm-paper-examples"
  exit 0
fi

BDM_SCRIPT=$1
shift
BDM_SCRIPT_ARGUMENTS=$@

# execute script
# avoid exit if $BDM_SCRIPT returns non zero exit code;
# returning exit code is done manually afterwards
set +e
BDM_SCRIPT_ABS=$(readlink -e $(GetAbsolutePath $BDM_SCRIPT))
if [[ "$BDM_SCRIPT_ABS" != $PROJECT_ROOT_DIR/* ]]; then
  echo "ERROR: Given script ($BDM_SCRIPT) is not inside $PROJECT_ROOT_DIR"
  echo "       Absolute path of given script determined to be: $BDM_SCRIPT_ABS"
  echo "       Please make sure you run a script within $PROJECT_ROOT_DIR and try again."
  echo "       Aborting."
  exit 1 
fi
echo ""
EchoNewStep "Execute ${BDM_SCRIPT}..."
docker exec \
  --user testuser \
  -ti \
  $BDM_CONTAINER \
  $BDM_SCRIPT_ABS $BDM_SCRIPT_ARGUMENTS

RETURN_VAL=$?
echo ""
EchoNewStep "Finished"
echo "$BDM_SCRIPT return code was: $RETURN_VAL"
echo "The container '$BDM_CONTAINER' is still running."
echo "You can connect to it by calling 'docker/exec.sh'"
echo "from the directory $PROJECT_ROOT_DIR/bdm-paper-examples"
exit $RETURN_VAL

