import numpy as np
import argparse
import os
from pathlib import Path


def main():
    """
    Parse bin and save as npy or npz

    Example:
    expdir=path/to/dir
    python matbin2npz.py \
        $expdir/feats.bin \
        --dtype float32 \
        --outfile $expdir/feats_netvlad_dim4096 \
        --reshape -1 4096 \
        --filesdir $expdir/images
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("fpath", help="path to file")
    parser.add_argument("--dtype", help="data type")
    parser.add_argument("--outfile", help="output file path")
    parser.add_argument(
        "--reshape", nargs="+", type=int, help="reshape size separate by space"
    )
    parser.add_argument("--filesdir", help="dir with filenames for npz")
    args = parser.parse_args()

    print(f'Reading file {args.fpath}')
    arr = np.fromfile(args.fpath, dtype=args.dtype)

    if args.reshape:
        print(f'Arr current shape: {arr.shape}')
        print(f'Reshaping file to {args.reshape}')
        arr = arr.reshape(args.reshape)
    print(f'Arr shape: {arr.shape}')

    outfile = args.outfile if args.outfile else Path(args.fpath).stem
    if args.filesdir:
        print(f'Reading files in {args.filesdir}')
        files = os.listdir(args.filesdir)
        if len(files) != len(arr):
            raise IOError(f"Num Files: {len(files)} != Array Rows: {len(arr)}")
        files = sorted(files)
        print(f'Found {len(files)} files')

        print('Preparing NPZ dict')
        d = {}
        for k, v in zip(files, arr):
            d[k] = v

        print(f'Saving NPZ file {outfile}')
        np.savez_compressed(outfile, **d)
    else:
        print(f'Saving NPY file {outfile}')
        np.save(outfile, arr)

    print('Successfully saved')


if __name__ == "__main__":
    main()
