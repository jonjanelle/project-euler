fh = open('p18.txt')
data = list()
for line in fh:
    row = list()
    for num in line.split():
        row.append(int(num))
    data.append(row)

currentRow = 0
pathSum = data[0][0]
for i in range(0,len(data)-1):
    if currentRow == 0:
        pathSum += data[currentRow+1][i+1]
        currentRow += 1
    elif currentRow == len(data[currentRow]):
        pathSum += data[currentRow+1][i-1]
        currentRow -= 1
    else:
        if data[currentRow+1][i+1] > data[currentRow+1][i+1]:
            pathSum += data[currentRow+1][i-1]
            currentRow -= 1
        else:
            pathSum += data[currentRow+1][i+1]
            currentRow += 1
    
print(pathSum)



##Use the bits in the count of all possible solutions to find the answer
##Ex: 01000110
# bit 0 = 0: turn left at first level
# bit 1 = 1: turn right at 2nd
# bit 2 = 1: turn right at 3rd
# bit 3 = 0: turn left at 4th
# etc...
