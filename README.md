# colaml-test

Test codes for CoLaML (joint inference of ancestral gene COntents and LAtent evolutionary modes by Maximum Likelihood method).

## Citation

CoLaML: Inferring latent evolutionary modes from heterogeneous gene content
Shun Yamanouchi, Tsukasa Fukunaga, Wataru Iwasaki
bioRxiv 2024.12.02.626417; doi: https://doi.org/10.1101/2024.12.02.626417

## file structure

```
├── colaml      # CoLaML code. See also https://github.com/mtnouchi/colaml.
├── config      # Mainly for managing paths
├── data        # public and intemediate data (symlink to elsewhere, not included)
├── datasets    # validation + use cases
├── etc         # utility functions   
├── metadata    # for datasets
├── notebooks   # codes to reproduce analyses
├── results     # processed data
└── singularity # container (for jupyter notebook + CoLaML)
```

