# -*- coding: utf-8 -*-
"""
@author: zouco
"""

# coding test

# reverse words in a string

# way 1
def rws(string):
    strs = string.split(' ')
    a = ''
    for i in range(len(strs)):
        a += str.strip(strs[len(strs)-i-1]) + ' '
    return a.strip()

test = 'reverse words in a string'
test2 = ' this one     is  harder   '

# way 2
def reverseWords(s):
    return " ".join(list(filter(lambda a:a!="",s.split(' ')))[::-1])

# explain
print(''.join(['a','b','c']))    
print('x'.join(['a','b','c']))

list(filter(lambda x: x>2, [1,2,3,4,5]))

a=[1,2,3,4,5]
print(a[::-1])

# why way 1 is not so good
str.split(test2, ' ')







            



