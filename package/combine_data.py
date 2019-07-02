# -*- coding:utf-8 -*-

import os
import sys
import codecs 
import argparse
import shutil
reload(sys)
sys.setdefaultencoding('utf-8')

print len(sys.argv)

extra_files = None 
if sys.argv[1].startswith("--"):
    extra_files = sys.argv[2]
    dest_dir = sys.argv[3]
    src_dirs = sys.argv[4:]
else:  
    dest_dir = sys.argv[1]
    src_dirs = sys.argv[2:]

if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)
os.mkdir(dest_dir)

file_list = ["utt2spk", 'utt2lang', 'utt2dur', 'reco2dur', 'feats.scp', 'text', 'cmvn.scp', 'vad.scp', 'reco2file_and_channel', 'wav.scp', 'spk2gender']
if extra_files != None:
    extra_file_list = extra_files.strip().split()
    file_list.extend(extra_file_list)

for f in file_list:
    dest_file = os.path.join(dest_dir, f)
    print dest_file
    with codecs.open(dest_file, 'w', 'utf-8') as fout:
        for path in src_dirs:
            file_path = os.path.join(path, f)
            if os.path.isfile(file_path):
                with codecs.open(file_path, 'r', 'utf-8') as fid:
                    for line in fid.readlines():
                        fout.write(line)
            
