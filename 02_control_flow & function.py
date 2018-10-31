# -*- coding: utf-8 -*-

# 1 control flow

# 1.1 while 
'''
    while else
'''

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
    print(f+i)
    return f+i

cm(3)
cm(i=1)

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



# 2.4 decorater
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
        print('[} ran in: {} sec'.format(ofunc.__name__, t2))
        return result
    return wfunc


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
