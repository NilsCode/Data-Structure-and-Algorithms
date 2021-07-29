# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 22:36:23 2021

@author: Nilesh
"""

def merge_array(a,b):
    c = [0]*len(a + b)
    
    x = 0
    y = 0
    
    for i in range(len(a + b)):
        if x < len(a) and y < len(b):
            if a[x] > b[y]:
                c[i] = b[y]
                y += 1
            elif b[y] >= a[x]:
                c[i] = a[x]
                x += 1
            
        else:
            if x >= len(a):
                c[i] = b[y]
                y += 1
            else:
                c[i] = a[x]
                x += 1
    return(c)

a  = [0,5,10,20]

b = [1, 6, 11, 15, 16, 18]

print(merge_array(a, b))