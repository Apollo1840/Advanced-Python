# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:11:48 2018

@author: zouco
"""

# exchage variable
a = 5
b = 3
a, b = b, a



# record time
import time
tic = time.time()
print(sum(range(10000)))
print('duration: ', time.time()-tic)




import sys
print(sys.argv[0])




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



from collections import Counter
a = ['1', '2', '3', '2', '3', '4', '2', '3', '4']
c = Counter(a)
print(c.most_common(1))

import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)