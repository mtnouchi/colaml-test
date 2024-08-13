from copy import deepcopy

import pandas as pd


def filter_table(phytbl, columns=None, max_missing=0.05, adjust_branch=True):
    from colaml.misc.parsimony import mean_mp_changes
    from colaml.phyTables import ExtantPhyTable

    counts = pd.DataFrame.from_dict(phytbl.to_dict(), orient='index', columns=columns)
    filt_counts = counts.loc[:, counts.ne(0).sum() > phytbl.tree.ntips * max_missing]
    filt_phytbl = ExtantPhyTable(
        filt_counts.T.to_dict(orient='list'), deepcopy(phytbl.tree)
    )

    if adjust_branch:
        filt_phytbl.tree.branch_lengths = mean_mp_changes(filt_phytbl).mean(axis=1)

    return filt_phytbl, filt_counts.columns.to_list()
