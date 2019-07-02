# -*-coding:utf-8-*-

import os
import sys
import argparse
import codecs
import shutil

parser = argparse.ArgumentiParser(description='')
parser.add_argument('--utt_extra_files', default=None, help='')
parser.add_argument('--spk_extra_files', default=None, help='')
parser.add_argument('data', help='')
args = parser.parse_args()

data = args.data
if os.path.exiscs(data+'/utt2spk') != True:
    print ("%s no such file %s" % (sys.argv[0], data+'/utt2spk'))
    exit(1)

back_path = data+'/.backup'
os.mkdirs(back_path)
shutil.copytree(data, back_path)

def check_sorted(file):
    pass

def filter_file()
    pass


def filter_recordings()
    pass


def filter_speakers()

    pass

def filter_utts()
    pass


if __name__ == "__main__":
    filter_recordings()
    filter_speakers()
    filter_utts()
    filter_speakers()
    filter_recordings()


