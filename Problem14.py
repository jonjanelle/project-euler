'''
The following iterative sequence is defined
for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

longLen = 0
longStart = 0
start = 0
prevLens = list()

while start < 1000000:
    n = start       #n holds current start
    seqLen = 0
    start+=1
    while n != 1:
        if n%2==0:
            n /= 2
        else:
            n = 3*n + 1
        
        if n == longStart:  #if you reach the previous longest, current sequence is longest
            longLen = seqLen+longLen 
            longStart = n
            break
        
        seqLen += 1
        
    if seqLen > longLen:
        longLen = seqLen
        longStart = start
    


'''
while start < 1000000:
    n = start
    seqLen = 0
    while n != 1:
        if n%2==0:
            n/=2
        else:
            n = 3*n+1
        seqLen += 1
        
    if seqLen > longLen:
        longLen = seqLen
        longStart = start
    start+=1
'''

print(longStart)
        
