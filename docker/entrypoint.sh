#!/bin/bash

# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://zenodo.org/record/5121618
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#

if [[ $# != 2 ]]; then
  echo "Wrong number of arguments.
Description:
  Update user id and group id of the precompiled image such that 
  mapped volumes can be accessed with the same rights as on the host. 
  Files created by the container can also be accessed on the host without chowning.
Usage:
  $0 NEW_UID NEW_GID
  "
  exit 1
fi

set -e
BDM_NEW_UID=$1
shift
BDM_NEW_GID=$1

echo "127.0.1.1   `hostname`" >> /etc/hosts

# using usermod hangs for a long time:
# Bug report https://github.com/containers/podman/issues/1808
# -> Use sed
sed -i "s|testuser:x:1000:|testuser:x:${BDM_NEW_GID}:|g" /etc/group
sed -i "s|testuser:x:1000:1000:Testuser|testuser:x:${BDM_NEW_UID}:${BDM_NEW_GID}:Testuser|g" /etc/passwd
# chowning not necessary because in the Dockerfile we gave full permission to other users.
# Reason: recursive chown is incredibly slow in docker https://github.com/docker/for-linux/issues/388
/bin/bash
