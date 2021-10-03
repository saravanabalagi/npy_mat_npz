import sys
import numpy as np
from scipy.io import loadmat
import os

assert len(sys.argv) > 1

files = sys.argv[1:]

for f in files:
    mat_vars = loadmat(f)
    mat_vars.pop('__version__')
    mat_vars.pop('__header__')
    mat_vars.pop('__globals__')

    fn = os.path.splitext(os.path.basename(f))[0]
    np.savez_compressed(fn, **mat_vars)
