# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 15:36:19 2018

@author: zouco
"""

import numpy as np
import time


# 0 - initilization
# array 
print(np.arange(5))
print(np.arange(0,11,2))  # exclude 11

print(np.linspace(0,10,100))  # include 10
print(np.linspace(0, 2*np.pi, 100))
# np.logspace(0,2,10)

print(np.zeros(3))
print(np.ones(3))

# matrix
print(np.zeros((3,3)))
print(np.ones((3,3)))
print(np.eye(3))

t0 = np.array([[1,2],[3,4]])
print(np.tile(t0, (2,2)))

a = np.array([1,4,2,6,7,8,9,3,4,6,4,5,7,3,6,2.3])
a.shape  # not a fixed array
A = a.reshape(4,4)  # the row order is keeped
# use resize will change the a
print(A)  # remember the A here

x1 = np.random.randn(3,3)
print(x1)


# 1 - np functions on np.array
xn = np.random.randn(100000)  # randn is normalvariate
%time print(sum(xn))
%time print(np.sum(xn))  # np function is incr ediablely faster

# more np functions:
np.sum(A, axis = 0)  # axis = 0 means columnwise
np.prod(A, axis = 0)

np.cumsum(A, axis = 0)
np.diff(A, axis = 0)  # a[n] = x[n+1] -x[n]

np.var(A, axis = 0)
np.std(A, axis = 0)

np.max(A, axis = 0)
np.argmax(A, axis = 0)

np.sort(A, axis = 0)
np.argsort(A.ravel()) # order

# entry-wise
np.exp(xn)  # this is crazy for for loop
np.sqrt(np.abs(xn))
np.floor(xn)


# 2 - matrix
# 2.1 matrix operations

# 1) index
print(A[1,2])
print(A[(1,2)])
print(A[:,3])

print(A[0])  # the first row
print(A[[1,3]]) # 2 rows
# print(A[(1,3)])
print(A[[0,2],[1,3]])
 


# sampling
x = np.arange(100)
x_sample = x[::10]
x_reverse = x[::-1]

# 2) reshape and ravel
print(A.reshape(2,-1,order='F')) # -1 means adaptive
print(A.ravel()) # return to vector

# 3) np.dot (faster than for loop multiplicaiton)
x = np.array([1,2,3])
x = x.reshape(3,1)
b = np.dot(A,x)   # weapon of vectorization
print(b)

# important: when one of the input lack dimension, it will be adaptive
a = np.random.randn(5)
a.shape
print(a.T)
print(np.dot(a.T,a))



# 4) stack and split
a = np.floor(10*np.random.random((2, 12)))
b = np.floor(10*np.random.random((2, 12)))
print('a\n', a)
print('b\n', b)

# stack
print(np.hstack((a, b)))
print(np.c_[a,b])  # increase columns

print(np.vstack((a, b))
print(np.r_[a,b]) # increase rows

# split
print(np.hsplit(a, 3))  # evenly into 3 part
print(np.hsplit(a, (3, 4)))   # 表示从某位置切割  (3, 4)  切两下 最左边记为0 第一块有3列

print(np.vsplit(b , 2))


# 2.2 matrix broadcasting

print('A\n',A)
print(A + 2)
print(A + np.array([[0,1,-1,100]]))
print(A + np.array([[0,1,-1,100]]).T)

# practice
np.sum(A, axis=0)
print(A / np.sum(A,axis=0))

# list of boolean
logic = [True, True, False, True]
np.where(logic)
np.where(logic, range(4), range(0,40,10)) # another ways to use np.where
np.nonzero([0, 2, 0, 1]) # it is better to not use it on boolean

np.logical_not(logic)



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

#################  bonus operation   #################

# np.c_ for 1 dim array
A = np.arange(6)
np.c_[A,A]


# np.meshgrid
xx, yy = np.meshgrid(A,A)
all_node = zip(xx.ravel(),yy.ravel())
print(list(all_node))

# np.all
np.all([True, False])
np.any([True, False])

# np.apply_along_axis 
np.apply_along_axis(lambda x: np.sum(x), 0, A.reshape(2,3))

# cov
np.cov(x,y)
np.cov(X.T)  # each column of X is an attribute 

np.corrcoef(x, y)






##########################################################################
##########################################################################
##########################################################################

# Handbook of numpy
a = np.arange(12)
print(a)

a.ndim
a.shape
a.size

# numpy initialization
A = a.reshape(3,4)
np.ones_like(a)
np.zeros_like(a)

B1 = np.random.rand(4,3)
B2 = np.random.randn(4,3)

# say that we want a matrix aij = i+j
np.fromfunction(lambda i,j:i+j, (3,3))

a = np.arange(9)
idx = [1,3,1,4]
print(np.take(a, idx))

idx = [[1,2,-1],[1,2,-1]]
print(np.take(a, idx))

# alter value
print(a)
np.put(a, [0,-1], [10,20])  # put 10 in position 0, put 20 to the last position
print(a)




# matrix operation
A @ B1  # np.dot

np.repeat([1,2,3],5).reshape(3,5)



# newaxis 
from numpy import newaxis
# it is None

a = np.arange(10)
print(a.shape)
b = a[newaxis,:]
print(b.shape)

b = a[:, newaxis]
print(b.shape)

a = a[:-1]
A = a.reshape(3,3)
B = A[:,newaxis,:]
print(B)
# delete newaxis
np.squeeze(A)


np.ptp(range(10)) # value_range (max-min)
np.ptp(np.ones(10))
np.ptp([[1,2,3],[2,3,4]], axis=0)
np.ptp([[1,2,3],[2,3,4]], axis=1)


# return the indices where elements should be inserted to maintain order.
np.searchsorted(range(10),5)  # find the position of 5
np.searchsorted(range(10),5, side = 'left')  # left is empty boundary



from numpy import linalg
A_ = linalg.solve(A)
x = linalg.solve(A, b)
u,s,vh = linalg.eig(M)
u,s,vh = linalg.svd(M)
