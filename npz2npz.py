import numpy as np
import argparse
import os
from tqdm.auto import tqdm


parser = argparse.ArgumentParser()
parser.add_argument('npz_file')
parser.add_argument('--outfile')
args = parser.parse_args()

file = args.npz_file
npz = np.load(file)

d = {}
for key in tqdm(npz.files):
    key_new = key.replace('.yml', '.jpg')
    # key_new = key_new.replace('image', '')
    # value_new = npz[key].flatten()
    value_new = npz[key]
    d[key_new] = value_new

if args.outfile is None:
    file_dir = os.path.dirname(file)
    basename = os.path.splitext(os.path.basename(file))[0]
    file_new = os.path.join(file_dir, f'{basename}_converted.npz')
else:
    file_new = args.outfile
np.savez_compressed(file_new, **d)

