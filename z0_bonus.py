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



import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)