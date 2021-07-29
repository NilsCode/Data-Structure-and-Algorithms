# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 21:57:00 2021

@author: Nilesh
"""

def pair_sum(a, s):
    
    d = {}
    for i in a:
        if s - i in d:
            print(i,s-i)
            continue
        else:
            if i not in d:
                d[i] = 0

def pair_sum_sorted(a, s):
    a.sort()
    start = 0
    end = len(a) - 1
    
    while start < end:
        num = s - a[start]
        while num <= a[end] and start < end:
            if num == a[end]:
                print(a[start], a[end])
                break
            else:
                end -= 1
        start += 1
        
a = [1,2,8,6,3,4,7,7,7]
s = 10

#pair_sum(a, s)
pair_sum_sorted(a, s)