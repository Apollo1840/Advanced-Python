# -*- coding: utf-8 -*-
# -------------------------------------------------
# system and os
import sys
print(sys.argv[0])
print(sys.path)
# sys.path.append()
sys.getsizeof(sys.maxsize)



import os
# os.system() this can run command line
os.system('pwd') 

# the running environment
os.getcwd()  
# the script
os.path.dirname(__file__)
os.path.dirname(os.path.abspath(__file__))

full_name = os.path.split(os.getcwd())  # dirname, basename
os.path.dirname(os.getcwd())
os.path.basename(os.getcwd())

full_name = os.path.splitext(os.getcwd()) # basename, file type

os.path.exists(os.getcwd())
# os.path.join('' ,' ',' ')
os.path.isfile(os.path.join(os.getcwd(),'01_basics.py'))

os.chdir('...')

# see the dir
os.listdir()
os.walk('...') # return a list of 3 tuple , first is path, secound is folds, third is files
os.mkdir('...')
os.makedirs('...')

os.rename('','')


from datetime import datetime
Mod_time=os.stat('demo.txt').st_time
print(datetime.fromtimestamp(mod_time))



# -------------------------------------------------
# see detail
import dis
dis.dis(swap)



# -------------------------------------------------
# record time
import time
tic = time.time()
print(sum(range(10000)))
print('duration: ', time.time()-tic)



# -------------------------------------------------
# readerable tuple
from collections import namedtuple
color = (255,255,0) # regular tuple
Color = namedtuple('Color', ['r','g','b'])
color = Color(255,255,0)
# color = Color(r=255,g=255,b=0)
print(color.r)


from collections import Counter
a = ['1', '2', '3', '2', '3', '4', '2', '3', '4']
c = Counter(a)
print(c.most_common(1))



# -------------------------------------------------
# heapq
import random
nums = list(range(10))
random.shuffle(nums)
# nums = [5, 1, 8, 2, 6, 0, 9, 3, 4, 7]

tuples = [(1,2),(3,4),(5,1)]

import heapq
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(2, tuples, key=lambda x:x[1]))



# -------------------------------------------------
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

