# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://zenodo.org/record/5121618
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#

#!/bin/bash

set -ex

CURRENT_WDIR=$(pwd)

sudo apt update

sudo apt install -y libkf5threadweaver-dev libkf5i18n-dev libkf5configwidgets-dev     libkf5coreaddons-dev libkf5itemviews-dev libkf5itemmodels-dev libkf5kio-dev     libkf5solid-dev libkf5windowsystem-dev libelf-dev libdw-dev cmake     extra-cmake-modules gettext libqt5svg5-dev
sudo apt install -y libkf5notifications-dev
sudo apt install -y linux-tools-5.8.0-23-generic
sudo apt install -y ninja-build

sudo strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
sudo mv /usr/bin/perf /usr/bin/perf.bk
sudo ln -s /usr/lib/linux-tools/5.8.0-23-generic/perf /usr/bin/perf

git clone https://github.com/KDAB/hotspot.git
cd hotspot
git checkout 1.3
git submodule update --init --recursive
mkdir build
cd build
cmake -GNinja ..
ninja

echo "export PATH=${CURRENT_WDIR}/hotspot/build/bin:$PATH" >> ~/.bashrc

cd $CURRENT_WDIR
git clone https://github.com/andikleen/pmu-tools.git
echo "export PATH=${CURRENT_WDIR}/pmu-tools:$PATH" >> ~/.bashrc

