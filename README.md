# npy mat npz

Convert `npy` or `npz` to `mat` and `mat` to `npz` format.

Also useful for converting NetVLAD `mat` descriptors and `yml` descriptors saved using OpenCV FileStorage API to `npz` files, see below for more details.

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

```sh
python mat2npz.py file.mat # outputs file.npz
python mat2npz.py file1.mat file2.mat file3.mat 
# outputs file1.npz file2.npz file3.npz

python npz2mat.py file.npz # outputs file.mat
python npz2mat.py file1.npz file2.npz file3.npz
# outputs file1.mat file2.mat file3.mat
```

Output files are generated in the same directory as the source.

### Directories

Generates one `npz` file from a directory containing multiple `mat` files:

```sh
python matdir2npz.py dir1withmatfiles dir2withmatfiles
# outputs dir1withmatfiles.npz dir2withmatfiles.npz
```

Note: This script assumes that each of the `mat` files have only one variable inside and the `npz` dictionary contains values against the name of the `mat` files without extension.

## NetVLAD Mat Files

[NetVLAD](https://github.com/Relja/netvlad) saves descriptors of images as a single [binary file](https://github.com/Relja/netvlad/blob/master/README_more.md#output-binary-files) which can then be read and saved as multiple .mat files, one for each image, in a `feats` directory. [matdir2npz.py](matdir2npz.py) shall be used to save this as a single npz file. For NetVLAD+whitening networks, the smaller dimensional descriptors can be generated using simple cropping.

```sh
python matdir2npz.py /data/feats # outputs feats.npz
python netvlad_crop.py /data/feats.npz 64 # outputs feats_dim64.npz
```

## OpenCV YAML Files

OpenCV CPP FileStorage API stores descriptors inside .yaml or .yml files under a specified key, say `desc`, then this can converted to npz individually using [yaml2npz.py](yaml2npz.py) or in bulk using [yamldir2npz.py](yamldir2npz.py) as shown below:

```sh
python yaml2npz.py cvdesc_001.yml desc # outputs cvdesc_001.npz
python yamldir2npz.py cvdescs_dir desc # outputs cvdescs_dir.npz
```
