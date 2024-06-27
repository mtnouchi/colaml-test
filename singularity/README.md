# singularity deinition files

All commands shown here are assumed to be executed from the top level of the analysis directory, unless explicitly stated.

## CoLaML + jupyter

So far, the CoLaML version used in jupyter was implicitly recorded by the Git submodule.
From now on, the build policy will be changed to make it clearer the CoLaML version to be used.
For version consistency of dependent packages, batch analyses are also carried out on the images with jupyter.

- build: `singularity build --fakeroot singularity/sif/jupyter+colaml.[COMMIT_ID] singularity/def/jupyter+colaml.[COMMIT_ID].def`
- up: `singularity exec --home $(pwd):/home/jovyan -B $(readlink data) singularity/sif/jupyter+colaml.[COMMIT_ID] jupyter lab --port [SECRET] --no-browser`

\*`data` is a symbolic link to somewhere to store large data. Its contents are not tracked in this repository.

