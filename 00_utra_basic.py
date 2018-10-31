# -*- coding: utf-8 -*-

# the first thing is how do you learn python by yourself
a = 'dgadfag'
dir(a)
b = [1,2,3]
dir(b)

dir()
dir('__builtins__')

help(repr)


def add2(x,y):
    'add two object'
    
    print('the sum is', x+y)
    return x+y
help(add2)


# what is repr and eval:
a='dgadf dga'
print(a)
repr(a)
eval(repr(a))==a


# math
import math
dir(math)
math.ceil(3.4)







'''
    to know:
        1, what is help() and dir(), how to see functions in a library
        2, how to see build_in functions
        3, what is repr() and eval()

'''