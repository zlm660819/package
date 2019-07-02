# -*- coding:utf-8 -*-

import os
import sys
import codecs
import re

args = sys.stdin.readlines()
score = float('inf')
for arg in args:
    pattern = re.compile(r'\w*WER (\d+\.\d+)\w*')
    arr = pattern.findall(arg)
    if score > float(arr[0]):
        score = float(arr[0])
        fout  = arg
final_list =  fout.strip().split(':') 
out1 = final_list[1:][0]
out2 = final_list[0][3:]
sys.stdout.write(out1+' ')
sys.stdout.write(out2)
