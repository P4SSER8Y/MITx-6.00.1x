__author__ = 'troy'

from time import time
import functools
import pylab
import math
import gc

def printTime(f):
    @functools.wraps(f)
    def wtf(*args, **kw):
        t = time()
        for _ in range(200):
            ret = f(*args, **kw)
            del ret
        t = time() - t
        print f.__name__ + ' exited in ' + str(round(t * 5,2)) + 'ms'
        return t / 200.0
    return wtf

@printTime
def primesList(N):
    '''
    N: an integer
    '''
    # Your code here
    if N < 2:
        return []
    ans = [2]
    for i in range(3, N + 1, 2):
        isPrime = True
        for k in [x for x in ans if x <= int(i ** 0.5 + 1)]:
            if (i % k) == 0:
                isPrime = False
                break
        if isPrime:
            ans.append(i)
    return ans

@printTime
def primesList2(N):
    if N < 2:
        return []
    flag = [False, False] + [True] * N
    k = 2
    ret = []
    while k < N + 1:
        ret.append(k)
        i = 2 * k
        while i <= N + 1:
            flag[i] = False
            i += k
        k += 1
        while (not flag[k]) and (k < N + 1):
            k += 1
    return ret

@printTime
def primesList3(N):
    flag = [True] * (N + 1)
    flag[0] = flag[1] = False
    primes = []
    for k in range(2, N + 1):
        if flag[k]:
            primes.append(k)
            for j in range(2, N / k + 1):
                flag[j * k] = False
    return primes

if __name__ == "__main__":
    X = []
    p2 = [] 
    p3 = []
    for i in range(1, 1000):
        print '\n', i
        X.append(i)

        t = primesList2(i)
        p2.append(t)

        t = primesList3(i)
        p3.append(t)
        
        t = time()
        gc.collect()
        print "Garbage Collected in ", int((time() - t)* 1000), 'ms'
