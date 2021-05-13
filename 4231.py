a=int(input())
stringNum= str(a)
first= stringNum[0]
last=stringNum[len(stringNum)-1]
middle= stringNum[1:len(stringNum)-1]
result=int(last+middle+first)
print(result)
