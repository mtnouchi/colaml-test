#!/bin/bash
#SBATCH --array 1-150%80
#SBATCH --output data/batch/02-bacteria/log/%x.stdxxx-%3a
set -eu -o pipefail

cd $SLURM_SUBMIT_DIR
eval `awk -v ARRAYID=$(( $SLURM_ARRAY_TASK_ID+1001 )) -F "\t" 'NR==ARRAYID {print $NF}' notebooks/fit-to-real-data/240701-batch-job-array-bacteria.txt`