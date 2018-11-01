# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:31:11 2018

@author: zouco
"""


# add [1,8,3] + [1,2] = [3,0,4]

# way 1 
def addLists(l1,l2):
    def list2num(l):
        num = 0
        for i in range(len(l)):
            num += l[i]*(10**i)
        return num
    
    the_sum = list2num(l1)+list2num(l2)
    return reversed(list(str(the_sum)))
