# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:47:43 2018

@author: zouco
"""

import threading
import time

def goto_sleep(name, n):
    print('{} is sleeping\n'.format(name))
    time.sleep(n)
    print('{} has woken up'.format(name))

t = threading.Thread(target=goto_sleep, name='worker01', args=('w1', 5))


t.start()

t.join()

print('hello world')



# multi-thread
t0 = time.time()

thread_list = []
for i in range(10):
    t = threading.Thread(target=goto_sleep, name='worker_{}'.format(i), args=('w{}'.format(i), 5))
    thread_list.append(t)
    t.start()
    
for t in thread_list:
    t.join()

print('it takes {} seconds'.format(time.time()-t0))    
print('hello world')