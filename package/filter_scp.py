# -*- coding:utf-8 -*-

import os 
import sys
import argparse
import codecs
#print sys.getdefaultencoding()  python 2 默认 asiic 编码
reload(sys)
sys.setdefaultencoding('utf-8')  #否则流处理的时候会出错

parser = argparse.ArgumentParser(description=" ")
#parser.add_argument('-e', '--exclude', default=None, help='')
parser.add_argument('--exclude', default=False, action='store_true', help='')
parser.add_argument('filter_file', help='filter file')
parser.add_argument('filtered_file', help='filtered file')
args = parser.parse_args()

print(args.exclude)

filter_file = args.filter_file
filtered_file = args.filtered_file

filter_set = set()
with codecs.open(filter_file, 'r', 'utf-8') as fid:
    for line in fid.readlines():
        id = line.strip().split()[0]
        filter_set.add(id)

with codecs.open(filtered_file, 'r', 'utf-8') as fou:
    #if args.exclude:
    #    for line in fou.readlines():
    #        filtered_id = line.strip().split()[0]
    #        if filtered_id not in filter_set:
    #            print line.strip()
    #else:
    #    for line in fou.readlines():
    #        filtered_id = line.strip().split()[0]
    #        if filtered_id in filter_set:
    #            print line.strip()
    for line in fou.readlines():
        filtered_id = line.strip().split()[0]
        if filtered_id in filter_set and not args.exclude:
            print(line.strip())
        if filtered_id not in filter_set and args.exclude:
            print(line.strip())

