# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://zenodo.org/record/5121618
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#


ulimit -u 8000

export VTUNE_BIN_DIR=/opt/intel/oneapi/vtune/latest/bin64/
export ADVISOR_BIN_DIR=/opt/intel/oneapi/advisor/latest/bin64/
export PATH="/home/testuser/pmu-tools:$PATH"

# Python
export PATH="$HOME/.pyenv/bin:$PATH"
export PYENV_ROOT="$HOME/.pyenv"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
pyenv shell 3.9.1

# NetLogo
export PATH="$HOME/NetLogo-6.2.0:$PATH"

# Use xvfb in headless environments or if the X configuration 
# is not working
if [ -z "$DISPLAY" ] || ! glxinfo &>/dev/null; then
  echo "INFO: Use xvfb"
  export DISPLAY=:99.0
  $PROJECT_ROOT_DIR/biodynamo/util/xvfb-initd.sh start
fi

export BDM_LOCAL_LFS=~/bdm-local-lfs

# remove also third_party directory 
# container uses BDM_LOCAL_LFS to omit downloads
export BPE_COMPLETE_CLEANBUILD=1

