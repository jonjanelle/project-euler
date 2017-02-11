'''
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
divisible by 41.

The incredible formula  n^2 − 79n + 1601 was discovered, which produces 80
primes for the consecutive values n = 0 to 79. The product of the coefficients,
−79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.

**** Need to check values up to max(a,b)
'''
from math import sqrt

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return True
    return False

#Determine the number of consecutive primes generated
#by the quadratic function f(n)=n^2+an+b, where |a|, |b| < 1000
def primeRunLen(a,b):
    count = 0
    while isPrime(count**2+a*count+b):
        count+=1
    return count

#Begin main brute-force loop
longRun = 0
bestAB = list()
for i in range(1,1000): #|a| values
    for j in range(1,1000): #|b| values
        x1 = primeRunLen(i,j)
        x2 = primeRunLen(-i,j)
        x3 = primeRunLen(i,-j)
        x4 = primeRunLen(-i,-j)
        x = max(x1,x2,x3,x4)
        if x > longRun:
            bestAB = [i,j]
            longRun = x

print(bestAB)   
