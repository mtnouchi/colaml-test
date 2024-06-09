# singularity deinition files

All commands shown here are assumed to be executed from the top level of the analysis directory, unless explicitly stated.

## jupyter

- build: `singularity build --fakeroot singularity/sif/jupyter.sif singularity/def/jupyter.def`
- up: `singularity exec --home $(pwd):/home/jovyan -B $(readlink data) singularity/sif/jupyter.sif jupyter lab --port XXXX --no-browser`

\*`data` is a symbolic link to somewhere to store large data. Its contents are not tracked in this repository.


