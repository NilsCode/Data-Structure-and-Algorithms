# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 23:17:30 2021

@author: Nilesh
"""

def binarySearch(key,arr):
    s = 0
    e = len(arr) - 1
    arr = sorted(arr)
    while True:
        m = int((s + e)/2)
        val = arr[m]
        if val == key:
            return m
        
        if val > key:
            e = m-1
        
        if val < key:
            s = m+1

        if s > e:
            return(-1)
        
arr  = [1,2,3,4,5,6]
key = 7

print(binarySearch(key, arr))