# colaml-test

Test codes for CoLaML (joint inference of ancestral gene COntents and LAtent evolutionary modes by Maximum Likelihood method).

## Citation

**Author's Original Version**:  
CoLaML: Inferring latent evolutionary modes from heterogeneous gene content  
Shun Yamanouchi, Tsukasa Fukunaga, Wataru Iwasaki  
bioRxiv 2024.12.02.626417; doi: https://doi.org/10.1101/2024.12.02.626417

## File structure

```
├── colaml      # CoLaML code. See also https://github.com/mtnouchi/colaml.
├── config      # mainly for managing paths
├── data        # public and intemediate data (symlink to elsewhere, not included)
├── datasets    # validation + presentation of use cases
├── etc         # utility functions   
├── metadata    # for datasets
├── notebooks   # codes to reproduce analyses
├── results     # processed data
└── singularity # container (for jupyter notebook + CoLaML)
```

## Credits

Datasets were created using data from multiple sources. We acknowledge and give credit to the following databases:

- **[OrthoDB v11](https://data.orthodb.org/v11/download/)**
  - Copyright © [E Zdobnov lab](https://www.ezlab.org)
  - Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  - Primary article: [Kuznetsov D, Tegenfeldt F et al., NAR, 2023](https://doi.org/10.1093/nar/gkac998)

- **[The Fish Tree of Life](https://fishtreeoflife.org)**
  - Public domain.
  - Provided by Jonathan Chang.
  - Alternative access: [the Dryad digital data repository](https://doi.org/10.5061/dryad.fc71cp4)
  - Primary article: [Rabosky DL, Chang J, Title O et al., Nature, 2018](https://doi.org/10.1038/s41586-018-0273-1)

- **[Extended Data for A rooted phylogeny resolves early bacterial evolution](https://doi.org/10.6084/m9.figshare.12651074.v12)**
  - Copyright © Coleman GA, Davínet AA et al.
  - Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  - Primary article: [Coleman GA, Davínet AA et al., Science, 2021](https://doi.org/10.1126/science.abe0511)

- **Assembly summary of [NCBI RefSeq](https://ftp.ncbi.nlm.nih.gov/genomes/refseq)**
  - Provided by [The National Center for Biotechnology Information](https://www.ncbi.nlm.nih.gov) under [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/)

When using these datasets, please ensure compliance with the terms of the **CC BY 4.0** license for "OrthoDB" and "Extended Data for A rooted phylogeny resolves early bacterial evolution", including proper attribution.

We would like to express our sincere gratitude to **Jonathan Chang** for kindly assisting us with our inquiries.

We also referred to the following databases in our analysis:

- **[eggNOG DB v5](http://eggnog5.embl.de/download/eggnog_5.0/)**
  - Copyright © The EggNOG database Team
  - "eggNOG data and the eggNOG-mapper tool are open-source and fully free resources for academics. However, any kind of commercial usage requires explicit licensing; please contact info@biobyte.de for further information." (http://eggnog-mapper.embl.de, last accessed Feb. 16, 2025).

- **[COG2020](https://ftp.ncbi.nih.gov/pub/COG/COG2020/data/)**
  - Provided by [The National Center for Biotechnology Information](https://www.ncbi.nlm.nih.gov) under [NCBI Website and Data Usage Policies and Disclaimers](https://www.ncbi.nlm.nih.gov/home/about/policies/) 

