'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the
terms increases by 3330, is unusual in two ways: (i) each of the
three terms are prime, and, (ii) each of the 4-digit numbers are
permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or
3-digit primes, exhibiting this property, but there is one other
4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms
in this sequence?

The 12 digit number is 296962999629
                       200322072411
'''
from math import sqrt

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

#n=1009	j=12
#100910211033

def main():
    isPrime = getPrimeArray(10000)
       
    for n in [2*n+1 for n in range(500,5000)]:
        if isPrime[n]:
            for j in range(1,(9999-n)//2+1):
                if (isPrime[n+j] and isPrime[n+2*j]):
                    #Need to check pemutation status.
                    for char1 in str(n):
                        if char1 not in str(n+j) or char1 not in str(n+2*j):
                            break
                    print("n="+str(n)+"\tj="+str(j))
                    print(str(n)+str(n+j)+str(n+2*j))
                    input()   

                
    
    print(isPrime[1009])
    print(isPrime[1021])
    print(isPrime[1033])

if __name__=="__main__":
    main()
