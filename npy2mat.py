import sys
from numpy import load
from scipy.io import savemat

assert len(sys.argv) > 1

files = sys.argv[1:]

for f in files:
   data = load(f)
   fn = f.replace('.npy', '')
   fn = fn.replace('.', '_')
   fn = fn + '.mat'
   savemat(fn, {fn : data})
