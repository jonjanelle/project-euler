#First write sieve prime generator to find all primes < 2000000
from math import sqrt

maxPrime = 2000000
primeList = list(range(2,maxPrime))
bound = int(sqrt(maxPrime)) 
primeSum = 0
for i in range(0,len(primeList)):
    primeSum = primeSum + primeList[i];
    if len(primeList[0:i+1]) > bound:
        break
    j = i+2
    while j < len(primeList):
        if primeList[j]%primeList[i]==0:
            del(primeList[j])
        j = j+1 
            
                   
print(primeSum)

