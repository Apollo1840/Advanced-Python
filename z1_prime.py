# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:09:11 2018

@author: zouco
"""

####################################################################
# simplify the program by math:
def is_prime(n):
    if n==1:
        return False
    
    if n==2:
        return True
    
    if n >2 and n%2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n%d == 0:
            return False
    return True
###################################################################