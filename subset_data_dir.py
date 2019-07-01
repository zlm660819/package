# -*- coding: utf-8 -*-

import os
import sys
import codecs
import argparse
import random

parser = argparse.ArgumentParser(description='')
parser.add_argument('srcdir', help='')
parser.add_argument('num_utt',type=int, help='')
parser.add_argument('destdir', help='')
args = parser.parse_args()

srcdir = args.srcdir
num_utt = args.num_utt
destdir = args.destdir

if not os.path.exists(destdir):
    os.mkdir(destdir)

utt2spk = os.path.join(srcdir, 'utt2spk')
with codecs.open(utt2spk, 'r', 'utf-8') as fid:
    lines = fid.readlines()
    for line in lines:
        if line == '\n': 
            lines.remove(line)
    lines_num = len(lines)
    ids = set()
    #for i in range(num_utt):
    while len(ids) < num_utt:
        ids.add(random.randint(0,lines_num-1))
    keys = []
    for j in ids:
        key = lines[j].strip().split()[0]
        keys.append(key)

file_list=["utt2spk", "spk2utt", "text", "cmvn.scp", "feats.scp", "wav.scp"]
for f in file_list:
    file_input = os.path.join(srcdir, f)
    file_output = os.path.join(destdir, f)
    with codecs.open(file_input, 'r', 'utf-8') as fid:
        file_dict = {}
        lines = fid.readlines()
        for line in lines:
            if line != '\n':
                arr = line.strip().split()
                file_dict[arr[0]] = ' '.join(arr[1:])
    with codecs.open(file_output, 'w', 'utf-8') as fout:
        for key in keys:
            if key in file_dict:
                fout.write("%s %s\n" % (key, file_dict[key]))


 
  
    

