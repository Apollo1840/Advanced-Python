# -*- coding: utf-8 -*-

# fast dict
dict(zip('abcd', range(4)))
# {'a': 0, 'b': 1, 'c': 2, 'd': 3}



# alternative value
a=4
feedback = 'yes' if a>5 else 'no'
print(feedback)



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