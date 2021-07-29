# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:16:15 2021

@author: Nilesh
"""

def bubble_sort(a):
    n = len(a)
    ns = 0
    while ns < n:
        for i in range(0,n-ns-1):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i ] = a[i + 1]
                a[i + 1] = temp
        ns += 1
    
    print(a)
        
a = [1,4,5,6,2,2]

bubble_sort(a)