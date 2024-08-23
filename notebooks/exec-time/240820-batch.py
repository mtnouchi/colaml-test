import os
import shlex
import subprocess

import numpy as np
import pandas as pd
from tqdm.auto import tqdm

from myconfig import DATASET_DIR, ROOT_DIR
SIM01_DIR = DATASET_DIR/'01-simulation01'
OUT_FILE = ROOT_DIR/'results'/'simulation-exec-time.jsonl'

os.chdir(os.path.dirname(__file__))

# clear files
subprocess.getoutput(f'> {OUT_FILE}')
subprocess.getoutput('> 240820-bench.log')

# machine info
subprocess.getoutput("lscpu | grep -i -e 'Model name' -e 'Socket(s)' -e 'numa' >> 240820-bench.log")
subprocess.getoutput("free -w >> 240820-bench.log")

conditions = pd.read_csv(SIM01_DIR/'conditions.tsv', sep='\t')
conditions_rep = pd.merge(
    conditions.assign(dummy=0), 
    pd.Series(range(1, 11), name='datarep').to_frame().assign(dummy=0), 
    on='dummy'
).drop(columns='dummy')

# randomize execution order　to average out external factors 
# such as CPU temperature and competing tasks
perm_seed = 4242424242
run_order = pd.concat([
    conditions_rep.sample(frac=1, random_state=np.array([perm_seed, i])).assign(runrep=i)
    for i in range(1, 11)
]).rename_axis('dataID').reset_index()

# run bench
for run in tqdm(run_order.itertuples(index=False)):
    args = ' '.join(map(str, run))
    cmd = f"""
    (PS4='$(date -Iseconds) '; set -x; python3 benchmark.py {args} >> {OUT_FILE}) >> 240820-bench.log 2>&1
    """
    subprocess.getoutput(cmd)
    