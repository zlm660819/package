# -*- coding: utf-8 -*-

import os
import sys
import codecs
import argparse

parser = argparse.ArgumentParser(description='')
#parser.add_argument('--utt2spk','-u', help='')
parser.add_argument('--jobs', '-j', action='store', help='')
parser.add_argument('--job_id', help='')

parser.add_argument('in_scp', help='')
parser.add_argument('out_scp', nargs='+', help='')
#parser.add_argument(help='')
args = parser.parse_args()

utt2spk = args.utt2spk
jobs = args.jobs
job_id = args.job_id
in_scp = args.in_scp
out_scp = args.out_scp

#print(out_scp)
with codecs.open(in_scp, 'r', 'utf-8') as fid:
    lines = fid.readlines()
    lines_num = len(lines)

#if jobs == None and utt2spk == None:
if jobs == None
    split_num = len(out_scp)
    if split_num > lines_num:
        print("You are splitting into too many pieces!")
        sys.exit(-1)
    num = lines_num / split_num
    rem = lines_num % split_num
    for i in range(0,rem):
        with codecs.open(out_scp[i], 'w', 'utf-8') as fout:
            for j in range(i*(num+1), (i+1)*(num+1)):
                fout.write(lines[j])
    for i in range(rem,split_num):
        with codecs.open(out_scp[i], 'w', 'utf-8') as fout:
            for j in range(i*num, (i+1)*num):
                fout.write(lines[j])  

#elif jobs != None and utt2spk == None:
else:
    if job_id >= jobs: 
        print("job_id out of range of number of splied jobs")
        sys.exit(-1)
    if len(out_scp) > 1:
        print(" ")
        sys.exit(-1)
    split_num = jobs
    num = lines_num / split_num
    rem = lines_num % split_num
    with codecs.open(out_scp[0], 'w', 'utf-8') as fout:
        if job_id > rem-1:
            for j in range(job_id*num, (job_id+1)*num):
                fout.write(lines[j]) 
        else:
            for j in range(job_id)*(num+1), (job_id+1)*(num+1))
                fout.write(lines[j])





