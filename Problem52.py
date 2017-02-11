'''
It can be seen that the number, 125874, and its double,
251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
and 6x, contain the same digits.
'''
from math import log10

#return true if a and b contain exactly the same digits, false otherwise
def isPermut(a,b):
    if int(log10(a)) != int(log10(b)): return False #a and b have different number of digits
    b = str(b)
    for char in str(a):
        if char not in b:
            return False
    return True

found = False
n = 100
maxMult = 6
while found == False:
    n+=1
    for i in range(2,maxMult+1):
        if not isPermut(n,i*n):
            break
        elif i==6:
            found = True
            print(n)

        


