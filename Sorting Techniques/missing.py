# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 21:17:36 2021

@author: Nilesh
"""

def missing_sorted(arr):
    
    diff = arr[0]
    for i in range(len(arr)):
        if arr[i] - i != diff:
            while diff < arr[i] - i:
                print(i + diff)
                diff += 1    

a = [1,2,3,7,9]

missing_sorted(a)