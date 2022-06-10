import numpy as np
from pathlib import Path
import argparse


def main():
    """
    Crop netvlad 4096 npz file to required dimensions and save NPZ

    Example:
    python netvlad_crop.py \
        $expdir/feats_dim4096.npz \
        --dim $dim \
        --outfile $expdir/feats_dim$dim
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("npz_file", help="path to NPZ file with dim 4096")
    parser.add_argument("--dim", type=int, help="required dims")
    parser.add_argument("--outfile", help="path to output file")
    args = parser.parse_args()

    print(f"Reading file {args.npz_file}")
    data = np.load(args.npz_file)

    dim = args.dim
    print(f"Cropping to dim {dim}")

    files = data.files
    data_new = {}
    for f in files:
        emb_cropped = data[f][:dim]
        emb_norm = np.linalg.norm(emb_cropped, ord=2)
        embedding_l2normed = emb_cropped / emb_norm
        data_new[f] = embedding_l2normed

    outfile = args.outfile if args.outfile else Path(args.fpath).stem
    print(f"Saving to file {outfile}")
    np.savez_compressed(outfile, **data_new)
    print("Save complete")


if __name__ == "__main__":
    main()
