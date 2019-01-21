# -*- coding: utf-8 -*-

# 0 - number 

# 0.1 int
import sys
print(sys.maxsize)  # the maxint of v3

# non-trial -> True
int(True)
bool(0)

# 0.2 float
# v2
print(36/float(7))

# v3
print(36/7)

print(36%7)
print(36//7)

# 0.3 complex
# complex
y = 1+2j
type(y)
print(y.real)
print(y.imag)


# -----------------------------------------------------------------------------
# 1 - string
# number fill
'2'.zfill(3)

# long string
this_string = '''dkljglakg:
dgfakdgja
    dfj'gadg'
"jdlfkaj"
'''
print(this_string)   
print(this_string.find('j')) # find is better than index, it returns -1 if there is no such substring
print(this_string.count('j'))

# format string
# print format
print('{0:.3f}'.format(1.0/3))

# 使用下划线填充文本，并保持文字处于中间位置, 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
print('{0:_^11}'.format('hell'))
# others like {: 02} {: , } {: ,.2f}
# see : https://docs.python.org/3.1/library/string.html

# usage format
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
# or
name='Swaroop'
book='A Byte of Python'
print(f'{name} wrote {book}')


# escape sequence \
print('what\'s your name')
print(r'what\'s your name')

# break string
print('what is your\
name')

# break command line
print\
('what is your name')

# --------------------------------------------------------------------------
# 2 - list, tuple, set and dictionary

# list
a = [1,2,3,4,5]
print(a.index(2))
print(a.remove(2))
print(a)

print(a.pop())
print(1, a)
print(a.pop(0))
print(2, a)
print(a.insert(0, 30))
print(3, a)
print(a.insert(-1, 40))
print(4, a)

# in
print(5 in [1,3,4,5])
a=[[1,2],[3,5],[5]]
print([(5 in i) for i in a])

# filter
list_x = [1,2,3,None,4,1,2,3,None]

x2 = filter(None, list_x)  # filter out NA value. Same as map, it do NOT return list
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

def tuple_output():
    return 1,2    # or return (1,2)
a,b = tuple_output()
a = tuple_output()


# set
set1=set()
set1.add(1)
set1.remove(1)
set1.discard(2) # without error

set2={3,4,5}
print(set1.union(set2))          # set1 | set2
print(set1)  # set1 do not change
print(set1.intersection(set2))  # set1 & set2


# dictionary
dikt = {}
dikt = dict(a=1, b=2, c=3)
dikt.get('dg', None)
dikt.keys()
dikt['A'] = 1          # for one
dikt.update({'A':1})   # for multiple

dikt.values()
dikt.keys()
dikt.items()

dikt.pop('a')
dikt.popitem()

# sort objects by key
points = [{'x0': 2, 'y': 3},
          {'x1': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

# example, how to sort a dic?
dic = dict(points[0], **points[1]) # merge dict and kwargs
sorted(list(dic.items()), key=lambda i: i[1])

# dict loc
dikt = dict(a=1, b=2, c=3)
dikt2=dikt
dikt["a"]=10
print(dikt2["a"])

import copy
dikt3=copy.copy(dikt)
dikt["a"]=10
print(dikt3["a"])

'''
    ##### list: 

    index, pop, insert, append & extend, filter & map
 
    ##### tuple: 

    tuple sign

    ##### set: 

    add, remove, discard, intersection, union

    ##### dictionary: 

    keys(), values(), items(), update, get, sort

'''



# --------------------------------------------------------------------------
# 5 - generator

# yield (with for or while)
def generator():
    for i in range(10):
        yield i

# use 1
for i in generator():
    print(i)
    
# use 2
g=generator()
print(next(g))
print(next(g)) 

    
# simple version of yield
g = (i for i in range(10))
print(list(g))



# --------------------------------------------------------------------------
# 6 - input and output

# simples IO
input_1 = input('pls input something:\n')
print(input_1)

# print out
print(x, file=f)












