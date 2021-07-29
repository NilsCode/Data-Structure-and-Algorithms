# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 23:34:59 2021

@author: Nilesh
"""

def reverseList(a):
    i = 0
    j = len(a) - 1
    
    while True:
        temp= a[i]
        a[i] = a[j]
        a[j] = temp
        
        i += 1
        j -= 1
        
        if i >= j:
            break
    return a

a = [1,2,3,4,5,6,4,8,7]

print(reverseList(a))