import numpy as np
from ruamel import yaml
import argparse
import os


def opencv_matrix(loader, node):
    mapping = loader.construct_mapping(node, deep=True)
    dt = mapping["dt"]
    if dt == "u": dt = np.uint8
    elif dt == "f": dt = np.float32
    elif dt == "d": dt = np.float64
    else: raise TypeError(f'Could not infer type {dt}')
    mat = np.array(mapping["data"], dtype=dt)
    mat.resize(mapping["rows"], mapping["cols"])
    return mat
yaml.add_constructor(u"tag:yaml.org,2002:opencv-matrix", opencv_matrix)


parser = argparse.ArgumentParser()
parser.add_argument('yaml_file')
parser.add_argument('key')
parser.add_argument('--new_key', default='')
args = parser.parse_args()

file = args.yaml_file
key = args.key
new_key = args.new_key

if new_key == '':
    new_key = key

with open(file, 'r') as f:
    yaml_data = yaml.load(f, Loader=yaml.Loader)
    data_required = yaml_data[key]

d = {}
d[new_key] = data_required
fn = os.path.splitext(file)[0]
np.savez_compressed(fn, **d)
