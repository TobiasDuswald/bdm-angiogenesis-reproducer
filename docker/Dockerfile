# -----------------------------------------------------------------------------
#
# Copyright (C) The BioDynaMo Project.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# See the LICENSE file distributed with this work for details.
# See the NOTICE file distributed with this work for additional information
# regarding copyright ownership.
#
# -----------------------------------------------------------------------------

FROM nvidia/cuda:11.0-devel-ubuntu20.04 

MAINTAINER Lukas Breitwieser


# This will avoid tzdata package from requesting user interaction (tzdata is a
# dependency of one of the prerequisites of PyEnv)
RUN apt-get update && apt-get install -y sudo
RUN if ! [ -L /etc/localtime ]; then \
      sudo ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime; \
    fi

RUN apt-get update && apt-get install -y \
  git \
  man \
  software-properties-common \
  wget \
  xvfb \
  time

RUN git config --system user.name "Test User" && \
    git config --system user.email user@test.com

RUN groupadd -g 1000 testuser && \
    useradd -u 1000 -g 1000 -m -c "Testuser" testuser && \
    passwd --delete testuser && \
    echo "testuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER testuser

 # Required to add Kitware ppa below
RUN sudo apt-get update && sudo apt-get install apt-transport-https

# Add ppa for newer CMake version
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | sudo apt-key add -
RUN sudo apt-add-repository "deb https://apt.kitware.com/ubuntu/ focal main"

RUN sudo apt update && sudo apt install -y \
  cmake \
  make \
  gcc \
  g++ \
  libopenmpi-dev \
  libomp5 \
  libomp-dev \
  libnuma-dev \ 
  freeglut3-dev \
  libpthread-stubs0-dev \
  valgrind \
  clang-format \
  clang-tidy \
  doxygen \
  graphviz \
  lcov \
  gcovr \
  libxml2-dev \
  curl \
  libssl-dev \
  zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  xz-utils \
  tk-dev \
  libffi-dev \
  liblzma-dev \
  python-openssl \
  libjemalloc-dev \
  lshw \
  sysbench \
  cloc \
  rsync \
  maven 

# Install pyenv
RUN curl https://pyenv.run | bash

# Install python 3.8.0 and python packages
RUN /bin/bash -c '\
  export PATH="$HOME/.pyenv/bin:$PATH" && \
  eval "$(pyenv init -)" && \
  PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.9.1 && \
  pyenv shell 3.9.1 && \
  python -m pip install \
  nbformat \
  jupyter \
  metakernel \
  numpy \
  scipy \
  matplotlib \
  statistics \
  pygal \
  pandas \
  seaborn \
  glances'

# preserve the environment variable BDM_LOCAL_LFS when calling scripts with
# sudo
RUN echo "Defaults env_keep += \"BDM_LOCAL_LFS\"" | sudo tee -a /etc/sudoers

RUN sudo apt update && sudo apt install -y ffmpeg numactl mesa-utils vim mlocate htop tig

# Prepare maven for offline usage 
COPY pom.xml /home/testuser/pom.xml
RUN cd /home/testuser && mvn clean package 
COPY mvn-settings.xml /home/testuser/.m2/settings.xml

# Cuda installation in base docker image is missing entire `samples` directory
RUN sudo mkdir -p /usr/local/cuda/samples/common/inc/
COPY helper_math.h /usr/local/cuda/samples/common/inc/

# Profiling environment
COPY setup-profiling-env.sh /home/testuser
RUN sudo chmod +x /home/testuser/setup-profiling-env.sh
RUN cd /home/testuser && ./setup-profiling-env.sh

# vim
COPY vim/.vimrc /home/testuser/.vimrc
COPY vim/.vimrc.plugins /home/testuser/.vimrc.plugins
COPY vim/setup-vim.sh /home/testuser
RUN sudo chmod +x /home/testuser/setup-vim.sh
RUN cd /home/testuser && ./setup-vim.sh

# BDM_LOCAL_LFS 
# Include third_party packages so they don't need to be downloaded.
RUN mkdir -p /home/testuser/bdm-local-lfs/third-party && \
    cd /home/testuser/bdm-local-lfs/third-party && \
    wget --progress=dot:giga http://biodynamo-lfs.web.cern.ch/biodynamo-lfs/third-party/root_v6.22.06_python3.9_ubuntu-20.04.tar.gz && \
    wget --progress=dot:giga http://biodynamo-lfs.web.cern.ch/biodynamo-lfs/third-party/qt_v5.12.10_ubuntu-20.04.tar.gz && \
    wget --progress=dot:giga http://biodynamo-lfs.web.cern.ch/biodynamo-lfs/third-party/paraview_v5.9.0_ubuntu-20.04_default.tar.gz

# Update pyenv
RUN /bin/bash -c '\
  export PATH="$HOME/.pyenv/bin:$PATH" && \
  pyenv update'

# Recursive chown is incredibly slow in docker https://github.com/docker/for-linux/issues/388
# -> Give other users full permission to skip this step when UID and GID are changed.
RUN sudo chmod -R o=rwX /home/testuser

# required by optim
RUN sudo apt-get -y install libgsl-dev libarmadillo-dev

# Install Intel oneAPI
# kmod and msr-tools packages required to use event-based sampling driver
RUN wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | gpg --dearmor | sudo tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" | sudo tee /etc/apt/sources.list.d/oneAPI.list && \
    sudo apt update && \
    sudo apt install -y kmod msr-tools intel-basekit

# Fix bug when starting Intel advisor (error while loading shared libraries: libgtk-x11-2.0.so.0)
RUN sudo apt-get install -y libgtk2.0-0

# Add missing key
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6AF7F09730B3F0A4

# Install debugging symbols
#
# https://wiki.ubuntu.com/Debug%20Symbol%20Packages
# https://stackoverflow.com/questions/64893723/how-to-install-libstdc6-debug-symbols-on-ubuntu-20-04
# Procedure to find the debug symbol package names
#    # 1. Search which package installed file with missing debug info
#    $ dpkg -S /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.28
#    libstdc++6:amd64: /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.28
#    # or
#    $ apt-file search /lib/x86_64-linux-gnu/libgomp.so.1
#    libgomp1: /usr/lib/x86_64-linux-gnu/libgomp.so.1
#    libgomp1: /usr/lib/x86_64-linux-gnu/libgomp.so.1.0.0
#
#
#    # 2. Search package names 
#    $ apt search libgomp1-dbg*
#    Sorting... Done
#    Full Text Search... Done
#    libgomp1-dbgsym/focal-updates,now 10.3.0-1ubuntu1~20.04 amd64 [installed]
#      debug symbols for libgomp1
#
#    # 3. Install 
#    sudo apt install libgomp1-dbgsym
#
RUN echo "deb http://ddebs.ubuntu.com $(lsb_release -cs) main restricted universe multiverse\
\ndeb http://ddebs.ubuntu.com $(lsb_release -cs)-updates main restricted universe multiverse\
\ndeb http://ddebs.ubuntu.com $(lsb_release -cs)-proposed main restricted universe multiverse" | \
  sudo tee -a /etc/apt/sources.list.d/ddebs.list && \
  sudo apt-get install -y ubuntu-dbgsym-keyring && \
  sudo apt-get update && \
  sudo apt-get install -y \
                       g++9-dbgsym \
                       libgomp1-dbgsym \
                       libjemalloc2-dbgsym \
                       libnuma1-dbgsym \
                       libopenmpi3-dbgsym \
                       zlib1g-dbgsym \
                       libc6-dbg \
                       libstdc++6-9-dbg

# Install apt-file
RUN sudo apt-get install -y apt-file && sudo apt-file update

# create alias to 
RUN echo 'alias vtune-gui="/opt/intel/oneapi/vtune/latest/bin64/vtune-gui"' >> /home/testuser/.bashrc
RUN echo 'alias advisor-gui="/opt/intel/oneapi/advisor/latest/bin64/advisor-gui"' >> /home/testuser/.bashrc

COPY entrypoint.sh /entrypoint.sh 
