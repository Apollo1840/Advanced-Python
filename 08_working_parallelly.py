# -*- coding: utf-8 -*-

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





# chicken lay egg example:
import random

eggs = []

class chicken():
    sound = 'koko\n'
    
    def __init__(self):
        self.name = random.randint(20)
    
    def lay_egg(self):
        time.sleep(random.choice([1, 1.1, 1.2, 1.3, 10]))
        print(self.name + ':' + self.sound)
        eggs.append(1)


def basic_process(): 
    ck0 = chicken()
    while(len(eggs) < 12):
        ck0.lay_egg()
    

def three_chicken():
    ck0 = chicken()
    ck1 = chicken()
    ck2 = chicken()
    
    while(len(eggs) < 12):
        ck0.lay_egg()
        ck1.lay_egg()
        ck2.lay_egg()
        

def three_chicken_parallel():
    ck0 = chicken()
    ck1 = chicken()
    ck2 = chicken()
    
    thread_list=[]
    
    for epoch in range(4):
        for i in range(3):
            ck = eval('ck{}'.format(i))
            t = threading.Thread(target=ck.lay_egg)
            thread_list.append(t)
            t.start()
        for t in thread_list:
            t.join()

def three_chicken_parallel_2():
    thread_list=[]
    
    for epoch in range(4):
        for i in range(3):
            t = threading.Thread(target=chicken().lay_egg)
            thread_list.append(t)
            t.start()
        for t in thread_list:
            t.join()
        
        chicken.sound = chicken.sound[:-1] + '!\n'

def lag4eggs():
    ck = chicken()
    for i in range(4):
        ck.lay_egg()
    chicken.sound = chicken.sound[:-1] + '!\n'
            
def three_chicken_parallel_3():
    thread_list=[]

    for i in range(3):
        t = threading.Thread(target=lag4eggs)
        thread_list.append(t)
        t.start()
        
    for t in thread_list:
        t.join()
        
        
        
def test():
    t0 = time.time()
    three_chicken_parallel_3()
    print('spend {}s'.format(time.time() - t0))



    
        