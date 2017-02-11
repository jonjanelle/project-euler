x = str()
for i in range(1,500000):
    x+=str(i)

cc = 1
for i in range(0,7):
    cc *= int(x[pow(10,i)-1])

print(cc)
