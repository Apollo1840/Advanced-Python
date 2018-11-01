# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:36:28 2018

@author: zouco
"""

# change 1000 dollars to 100,50,20,5 how many possiblities do we have


# 20x + 10y + 4z + j = 200

count = 0
for x in range(200//20+1):
    for y in range((200-20*x)//10+1):
        for z in range((200-20*x-10*y)//4+1):
            for j in range(200-20*x-10*y-4*z+1):
                # print(x,y,z,j)
                if 20*x + 10*y + 4*z + j == 200:
                    count += 1
print(count)
                    
                