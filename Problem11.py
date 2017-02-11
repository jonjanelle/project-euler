'''
The file p11.txt contains a 20x20 grid of integers.

What is the greatest product of four adjacent numbers in the same
direction (up, down, left, right, or diagonally) in the 20×20 grid?

The greatest product of 4 entries is 70600674

'''

fh = open("p11.txt")
numArr = list()
for line in fh:             #create 2d int array
    row = list()
    for num in line.split():
        row.append(int(num))
    numArr.append(row)

maxProd = 1

for i in range(0, len(numArr)):
    currentProd = 1
    for j in range(0,len(numArr[i])):
        downProd,rProd,diagProd1,diagProd2 = 1,1,1,1
        for k in range(0,4):
            if j <= (len(numArr[i])-4):  #horizontal product to right
                rProd *= numArr[i][j+k]
            if i <= (len(numArr)-4):     #vertical product down
                downProd *= numArr[i+k][j]
            if (j <= (len(numArr[i])-4)) and (i <= (len(numArr)-4)): #toward bottom right diagonal
                diagProd1 *= numArr[i+k][j+k]
            if  j >= 3 and (abs(j-i))>=4 and i <= len(numArr)-4: #toward bottom left diagonal
                diagProd2 *= numArr[i+k][j-k]
    print([maxProd,rProd,downProd,diagProd1,diagProd2])
    maxProd = max([maxProd,rProd,downProd,diagProd1,diagProd2])
    
            
print(maxProd)
