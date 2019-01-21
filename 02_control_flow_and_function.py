# -*- coding: utf-8 -*-

# 1 control flow

# 1.1 while 
'''
    while else
'''
# example: jumping check
# 0, 1, 3, 7, 15, 31
numbers = range(1000)
index = 0
end_index = 100
wanted = 15

while index < end_index:
    print(numbers[index])
    if numbers[index]==wanted:
        print("we find it")
        break
        
    index = index + numbers[index] + 1
    
else:
    # do it while while-loop ends (without break)
    print('no within end_index.')

print('Done')

# !! the else will not run, if you use break


# 1.2 try
'''
    try, except, else, finally
'''

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:       # run this when successed
        print("result is", result)
    finally:    # run it whatever happend
        print("executing finally clause")


# Error
class SimpleError(Exception):
    pass        
        
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')        
    


# --------------------------------------------------------------------------
# 2 - function
# 2.1 function input
def cm(f=0,i=0):
    print(f+i*2)
    return f+i*2

cm(3)
cm(i=1)

# default assign acts in a static way
# this i will always assign to the same loc
def f(i=[]):
    # print(id(i))
    i.append(1)
    # print(id(i))
    return i

print(f())
print(f())

# some false solution to this problem:
def f(i=[]):
    j=i
    # print(id(i))
    j.append(1)
    # print(id(i))
    return j

print(f())
print(f())


def f(i=[]):
    # print(id(i))
    i += [1]
    # print(id(i))
    return i

print(f())
print(f())

# true solution should change the loc
def f(i=None):
    if i is None:
        i=[]
    # print(id(i))
    i.append(1)
    # print(id(i))
    return i

print(f())
print(f())

def f(i=[]):
    # print(id(i))
    i = i + [1]
    # print(id(i))
    return i

print(f())
print(f())

# now how about:
def f(i=1):
    # print(id(i))
    i+=1
    # print(id(i))
    return i

print(f())
print(f())

# use lambda to create function generator
def qua(a,b,c):
    return lambda x: a*x**2 +b*x+c

f = qua(2,1,3)
f(2)    


# 2.2 function doc
# you can use __doc__ to descripe your function
def print_max(x, y):
    'bla bla'
    pass

help(print_max)
print(print_max.__doc__)


# 2.3 multiple args
def total(a=5, *numbers, **phonebook):
    print('a', a)
    print('numbers', numbers)
    print('phonebook', phonebook)
    
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

a = 10
numbers = (1,2,3)
phonebook = {'Jack': 1123,'John':2231,'Inge':1560}
print(total(a, *numbers, **phonebook))

Maxn,*middlen,minn=sorted([12,3,24,435,46,3422,])


# 2.4 variable scoup 
# global and nonlocal
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

def outer2():
    x = "local"  
    def inner():
        global x
        x = "global"
        print("inner:", x)
        
    inner()
    print("outer:", x)

x = 'global'
outer()
outer2()  


# 2.5 decorater
# the thought
def outer_function(msg='hi'):
    def inner_function():
        print(msg)
    return inner_function

my_func = outer_function()
my_func()    
my_func2 = outer_function('hallo')
my_func2()

# basic decorator
# add functionality to existing funciton
def dfunc(ofunc):
    def wfunc():
        print('decorator is working')
        return ofunc()
    return wfunc

@dfunc
def display():
    print('hello world')

display()   # when you added decorator, display = dfunc(display)


# advanced decorator        
def dfunc(ofunc):
    def wfunc(*args, **kwargs):
        print('decorator is working')
        return ofunc(*args, **kwargs)
    return wfunc        

# decorator class
class dclass(object):
    
    def __init__(self, ofunc):
        self.ofunc = ofunc
    
    def __call__(self, *args, **kwargs):
        print('decorator class is working')
        return self.ofunc(*args, **kwargs)


# examples 1:
import time
def my_timer(ofunc):
    
    def wfunc(*args, **kwargs):
        t1 = time.time()
        result = ofunc(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(ofunc.__name__, t2))
        return result
    
    return wfunc



@my_timer
def somejob():
    print(sum(range(10000000)))

somejob()



# examples 2:
# recursive function
def fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n>=2:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci_cache = {0:1, 1:1}

def fibonacci_fast(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    if n>=2:
        value = fibonacci(n-1) + fibonacci(n-2)
        # enlarge the cache
        fibonacci_cache[n] = value
        return value

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci_fast2(n):
    # check the input...
    # ...
    
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n>=2:
        value = fibonacci(n-1) + fibonacci(n-2)
        return value



'''
    how to use decorator and the lru_cache decorator

'''




