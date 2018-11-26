# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:17:53 2018

@author: zouco
"""

import sys,time
for i in range(20): #进度条类型 
    sys.stdout.write("*")
    sys.stdout.flush()  # without this line the speed of the progress bar is weird
    time.sleep(0.2)