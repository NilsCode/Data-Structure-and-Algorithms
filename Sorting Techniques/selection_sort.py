# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:26:42 2021

@author: Nilesh
"""

def selection_sort(a):
    min_index = 0
    for i in range(len(a)):
        min_index = i
        num = a[i]
        for j in range(i, len(a)):
            if a[j] < a[min_index]:
                min_index  = j
                min_num = a[min_index]
        temp = a[i]
        a[i] = a[min_index]
        a[min_index] = temp
        
    print(a)
    
a = [1,2,4,4,3,5,9,9,9,2,2]

selection_sort(a)