#!/bin/bash
#SBATCH --array 1-1000%80
#SBATCH --output data/batch/02-bacteria-map/log/%x.stdxxx-%3a
set -eu -o pipefail

cd $SLURM_SUBMIT_DIR
eval `awk -v ARRAYID=$(( $SLURM_ARRAY_TASK_ID+151 )) -F "\t" 'NR==ARRAYID {print $NF}' notebooks/fit-to-real-data/240716-batch-job-array-bacteria-map.txt`
