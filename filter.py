#-*-coding:utf-8-*-
import math

print "filter()接受一个函数和一个序列，filter把函数作用于每一个元素，然后根据返回值是True后者False来决定是否保留该元素"
print "返回的同样是一个序列"
def isOdd(n):
    return n % 2 == 1

L = [1, 2, 3, 4, 5, 6]
print filter(isOdd,L)

L = range(100)
print L

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1) ):#必须转为int型的，因为sqrt返回的是float，而range需要int
        if (n % i == 0 ):
            return False
    return True

print filter(isPrime, L)       
