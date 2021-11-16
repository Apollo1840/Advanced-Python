# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 15:36:19 2018

@author: zouco
"""

import numpy as np
import time

# 0 - initilization
# array
print("range:", np.arange(5))
print("range:", np.arange(0, 11, 2))  # exclude 11, gap = 2

print("linspace:", np.linspace(0, 10, 6))  # include 10, number=6
print("linspace:", np.linspace(0, 2 * np.pi, 10))
# np.logspace(0,2,10)

print(np.zeros(3))
print(np.ones(3))

#######################################################
# matrix
print(np.zeros((3, 3)))
print(np.ones((3, 3)))
print(np.eye(3))

# --------
print("-" * 32)
t0 = np.array([1, 2, 3])
# print(t0)
print(t0.shape)

t1 = np.tile(t0, (3, 1))
print(t1)
print(t1.shape)
t2 = np.tile(t1, (2, 2))
print(t2)
print(t2.shape)

a = np.array([1, 4, 2, 6, 7, 8, 9, 3, 4, 6, 4, 5, 7, 3, 6, 2.3])
print(a.shape)

# not a fixed array
A = a.reshape(4, 4)  # the row order is keeped
# use resize will change the a
print(A)  # remember the A here

# A userful way to create random tensor
x1 = np.random.randn(3, 3)
print(x1)

# 1 - np functions on np.array
xn = np.random.randn(100000)  # for demo purposes,, randn is normalvariate
# %time print(sum(xn))
# %time print(np.sum(xn))  # np function is incr ediablely faster

# more np functions:
A = np.array([1, 2, 3, 4])
print(np.sum(A, axis=0))  # axis = 0 means columnwise
print(np.prod(A, axis=0))

print(np.cumsum(A, axis=0))
print(np.diff(A, axis=0))  # a[n] = x[n+1] -x[n]

print(np.var(A, axis=0))
print(np.std(A, axis=0))

print(np.max(A, axis=0))
print(np.argmax(A, axis=0))

print(np.sort(A, axis=0))
print(np.argsort(A.ravel()))  # order

# entry-wise
print(np.exp(xn))  # this is crazy for for loop
print(np.sqrt(np.abs(xn)))
print(np.floor(xn))

# 2 - matrix
# 2.1 matrix operations

# 1) index
print(A[1, 2])
print(A[(1, 2)])
print(A[:, 3])

print(A[0])  # the first row
print(A[[1, 3]])  # 2 rows
# print(A[(1,3)])
print(A[[0, 2], [1, 3]])

# sampling
x = np.arange(100)
x_sample = x[::10]
x_reverse = x[::-1]

# 2) reshape and ravel
print(A.reshape(2, -1))  # -1 means adaptive

print(A.ravel())  # return to vector

# 3) np.dot (faster than for loop multiplicaiton)
x = np.array([1, 2, 3])
x = x.reshape(3, 1)
b = np.dot(A, x)  # weapon of vectorization
print(b)

# important: when one of the input lack dimension, it will be adaptive
a = np.random.randn(5)
print(a.shape)
print(a.T)
print(np.dot(a.T, a))
# 4) stack and split

a = np.floor(10 * np.random.random((2, 6)))
b = np.floor(10 * np.random.random((2, 6)))
print('a\n', a)
print('b\n', b)

# stack
print(np.hstack((a, b)))
print("c_:", np.c_[a, b])  # increase columns

print(np.vstack((a, b)))
print("r_:", np.r_[a, b])  # increase rows

# split
print(np.hsplit(a, 3))  # evenly into 3 part
print(np.hsplit(a, (3, 4)))  # 表示从某位置切割  (3, 4)  切两下 最左边记为0 第一块有3列

print(np.vsplit(b, 2))

# 2.2 matrix broadcasting

print('A\n', A)
print(A + 2)
print(A + np.array([[0, 1, -1, 100]]))
print(A + np.array([[0, 1, -1, 100]]).T)

# practice
np.sum(A, axis=0)
print(A / np.sum(A, axis=0))

# list of boolean
logic = [True, True, False, True]
np.where(logic)
np.where(logic, range(4), range(0, 40, 10))  # another ways to use np.where
np.nonzero([0, 2, 0, 1])  # it is better to not use it on boolean
# == np.where(!=0)

np.logical_not(logic)

#################  program operation   #################
a = np.array([[1, 4, 2, 6, 7, 8, 9, 3, 4, 6, 4, 5, 7, 3, 6, 2.3]])
a2 = a
a_copy = a.copy()
a_view = a.view()

a[0, 0] = 404
print("a:", a)
print("a equal:", a2)
print("a copy:", a_copy)
print("a view:", a_view)

print("-" * 32)

a = np.array([[1, 4, 2, 6, 7, 8, 9, 3, 4, 6, 4, 5, 7, 3, 6, 2.3]])
a2 = a
a_copy = a.copy()
a_view = a.view()

a.shape = (4, 4)
a[0, 0] = 404
print("a:", a)
print("a equal:", a2)
print("a copy:", a_copy)
print("a view:", a_view)

#################  bonus operation   #################

# np.all
np.all([True, False])
np.any([True, False])

# np.c_ for 1 dim array
A = np.arange(6)
print(np.c_[A, A])

# cov
x = np.array([1, 2, 3])
y = x
X = np.concatenate([x, y+0.5])
print("cov:", np.cov(x, y))
print("cov:", np.cov(X.T))  # each column of X is an attribute

print("corrcoef:", np.corrcoef(x, y))

# np.meshgrid
xx, yy = np.meshgrid(A, A)
all_node = zip(xx.ravel(), yy.ravel())
print(list(all_node))

# np.apply_along_axis
print("apply along axis", np.apply_along_axis(lambda x: np.sum(x), 0, A.reshape(2, 3)))


##########################################################################
##########################################################################
##########################################################################

# Handbook of numpy
a = np.arange(12)
print(a)

print(a.ndim)
print(a.shape)
print(a.size)

# numpy initialization
A = a.reshape(3, 4)
np.ones_like(a)
np.zeros_like(a)

B1 = np.random.rand(4, 3)
B2 = np.random.randn(4, 3)

# say that we want a matrix aij = i+j
np.fromfunction(lambda i, j: i + j, (3, 3))

a = np.arange(9)
idx = [1, 3, 1, 4]
print(np.take(a, idx))

idx = [[1, 2, -1], [1, 2, -1]]
print(np.take(a, idx))

# alter value
print(a)
np.put(a, [0, -1], [10, 20])  # put 10 in position 0, put 20 to the last position
print(a)

# matrix operation
A @ B1  # np.dot

np.repeat([1, 2, 3], 5).reshape(3, 5)
# newaxis
from numpy import newaxis

# it is None

a = np.arange(10)
print(a.shape)
b = a[newaxis, :]
print(b.shape)

b = a[:, newaxis]
print(b.shape)

# add new axis
a = a[:-1]
A = a.reshape(3, 3)
print("A.shape", A.shape)
B = A[:, newaxis, :]
print("B shape", B.shape)
print(B)

# delete newaxis
np.squeeze(A)

np.ptp(range(10))  # value_range (max-min)
np.ptp(np.ones(10))
np.ptp([[1, 2, 3], [2, 3, 4]], axis=0)
np.ptp([[1, 2, 3], [2, 3, 4]], axis=1)

# return the indices where elements should be inserted to maintain order.
np.searchsorted(range(10), 5)  # find the position of 5
np.searchsorted(range(10), 5, side='left')  # left is empty boundary

from numpy import linalg

A_ = linalg.solve(A)
x = linalg.solve(A, b)
M = np.array([1, 2, 3, 4])

w, v = linalg.eig(M)
u, s, vh = linalg.svd(M)
