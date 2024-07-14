import numpy as np

def assign_mmm_category(ans, est):
    from scipy.optimize import linear_sum_assignment
    
    abs_perc_err = np.abs(
        np.asarray(est['cpy_change_rates'])[None,:,...]
         / np.asarray(ans['cpy_change_rates'])[:,None,...]
         - 1
    ).sum(axis=(2,3))
    ans_idx, est_idx = linear_sum_assignment(abs_perc_err)
    return ans_idx, est_idx

def _build_switch_matrix(rates):
    from math import isqrt
    
    rshape = np.asarray(rates).shape
    ncat = (1 + isqrt(1 + 8 * rshape[1])) // 2
    assert rshape == (2, ncat * (ncat - 1) // 2), f'invalid shape: {rshape}'
    
    R = np.full((ncat, ncat), np.nan)
    lower_mask = np.tri(ncat, dtype=bool, k=-1)
    upper_mask = lower_mask.T
    R[upper_mask], R[lower_mask] = rates
    return R

def mmm_param_dist(ans, est):
    from scipy.linalg import toeplitz
    from myutil import earth_movers_dist
        
    ncat, nst = np.asarray(est['cpy_root_probs']).shape
    ans_idx, est_idx = assign_mmm_category(ans, est)
    
    diffs = dict(
        cpy_change_rates = np.abs(
            np.asarray(est['cpy_change_rates'])[est_idx, ...]
             / np.asarray(ans['cpy_change_rates'])[ans_idx, ...]
             - 1
        ).mean(), 
        
        cpy_root_probs = np.array([
            earth_movers_dist(
                ans['cpy_root_probs'][a], 
                est['cpy_root_probs'][e], 
                toeplitz(range(nst))
            )[0]
            for a, e in zip(ans_idx, est_idx)
        ]).mean(), 
           
        cat_switch_rates = np.abs(
            _build_switch_matrix(est['cat_switch_rates'])[est_idx,:][:,est_idx]
            / _build_switch_matrix(ans['cat_switch_rates'])[ans_idx,:][:,ans_idx]
            - 1
        )[~np.eye(ncat, dtype=bool)].mean()
        if ncat > 1 else 
        np.nan,
     
        cat_root_probs = earth_movers_dist(
            np.asarray(ans['cat_root_probs'])[ans_idx], 
            np.asarray(est['cat_root_probs'])[est_idx], 
            1 - np.eye(ncat)
        )[0]
        if ncat > 1 else
        np.nan, 
    )
    
    return diffs