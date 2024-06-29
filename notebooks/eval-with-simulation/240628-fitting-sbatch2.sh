#!/bin/bash
#SBATCH --array 1-900%80
#SBATCH --output data/batch/01-simulation01/log/%x.stdxxx-%3a
set -eu -o pipefail

cd $SLURM_SUBMIT_DIR
eval `awk -v ARRAYID=$(( $SLURM_ARRAY_TASK_ID+1001 )) -F "\t" 'NR==ARRAYID {print $9}' notebooks/eval-with-simulation/240628-batch-job-array.txt`
