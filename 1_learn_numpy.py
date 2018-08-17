# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 15:36:19 2018

@author: zouco
"""

import numpy as np
import time


# randn is normalvariate
xn = np.random.randn(100000)

# np.sum is faster than sum
tic = time.time()
print(sum(xn))
print('duration: ', time.time()-tic)

tic = time.time()
print(np.sum(xn))
print('duration:', time.time()-tic)

np.exp(xn)  # this is crazy for for loop
np.sqrt(np.abs(xn))
np.floor(xn)


a = np.array([[1,4,2,6,7,8,9,3,4,6,4,5,7,3,6,2.3]])
A = a.reshape(4,4)

np.sum(A, axis = 0)  # axis = 0 means columnwise
np.argmax(A, axis = 0)
np.sort(A, axis = 0)
np.argsort(A.ravel()) # order





# numpy deal with matrix operations

a = np.array([1,4,2,6,7,8,9,3,4,6,4,5,7,3,6,2.3])
a.shape  # not a fixed array

A = a.reshape(4,4)  # the row order is keeped
print(A)
print(A[2,2])
print(A[:,3])
print(A.reshape(2,-1,order='F')) # the column order is 
print(A.ravel()) # return to vector


x = np.array([1,2,3,4])
print(A)
print(x)
b = np.dot(A,x)   # weapon of vectorization
print(b)

x2 = np.array([[1,2,3,4]]).T
b2 = np.dot(A,x2)
print(b2)

# np.dot is faster than for loop

# important fact:

a = np.random.randn(5)
a.shape
print(np.dot(a.T,a))

a = np.random.randn(1,5)
a.shape
print(np.dot(a.T,a))


# numpy broadcasting
a = np.array([[1,4,2,6,7,8,9,3,4,6,4,5,7,3,6,2.3]])
A = a.reshape(4,4)
print('A\n',A)
print(A + 2)
print(A + np.array([[0,1,-1,100]]))
print(A + np.array([[0,1,-1,100]]).T)
np.sum(A,axis=0)
print(A / np.sum(A,axis=0))



################# numpy initialization   ####################
print(np.arange(5))
print(np.linspace(0, 2*np.pi, 100))


print(np.zeros(3))
print(np.zeros((3,3)))
print(np.eye(3))

t0 = np.array([[1,2],[3,4]])
print(np.tile(t0, (2,2)))

#################  numpy matrix operation   #################
a = np.floor(10*np.random.random([2, 12]))
b = np.floor(10*np.random.random([2, 12]))
print('a\n', a)
print('b\n', b)

# row 
print(np.hstack([a, b]))
print(np.hsplit(a, 3))

# 表示从某位置切割  (3, 4)  切两下 最左边记为0 第一块有3列
print(np.hsplit(a, (3, 4)))

# column
print(np.vstack(a,b))
print(np.vsplit(b , 2))


#################  program operation   #################
a = np.array([[1,4,2,6,7,8,9,3,4,6,4,5,7,3,6,2.3]])
a2 = a
a_copy = a.copy()
a_view = a.view()

a[0,0] = 10
print(a)
print(a2)
print(a_copy)
print(a_view)

a = np.array([[1,4,2,6,7,8,9,3,4,6,4,5,7,3,6,2.3]])
a2 = a 
a_copy = a.copy()
a_view = a.view()

a.shape = (4,4)
a[0,0] = 10
print(a)
print(a2)
print(a_copy)
print(a_view)



