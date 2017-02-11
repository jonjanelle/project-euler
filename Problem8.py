fh = open("p8.txt") #Number block string loaded from file
numStr = str()

for line in fh:
    numStr+=line.strip()

maxProd = 1
minProd = 1
for i in range(0, len(numStr)-13):
    currentProd = 1
    for j in range(i, i+13):
        cNum = int(numStr[j])
        if cNum==0: break
        currentProd *= int(cNum)

    if currentProd > maxProd:
        maxProd = currentProd

print(maxProd)
