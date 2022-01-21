import numpy as np
import sys
import os


assert len(sys.argv) == 3
npz_file = sys.argv[1]
dim = int(sys.argv[2])

data = np.load(npz_file)
files = data.files
data_new = {}
for f in files:
    embedding_cropped = data[f][:dim]
    embedding_l2normed = embedding_cropped / np.linalg.norm(embedding_cropped, ord=2)
    data_new[f] = embedding_l2normed

npz_file_new = os.path.splitext(npz_file)[0] + f'_dim{dim}'
np.savez_compressed(npz_file_new, **data_new)

