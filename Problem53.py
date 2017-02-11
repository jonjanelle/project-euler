
def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod*=i
    return prod


def nCr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

count = 0
for i in range(1,101):
    for j in range(0,i):
        if nCr(i,j)>1000000:
            count += i-2*j+1
            break
            #count+=1

print(count)

