# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:42:28 2021

@author: Nilesh
"""

def insertion_sort(a):
    nlist = [a[0]]
    start = 1
    for i in range(start, len(a)):
        nlist.append(a[start])
        index  = len(nlist) - 1
        while index >0:
            if nlist[index - 1] > nlist[index]:
                temp = nlist[index]
                nlist[index] = nlist[index - 1]
                nlist[index -1] = temp
            
                index -= 1
            else:
                break
        start += 1
        
    print(nlist)
    
a = [2,1,3,4,5,7,8,4]
insertion_sort(a)
