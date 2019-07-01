# -*- coding: utf-8 -*-

import os
import sys
import codecs


def bubble(list, length):
    for j in range(length-1):
	    for i in range(0,length-1-j):
		if list[i] > list[i+1]:
		    arr = list[i]
		    list[i] = list[i+1]
		    list[i+1] = arr
		   # list[i], list[i+1] = list[i+1], list[i]
    return list

def selection(list, length):
    for j in range(length-1):
        min_index = j
        for i in range(j,length-1):
            if list[i] > list[i+1]:
                min_index = i+1
        list[j], list[min_index] = list[min_index], list[j] 
    return list

def insert(list, length):
    for i in range(1,length):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
    return list

if __name__ == "__main__":
    file = "text"
    with codecs.open(file, 'r', 'utf-8') as fid:
        content = fid.read()
        list = content.strip().split()
    length = len(list)
    for i in range(length):
        list[i] = int(list[i])
    print(bubble(list,length))
    print(selection(list,length))
    print(insert(list,length))
