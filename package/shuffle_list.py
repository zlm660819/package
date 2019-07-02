# -*-coding: utf-8 -*-

import os
import sys
import codecs
import argparse
import random

parser = argparse.ArgumentParser(description='')
parser.add_argument('--srand', type=int, help='')
parser.add_argument('input_file', help='')
args = parser.parse_args()

seed_value = args.srand
input_file = args.input_file

file_dict = {}
i = 0
with codecs.open(input_file, 'r', 'utf-8') as fid:
    lines = fid.readlines()
    for line in lines:
        file_dict[i] = line
        i += 1

if seed_value != None:
   random.seed(seed_value)
keys = file_dict.keys()
random.shuffle(keys)
for key in keys:
    print (key)
    sys.stdout.write(file_dict[key])

