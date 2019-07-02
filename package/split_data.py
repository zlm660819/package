# -*- coding: utf-8 -*-

import os 
import sys
import codecs
import argparse
reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser(description='')
parser.add_argument('--per_utt', default=True, action='store_true', help='')
parser.add_argument('date', help='')
parser.add_argument('numsplit', help='')
args = parser.parse_args()

data = args.data
numsplit = args.numsplit

if numsplit <= 0:
    print('Invalid num-split argument %s' %numsplit)
    exit(-1)

