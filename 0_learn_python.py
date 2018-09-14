# -*- coding: utf-8 -*-

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




# 1 - number and long string
# v2
print(36/float(7))

# v3
print(36/7)
print(36%7)
print(36//7)

import sys
print(sys.maxsize)  # the maxint of v3

# complex
y = 1+2j
type(y)
print(y.real)
print(y.imag)


# non-trial -> True
int(True)

# random
import random

# generate random number
# 3 uniforms
for i in range(100):
    print(random.random())  # uniform distribute in [0,1)

for i in range(100):
    print(random.uniform(1,10)) # uniform distribute in [1,10)
    
for i in range(100):
    print(random.randint(5)) # 0,1,2,3,4,5

# normal
random.normalvariate(0,1)

# random choice
print(random.choice(['a','b','c']))
print(random.choices(['a','b','c'],k=3))
print(random.sample(['a','b','c'],3))  # this is do not have replacement




# long string
this_string = '''dkljglakg:
dgfakdgja
    dfj'gadg'
"jdlfkaj"
'''
print(this_string)   



# 2 - datetime
import datetime as dt
gvr = dt.date(1993,8,8)
lauch_time = dt.time(23,12,10)

# print time
print(gvr)
print(gvr.strftime('%A, %B %d'))

print(dt.datetime.strptime('07/20/1969', '%m/%d/%Y'))
print(dt.datetime.strptime('07:06:05', '%H:%M:%S'))
print(dt.datetime.strptime('07:06:05', '%X'))

print(gvr.day)
gvr + 100
gvr + dt.timedelta(days=100)
gvr + dt.timedelta(seconds=100000)

(dt.datetime.today()-gvr).days



# 3 - list, tuple, set and dictionary

# list
a = [1,2,3,4]
print(a.pop())
print(a)

print(a)
print(a.pop(0))
print(a)

print(a)
print(a.insert(0, 10))
print(a)

print(a.insert(-1, 10))
print(a)

a=[[1,2],[3,5],[5]]
print([5 in i for i in a])

# filter
list_x = [1,2,3,None,4,1,2,3,None]

x2 = filter(None, list_x)  # filter out NA value. Same as map, it do not return list
x2 = list(x2)
print(x2)

x2 = filter(lambda x: x>2, x2)  # return qualified ones 
print(list(x2))


# tuple
# tuple is smaller
import sys
a = (1,2,3,4,5)
sys.getsizeof(a)

# tuple assignment, works also for list
q,w,e,r,t = a
print(w)


# set
set1=set()
set1.add(1)
set1.remove(2)
set1.discard(2) # without error

set2={3,4,5}
set1.union(set2)
set1.intersection(set2)

# dictionary
dikt = {}
dikt.get('dg', None)
dikt.keys()
dikt['A'] = 1          # for one
dikt.update({'A':1})   # for multiple

# JSON is slight differently defined dictionary in Python
import json
with open('... .txt','w',encoding = 'utf-8') as f:
    json.dump(a_dict, f, ensure_ascii = False)
with open('... .txt','r',encoding = 'utf-8') as f:
    a_dict = json.load(f)

# change between json_file_string and dict
json.loads(a_string_of_json_file) # this will output a dict
json.dumps(a_dict, ensure_ascii = False, sort_keys=True, indent=4) # this will output a json_file_string
# json.dumps can also be used as a method to show dictionary



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



# 5 - generator

# yield
def generator():
    for i in range(10):
        yield i

# use 1
g=generator()
print(next(g))
print(next(g)) 

# use 2
for i in g:
    print(i)
    
# simple version of yield
g = (i for i in range(10))
print(list(g))




# 6 - input and output

# simples IO
input_1 = input('pls input something:\n')
print(input_1)

# print out
print(x, file=f)





# logging
import logging
logging.basicConfig('logger01.log')
logger1=logging.getLogger()
logger1.info('what')  # nothing in log file
print(logger1.level)

# levels : debug, Info, warning, error, critical
logging.basicConfig(filename='logger01.log', level = logging.DEBUG)
logger1=logging.getLogger()
logger1.info('what')

# where to find log_formats: ...
log_format = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='logger01.log',  file_mode = 'a', level = logging.DEBUG, format = log_format)
logger1=logging.getLogger()
logger1.info('what')





# class
# class can take variable out of definition






# bonus
# record time
import time
tic = time.time()
print(sum(range(10000)))
print('duration: ', time.time()-tic)



import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)


