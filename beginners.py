
from random import randint

names = ['umer','farhan','zeeshan','rayhan','vamshi','younus','ameem','arman']
iters = [0,0,0,0,0,0,0,0]
k=0
while True:
    temp = randint(0,len(names)-1)
    iters[temp]+=1
    for i in range(0,len(iters)):
        if iters[i]==3:
            print("The Lucky Winner is : ",names[i])
            k=1
    if k==1:
        break

