# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:18:02 2018

@author: zouco
"""

# while can working with else
number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # 这将导致 while 循环中止
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # 在这里你可以做你想做的任何事

print('Done')


# try
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:   # run this when successed
        print("result is", result)
    finally:  # run it whatever happend
        print("executing finally clause")



# Error
class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # 其他工作能在此处继续正常运行
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')        
    

# --------------------------------------------------------------------------
# 4 - function
# function input
def cm(f=0,i=0):
    print(f+i)
    return f+i

cm(3)
cm(i=1)

# use lambda to create function generator
def qua(a,b,c):
    return lambda x: a*x**2 +b*x+c

f = qua(2,1,3)
f(2)    


# you can use __doc__ to descripe your function
def print_max(x, y):
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print('')
print(print_max.__doc__)
print('-------------')
help(print_max)



# multiple args
def total(a=5, *numbers, **phonebook):
    print('a', a)
    print('numbers', numbers)
    print('phonebook', phonebook)
    
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

a = 10
numbers = (1,2,3)
phonebook = {'Jack': 1123,'John':2231,'Inge':1560}
print(total(a, numbers, phonebook))






# decorater
def outer_function(msg='hi'):
    
    def inner_function():
        print(msg)
    return inner_function

my_func = outer_function()
my_func()    
my_func2 = outer_function('hallo')
my_func2()


# add functionality to existing funciton
def dfunc(ofunc):
    def wfunc():
        print('decorator is working')
        return ofunc()
    return wfunc

def display():
    print('hello world')
    
dis2 = dfunc(display)
dis2()


# equal to 

@dfunc
def display():
    print('hello world')

display()


# advanced decorator        
def dfunc(ofunc):
    def wfunc(*args, **kwargs):
        print('decorator is working')
        return ofunc(*args, **kwargs)
    return wfunc        


class dclass(object):
    
    def __init__(self, ofunc):
        self.ofunc = ofunc
    
    def __call__(self, *args, **kwargs):
        print('decorator class is working')
        return self.ofunc(*args, **kwargs)


import time
def my_timer(ofunc):
    
    def wfunc(*args, **kwargs):
        t1 = time.time()
        result = ofunc(*args, **kwargs)
        t2 = time.time() - t1
        print('[} ran in: {} sec'.format(ofunc.__name__, t2))
        return result
    return wfunc










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


