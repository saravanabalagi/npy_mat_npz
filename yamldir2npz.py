import sys
import numpy as np
from ruamel import yaml
import os
import argparse
import glob
from tqdm.auto import tqdm
from multiprocessing import Pool


def opencv_matrix(loader, node):
    mapping = loader.construct_mapping(node, deep=True)
    mat = np.array(mapping["data"])
    mat.resize(mapping["rows"], mapping["cols"])
    return mat
yaml.add_constructor(u"tag:yaml.org,2002:opencv-matrix", opencv_matrix)


parser = argparse.ArgumentParser()
parser.add_argument('yaml_dir')
parser.add_argument('key')
args = parser.parse_args()

yaml_dir = args.yaml_dir
key = args.key

# dry run, validate
assert os.path.isdir(yaml_dir), "Must be a dir with .yml or .yaml files"
file_types = ['.yml', 'yaml']
files = []
for t in file_types:
    files.extend(glob.glob(f'{yaml_dir}/*{t}'))
print(f'{len(files)} files found')


def get_required_data(filepath):
    with open(filepath, 'r') as f:
        yaml_data = yaml.load(f, Loader=yaml.Loader)
        data_required = yaml_data[key]
    return data_required


with Pool(processes=12) as p:
    p_args = files
    results = list(tqdm(p.imap(get_required_data, p_args), total=len(p_args)))

d = {}
for filepath, result in zip(files, results):
    filename = os.path.splitext(os.path.basename(filepath))[0]
    d[filename] = result

npz_file = f'{yaml_dir}.npz'
np.savez_compressed(npz_file, **d)
