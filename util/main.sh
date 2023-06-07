# Statement:
# The docker infrastructure used here was developed by Lukas Breitwieser for
# his published research work. 
# It is available at https://zenodo.org/record/5121618
# Here we simply reuse it with minor modifications.
#
# File Author: Lukas Breitwieser
#

export PROJECT_ROOT_DIR=$(readlink -e $(dirname "${BASH_SOURCE[0]}")/../..)
export INSTALL_DIR=$PROJECT_ROOT_DIR/opt
export RESULT_DIR=$PROJECT_ROOT_DIR/bdm-paper-examples/result
export RESULT_METADATA_DIR=$RESULT_DIR/metadata
export TMP_DIR=$(dirname $(mktemp -u))

if [ $(echo "$PROJECT_ROOT_DIR" | grep -c " ") != 0 ]; then
  echo "ERROR: The project root path contains (a) space(s)."
  echo "       Detected PROJECT_ROOT_DIR: \"${PROJECT_ROOT_DIR}\""
  echo "       Please move the contents of PROJECT_ROOT_DIR to a path that doesn't contain spaces and try again."
  echo "       Aborting."
  exit -1
fi

# determine machine specific configuration
export MACHINE_SPECIFIC_DIR=$PROJECT_ROOT_DIR/bdm-paper-examples/util/machine-specific/$(hostname)
if [ ! -d "$MACHINE_SPECIFIC_DIR" ]; then
  echo "ERROR: Could not find directory with machine specific configuration files!"
  echo "       ($MACHINE_SPECIFIC_DIR)"
  echo "       Please copy one of the directories in dir util/machine-specific"
  echo "       and adapt the files accordingly."
  exit -1
fi
if [ ! -e "$MACHINE_SPECIFIC_DIR/env.sh" ]; then
    echo "ERROR: Could not find machine specific env.sh file!"
    echo "       ($MACHINE_SPECIFIC_DIR/env.sh)"
    echo "       Please create it."
    exit -1
fi
if [ ! -e "$MACHINE_SPECIFIC_DIR/prerequisites.sh" ]; then
    echo "ERROR: Could not find machine specific prerequisites.sh file!"
    echo "       ($MACHINE_SPECIFIC_DIR/prerequisites.sh)"
    echo "       Please create it."
    exit -1
fi

# CPU info:
# based on `numactl -H` and
# cat /sys/devices/system/cpu/cpu**/topology/thread_siblings_list
#
# CPU1: [0-13] and [28-41]
# CPU2: [14-27] and [42-55]

# Returns the number of CPU cores on numa node 0 
# excluding hyperthreads
function CPUCountNuma {
  $PROJECT_ROOT_DIR/bdm-paper-examples/util/get_cpus_in_numa.py
}

# Returns the number of CPU cores including hyperthreads
function CPUCount {
  if [ `uname` = "Darwin" ]; then
    sysctl -n hw.ncpu
  else
    grep -c ^processor /proc/cpuinfo
  fi
}

# openmp environment variables
export OMP_PROC_BIND=true
export OMP_DISPLAY_ENV=true

export DEFAULT_BPE_REPEAT=3
if [ -z "$BPE_REPEAT" ]; then
  export BPE_REPEAT=$DEFAULT_BPE_REPEAT
elif [ "$BPE_REPEAT" != "$DEFAULT_BPE_REPEAT" ]; then
  echo "WARNING: BPE_REPEAT was set to non-standard value: $BPE_REPEAT"
fi

function scalabilitySequence {
  local NUM_CPUS=$1
  local NUM_MEASUREMENTS=$2

  local INCREMENT=$(($NUM_CPUS / $NUM_MEASUREMENTS))
  if [[ $INCREMENT -lt 2 ]]; then
    seq 1 $NUM_CPUS
  else
    seq 1 ; seq $INCREMENT $INCREMENT $NUM_CPUS 
  fi
}

export DEFAULT_BPE_SCALABILITY=$(scalabilitySequence $(CPUCount) 8)
if [ -z "$BPE_SCALABILITY" ]; then
  export BPE_SCALABILITY=$DEFAULT_BPE_SCALABILITY
elif [ "$BPE_SCALABILITY" != "$DEFAULT_BPE_SCALABILITY" ]; then
  echo "WARNING: BPE_SCALABILITY was set to non-standard value: $BPE_SCALABILITY"
fi

if [ ! -z "${BPE_NO_CLEANBUILD}" ]; then
  echo "WARNING: BPE_NO_CLEANBUILD was set"
fi

# Check minimum required OpenGL version
function CheckOpenGLVersion {
  local OPENGL_VERSION=$(glxinfo | awk '/OpenGL core profile version/ {print $6}')
  local OPENGL_VERSION_MAJOR=$(echo "$OPENGL_VERSION"| cut -d'.' -f 1)
  local OPENGL_VERSION_MINOR=$(echo "$OPENGL_VERSION"| cut -d'.' -f 2)

  local RET_VAL=0
  if [ "${OPENGL_VERSION_MAJOR}" -ge 3 ] && \
     [ "${OPENGL_VERSION_MINOR}" -ge 3 ]; then
    # OpenGL version >= 3.3
    RET_VAL=0
  else
    RET_VAL=1
    echo "ERROR: OpenGL version found ${OPENGL_VERSION}"
    echo "       Minimum required version: 3.3"
    echo "       Your graphics hardware/driver doesn't support the minimum required version."
    echo "       Please fix this issue and try again."
    echo "       Here the complete output of 'glxinfo | grep OpenGL'"
    echo ""
    glxinfo | grep OpenGL
    echo ""
    echo "       Aborting."
  fi
  return $RET_VAL
}

# Executes a given command with the specified number of threads.
# Until the number of physical CPUS is reached, only physical cores are used.
# First, all physical cores on numa node 0 are used. If they are exhausted,
# physical cores on numa node 1 are used, ...
# Once the number of THREADS exceeds the number of physical cores, another strategy
# is followed. All physical cores are used. The remaining number of hyperthreads
# are evenly distributed among numa nodes.
# \see `numactl -h` and `/proc/cpuinfo`
# Arguments:
#   \$1 number of THREADS
#   \$@ command with parameters
function bdmTaskset {
  local NUM_THREADS=$1
  shift
  taskset -c $($PROJECT_ROOT_DIR/bdm-paper-examples/util/get_cpu_list.py $NUM_THREADS) "$@"
}

# Executes a given command with the specified number of physical CPUS with their.
# available hyperthreads.
# \see `numactl -h` and `/proc/cpuinfo`
# Arguments:
#   \$1 number of CPUS
#   \$@ command with parameters
function bdmTasksetPhysicalCpus {
  local NUM_CPUS=$1
  shift
  taskset -c $($PROJECT_ROOT_DIR/bdm-paper-examples/util/get_physical_cpu_list.py $NUM_CPUS true) "$@"
}

# Execute a given command 5 times and sleep one second between invocations
function repeat {
  for i in $(seq 0 $(($BPE_REPEAT - 1))); do
    echo ""
    echo "---------------------------------------------------------------------"
    echo "Start `date`"
    echo "$@"
    echo "Iteration: $i"
    echo ""
    "$@"
    echo ""
    echo "End   `date`"
    echo "---------------------------------------------------------------------"
    sleep 1
  done
}

function extract {
  local BENCH_LOG=$1
  local RESULT_FILE="${2}-${4}"
  local PATTERN=$3 
  local SUFFIX=$4

  cat $BENCH_LOG | grep -Eo "$PATTERN" | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' > $RESULT_FILE || rm $RESULT_FILE
}

# Run a benchmark. The given command will be executed using repeat
# Arguments:
#   $1 THREADS parameter to tell taskset on which threads the benchmark should be executed
#   $2 RESULT_FILE
#   $@ CMD benchmark command
function benchmarkIC {
  local THREADS=$1
  shift
  local RESULT_FILE=$1
  shift

  # create directory of RESULT_FILE and delete RESULT_FILE if it existed before
  mkdir -p $(dirname $RESULT_FILE)
  rm $RESULT_FILE &>/dev/null || true
  touch $RESULT_FILE

  local BENCH_METADATA_DIR=$RESULT_METADATA_DIR/benchmark/$(realpath --relative-to=$RESULT_DIR $RESULT_FILE | cut -f 1 -d '.')
  mkdir -p $BENCH_METADATA_DIR
  rm $BENCH_METADATA_DIR/* &>/dev/null || true

  # collect system performance data
  #  start with empty PYTHONPATH - there is a conflict with BDM/Paraview
  #  PYTHONPATH
  # pkill -f "glances -q -t 5" || true
  # PYTHONPATH="" nice -n 19 \
  #   glances -q -t 5 \
  #   --export csv \
  #   --export-csv-file $BENCH_METADATA_DIR/glances.csv &

  # sleep a bit to capture system state before the start of the benchmark
  sleep 7

  local BENCH_LOG=$BENCH_METADATA_DIR/log
  repeat bdmTaskset "$THREADS" "$@" >> $BENCH_LOG 2>&1
  cat $BENCH_LOG

  EXTRACT_PATTERN='^RUNTIME [+-]?[0-9]+([.][0-9]+)? ms$'
  cat $BENCH_LOG | grep -Eo "$EXTRACT_PATTERN" | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' > $RESULT_FILE
  cat $BENCH_LOG | grep "^TOTAL RUNTIME" | sed "s|TOTAL RUNTIME ||g" > ${RESULT_FILE}.total
  extract $BENCH_LOG $RESULT_FILE '^Peak memory usage \(MB\)[[:space:]]+: [+-]?[0-9]+([.][0-9]+)?$' memory

  if [ ! -z $(type -t extractAdditional) ]; then
    extractAdditional $BENCH_LOG $RESULT_FILE
  fi
  sleep 7
  pkill -f "glances -q -t 5" || true
}

# Run a benchmark. The given command will be executed using repeat
# Arguments:
#   $1 CPUS parameter to tell taskset on which physical cpus the benchmark should be executed
#      corresponding threads of each CPU are used
#   $2 RESULT_FILE
#   $@ CMD benchmark command
function benchmarkIC_PhysicalCpus {
  local CPUS=$1
  shift
  local RESULT_FILE=$1
  shift

  # create directory of RESULT_FILE and delete RESULT_FILE if it existed before
  mkdir -p $(dirname $RESULT_FILE)
  rm $RESULT_FILE &>/dev/null || true
  touch $RESULT_FILE

  local BENCH_METADATA_DIR=$RESULT_METADATA_DIR/benchmark/$(realpath --relative-to=$RESULT_DIR $RESULT_FILE | cut -f 1 -d '.')
  mkdir -p $BENCH_METADATA_DIR
  rm $BENCH_METADATA_DIR/* &>/dev/null || true

  sleep 7

  local BENCH_LOG=$BENCH_METADATA_DIR/log
  repeat bdmTasksetPhysicalCpus "$CPUS" "$@" >> $BENCH_LOG 2>&1
  cat $BENCH_LOG

  EXTRACT_PATTERN='^RUNTIME [+-]?[0-9]+([.][0-9]+)? ms$'
  cat $BENCH_LOG | grep -Eo "$EXTRACT_PATTERN" | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' > $RESULT_FILE
  cat $BENCH_LOG | grep "^TOTAL RUNTIME" | sed "s|TOTAL RUNTIME ||g" > ${RESULT_FILE}.total
  extract $BENCH_LOG $RESULT_FILE '^Peak memory usage \(MB\)[[:space:]]+: [+-]?[0-9]+([.][0-9]+)?$' memory

  if [ ! -z $(type -t extractAdditional) ]; then
    extractAdditional $BENCH_LOG $RESULT_FILE
  fi
  sleep 7
}

# Run a benchmark. The given command will be executed using repeat
# Arguments:
#   $1 CPUS parameter to tell taskset on which cpus the benchmark should be executed
#   $2 CMD benchmark command
#   $3 RESULT_FILE
function benchmark {
  local CPUS=$1
  local CMD=$2
  local RESULT_FILE=$3

  benchmarkIC $CPUS $RESULT_FILE $CMD
}
# Run a benchmark. The given command will be executed using repeat
# Arguments:
#   $1 CPUS parameter to tell taskset on which cpus the benchmark should be executed
#   $2 RESULT_FILE
#   $3 GPU ID: which GPU to run the benchmark on
#   SIM PARAMS
function benchmarkGpu {
  CPUS=$1
  RESULT_FILE=$2
  BDM_GPU=$3
  shift
  shift
  shift

  # create directory of RESULT_FILE and delete RESULT_FILE if it existed before
  mkdir -p $(dirname $RESULT_FILE)
  rm $RESULT_FILE &>/dev/null || true
  touch $RESULT_FILE

  BENCH_METADATA_DIR=$RESULT_METADATA_DIR/benchmark/$(realpath --relative-to=$RESULT_DIR $RESULT_FILE | cut -f 1 -d '.')
  mkdir -p $BENCH_METADATA_DIR
  rm $BENCH_METADATA_DIR/* &>/dev/null || true

  # collect system performance data
  #  start with empty PYTHONPATH - there is a conflict with BDM/Paraview
  #  PYTHONPATH
  pkill -f "glances -q -t 5" || true
  PYTHONPATH="" nice -n 19 \
    glances -q -t 5 \
    --export csv \
    --export-csv-file $BENCH_METADATA_DIR/glances.csv &

  # sleep a bit to capture system state before the start of the benchmark
  sleep 7

  BENCH_LOG=$BENCH_METADATA_DIR/log
  for i in $(seq 0 $(($BPE_REPEAT - 1))); do
    echo ""
    echo "---------------------------------------------------------------------"
    echo "Start `date`"
    echo "bdmTaskset $CPUS $@ --inline-config="{ \"bdm::Param\": { \"preferred_gpu\": $BDM_GPU } }" >> $BENCH_LOG 2>&1"
    echo "Iteration: $i"
    echo ""
    taskset -c $($PROJECT_ROOT_DIR/bdm-paper-examples/util/get_cpu_list.py $CPUS) $@ --inline-config="{ \"bdm::Param\": { \"preferred_gpu\": $BDM_GPU } }" >> $BENCH_LOG 2>&1
    echo ""
    echo "End   `date`"
    echo "---------------------------------------------------------------------"
    sleep 1
  done
  cat $BENCH_LOG

  EXTRACT_PATTERN='^RUNTIME [+-]?[0-9]+([.][0-9]+)? ms$'
  cat $BENCH_LOG | grep -Eo "$EXTRACT_PATTERN" | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' > $RESULT_FILE
  cat $BENCH_LOG | grep "^TOTAL RUNTIME" | sed "s|TOTAL RUNTIME ||g" > ${RESULT_FILE}.total

  # sleep 7
  # pkill -f "glances -q -t 5" || true
}

function bdmTime {
  local START_TS=$(date +%s%N) 
  $@
  local RUNTIME=$((($(date +%s%N) - $START_TS)/1000000))
  echo "RUNTIME $RUNTIME"
}

# Benchmark arbitrary command. Doesn't have to be a simulation.
# The given command will be executed using repeat
# Arguments:
#   $1 CMD benchmark command
#   $2 RESULT_FILE
function benchmarkArbitraryCommand {
  local CMD=$1
  local RESULT_FILE=$2

  # create directory of RESULT_FILE and delete RESULT_FILE if it existed before
  mkdir -p $(dirname $RESULT_FILE)
  rm $RESULT_FILE &>/dev/null || true
  touch $RESULT_FILE

  local BENCH_METADATA_DIR=$RESULT_METADATA_DIR/benchmark/$(realpath --relative-to=$RESULT_DIR $RESULT_FILE | cut -f 1 -d '.')
  mkdir -p $BENCH_METADATA_DIR
  rm $BENCH_METADATA_DIR/* &>/dev/null || true

  # collect system performance data
  #  start with empty PYTHONPATH - there is a conflict with BDM/Paraview
  #  PYTHONPATH
  # pkill -f "glances -q -t 5" || true
  # PYTHONPATH="" nice -n 19 \
  #   glances -q -t 5 \
  #   --export csv \
  #   --export-csv-file $BENCH_METADATA_DIR/glances.csv &

  # sleep a bit to capture system state before the start of the benchmark
  sleep 7

  local BENCH_LOG=$BENCH_METADATA_DIR/log
  repeat bdmTime $CMD >> $BENCH_LOG 2>&1
  cat $BENCH_LOG

  cat $BENCH_LOG | grep "^RUNTIME" | sed "s|RUNTIME ||g" > $RESULT_FILE

  # sleep 7
  # pkill -f "glances -q -t 5" || true
}

# Measure runtime and memory consumption.
# Arguments:
#   $1 CPUS parameter to tell taskset on which cpus the benchmark should be executed
#   $2 CMD benchmark command
#   $3 RESULT_FILE_RUNTIME
#   $4 RESULT_FILE_MEMORY
function benchmarkRuntimeAndMemory {
  local CPUS=$1
  local CMD=$2
  local RESULT_FILE_RUNTIME=$3
  local RESULT_FILE_MEMORY=$4

  # create directory of RESULT_FILE and delete RESULT_FILE if it existed before
  mkdir -p $(dirname $RESULT_FILE_RUNTIME)
  mkdir -p $(dirname $RESULT_FILE_MEMORY)
  rm $RESULT_FILE_RUNTIME &>/dev/null || true
  rm $RESULT_FILE_MEMORY &>/dev/null || true
  touch $RESULT_FILE_RUNTIME
  touch $RESULT_FILE_MEMORY

  local BENCH_METADATA_DIR=$RESULT_METADATA_DIR/benchmark/$(realpath --relative-to=$RESULT_DIR $RESULT_FILE_RUNTIME | cut -f 1 -d '.')
  mkdir -p $BENCH_METADATA_DIR
  rm $BENCH_METADATA_DIR/* &>/dev/null || true

  local BENCH_LOG=$BENCH_METADATA_DIR/log
  repeat bdmTaskset $CPUS /usr/bin/time -v $CMD >> $BENCH_LOG 2>&1
  cat $BENCH_LOG

  EXTRACT_PATTERN='^RUNTIME [+-]?[0-9]+([.][0-9]+)? ms$'
  cat $BENCH_LOG | grep -Eo "$EXTRACT_PATTERN" | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' > $RESULT_FILE_RUNTIME

  # extract memory and convert to MB
  cat $BENCH_LOG | grep "^	Maximum resident set size (kbytes):" | \
    sed "s|\tMaximum resident set size (kbytes): ||g" | \
    awk '{ print $1 / 1024.0 }' > $RESULT_FILE_MEMORY
}

# Run a scalability benchmark. The given command will be executed with
# increasing number of threads. Thr result files will be created in the
# given result directory
#
# Arguments:
#   $1 RESULT_DIR
#   $@ CMD benchmark command
function scalabilityBenchmark {
  local SIM_RESULT_DIR=$1
  shift

  for i in $BPE_SCALABILITY; do
    echo ""
    echo "Running with $i threads"

    local NUM_THREADS=$(printf "%03d" $i)
    export OMP_NUM_THREADS=$i
    benchmarkIC $i "$SIM_RESULT_DIR/${NUM_THREADS}-threads.csv" "$@"
  done
}

# Run a bdm static benchmark. Runs a cx3d comparison and scalability benchmark
# for AOS and SOA memory layouts.
#
# Arguments:
#   $1 command for bdm-cx3d benchmark
#   $2 result dir for bdm-cx3d benchmark
#   $3 command for scalability benchmark
#   $4 result dir for scalability benchmark
function bdmStaticBenchmark {
  # SOA layout
  #   compile
  compileAndInstallBdm $PROJECT_ROOT_DIR/biodynamo-static
  compileSimulation $BDM_SCRIPT_DIR

  #   comparison with cx3d
  export OMP_NUM_THREADS=1
  benchmark 1 "$1" "$2/bdm-static-soa.csv"

  #   scalability test
  scalabilityBenchmark "$3" "$4/bdm-static-soa"
  # ----------------------------------------------------------------------------

  # AOS layout
  #   compile
  compileAndInstallBdm $PROJECT_ROOT_DIR/biodynamo-static
  compileSimulation $BDM_SCRIPT_DIR -DCMAKE_CXX_FLAGS="-DSCALAR_BACKEND"

  #   comparison with cx3d
  export OMP_NUM_THREADS=1
  benchmark 1 "$1" "$2/bdm-static-aos.csv"

  #   scalability test
  scalabilityBenchmark "$3" "$4/bdm-static-aos"
}

# Compile and install BioDynaMo (clean build)
# Arguments:
#   $1 Path to BioDynaMo
#   $@ Additional cmake flags
function compileAndInstallBdm {
  pushd $1
  shift
  mkdir -p build && cd build
  if [ -z "${BPE_NO_CLEANBUILD}" ]; then
    ../util/clean-build-dir.sh . &> /dev/null || true
    if [ ! -z ${BPE_COMPLETE_CLEANBUILD} ]; then
      rm -rf third_party || true
    fi 
    cmake -Djemalloc=on -Dtest=off "$@" .. && make -j$(CPUCount)
  else
    make -j$(CPUCount)
  fi
  popd
}

# like `compileAndInstallBdm` but not a clean build
# Arguments:
#   $1 Path to BioDynaMo
function makeInstallBdm {
  pushd $1/build
  rm -rf $BDM_INSTALL_DIR/biodynamo-static/include/*
  make -j$(CPUCount) install
  popd
}

# Compiles a biodynamo simulation (clean build)
# Arguments:
#   $1 Path to simulation
#   $@ Additional cmake flags
function compileSimulation {
  cd $1
  shift
  mkdir -p build ; cd build
  if [ -z "${BPE_NO_CLEANBUILD}" ]; then
    rm -rf * ; cmake -Djemalloc=on "$@" .. && make -j$(CPUCount)
  else
    make -j$(CPUCount)
  fi
}

# like `compileSimulation` but not a clean build
# Arguments:
#   $1 Path to simulation
function makeSimulation {
  cd $1/build
  make -j$(CPUCount)
}

# Calls simulation with enabled export_visualization_ and moves the 
# output directory to DEST_DIR.
# Arguments:
#   DEST_DIR
#   SIMULATION PARAMS...
function visualize {
  local dest_dir=$1
  shift

  rm -rf output
  /usr/bin/time -v "$@" --inline-config='{"bdm::Param": { "export_visualization": true }}'
  mkdir -p $dest_dir
  rm -rf $dest_dir/output &>/dev/null || true
  mv output $dest_dir
}

# Calls the rendering script inside the given working directory.
# Arguments:
#   WORKING_DIR
#   RENDER_SCRIPT
function render {
  local WORKING_DIR=$1
  local RENDER_SCRIPT=$2

  cd ${WORKING_DIR}
  rm *.png || true
  OLD_OMP_NUM_THREADS=${OMP_NUM_THREADS}
  unset OMP_NUM_THREADS
  unset OMP_PROC_BIND
  ${ParaView_DIR}/bin/pvbatch $RENDER_SCRIPT
  export OMP_PROC_BIND=true
  export OMP_NUM_THREADS=${OLD_OMP_NUM_THREADS}
}

function pvOpen {
  pushd $1
  paraview output/$(ls -A output)/*pvsm
  popd
}

# This function collects metadata for a git repo in the cwd
function gitRepoMetadata {
  local SCRIPT=$(getScriptName)
  local REPRODUCE_DIR=$RESULT_DIR/reproduce
  local REPRODUCE_MD_DIR=$REPRODUCE_DIR/metadata/${SCRIPT}
  mkdir -p "${REPRODUCE_MD_DIR}"
  local WORKING_DIR=`pwd`

  echo ""
  # repo name
  local REPO_NAME=$(basename $PWD)

  echo "Repository:     $REPO_NAME"
  # last commit id
  echo "Last commit id: $(git rev-parse HEAD)"
  echo "git status"
  git rev-parse HEAD > ${REPRODUCE_MD_DIR}/$REPO_NAME.commit
  if [ "$(git diff HEAD | wc -l)" != "0" ]; then
    git diff HEAD > $REPRODUCE_MD_DIR/$REPO_NAME.patch
  fi
  git clone . $REPRODUCE_DIR/$REPO_NAME
}

function getScriptName {
  echo $(basename $0 2>/dev/null || echo "unknown") | sed "s|\.|_|g"
}

function captureReproductionData {
  local SCRIPT=$(getScriptName)
  local REPRODUCE_MD_DIR=$RESULT_DIR/reproduce/metadata/${SCRIPT}
  mkdir -p "${REPRODUCE_MD_DIR}"
  local WORKING_DIR=`pwd`

  cat /proc/self/status | awk '/VmPeak:/ {print $2}' > ${REPRODUCE_MD_DIR}/peak-memory-kb
  du -sm "${PROJECT_ROOT_DIR}" | awk '{print $1}' > ${REPRODUCE_MD_DIR}/disk-space-mb
  cd $WORKING_DIR
}

function verify {
  local SCRIPT=$(getScriptName)
  local REPRODUCE_MD_DIR=$PROJECT_ROOT_DIR/metadata/${SCRIPT}
  
  local RET_VAL=0
  if [ ! -z "$(ls -A $RESULT_DIR &> /dev/null)" ]; then
    echo "ERROR: RESULT_DIR ($RESULT_DIR) is not empty"
    echo "       Please empty ${RESULT_DIR} and try again."
    RET_VAL=1
  fi

  local WORKING_DIR=`pwd`

  if [ -f "${REPRODUCE_MD_DIR}/docker-image-id" ]; then
    echo "INFO: Checking docker image id ..."
    local IMAGE_ID=$(cat ${REPRODUCE_MD_DIR}/docker-image-id)
    if [ "$IMAGE_ID" != "$BDM_DOCKER_IMAGE_ID" ]; then
      echo "ERROR: Incorrect docker image id"
      echo "       Expected: $BDM_DOCKER_IMAGE_ID"
      echo "       Actual:   $IMAGE_ID"
      echo "       Please make sure" 
      echo "         * to run the script with docker/run.sh" 
      echo "         * and that you have the correct docker image"
      echo "       Afterwards try again."
      echo "       To ignore this check delete the file ${REPRODUCE_MD_DIR}/docker-image-id"
      return 1
    fi
  fi

  # check git repositories version
  for repo in "biodynamo" "bdm-paper-examples"; do
    if [ -f "${REPRODUCE_MD_DIR}/$repo.commit" ]; then
      cd "$PROJECT_ROOT_DIR/$repo"

      echo "INFO: Checking $repo for the correct commit id ..."
      local COMMIT=$(cat ${REPRODUCE_MD_DIR}/$repo.commit)
      if [ "$COMMIT" != "$(git rev-parse HEAD)" ]; then
        echo "ERROR: Incorrect $repo commit"
        echo "       Expected: $COMMIT"
        echo "       Actual:   $(git rev-parse HEAD)"
        echo "       Please change the $repo commit and try again."
        echo "       To ignore this check delete the file ${REPRODUCE_MD_DIR}/$repo.commit"
        return 1
      fi
      
      echo "INFO: Checking $repo for uncommited changes ..."
      if [ -f "${REPRODUCE_MD_DIR}/$repo.patch" ]; then
        if ! diff "$REPRODUCE_MD_DIR/$repo.patch" <(git diff HEAD) &>/dev/null; then
          echo "ERROR: The state of the $repo repository differs from the patch"
          echo "       found in: ${REPRODUCE_MD_DIR}/$repo.patch"
          echo "       Please stash any uncommited changes and apply the patch."
          echo "       To ignore this check delete the file ${REPRODUCE_MD_DIR}/$repo.commit"
          return 1
        fi
      elif [ "$(git diff HEAD | wc -l)" != "0" ]; then
        echo "ERROR: The $repo repository has uncommited changes."
        echo "       Please stash these changes and try again."
        echo "       To ignore this check delete the file ${REPRODUCE_MD_DIR}/$repo.commit"
        return 1
      fi
    fi
  done
  
  if [ -f "${REPRODUCE_MD_DIR}/peak-memory-kb" ]; then
    echo "INFO: Checking available memory ..."
    local REQUIRED_MEM=$(cat "$REPRODUCE_MD_DIR/peak-memory-kb")
    local AVAILABLE_MEM=$(awk '/MemAvailable/{print $2}' /proc/meminfo)
    if [ $AVAILABLE_MEM -lt $REQUIRED_MEM ]; then
        echo "ERROR: The system doesn't have enough available memory to run this script."
        echo "       Required [kB]:  $REQUIRED_MEM"
        echo "       Available [kB]: $AVAILABLE_MEM"
        echo "       To ignore this check delete the file ${REPRODUCE_MD_DIR}/peak-memory-kb"
        RET_VAL=1
    fi
  fi

  if [ -f "${REPRODUCE_MD_DIR}/disk-space-mb" ]; then
    echo "INFO: Checking available disk space ..."
    local REQUIRED_DISK=$(cat "$REPRODUCE_MD_DIR/disk-space-mb")
    local AVAILABLE_DISK=$(df -Pm . | tail -1 | awk '{print $4}')
    if [ $AVAILABLE_DISK -lt $REQUIRED_DISK ]; then
        echo "ERROR: The system doesn't have enough available disk space to run this script."
        echo "       Required [MB]:  $REQUIRED_DISK"
        echo "       Available [MB]: $AVAILABLE_DISK"
        echo "       To ignore this check delete the file ${REPRODUCE_MD_DIR}/disk-space-mb"
        RET_VAL=1
    fi
  fi

  cd $WORKING_DIR
  return $RET_VAL
}

function collectMetadata {
  cp $PROJECT_ROOT_DIR/bdm-paper-examples/util/reproduce/* $RESULT_DIR

  mkdir -p $RESULT_METADATA_DIR
  local LOG=$RESULT_METADATA_DIR/log
  echo "Start timestamp: $(date)" > $LOG

  local REPRODUCE_MD_DIR=$RESULT_DIR/reproduce/metadata/$(getScriptName)
  mkdir -p "${REPRODUCE_MD_DIR}"
  echo $BDM_DOCKER_IMAGE_ID > ${REPRODUCE_MD_DIR}/docker-image-id

  pushd $PROJECT_ROOT_DIR/bdm-paper-examples
  gitRepoMetadata >> $LOG
  cd $PROJECT_ROOT_DIR/biodynamo
  gitRepoMetadata >> $LOG
  popd
  
  $PROJECT_ROOT_DIR/bdm-paper-examples/util/system-info.sh &> $RESULT_METADATA_DIR/system-info
  $PROJECT_ROOT_DIR/bdm-paper-examples/util/lines-of-code.sh &> $RESULT_METADATA_DIR/lines-of-code
}

function createTarAndShaSum {
  pushd $RESULT_DIR &> /dev/null
  local RESULT_FILE=result-`getScriptName`.tar.gz
  # exclude tmp dir
  tar -zcf ${RESULT_FILE} `ls . | sed "s|tmp||g"`
  sha256sum ${RESULT_FILE} > ${RESULT_FILE}.sha256
  popd &> /dev/null
}

function passwordlessSudo {
  # The following command on CentOS overwrites sudo
  # but doesn't parse all arguments correctly
  # . scl_source enable devtoolset-7
  # already reported: https://bugzilla.redhat.com/show_bug.cgi?id=1319936i
  # -> use /usr/bin/sudo 
  # if sudo command does not exist return false
  command -v /usr/bin/sudo &>/dev/null || return
  # if sudo is not passwordless return false
  /usr/bin/sudo -n echo "test" &>/dev/null || return
  # if user does not have sudo rights return false
  /usr/bin/sudo -l -U $(whoami) &>/dev/null 
  return
}

source $MACHINE_SPECIFIC_DIR/env.sh

