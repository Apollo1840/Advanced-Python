# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:24:20 2018

@author: zouco
"""

# 0 - ths first thing is how do you learn python by yourself
a = 'dgadfag'
dir(a)
b = [1,2,3]
dir(b)

dir()
dir('__builtins__')

help(repr)

# what is repr and eval:
a='dgadf dga'
print(a)
repr(a)
eval(repr(a))==a


# math
import math
dir(math)
math.ceil(3.4)