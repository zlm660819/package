# -*-coding: utf-8 -*-

import sys
import os
import codecs

def quick_sort(list_obj, left, right):
    if left < right:
        i = left
        j = right
        pivot = list_obj[left]
        while i != j:
            while j > i and list_obj[j] > pivot:
                j -= 1
            if j > i:
                list_obj[i] = list_obj[j]
                i += 1
            while i < j and list_obj[i] < pivot:
                i += 1
            if i < j:
                list_obj[j] = list_obj[i]
                j -= 1
        list_obj[i] = pivot
        quick_sort(list_obj, left, i-1)
        quick_sort(list_obj, i+1, right)

text_file = sys.argv[1]
id_list = []
text_dict = {}
with codecs.open(text_file, 'r', 'utf-8') as fid:
    lines = fid.readlines()
    for line in lines:
        arr = line.strip().split() 
        if arr != None and arr[0] not in text_dict:
            text_dict[arr[0]] = arr[1:]
            id_list.append(arr[0])
        elif arr[0] in text_dict:
            print("%s not uniq and %s repeats" %(text_file, arr[0]))
    
with codecs.open(text_file, 'w', 'utf-8') as fout:
    quick_sort(id_list, 0, len(id_list)-1)
    for i in range(len(id_list)):
        fout.write("%s %s\n" %(id_list[i], ' '.join(text_dict[id_list[i]])))
