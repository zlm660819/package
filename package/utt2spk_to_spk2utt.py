# -*- coding: utf-8 -*-

import os
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

spk2utt_dict = {}
utt2spk_file = sys.argv[1]
with codecs.open(utt2spk_file, 'r', 'utf-8') as fid:
    lines = fid.readlines()
    for line in lines:
        arr = line.strip().split()
        key = arr[1]
        if key not in spk2utt_dict:
            spk2utt_dict[key]  = []
        spk2utt_dict[key].append(arr[0])

for key in spk2utt_dict:         
    spk2utt = ' '.join(spk2utt_dict[key])
    spk2utt = key + ' ' +  spk2utt + '\n'
    sys.stdout.write(spk2utt)
    #sys.stdout.writelines(spk2utt_dict[key])
