import os

# limit numpy/scipy threads
os.environ['OPENBLAS_NUM_THREADS'] \
= os.environ['MKL_NUM_THREADS'] \
= os.environ['VECLIB_NUM_THREADS'] \
= os.environ['OMP_NUM_THREADS'] \
= os.environ['NUMEXPR_NUM_THREADS'] \
= '1'

# limit numba threads
os.environ['NUMBA_DISABLE_JIT'] = '1'
os.environ['NUMBA_NUM_THREADS'] = '1'

# process on a single NUMA node
import psutil
p = psutil.Process(os.getpid())
p.cpu_affinity(cpus=range(10, 20))

# make sure numpy is working on a single thread
from threadpoolctl import threadpool_limits
threadpool_limits(1)

import argparse
import json
import time
import traceback
import warnings

import numba
import numpy as np

from colaml import *
from colaml.__main__ import phytbl_from_json
from myconfig import DATASET_DIR, ROOT_DIR
SIM01_DIR = DATASET_DIR/'01-simulation01'

parser = argparse.ArgumentParser()
parser.add_argument('dataID' , type=int)
parser.add_argument('conditionID')
parser.add_argument('lmax'   , type=int)
parser.add_argument('ncat'   , type=int)
parser.add_argument('ntips'  , type=int)
parser.add_argument('nOGs'   , type=int)
parser.add_argument('datarep', type=int)
parser.add_argument('runrep' , type=int)
    
class Timer():
    def __enter__(self):
        self._proc_start = time.process_time()
        self._perf_start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._proc_end = time.process_time()
        self._perf_end = time.perf_counter()
        
    def get(self):
        return dict(
            process_time = self._proc_end - self._proc_start, 
            perf_counter = self._perf_end - self._perf_start, 
        )

ROOT_SEED = 9768652837

def bench(run):
    path = SIM01_DIR/run.conditionID/f'{run.conditionID}-rep{run.datarep:02d}.json.gz'
    phytbl, columns = phytbl_from_json(path, run.lmax)
    approx_rate = phytbl.min_changes.mean() / phytbl.tree.branch_lengths.sum()
    distr_kw = dict(
        cpy_root_probs=np.ones(run.lmax + 1), 
        cat_root_probs=np.ones(run.ncat), 
        cpy_change_rates=(2, approx_rate / 2),
        cat_switch_rates=(3, approx_rate / 3 * 0.1),
    )

    mmm = MarkovModulatedTreeModel(
        run.lmax+1, run.ncat, MarkovModulatedBDARD, 
        init_params_method='skip'
    )
    
    for trial in range(3):
        try:
            rng = np.random.default_rng([ROOT_SEED, run.dataID, trial])
            mmm.init_params_random(rng=rng, distr_kw=distr_kw)
            with Timer() as timer:
                mmm.fit(phytbl, method='EM', max_rounds=50, show_progress=False, stop_criteria=(0,0))
        except Exception as err:
            warnings.warn(f'In {run}, trial#{trial+1}\n'+traceback.format_exc())
            continue
        else:
            return vars(run) | dict(trial=trial) | timer.get()
    else:
        raise RuntimeError(f'fitting failure possibly due to numerical issues\nIn {run}.')
    
if __name__ == '__main__':
    run = parser.parse_args()
    result = bench(run)
    print(json.dumps(result))
