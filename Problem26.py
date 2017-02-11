'''
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
'''
import time

#Find the multiplicative order (Haupt exponent)
#given a number and base
def findHaupt(b,n):
    e = 1
    while b**e%n != 1:
        e+=1
    return e

#begin main loop
maxHaupt = 0
num = 0
for i in range(2,1000):
    if i%2!=0 and i%5!=0:
        haupt = findHaupt(10,i)
        if haupt > maxHaupt:
            num = i
            maxHaupt = haupt

print(num)

