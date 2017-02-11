'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220
are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.

The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from math import sqrt

def getDivisors(n):
    divSet = {1}
    for i in range(2, int(sqrt(n))):
        if n%i==0:
            divSet.add(i)
            divSet.add(n//i)
    return divSet

def sumAmicable(limit):
    amicSet = set()
    for i in range(1, limit):
        x1 = sum(getDivisors(i))
        x2 = sum(getDivisors(x1))
        if i==x2 and i!=x1:
            amicSet.add(i)
            amicSet.add(x1)
    print(sum(amicSet))


sumAmicable(10000)
