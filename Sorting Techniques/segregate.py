# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 12:55:38 2021

@author: Nilesh
"""

def segregate(arr):
    s = 0
    e = len(arr)-1
    
    while True:
        if s >= e:
            break
        if arr[s] >= 0:
            if arr[e] < 0:
                temp = arr[s]
                arr[s] = arr[e]
                arr[e] = temp
                s += 1
                e -= 1
            else:
                e -= 1
        
        else:
            s += 1
    
    return arr

arr = [1,-2,0, -2,-4,-6,-10]

print(segregate(arr))
                
                