# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:31:39 2021

@author: Nilesh
"""

def radix_sort(a):
    m = max(a)
    n = len(list(str(m)))
    
    d = {}
    
    for i in range(n):
        d = {}
        for j in range(len(a)):
            digit = int(a[j]/(10**i)) % 10
            if digit not in d:
                d[digit] = [a[j]]
            else:
                d[digit] += [a[j]]
        a = []
        for k in range(10):
            if k in d:
                a += d[k]
    
    print(a)
    

a = [11,65,54,6556]

radix_sort(a)