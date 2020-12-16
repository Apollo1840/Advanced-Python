# -*- coding: utf-8 -*-

# math
import math

dir(math)
math.ceil(3.4)

# 0.4 random
import random

# generate random number
# 3 uniforms
'''
    * .random()
    * .uniform()
    * .randint()
    * .normalvariate()
    * .choice
    * .choices
    * .sample
    * .shuffle
    
'''

for i in range(100):
    print(random.random())  # uniform distribute in [0,1)

for i in range(100):
    print(random.uniform(1, 10))  # uniform distribute in [1,10)

for i in range(100):
    print(random.randint(5))  # 0,1,2,3,4,5

##########################
# normal
random.normalvariate(0, 1)
##########################


# random choice
x = ['a', 'b', 'c', 'd']

print(random.choice(x))

print(random.choices(x, k=3))  # may have duplicates
print(random.choices(x, k=3, weights=[70, 20, 10, 0]))
print(random.sample(x, 3))  # this is do not have replacement

print(random.shuffle(x))
print(x)

# --------------------------------------------------------------------------
# 2 - datetime
import datetime as dt

# get time
gvr = dt.date(1993, 8, 8)  # year month day
lauch_time = dt.time(23, 12, 10)

# date format
# see: https://www.w3schools.com/python/python_datetime.asp
print(dt.datetime.strptime('07/20/1969', '%m/%d/%Y'))
print(dt.datetime.strptime('07:06:05', '%H:%M:%S'))
print(dt.datetime.strptime('07:06:05', '%X'))

# print time
print(gvr)
print(gvr.strftime('%A'))  # weekday
print(gvr.strftime('%B, %y'))  # monthName and short year
print(gvr.day == gvr.strftime('%d'))

# operations on time
gvr + 100
gvr + dt.timedelta(days=100)
gvr + dt.timedelta(seconds=100000)

(dt.datetime.today() - gvr).days

'''
    init: dt.date and dt.time

    format: dt.datetime.strptime(str, re), DT.strftime(re) or simplier re.day

    delta: dt.timedelta


'''
