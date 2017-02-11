from math import sqrt
fh = open("p042_words.txt")
words = fh.read().replace('"','').split(',')
fh.close()

def isTriangular(n):
    '''
    Determine whether an integer n is a triangular number
    '''
    return sqrt(1+8*n).is_integer()
   
#for i in range(1,51):
#    print("i = "+str(i)+" Tri? "+ str(isTriangular(i)))
triCount = 0
for word in words:
    wSum = 0
    for char in word:
        wSum += ord(char)-ord('A')+1
    if isTriangular(wSum):
        triCount+=1
print(triCount)


'''
To determine whether an integer n is triangular:
    n=k(k+1)/2
    2n = k(k+1)
    k^2+k-2n = 0
    k = (-1 + sqrt(1+8*n))/2  #n is triangular for integer values of k, discard negative
'''
