'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of
the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not
included.

'''
from math import factorial
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

'''

from math import factorial

def isCurious(n):
    fSum = 0
    num = n
    while n>0:
        fSum += factorial(n%10)
        n = n//10
    return fSum == num


ub = 40585
cSum = 0
for i in range(3,ub+1): #Began with upper bound 7*9!
    if isCurious(i):
        cSum+=i
        
print(cSum)

