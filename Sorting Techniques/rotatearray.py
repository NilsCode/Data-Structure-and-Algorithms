# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 23:40:01 2021

@author: Nilesh
"""

def rotate_array(arr):
    l = arr[-1]
    for i in range(-1, len(arr) -1):
        if i == (len(arr)-2):
            arr[i] = l
        else:
            arr[i] = arr[i+1]
    
    return(arr)

arr = [1,2,3,4,5,6,7,8,9]

print(rotate_array(arr))