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
PROJECT_ROOT_DIR=$(readlink -e $BDM_SCRIPT_DIR/../..)

# include util functions
. $BDM_SCRIPT_DIR/util.sh


BDM_CONTAINER_ID=$(docker inspect --format="{{.Id}}" "$BDM_CONTAINER")
echo "max memory usage in bytes"
BDM_MAX_USAGE_BYTES=$(cat /sys/fs/cgroup/memory/docker/$BDM_CONTAINER_ID/memory.max_usage_in_bytes)
echo "$BDM_MAX_USAGE_BYTES"
echo "max memory usage in GB"
echo $(($BDM_MAX_USAGE_BYTES/1024/1024/1024))
