# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://zenodo.org/record/5121618
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#

BDM_DOCKER_DIR=$(readlink -e $(dirname "${BASH_SOURCE[0]}"))

# Image name and container name
export BDM_DOCKER_IMAGE_VERSION=v7
export BDM_DOCKER_IMAGE=bdm-publication-image-${BDM_DOCKER_IMAGE_VERSION}
if [ ! -f $BDM_DOCKER_DIR/container-${BDM_DOCKER_IMAGE_VERSION}.name ]; then
  echo "bdm-publication-${BDM_DOCKER_IMAGE_VERSION}-$RANDOM" > "$BDM_DOCKER_DIR/container-${BDM_DOCKER_IMAGE_VERSION}.name"
fi
export BDM_CONTAINER=$(cat "$BDM_DOCKER_DIR/container-${BDM_DOCKER_IMAGE_VERSION}.name")

function CheckDockerInstalled {
  if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker command not found."
    echo "       It looks like docker is not installed on your system."
    echo "       Please follow the instructions at the following link and retry."
    echo "       https://docs.docker.com/engine/install"
    echo "       Aborting."
    return 1
  fi
}

function CheckDockerRunning {
  if ! docker info &> /dev/null; then
    echo "ERROR: It seems that the docker daemon is not running."
    echo "       Please start the docker daemon and retry."
    echo "       Aborting."
    echo "       Here the output of 'docker info':"
    docker info || true
    return 1
  fi
  return 0
}

function CheckDockerVersion {
  local DOCKER_VERSION=$(docker version -f "{{.Server.Version}}")
  local DOCKER_VERSION_MAJOR=$(echo "$DOCKER_VERSION"| cut -d'.' -f 1)
  local DOCKER_VERSION_MINOR=$(echo "$DOCKER_VERSION"| cut -d'.' -f 2)
  local DOCKER_VERSION_BUILD=$(echo "$DOCKER_VERSION"| cut -d'.' -f 3)

  local RET_VAL=1
  if [ "${DOCKER_VERSION_MAJOR}" -eq 19 ]; then
    if [ "${DOCKER_VERSION_MINOR}" -ge 0 ]; then
      if [ "${DOCKER_VERSION_BUILD}" -ge 3 ]; then
        # Docker version >= 19.0.3
        RET_VAL=0
      fi
    fi
  elif [ "${DOCKER_VERSION_MAJOR}" -gt 19 ]; then
    # Docker version >= 20
    RET_VAL=0
  fi

  if [ $RET_VAL -eq 0 ]; then
    return $RET_VAL
  fi

  echo "ERROR: Docker version found ${DOCKER_VERSION}"
  echo "       Minimum required version: 19.0.3"
  echo "       Please update your docker version and try again."
  echo "       Aborting."
  return 1
}

function CheckNonSudoDocker {
  # check if docker socket exists (-S file exists and is a socket)
  if [ ! -S "/var/run/docker.sock" ]; then
    echo "WARNING: It seems that the docker daemon is not running."
    echo "         The file /var/run/docker.sock does not exist."
    echo "         Another explanation would be that the docker "
    echo "         daemon uses a non-default socket."
  elif ! test -r /var/run/docker.sock; then
    echo "WARNING: It seems that your user (`whoami`) doesn't have the rights to"
    echo "         run docker commands."
    echo "         Please follow the instructions at the following link and try again."
    echo "         https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"
    echo "         Another explanation would be that the docker "
    echo "         daemon uses a non-default socket."
    echo "         We tested the location: /var/run/docker.sock"
  fi
}

function CheckImage {
  local OUTPUT=$(docker run --rm $1 echo hello-world)
  if [ "$OUTPUT" != "hello-world" ]; then
    echo "ERROR: Docker check for image $1 failed."
    echo "       Test command: docker run $1 echo hello-world"
    echo "       Expected output: hello-world"
    echo "       Actual   output: $OUTPUT"
    echo "       Please make sure your docker installation is working and try again."
    echo "       Aborting."
    return 1
  fi
  return 0
}

function DockerChecks {
  # don't reorder
  CheckDockerInstalled
  CheckNonSudoDocker
  CheckDockerRunning
  CheckDockerVersion
}

# Return absolute path.
# If absolute path is given as parameter it is returned as is. Otherwise it gets converted.
# Arguments:
#  $1 path (absolute or relative)
function GetAbsolutePath {
  if [[ $# -ne 1 ]]; then
    echo "ERROR in GetAbsolutePath: Wrong number of arguments"
    exit 1
  fi

  if [[ "$1" = /* ]]; then
    echo "$1"
  else
    echo "${PWD}/${1}"
  fi
}

BDM_ECHO_PURPLE='\033[95m'
BDM_ECHO_CYAN='\033[96m'
BDM_ECHO_DARKCYAN='\033[36m'
BDM_ECHO_BLUE='\033[94m'
BDM_ECHO_GREEN='\033[92m'
BDM_ECHO_YELLOW='\033[93m'
BDM_ECHO_RED='\033[91m'
BDM_ECHO_BOLD='\033[1m'
BDM_ECHO_UNDERLINE='\033[4m'
BDM_ECHO_RESET='\033[0m'

function EchoSuccess {
  echo -e "${BDM_ECHO_BOLD}${BDM_ECHO_GREEN}$@${BDM_ECHO_RESET}"
}

function EchoError {
  echo -e "${BDM_ECHO_BOLD}${BDM_ECHO_RED}$@${BDM_ECHO_RESET}"
}

function EchoWarning {
  echo -e "${BDM_ECHO_BOLD}${BDM_ECHO_YELLOW}$@${BDM_ECHO_RESET}"
}

function EchoNewStep {
  echo -e "${BDM_ECHO_BOLD}${BDM_ECHO_BLUE}$@${BDM_ECHO_RESET}"
}

function EchoInfo {
  echo -e "${BDM_ECHO_PURPLE}$@${BDM_ECHO_RESET}"
}

