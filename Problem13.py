'''
Work out the first ten digits of the sum
of the one-hundred 50-digit integers in
p13.txt.
'''
#nSum = 0
fh = open('p13.txt')
print (str(sum([int(line.rstrip()) for line in fh]))[0:10])
#for line in fh:
#    line = line.strip()
#    nSum += int(line)

#print(str(nSum)[0:10])
