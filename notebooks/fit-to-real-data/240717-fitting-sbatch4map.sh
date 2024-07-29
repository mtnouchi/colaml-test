#!/bin/bash
#SBATCH --array 1-1000%80
#SBATCH --output data/batch/03-fish-map/log/%x.stdxxx-%3a
set -eu -o pipefail
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1

cd $SLURM_SUBMIT_DIR
eval `awk -v ARRAYID=$(( $SLURM_ARRAY_TASK_ID+151 )) -F "\t" 'NR==ARRAYID {print $NF}' notebooks/fit-to-real-data/240717-batch-job-array-fish-map.txt`
