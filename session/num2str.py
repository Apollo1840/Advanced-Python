# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:49:31 2018

@author: zouco
"""

# formalize the number to string, separate with blank

solution = lambda a: ' '.join(list(str(a)))
a = 1234
solution(a) 


# way 2, without str()
a = 1234

w = []
while a//10 > 0:
    w.append(a%10)
    a = a//10
w.append(a%10)
'{} {} {} {}'.format(*w[::-1])



