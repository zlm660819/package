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

"""QuickSort in Python"""

def paritiion(array, first, last):
    pivot = array[last]

    p = first
    q = last - 1

    while p != q:
        if array[p] > pivot:
            array[p], array[q] = array[q], array[p]
            q -= 1
        else:
            p += 1
    
    if array[p] > pivot:
        array[p], array[last] = array[last], array[p]
    else:
        p += 1
        array[p], array[last] = array[last], array[p]
    return p

def quicksort(array, first, last):
    if first < last:
        mid = paritiion(array, first, last)
        quicksort(array, first, mid-1)
        quicksort(array, mid+1, last)

if __name__ == '__main__':
    array = [3, 5, 11, 4, 2, 0, 12, 2, 3, 1]
    quicksort(array, 0, len(array)-1)
    print(array)
