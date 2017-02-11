'''
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''
from math import sqrt,log10
import time

def getPrimeArray(limit):
    '''
    Get a boolean array whose entries are true
    if the corresponding index is a prime number,
    false otherwise.
    @param limit The integer upper limit of the array
    '''
    isPrime = [True for i in range(0,limit+1)]
    isPrime[0] = isPrime[1] = False
    upperBound = int(sqrt(limit)+1)
    for i in range(2,upperBound):
        if isPrime[i]:
            ub = limit//i
            for j in range(i,ub+1):
                isPrime[i*j]=False
    return isPrime
    



#n is a prime number
#isPrime is a boolean prime array
def isTruncatable(n,isPrime):
    '''
    First checks whether all right truncated numbers are prime
    n = 3797
    379
    37
    3
    And then whether the left-truncated numbers are prime
    3797
     797
      97
       7
    '''
    n1 = n
    degree = int(log10(n))+1
    
    count = 0
    while n>0:
       #print("n = "+str(n) + "\tn1 = " + str(n1))
        if not (isPrime[n] or isPrime[n1]):
            return False
        n = n//10
        count+=1
        n1 = n1%(10**(degree-count))
    
    return True
    '''    
    for i in range(0,degree+1):
        if not isPrime[n1]:
            return False
        n1 = n1%(10**(degree-i))
    return True
    '''

    
def main():
    #start = time.time()
    #isPrime = getPrimeArray(1000000)
    #print(time.time()-start)   #284ms at last test with 1000000
    #for i in range(0,100):
    #    print("i = "+str(len(isPrime)-i-1)+"\tprime? "+str(isPrime[len(isPrime)-i-1]))
    start = time.time()
    isPrime = getPrimeArray(1000000)
    numFound = 0
    num = 11
    tSum = 0
    while numFound<11: #given that there are 11 total
        if (isPrime[num] and isTruncatable(num, isPrime)): #yay short circuit efficiency
            numFound+=1
            tSum += num
            # print("Trucatable Found!\t"+str(num))

        num+=1
        
    print(tSum)
    print(time.time()-start)   #284ms at last test with 1000000
    
if __name__=="__main__":
    main()
    #isTruncatable(3799,getPrimeArray(1000000))
