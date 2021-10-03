import sys
import numpy as np
import scipy.io
from tqdm import tqdm
import glob
import os

assert len(sys.argv) > 1
matdirs = sys.argv[1:]

# dry run, validate
for matdir in matdirs:
    assert os.path.isdir(matdir), "Must be a dir with .mat files"

for matdir in matdirs:
# for matdir in tqdm(matdirs):
    files = glob.glob(f'{matdir}/*.mat')
    d = {}
    for f in files:
    # for f in tqdm(files, leave=False):
        mat_dict = scipy.io.loadmat(f)
        filename = os.path.splitext(os.path.basename(f))[0]
        key_first = ''
        for k in mat_dict.keys():
            if k not in ['__globals__', '__header__', '__version__']:
                key_first = k
                break
        d[filename] = mat_dict[key_first]

    npz_file = f'{matdir}.npz'
    np.savez_compressed(npz_file, **d)
