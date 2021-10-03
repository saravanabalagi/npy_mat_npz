# npy mat npz

Convert `npy` or `npz` to `mat` and `mat` to `npz` format.

## Quick Install

```sh
git clone https://github.com/saravanabalagi/npy_mat_npz.git
cd mat_npy_npz
poetry install
```

## Usage

Activate `.venv` environment.
If poetry is configured with `virtualenvs.in-project = true`, simply execute `. .venv/bin/activate`

### Files

```
python mat2npz.py file.mat
python mat2npz.py file1.mat file2.mat file3.mat

python npz2mat.py file.npz
python npz2mat.py file1.mat file2.mat file3.mat
```

Output files are generated in the same directory as the source.

### Directories

Generates one `npz` file from a directory containing multiple `mat` files:

```
python matdir2npz.py dir1withmatfiles dir2withmatfiles
# generates dir1withmatfiles.npz dir2withmatfiles.npz
```

Note: This script assumes that each of the `mat` files have only one variable inside and the `npz` dictionary contains values against the name of the `mat` files without extension.
