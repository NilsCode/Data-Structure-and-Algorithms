# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:46:39 2021

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
            k +=1
    else:
        for x in range(i, len(a)):
            c[k] = a[x]
            k += 1
    
    return(c)
    
    
a = [1,8,2,9,4,6]

def merge_sort(arr):
    x = [a[0]]
    y = [a[1]]
    for i in range(0, len(a)-1):
        y = [a[i+1]]
        x = merge(x,y)
    print(x)
    
merge_sort(a)
