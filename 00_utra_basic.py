# -*- coding: utf-8 -*-

# the first thing is: how do you learn python by yourself
# dir
a = 'dgadfag'
dir(a)
b = [1,2,3]
dir(b)

dir()
dir('__builtins__')



# help
def add2(x,y):
    'add two object'
    
    print('the sum is', x+y)
    return x+y
help(add2)

help(repr)


# - - - - - - - - - - - - 
# what is repr and eval:
a='dgadf dga'
print(a)
repr(a) # print the variable in the way python(not human) reads
eval(repr(a))==a
# - - - - - - - - - - - - 



'''
    to know:
        1, what is help() and dir(), how to see functions in a library
        2, how to see built_in functions
        
        * what is repr() and eval()

'''