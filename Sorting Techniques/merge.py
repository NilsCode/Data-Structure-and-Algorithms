# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:12:17 2021

@author: Nilesh
"""

def merge(a,b):
    c = [0]*(len(a) + len(b))
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
            k += 1
        else:
            c[k] = b[j]
            j += 1
            k += 1
    
    
    if i == len(a):
        for x in range(j, len(b)):
            c[k] = b[x]
            k += 1
    else:
        for x in range(i, len(a)):
            c[k] = a[x]
            k += 1
    
    print(c)
    
    
a = [1,4,6]
b = [2,3,5]

merge(a,b)