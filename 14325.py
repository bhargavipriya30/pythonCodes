a=int(input())
stringNum= str(a)
first= stringNum[0]
last=stringNum[len(stringNum)-1]
middle= stringNum[1:len(stringNum)-1][::-1]
result=int(first+middle+last)
print(result)
