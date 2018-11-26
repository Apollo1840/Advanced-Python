# -*- coding: utf-8 -*-


import math
####################################################################
# simplify the program by math:
def is_prime(n):
    if n==1:
        return False
    
    if n==2:
        return True
    
    if n >2 and n%2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n%d == 0:
            return False

    return True
###################################################################
    
n=10
num = 0
for i in range(1, n+1):
    if is_prime(i):
        num += 1

print(num)




#?
def countPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])  # this is faster than for loop
    return sum(primes)