# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:46:36 2021

@author: Nilesh
"""

def shell_sort(a):
    j = 0
    k = 0
    gap = int(len(a)/2)
    while gap >= 1:
        print(a)
        for i in range(len(a)):
            j = i + gap
            if j >= len(a):
               break
            ind = i
            while ind >= 0:
                if a[ind] > a[j]:
                    temp = a[ind]
                    a[ind] = a[j]
                    a[j] = temp
                    j = ind
                    ind -= 1
                else:
                    break
        gap = int(gap/2)
    
    print(a)
    
a = [1,4,24,12,1,54,0]

shell_sort(a)           