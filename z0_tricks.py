# -*- coding: utf-8 -*-

# fast dict
dict(a=0, b=1, c=2, d=3)
dict(zip('abcd', range(4)))
# {'a': 0, 'b': 1, 'c': 2, 'd': 3}



# duplicates
[0]*10
'a'*10

[[0]]*10  # be carefull, those [0] share same id
# better use [[0] for _ in range(10)]



# multi assign
a = b = c =2
print(id(a), id(b)) # same
b += 2
print(id(a), id(b))
print(a, b)

a,b,c=1,2,3
a,b,c=[1,2,3]
a == a



# alternative value
a=4
feedback = 'yes' if a>5 else 'no'
print(feedback)



# chain logic
a=4
0 < a < 5



# group logic
all([True, True, False])  
any([True, True, False])



# enumerate
str1 = ['abcd','abcd','abcd','abcd']
for i,s in enumerate(str1):  # [(0, 'abcd'),(1, 'abcd'),(2, 'abcd'),(3, 'abcd')]
    print(s[i])



# re and filter
import re
list1 = ['','','']
print(filter(lambda x: re.findall('(to_)', x), list1))



# flat the multi list
flat = lambda L : sum(map(flat, L), []) if isinstance(L, list) else [L]
flat([1,2,[3,[4,5]]])



# pythonic list
list_of_list= [[1,2,3],[4,5],[5,6,7,8]]
print([y for x in list_of_list for y in x])

