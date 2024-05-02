import json
import argparse
import os
from tqdm import tqdm
import shutil


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--json_path', default='viscot_benchmark/benchmark/sroie.json', type=str)
    parser.add_argument('--src_path', default='playground/data', type=str)
    parser.add_argument('--dst_path', default='data', type=str)
    args = parser.parse_args()

    with open(args.json_path, 'r') as f:
        data = json.load(f)

    for data_sample in tqdm(data):
        src_file = os.path.join(args.src_path, data_sample['image'][0])
        if not os.path.exists(src_file):
            print(f'{src_file} does not exist!', flush=True)
        dst_file = os.path.join(args.dst_path, data_sample['image'][0])
        dst_root = os.path.dirname(dst_file)
        os.makedirs(dst_root, exist_ok=True)
        shutil.copyfile(src_file, dst_file)
