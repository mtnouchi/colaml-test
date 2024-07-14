import numpy as np
from scipy.optimize import linprog
    
def earth_movers_dist(src, dst, cost):
    """
    Computes the Earth mover's distance (EMD)
    
    Parameters
    ----------
    src  : NDArray
        Source distribution
    dst  : NDArray
        Destimation distribution
    cost : NDArray
        Cost matrix where `cost[i, j]` represents the unit cost of 
        transport from `i`-th group in `src` to `j`-th group in `dst`
        
    Returns
    -------
    distance : float
        EMD between `src` and `dst`
    flow : NDArray
        Optimal flow matrix where `flow[i, j]` represents the flow 
        from `src[i]` to `dst[j]` such that the total cost is minimal
    """
    nsrc, = src.shape
    ndst, = dst.shape
    assert cost.shape == (nsrc, ndst), (cost.shape, nsrc, ndst)
    
    # P1 = src & 1P = dst
    A = np.vstack([
        np.kron(np.eye(nsrc), np.ones(ndst)), 
        np.kron(np.ones(nsrc), np.eye(ndst)), 
    ])
    b = np.hstack([src, dst])
    result = linprog(cost.reshape(-1), A_eq=A, b_eq=b)
    assert result.success
    
    return result.fun, result.x.reshape(nsrc, ndst)
