'''
The number, 197, is called a circular prime because all
rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''
from math import sqrt

#Generate a list of all prime numbers
#between 2 and upperBound, inclusive
def getPrimeList(upperBound):
    pList = list(range(2,upperBound+1))

    maxFac = int(sqrt(upperBound))+1
    for i in range(0,len(pList)):
        if pList[i] > maxFac: break
        for j in range(len(pList)-1,i,-1):
            if pList[j] % pList[i] == 0:
                pList.pop(j)                
    return pList

#Determine whether a given prime number is circular
def isCircular(pList):
    pass
    

#Perform a left 'rotation' of 1 to a number
#234 -> 342
#342 -> 423
#423 -> 234
def rotate(num):
    num = str(num)
    result = str()
    for i in range(len(num)-2):
        
        result = result*10+num%10
        num = num//10
    return result

print(rotate(123))
#primeList = getPrimeList(1000000)

