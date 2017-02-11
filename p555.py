#McCarthy-91
from math import ceil

#m91(n) == mmks(100,11,10,n)
def m91(n):
    if n>100:
        print(n)
        return n-10
    else:
        print(n)
        return m91(m91(n+11))

#generalized m91
def mmks(m,k,s,n):
    if n>m:
        #print(n)
        return n-s
    else:
        #print(n)
        return mmks(m,k,s,mmks(m,k,s,n+k))

#sum of fixed-point values in mmks(m,k,s)
def sfmks(m,k,s):
    fpSum=0
    for i in range(1,m+1):
        if mmks(m,k,s,i) == i:
            fpS um+=i
    return fpSum

def getEnd(m,k,s,n):
    if n <= m:
        stop = n+ceil((m-n)/k)*k
        return stop - (int((stop-m)/s)+1)*s
    else:
        return n-s

def s(p,m):
    fpSum = 0
    for i in range(1,p+1): #values of k
        for j in range(1,i): #values of s
            fpSum+=sfmks(m,i,j)
    print(fpSum)


def s2(p,m):
    fpSum = 0
    for i in range(1,p+1): #values of k
        for j in range(1,i): #values of s
            for k in range(i,m+1):
                if getEnd(m,i,j,k)==k:
                    fpSum+=k
    print(fpSum)

m91(91)
#s(10,10)
print(getEnd(100,11,10,91))
s2(10,10)
#sfmks(100,11,10)
#for i in range(1,15):
#    print(mmks(14,12,10,i))

