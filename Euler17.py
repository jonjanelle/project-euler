ones = ['one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven', 'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens  = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']


onesCount = sum(len(x) for x in ones)*9*10   #each shows up 9 times per 100, 10 groups of 100 total 
teensCount = sum(len(x) for x in teens)*10   #each shows up 1 time per 100, 10 groups of 100 total
tensCount = sum(len(x) for x in tens)*10*10  #each shows up 10 times for 100, 10 groups of 100 total
hunCount = len('hundred')*100*9              #word hunded appears 100 times per 100, one through nine hundred
thouCount = len('thousand')+3                #length of 'one thousand'
andCount = len('and')*99*9                   #and used 99 times per 100 from one to nine hundred
extraOnes = sum(len(x) for x in ones)*100    #The units words like 'one' in one hundred, 'two' in two hundred, etc...

print(onesCount+teensCount+tensCount+hunCount+thouCount+andCount+extraOnes)
